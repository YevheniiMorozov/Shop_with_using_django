from django.shortcuts import render

from .models import OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart

from .task import order_created


def create_order(request):
    cart = Cart(request)
    if request.method == "POST":
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
                cart.clear()
                order_created.delay(order.id)
                return render(request, "order/created.html", {'order': order})
    else:
        form = CreateOrderForm
        return render(request, "order/create.html", {"cart": cart, 'form': form})
