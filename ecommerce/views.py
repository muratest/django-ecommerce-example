from django.http import HttpResponse
from django.shortcuts import render
from ecommerce.models import Product, Payment, Order


def index(request):
    return HttpResponse("Hello, world. You're at the ecommerce index.")


def order_form(request):
    if request.method == 'POST':

        # 注文をPOST

        return HttpResponse('注文しました')

    # あとでセッションから一覧持ってくる
    products = Product.objects.all()

    payments = Payment.objects.all()

    # オーダー画面

    return render(request, 'order.html', {'products': products, 'payments': payments})


def order_execute(request):
    if request.method != 'POST':
        return HttpResponse('Bad request', status_code=400)

    payment = Payment.objects.get(id=request.POST['payment'])

    # あとでセッションから一覧持ってくる
    products = Product.objects.all()

    Order.objects.create(payment=payment, products=products)

    return render(request, 'order_complete.html', {'products': 'products', 'payments': 'payments'})
