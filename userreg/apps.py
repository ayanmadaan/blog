from django.apps import AppConfig


class userregConfig(AppConfig):
    name = 'userreg'

    def ready(self):
        import userreg.signals

