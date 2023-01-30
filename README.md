# Scripts for saving admin boundaries of South East Asian countries in better geofile formats

Access South East Asian admin boundaries in better formats.

## Accessing the data

These files are hosted in https://opendata.jtmiclat.me

### Basic usage

```python
import geopandas as gpd
gdf = gpd.read_file("https://opendata.jtmiclat.me/PH/admin3.fgb")
gdf.plot()
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
