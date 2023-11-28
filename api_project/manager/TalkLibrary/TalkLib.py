import openai
from django.conf import settings
from .textToVoice import VoiceGenerate
from .voiceToText_cloudLib import transcribe_audio_file

def VoiceToText(audio_data):
    
    text = transcribe_audio_file(audio_data)
    return text

def TextToVoice(text):
    vg = VoiceGenerate(text)
    vg.query_generate()
    audio_data = vg.voice_generate()
    return audio_data

class JsonToTalk():

    audio_file = 'audio_file'
    new_answer = "<new_answer>"
    responses = 'responses'
    answer = 'answer'

    user_template= {"name": "user", answer: ""}
    assistant_template = {"name": "assistant", answer: new_answer}

    base_prompt =f"""
#次のデータを以下の条件で返して
{new_answer}に当てはまる答えを入れる
json形式で返答


"""

    def __init__(self,json_data):
        self.json_data = json_data
        
    def TransTalk(self,text):
        #assistantの入力欄の生成
        self.json_data[self.new_answer] = self.assistant_template
        
        #responses内のuserの発言を生成
        self.user_template[self.answer] = text  
        self.json_data[self.responses].append(self.user_template)

        #responses内のassistantの入力欄の生成
        self.json_data[self.responses].append(self.assistant_template)

        return self.json_data

    #会話用のapiと連携
    def talk(self):

        openai.api_key = settings.OPENAI_APIKEY

        prompt = f"{self.base_prompt}{self.json_data}"

        response = openai.Completion.create(
        prompt=prompt,
        engine="text-davinci-003",
        max_tokens=1024
        )

        self.json_data = response.choices[0].text.strip()

        return self.json_data[self.new_answer][self.answer]

    def TransResponse(self,audio_data):
        
        #音声ファイルの挿入
        if self.audio_file in self.json_data:
            self.json_data[self.audio_file] = audio_data
        
        #返答の入力欄の削除
        if self.new_answer in self.json_data:
            del self.json_data[self.new_answer]
        
        return self.json_data