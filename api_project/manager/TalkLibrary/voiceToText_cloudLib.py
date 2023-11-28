from google.cloud import speech_v1p1beta1 as speech

def transcribe_audio_file(content):
    client = speech.SpeechClient()

    content = content.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=24000,
        language_code="ja-JP",
        # speech_contexts=[{"phrases": ["ハンバーグ","ござる"]}],
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript