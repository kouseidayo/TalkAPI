from .voiceToText_cloudLib import transcribe_audio_file
from .textToVoice_cloudLib import text_to_speech
from .talk_cloudLib import interview

def VoiceToText(audio_data):
    text = transcribe_audio_file(audio_data)
    return text

def TextToVoice(text):
    audio_data = text_to_speech(text)
    return audio_data

class JsonToTalk():

    audio_file = 'audio_file'
    new_answer = "<new_answer>"
    responses = 'responses'
    answer = 'answer'
    add = 'add'

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
        self.json_data[self.add] = self.assistant_template
        
        #responses内のuserの発言を生成
        self.user_template[self.answer] = text  
        self.json_data[self.responses].append(self.user_template)

        #responses内のassistantの入力欄の生成
        self.json_data[self.responses].append(self.assistant_template)

        return self.json_data

    #会話用のapiと連携
    def talk(self):

        self.json_data = interview(
            temperature=0.2,
            project_id='formal-province-366012',
            location='asia-northeast1',
            max_output_tokens=256,
            top_k=40,
            top_p=0.8,
            model_name="text-bison@001",
            prompt=f"{self.base_prompt}{self.json_data}"
            )

        return self.json_data[self.add][self.answer]

    def TransResponse(self,audio_data):
        
        #音声ファイルの挿入
        if self.audio_file in self.json_data:
            self.json_data[self.audio_file] = audio_data
        
        #返答の入力欄の削除
        if self.add in self.json_data:
            del self.json_data[self.add]
        
        return self.json_data