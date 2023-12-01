from google.cloud import texttospeech

# テキストとを音声に変換し、返す
def text_to_speech(text):
    # クライアントをインスタンス化します
    client = texttospeech.TextToSpeechClient()
    # 合成するテキスト入力を設定します
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # 声のリクエストを構築し、言語コード（「en-US」）と
    # SSML音声のジェンダー（「neutral」）を選択します
    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # 返されるオーディオファイルの種類を選択します
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # 選択した音声パラメータとオーディオファイルタイプを使用して、
    # テキスト入力に対してテキストから音声に変換するリクエストを実行します
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response.audio_content

if __name__ == '__main__':
    audio_content = text_to_speech('こんにちは')
    with open('output.wav', 'wb') as out:
        out.write(audio_content)