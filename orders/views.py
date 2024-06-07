from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from orders.models import Order
from products.models import Product
from products.views import home_page


def create_order(request, slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=slug)
        quantity = int(request.POST['quantity'])
        address = request.POST['address']
        Order.objects.create(user=request.user, product=product, quantity=quantity, address=address)
        return redirect(home_page)
    else:
        product = get_object_or_404(Product, slug=slug)
    return render(request, 'create_order.html', {'product': product})


class OrderListView(View):
    def get(self, request):
        if request.user.is_staff:
            orders = Order.objects.all().order_by('-order_date')
        else:
            orders = Order.objects.filter(user=request.user).order_by('-order_date')
        return render(request, 'order_list.html', {'orders': orders})