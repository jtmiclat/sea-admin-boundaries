import os
from hdx.api.configuration import Configuration
from hdx.data.dataset import Dataset
import geopandas as gpd
import pyogrio
import yaml


os.makedirs("data/staging", exist_ok=True)

Configuration.create(hdx_site="prod", user_agent="Sea-Countries", hdx_read_only=True)
datasets = {}

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


def download_file(dataset_name, resource_name):
    if dataset_name in datasets:
        dataset = datasets[dataset_name]
    else:
        dataset = Dataset.read_from_hdx(dataset_name)
        datasets[dataset_name] = dataset
    resource = next(r for r in dataset.resources if r["name"] == resource_name)
    url, filename = resource.download("data/staging/")
    os.rename(filename, filename.replace('.shp', ''))


def process_file(source, output, isocode):
    os.makedirs(f"data/processed/{isocode}", exist_ok=True)
    gdf = gpd.read_file(f"data/staging/{source}")
    pyogrio.write_dataframe(
        gdf, f"data/processed/{isocode}/{output}.fgb", driver="FlatGeobuf"
    )
    gdf.to_parquet(f"data/processed/{isocode}/{output}.geoparquet")


for country in config:
    print(f"Processing country: {country['country']}")
    for download in country["download"]:
        download_file(download["dataset"], download["resource"])
    for process in country["processing"]:
        process_file(process["source"], process["output"], country["isocode"])
