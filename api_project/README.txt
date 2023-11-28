APIの流れ

url
/api/talk/

json
'json_data'
{'responses':[
    {'name':'user','answer','testmessage'},
    {'name':'assistant','answer','testmessage'}
    ]
}

content
'audio_file'
audio/wav

urls
↓
views
↓
serializers　入力値の検査
↓
views　処理
    (TalkLib(会話の生成),
    textToVoice(テキストを音声に),
    voiceToText(音声をテキストに))
↓
返却