# Deployment Notes

## Cloudflare

By default cloudflare blocks requests from python's `urlopen` which pandas and geopandas use.
The source is an attached user agent header made to the request and cloudflare's browser integrity checks.
I verified this by running the following curl command
```
curl -H "User-Agent: Python-Urlib/3.8" https://opendata.jtmiclat.me/index.html
```
vs
``

A way to disable this Cloudflare behavior is to create a configuration rule that bypass this check for certains hostnames or filetypes.

Note: I tried hosting the files in R2 bucket but it seems the R2 buckets have a similar rule that cannot be disabled via configuration rules.
