from celery import task
from django.core.mail import send_mail

from .models import Order


@task
def order_created(order_id):
    """Отправка e-mail при оформлении заказа"""
    order = Order.objects.get(id=order_id)
    subject = f'Заказ номер: {order.id}'
    message = f'Уважаемый {order.first_name}, Ваш заказ успешно составлен, ' \
              f'ID заказа {order.id}'
    mail_sent = send_mail(subject, message, 'admin@example.com', [order.email])

    return mail_sent
