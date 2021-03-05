# Audio Transcribe Service

This repo offers an audio file transcribe service. However, the format of audio uri is only limited to Google Storage link, which begins with `gs://`.

## Set up Google Cloud API

1. Log into Google Cloud Platform
2. Enable `text-to-speech`/`speech-to-text` library 
3. Create one service account
4. Add and download the key `json` file from the created service account
5. Google only accepts audio file from Google Storage, where url begins with `gs://`. Add a new bucket name linked to the created service account. [Link here](https://console.cloud.google.com/storage). 
6. Set GOOGLE_APPLICATION_CREDENTIALS before running the program.

```sh
# https://cloud.google.com/docs/authentication/getting-started
set GOOGLE_APPLICATION_CREDENTIALS=[PATH-TO-KEY-FILE]
```

