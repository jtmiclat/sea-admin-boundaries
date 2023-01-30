# Scripts for saving admin boundaries of South East Asian countries in better geofile formats

Access South East Asian admin boundaries in better formats than [shapefiles](http://switchfromshapefile.org/)

## Accessing the data

These files are hosted in https://opendata.jtmiclat.me.
It follows the format of `https://opendata.jtmiclat.me/{COUNTRY_CODE}/admin{ADMIN_LEVEL}.{FILE_FORMAT}`

The current available countries are Philippines (PH), Thailand (TH), and Indonesia (ID).

The current available file formats are FlatGeobuf (.fgb), Geoparquet (.geoparquet), and GeoPackage (.gpkg).

Admin level are from 0-3.

### Basic usage

I recommend sticking with flatgeobuff for reading as geoparquet is still in beta and geopacakge is less efficient for reads.

```python
import geopandas as gpd
gdf = gpd.read_file("https://opendata.jtmiclat.me/PH/admin3.fgb")
gdf.plot()
```

### Advance usage

Selecting geometries by attribute value

```python
import pyogrio

gdf = pyogrio.read_dataframe(
    "https://opendata.jtmiclat.me/ID/admin3.fgb",
    where="ADM2_PCODE = 'ID9401'"
)
```

Selecting geometries by bbox value

```python
import pyogrio
gdf = pyogrio.read_dataframe(
    "https://opendata.jtmiclat.me/PH/admin3.fgb",
    bbox=(120.7584, 4.2314, 128.9682, 9.4687)
)
```

## Source of Data

Data is from [The Humanitarian Data Exchange](https://data.humdata.org/).

Country Specific URLs:

- [Philippines](https://data.humdata.org/dataset/cod-ab-phl)
- [Thailand](https://data.humdata.org/dataset/cod-ab-tha)
- [Indonesia](https://data.humdata.org/dataset/cod-ab-ind)

## Notes

This was for me to play around with using different geospatial file formats and hosting data.

## TODO:

- [ ] Add other SEA countries
- [ ] Benchmark geoparquet compression and select one
- [ ] Add indexing of flatgeobuf
