from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .TalkLibrary.TalkLib import JsonToTalk,VoiceToText,TextToVoice

class TalkAPIView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():

            #会話用クラス
            Talk = JsonToTalk(serializer.validated_data['json_data'])
            
            #ユーザーの音声ファイルの取得
            user_audio_file = serializer.validated_data['audio_file']
            
            #音声ファイルをテキストへ変換
            user_text = VoiceToText(user_audio_file)
            
            #会話用のapiに適した形に変換
            Talk.TransTalk(user_text)

            #apiから返答を取得
            assistant_text = Talk.talk()

            #返答を音声へ変換
            Response_audio_file = TextToVoice(assistant_text)
            
            #レスポンスに適した形に変換
            data = Talk.TransResponse(Response_audio_file)

            # 音声ファイルのContent-Typeを指定
            response = Response(data, content_type='application/json', status=status.HTTP_200_OK)
            response['Content-Disposition'] = 'attachment; filename="audio_file.mp3"'
            return response

        else:
            # データが無効な場合の処理をここに書く
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
