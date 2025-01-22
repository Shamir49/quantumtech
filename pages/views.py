from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from pages.models import *
from pages.forms import *
from django.http import JsonResponse
import json
from pages.utility import getCartCount, processFilter
# Create your views here.

def SearchPage(request):
    search = request.GET.get('search')

    products = Product.objects.filter(name__icontains=search)
    cartcount = getCartCount(request)
    return render(request,'search.html',{'products':products,'cartCount':cartcount,'searchText':search})



def HomePage(request):
    fproducts = Product.objects.filter(featured=True)
    cart = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(customer=request.user.customer)
    else:
        pass 
    cartCount = getCartCount(request)
    return render(request,'home.html',{'fproducts':fproducts,'cart':cart,'cartCount':cartCount})


def SignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                username = user.username
            except:
                username = username
                
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials!')
    cartCount = getCartCount(request)
    return render(request,'signin.html',{'cartCount':cartCount})

def SignUp(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists!')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists!')
        else:
            if password1 != password2:
                messages.error(request,'Passwords do not match!')
            else:
                user = User.objects.create_user(first_name=name,username=username,email=email,password=password1)
                customer = Customer.objects.create(user=user,email=email,name=name)
                if user is not None:
                    user.save()
                    customer.save()
                    auth.login(request,user)
                    return redirect('/')
                
    cartCount = getCartCount(request)
    return render(request,'signup.html',{'cartCount':cartCount})


def Logout(request):
    auth.logout(request)
    return redirect('/')

def ProductPage(request,type):
    filters = request.GET.get('filter')
    products = None

    if type == 'desktop':
        products = Product.objects.filter(product_type='desktop')
        if filters != None:
            stock, processor, ram, ssd, graphics = processFilter(filters)
            if processor != []:
                products = products.filter(brand__in=processor)
            if ram != []:
                
                products = products.raw("SELECT name, product_type, product_sub_type, price, brand, stock, picture, ram_type, model, feature1, feature2, feature3, feature4,generation, specs.Basic Information.RAM AS ram WHERE ram LIKE '%16 GB%' FROM pages_Products WHERE specs")
        
    elif type == 'laptop':
        products = Product.objects.filter(product_type='laptop')
    elif type == 'component':
        products = Product.objects.filter(product_type='component')
    elif type == 'monitor':
        products = Product.objects.filter(product_type='monitor')
    elif type == 'ups':
        products = Product.objects.filter(product_type='ups')
    elif type == 'tablet':
        products = Product.objects.filter(product_type='tablet')
    elif type == 'camera':
        products = Product.objects.filter(product_type='camera')
    elif type == 'security':
        products = Product.objects.filter(product_type='security')
    elif type == 'networking':
        products = Product.objects.filter(product_type='networking')
    elif type == 'software':
        products = Product.objects.filter(product_type='software')
    elif type == 'accessories':
        products = Product.objects.filter(product_type='accessories')
    cartCount = getCartCount(request)
    return render(request,'productPage.html',{'products':products,'cartCount':cartCount,'type':type})

def ProductInside(request,id):
    id = int(id)
    product = Product.objects.get(id=id)
    form1 = QuestionForm()
    form2 = ReviewForm()
    questions = Question.objects.filter(product=id)
    reviews = Review.objects.filter(product=id)

    if request.method == 'POST':
        f1 = QuestionForm(request.POST)
        print(request.POST)
        if f1.is_valid():
            f1.save()
            print('Question submitted!')
            messages.error(request,'Question submitted successfully!')
            
    if request.method == 'POST':
        f2 = ReviewForm(request.POST)
        if f2.is_valid():
            f2.save()
            messages.error(request,'Review submitted successfully!')

    cartCount = getCartCount(request)
    return render(request,'ProductInside.html',{'product':product,'form1':form1,'form2':form2,'questions':questions,'reviews':reviews,'cartCount':cartCount})



def CartPage(request):
    cart = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(customer=request.user.customer)
        cartItems = cart.cartItems.filter(cart__customer=request.user.customer)
    else:
        deviceID = request.COOKIES['deviceID']
        customer, created = Customer.objects.get_or_create(deviceID=deviceID)
        cart, created = Cart.objects.get_or_create(customer=customer)
        cartItems = cart.cartItems.filter(cart__customer=customer)
    cartCount = getCartCount(request)
    return render(request,'cartPage.html',{'cart':cart,'cartItems':cartItems,'cartCount':cartCount})



def addToCart(request):
    data = json.loads(request.body)['data']
    print(data)

    cart = None 
    customer = None
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        cart, created = Cart.objects.get_or_create(customer=customer)
    else:
        deviceID = request.COOKIES['deviceID']
        customer, created = Customer.objects.get_or_create(deviceID=deviceID)
        cart, created = Cart.objects.get_or_create(customer=customer)

    product = Product.objects.get(id=data['id'])
    cartItem, created = CartItem.objects.get_or_create(cart=cart,product=product)
    cartItem.quantity += 1
    cartItem.save()
    
    cartCount = cart.cartCount
    return JsonResponse(cartCount,safe=False)

def removeFromCart(request):
    data = json.loads(request.body)['data']
    cartcount = 0
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(customer=customer)
        product = Product.objects.get(id=data['id'])
        cartItem = CartItem.objects.get(cart=cart,product=product)
        cartItem.delete()
        cartcount = cart.cartCount
    else:
        deviceID = request.COOKIES['deviceID']
        customer = Customer.objects.get(deviceID=deviceID)
        cart = Cart.objects.get(customer=customer)
        product = Product.objects.get(id=data['id'])
        cartItem = CartItem.objects.get(cart=cart,product=product)
        cartItem.delete()
        cartcount = cart.cartCount

    return JsonResponse(cartcount,safe=False)




