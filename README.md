# Dropbox Uploader

A python script for uploading files to your dropbox account.

This script is based on a [python sdk example](https://github.com/dropbox/dropbox-sdk-python/blob/master/example/back-up-and-restore/backup-and-restore-example.py).

## Requirements

- Python 2.7
- Dropbox Python SDK

## Configuration

A token must be provided as environment variable:
```bash
$ DROPBOX_TOKEN='my_token'
```

You can get your personal token from [here](https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/).

An optional remote path can be set up defining `DROPBOX_PATH` env variable.

## Run it

```bash
$ python dropbox-uploader.py my-file.txt
```


