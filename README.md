# TalkAPI

### 使用方法
```
import requests
import json

def main():
    # JSONデータと音声ファイルを準備します
    json_data = {
        "responses": [
            {"name": "user", "answer": "こんにちは!"},
            {"name": "assistant", "answer": "こんにちは"}
        ]
    }
    audio_file = open('load_audio_data.mp3', 'rb')
    url = 'https://example.com/api/talk/'

    data = {'json_data': json.dumps(json_data),}
    files = {'audio_file': ('output.mp3', audio_file, 'audio/mp3'),}

    response = requests.post(url, data=data, files=files)

    # 応答を表示
    print(response)
    print(response.json())#会話内容

    # 音声ファイルを保存
    with open('audio_data.mp3', 'wb') as file:
        file.write(response.content)

if __name__ == '__main__':
    main()
```

## 送信データ形式
url
```
/api/talk/
```

json
```
{'responses':[
    {'name':'user','answer':'testmessage'},
    {'name':'assistant','answer':'testmessage'}
    ]
}
```

content_type
```
audio/mp3
```

## 処理の流れ
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
