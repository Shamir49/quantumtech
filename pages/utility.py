from pages.models import *
def getCartCount(request):
    cartCount = 0
    if request.user.is_authenticated:
        customer,created = Customer.objects.get_or_create(user=request.user)
        cart, created = Cart.objects.get_or_create(customer=customer)
        cartCount = cart.cartCount
    else:
        try:
            deviceID = request.COOKIES['deviceID']
            customer, created = Customer.objects.get_or_create(deviceID=deviceID)
            cart, created = Cart.objects.get_or_create(customer=customer)
            cartCount = cart.cartCount
        except:
            cartCount = 0
    return cartCount




def processFilter(filters):
    filtersB = {
    "s1":"In Stock",
    "s2":"Pre Order",
    "s3":"up coming",
    "p1":"Intel",
    "p2":"AMD",
    "r1":"4 GB",
    "r2":'8 GB',
    "r3":'16 GB',
    'ss1':"128 GB",
    'ss2':'256 GB',
    'ss3':'512 GB',
    'ss4':'1 tb',
    'g1':'Shared / Integrated',
    'g2':'2 GB',
    'g3':'4 GB',
    'g4':'6 GB',
    'g5':'8 GB',
    'g6':'12 GB',
    'g7':'16 GB',
    'g8': '24 GB'
    }
    filters = filters.split(',')
    stock = []
    processor = []
    ram = []
    graphics = []
    ssd = []
    for i in range(len(filters)):
        if len(filters[i]) == 2:
            if (filters[i][0] == 's'):
                filters[i] = filtersB[filters[i]]
                stock.append(filters[i])
            elif filters[i][0] == 'p':
                filters[i] = filtersB[filters[i]]
                processor.append(filters[i])
            elif filters[i][0] == 'r':
                filters[i] = filtersB[filters[i]]
                ram.append(filters[i])
            elif filters[i][0] == 'g':
                filters[i] = filtersB[filters[i]]
                graphics.append(filters[i])
        elif len(filters[i]) == 3:
            if filters[i][0] == 's':
                ssd.append(filters[i])
    return stock, processor, ram, ssd, graphics