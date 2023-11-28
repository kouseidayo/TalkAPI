import json
import requests
import wave


class VoiceGenerate():

    host = 'localhost'
    port = 50021

    def __init__(self,text, speaker=1):
        self.params = (
            ('text', text),
            ('speaker', speaker),
        )


    #クエリ生成
    def query_generate(self):

        self.query = requests.post(
            f'http://{self.host}:{self.port}/audio_query',
            params=self.params
        ).json()
        return self.query
    

    #音声生成
    def voice_generate(self, query=None):

        if(query == None):
            query = self.query
        
        headers = {'Content-Type': 'application/json',}

        self.voice_data = requests.post(
            f'http://{self.host}:{self.port}/synthesis',
            headers=headers,
            params=self.params,
            data=json.dumps(query)
        )

        return self.voice_data
    
    #保存
    def save(self, file_path, voice_data=None):

        if(voice_data == None):
            voice_data = self.voice_data

        wf = wave.open(file_path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(voice_data.content)
        wf.close()