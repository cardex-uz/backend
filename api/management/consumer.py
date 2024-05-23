from channels.generic.websocket import AsyncJsonWebsocketConsumer

from management.choices import ComputingDeviceStatus


class TaskConsumer(AsyncJsonWebsocketConsumer):
    """ """

    async def connect(self):
        device = self.scope['device']
        if device.is_authenticated:
            device.set_waiting()
            await self.channel_layer.group_add(f"notifications_{device.imei}", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        device = self.scope['device']
        if device.is_authenticated:
            device.set_offline()
            await self.channel_layer.group_discard(f"notifications_{device.imei}", self.channel_name)
        await self.close(code)

    async def send_task(self, event):
        await self.send_json(
            {
                "type": "task",
                "message": event["message"]
            }
        )

