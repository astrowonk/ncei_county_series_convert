
## Convert NOAA County Time Series Data to CSV

This code works on the [bulk NCEI climate division files](https://www.ncei.noaa.gov/pub/data/cirs/climdiv/) at the NCEI for **counties**. For an interactive way to view this data, try the [County Time Series page](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/time-series).

It should convert files in that link that have the filenames:

```
climdiv-pcpncy-vx.y.z-YYYYMMDD
climdiv-tmaxcy-vx.y.z-YYYYMMDD
climdiv-tmincy-vx.y.z-YYYYMMDD
climdiv-tmpccy-vx.y.z-YYYYMMDD
climdiv-cddccy-vx.y.z-YYYYMMDD
climdiv-hddccy-vx.y.z-YYYYMMDD
```

In addition to converting from a fixed width formation to CSV, the script creates a 5 digit FIPS that combines state FIPS and county FIPS. This is available as an integer (4 or 5 digits) as FIPS_int (5001) as as five character string with leading zeros ("05001") in FIPS_str. The combined state+county FIPS code should make it easier to merge into other data sources that have a five digit FIPS.

The element (and other columns) are described in the [county readme](https://www.ncei.noaa.gov/pub/data/cirs/climdiv/county-readme.txt), but is generally the same for every row for the same filename (`tmpccy` files wil be all be a "2" element code, for example.)

The script requires [pandas](https://pandas.pydata.org). If you want to export to parquet, you'll need something like pyarrow or a parquet backend for pandas.

