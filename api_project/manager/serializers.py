from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    answer = serializers.CharField(max_length=300)

    def validate_name(self, value):
        if (value != 'user' and value != 'assistant'):
            raise serializers.ValidationError("JSONデータに不正な名前が含まれています")
        return value

class ResponsesSerializer(serializers.Serializer):
    responses = serializers.ListField(child=MessageSerializer())

class PostSerializer(serializers.Serializer):

    json_data = serializers.JSONField()
    audio_file = serializers.FileField()

    def validate_audio_file(self, value):

        if not value.content_type.endswith('audio/mp3'):
            raise serializers.ValidationError("無効なファイル形式です。mp3ファイルのみ許可されています。")
        return value

    def validate_json_data(self, data):

        responses_serializer = ResponsesSerializer(data=data)
        responses_serializer.is_valid(raise_exception=True)
        return data