from core.celery import app
from utils.helpers import send_sms


@app.task
def send_verify_code(phone_number, code):
    """ """
    text = f"""
        НИКОМУ НЕ СООБЩАЙТЕ ЭТОТ КОД!!!
        Ваш код подтверждения: {code}
    """
    return send_sms(phone_number, text)
