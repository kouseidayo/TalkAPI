from django.apps import AppConfig
from django.conf import settings
import os
import subprocess


def run_voicevox_server():
    subprocess.run(settings.VOICEVOX_SERVERRUN_PATH)

class ManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manager'

    #起動時の処理
    def ready(self):
        #環境変数の設定
        os.environ[settings.GOOGLE_API_ENVIRONMENT_VAR_NAME] = settings.GOOGLE_API_ENVIRONMENT_VAR_VALUE
        
        import threading
        # Djangoサーバーが起動するときにVOICEVOXサーバーを起動します
        voicevox_thread = threading.Thread(target=run_voicevox_server)
        voicevox_thread.start()
        # #VOICEVOXの起動
        # subprocess.run(settings.VOICEVOX_SERVERRUN_PATH)