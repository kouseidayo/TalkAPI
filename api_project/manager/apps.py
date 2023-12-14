from django.apps import AppConfig
from django.conf import settings
import os

class ManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manager'

    #起動時の処理
    def ready(self):
        #環境変数の設定
        os.environ[settings.GOOGLE_API_ENVIRONMENT_VAR_NAME] = settings.GOOGLE_API_ENVIRONMENT_VAR_VALUE