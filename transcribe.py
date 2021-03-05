def auth():
    from google.cloud import storage
    
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    print(buckets)

def transcribe(uri):
    from google.cloud import speech
    import sys

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code = 'en-US',
        audio_channel_count=2,
    )

    operation = client.long_running_recognize(config=config, audio=audio)
    print('proccessing...')
    response = operation.result(timeout=90)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))

    sys.exit()
    
# auth()
transcribe('gs://demo-bucket-demo/LongWelcome.wav')