def CheckoutPage(request):
    cart = None
    cartItems = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(customer=request.user.customer)
        cartItems = cart.cartItems.filter(cart__customer=request.user.customer)
        customer = request.user.customer
    else:
        deviceID = request.COOKIES['deviceID']
        customer, created = Customer.objects.get_or_create(deviceID=deviceID)
        cart, created = Cart.objects.get_or_create(customer=customer)
        cartItems = cart.cartItems.filter(cart__customer=customer)
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        phone = request.POST['phone']
        message = request.POST['message']
        delivery = request.POST['delivery']

        order = Order.objects.create(customer=customer)
        if (delivery == 'Online Payment'):
            order.payment = True
        order.save()

        for cartItem in cartItems:
            orderItem = OrderItem.objects.create(order=order,product=cartItem.product,quantity=cartItem.quantity)
            orderItem.save()
        
        orderInfo = OrderInfo.objects.create(order=order,name=name,email=email,address1=address1,address2=address2,phone=phone,message=message,delivery=delivery)
        orderInfo.save()
        cart.delete()
        return render(request,'order_placed.html',{})

    cartCount = getCartCount(request)


    return render(request,'checkout.html',{'cart':cart,'cartItems':cartItems, 'cartCount':cartCount})


def pcbuilder(request):
    cartCount = getCartCount(request)
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
    else:
        deviceID = request.COOKIES['deviceID']
        customer = Customer.objects.get(deviceID=deviceID)

    pcbuilder, created = PCBuilder.objects.get_or_create(customer=customer)

    return render(request,'pc_builder.html',{'cartCount':cartCount,'pcbuilder':pcbuilder})


def PCBuilderSuggestion(request,type):
    try:
        components = Product.objects.filter(product_sub_type=type)

    except:
        components = None

    return render(request,'pc_builder_suggestion.html',{'type':type,'components':components})

def AddToPcBuilder(request):
    data = json.loads(request.body)['data']
    product = Product.objects.get(id=data['id'])
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
    else:
        deviceID = request.COOKIES['deviceID']
        customer,created = Customer.objects.get_or_create(deviceID=deviceID)

    pcbuilder,created = PCBuilder.objects.get_or_create(customer=customer)

    if product.product_sub_type == 'processor':
        pcbuilder.processor = product
        pcbuilder.generation = product.generation
        pcbuilder.ram_type = product.ram_type
        pcbuilder.save()

    elif product.product_sub_type == 'motherboard':
        pcbuilder.motherboard = product
        pcbuilder.generation = product.generation
        pcbuilder.ram_type = product.ram_type
        pcbuilder.save()
    elif product.product_sub_type == 'cpu cooler':
        pcbuilder.cpu_cooler = product
        pcbuilder.save()
    elif product.product_sub_type == 'ram':
        pcbuilder.ram = product
        pcbuilder.ram_type = product.ram_type
        pcbuilder.save()
    elif product.product_sub_type == 'graphics card':
        pcbuilder.gpu = product
        pcbuilder.save()
    elif product.product_sub_type == 'storage':
        pcbuilder.storage = product
        pcbuilder.save()
    elif product.product_sub_type == 'power supply':
        pcbuilder.psu = product
        pcbuilder.save()
    elif product.product_sub_type == 'casing':
        pcbuilder.casing = product
        pcbuilder.save()
    elif product.product_sub_type == 'monitor':
        pcbuilder.monitor = product
        pcbuilder.save()
    elif product.product_sub_type == 'casing cooler':
        pcbuilder.casingCooler = product
        pcbuilder.save()
    return JsonResponse({"200":"ok"},safe=False)


def DeleteFromPcBuilder(request):
    data = json.loads(request.body)['data']
    print(data)

    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
    else:
        deviceID = request.COOKIES['deviceID']
        customer,created = Customer.objects.get_or_create(deviceID=deviceID)

    pcbuilder = PCBuilder.objects.get(customer=customer.id)
    if data['id'] == 'processor':
        print('processor deleted')
        pcbuilder.processor = None
        pcbuilder.save()
    
    elif data['id'] == 'motherboard':
        print('motherboard deleted')
        pcbuilder.motherboard = None
        pcbuilder.save()
    elif data['id'] == 'cpu cooler':

        pcbuilder.cpu_cooler = None
        pcbuilder.save()
    
    elif data['id'] == 'ram':
        print('processor deleted')
        pcbuilder.ram = None
        pcbuilder.save()

    elif data['id'] == 'storage':
        print('storage deleted')
        pcbuilder.storage = None
        pcbuilder.save()
    elif data['id'] == 'gpu':
        
        pcbuilder.gpu = None
        pcbuilder.save()
    elif data['id'] == 'psu':
       
        pcbuilder.psu = None
        pcbuilder.save()
    elif data['id'] == 'casing':
        pcbuilder.casing = None
        pcbuilder.save()
    elif data['id'] == 'monitor':
        pcbuilder.monitor = None
        pcbuilder.save()
    elif data['id'] == 'casing cooler':
        pcbuilder.casingCooler = None
        pcbuilder.save()
    
    
    return JsonResponse({'status':200},safe=False)


def GetCartCount(request):
    cartCount = 0
    if request.user.is_authenticated:
        cartCount = request.user.customer.cart.cartCount
    else:
        deviceID = request.COOKIES['deviceID']
        customer, created = Customer.objects.get_or_create(deviceID=deviceID)
        cart, created = Cart.objects.get_or_create(customer=customer.id)
        cartCount = cart.cartCount

    return JsonResponse({'cartCount':cartCount},safe=False)



def learnPhp(request):

    return render(request,'learn_php.php',{})