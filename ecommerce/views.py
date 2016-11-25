from django.http import HttpResponse
from django.shortcuts import render
from ecommerce.models import Product, Payment, Order, Order_Product, Customer

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the ecommerce index.")

def cart_list(request):
  """
  カートに入っている商品情報を表示する
  """
  if not request.session.has_key('cart'):
    request.session['cart'] = list()
  cart = request.session['cart']

  products = Product.objects.filter(id__in=cart)
  context = {'products': products}
  return render(request, 'cart_list.html', context)


@login_required
def order_form(request):
    # あとでセッションから一覧持ってくる
    products = Product.objects.all()

    # 決済方法一覧を取得
    payments = Payment.objects.all()

    # オーダー画面

    return render(request, 'order.html', {'products': products, 'payments': payments})


def order_execute(request):
    if request.method != 'POST':
        return HttpResponse('Bad request')

    # 決済方法をPOSTリクエストから取得
    payment = Payment.objects.get(id=request.POST['payment'])

    # あとでセッションから一覧持ってくる
    products = Product.objects.all()
    customer = Customer.objects.get(first_name='a', last_name='a')

    payment = Payment.objects.get(id=int(request.POST['payment']))

    # 注文作成
    order = Order.objects.create(customer=customer, payment=payment)

    for product in products:
        # 注文対象商品をとりあえず1個ずつ持ってきて注文と関連づけ
        item_order = Order_Product(
            product=product, count=1, price=product.price, order=order)
        item_order.save()

    return render(request, 'order_complete.html', {'products': products, 'payment': payment})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def create_user_form(request):

    return render(
        request,
        'registration/create_user_form.html',
    )


def create_user(request):

    username = request.POST['username']
    password = request.POST['password']

    if not username or not password:
        return HttpResponseBadRequest()

    if User.objects.filter(username=username).exists():
        return HttpResponseBadRequest()

    user = User.objects.create_user(username, '', password)
    user.save()

    return render(request, 'registration/create_user_complete.html')

def order_history(request):
    # セッションからログインしているカスタマIDを持ってくる
    customerId = 1
    orders = Order.objects.get(Customer=customerId).select_related()
    payments = Payment.objects.all() # 支払方法を全件取得

    print(orders)
    return rendere(request, 'order_history.html', {'orders': orders})
