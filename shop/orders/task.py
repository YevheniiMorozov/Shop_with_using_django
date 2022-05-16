from shop.celery import app

from django.core.mail import send_mail
from .models import Order


@app.task()
def order_created(order_id):
    """

    Mailing that order is created

    """
    order = Order.object.get(id=order_id)
    subj = f"Order {order_id}"
    message = f"Hi {order.first_name} \n\n Your order was successfully completed. It id is {order.id}"

    mail_sent = send_mail(subj, message, 'admin@osh.com', [order.email])

    return mail_sent