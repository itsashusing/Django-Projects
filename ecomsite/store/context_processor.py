<<<<<<< HEAD
from .models import Category
from cart.models import Cart, CartItem
from cart.views import _cart_id


def categories_links(request):
    links = Category.objects.all()
    return dict(links=links)


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {cart_count: 12}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)


=======
from .models import Category
from cart.models import Cart, CartItem
from cart.views import _cart_id


def categories_links(request):
    links = Category.objects.all()
    return dict(links=links)


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {cart_count: 12}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)


>>>>>>> 1b920148f1a38f4fbf6aa142e7f7c9e4481a5ad6
