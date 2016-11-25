from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404
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



def cart_add(request, product_id):
    """

    カートセッションに商品IDを追加

    """


    if not request.session.has_key('cart'):

        request.session['cart'] = list()

    cart = request.session['cart']

    cart.append(product_id)

    request.session['cart'] = cart


    products = get_list_or_404(Product)

    context = {'products': products}

    response = redirect('../../../ecommerce/cart_list/', context)

    return response



def cart_delete(request, product_id):
    """

    カートセッションから商品IDを削除

    """

    if not request.session.has_key('cart'):

        request.session['cart']

    cart = request.session['cart']


    cart = [item for item in cart if item is not str(product_id)]

    request.session['cart'] = cart


    products = get_list_or_404(Product)

    context = {'products': products}

    response = redirect('../../../ecommerce/cart_list/', context)

    return response



def cart_reset(request):
    """

    カートセッション内の商品IDをすべて削除

    """

    if not request.session.has_key('cart'):

        request.session['cart'] = list()

    del request.session['cart']


    products = get_list_or_404(Product)

    context = {'products': products}

    response = redirect('../../../ecommerce/cart_list/', context)

    return HttpResponse("カートの内容をクリアしました")



@login_required
def order_form(request):

    if 'cart' not in request.session:
        return HttpResponse("カートの中身が空です")

    products = []

    for item_id in request.session['cart']:
        items = Product.objects.get(id=int(item_id))
        products.append(items)

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
