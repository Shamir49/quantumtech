from django.urls import path 
from pages import views
urlpatterns = [
    path('',views.HomePage,name='home'),
    path('signIn',views.SignIn,name='signIn'),
    path('signUp',views.SignUp,name='signUp'),
    path('logout',views.Logout,name='logout'),
    path('product/<str:id>',views.ProductInside,name='productInside'),
    path('productView/<str:type>',views.ProductPage,name='productPage'),
    path('cartpage',views.CartPage,name='cartPage'),
    path('addtocart',views.addToCart,name='addtocart'),
    path('removefromcart',views.removeFromCart,name='removefromcart'),
    path('checkout',views.CheckoutPage,name='checkout'),
    path('pcBuilder',views.pcbuilder,name='pcBuilder'),
    path('pcBuilder/<str:type>',views.PCBuilderSuggestion,name='pcBuilderSuggestion'),
    path('addtopcbuilder',views.AddToPcBuilder,name='addToPcBuilder'),
    path('deletefrompcbuilder',views.DeleteFromPcBuilder,name='deleteFromPcBuilder'),
    path('search',views.SearchPage,name='search'),

    path('getCartCount',views.GetCartCount,name='getCartCount'),

    path('learnphp',views.learnPhp,name='learnphp')
]