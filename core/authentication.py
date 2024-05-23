from channels.middleware import BaseMiddleware
from rest_framework_simplejwt.exceptions import InvalidToken


class WSAuthentication(BaseMiddleware):

    async def __call__(self, scope, receive, send):
        try:
            token = self.validated_token(scope['headers'])
            scope['device'] = self.get_device(token)
        except InvalidToken:
            from management.models import AnonymousDevice
            scope['user'] = AnonymousDevice()
        return await super().__call__(scope, receive, send)

    def validated_token(self, headers):
        for key, value in headers:
            if key.lower() == b'authorization':
                return value

        raise InvalidToken("Token contained no recognizable user identification")

    def get_device(self, token):
        from management.models import Device
        try:
            return Device.objects.get(imei=token)

        except Device.DoesNotExist:
            from management.models import AnonymousDevice
            return AnonymousDevice()
