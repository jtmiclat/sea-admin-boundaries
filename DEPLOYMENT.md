# Deployment Notes

## Cloudflare

By default cloudflare blocks requests from python's `urlopen` which pandas and geopandas use.
The source is an attached user agent header made to the request and cloudflare's browser integrity checks.
A way to disable this Cloudflare behavior is to create a configuration rule that bypass this check for certains hostnames or filetypes.

Note: I tried hosting the files in R2 bucket but it seems the R2 buckets have a similar rule that cannot be disabled via configuration rules.
