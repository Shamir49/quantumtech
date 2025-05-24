from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


generation_choices = (
    ("12th Gen",'12th gen'),
    ("8th Gen","8th gen"),
    ("9th Gen","9th gen"),
    ("10th Gen","10th gen"),
    ("11th Gen","11th gen"),
    ("13th Gen","13th gen"),
    ("No Gen","no gen")
)
ram_type = (
    ("DDR4","ddr4"),
    ('DDR5','ddr5'),
    ('DDR3','ddr3')
)


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer',null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    deviceID = models.CharField(max_length=200,blank=True,null=True)

    
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.deviceID
     
class Product(models.Model):
    name = models.CharField(max_length=300,blank=False,null=False)
    product_type = models.CharField(max_length=50,blank=False,null=False)
    product_sub_type = models.CharField(max_length=50,blank=False,null=False,default='')
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    stock = models.IntegerField()
    picture = models.ImageField(upload_to='images/',default='')
    ram_type = models.CharField(max_length=100,choices=ram_type,null=True,blank=True)

    #key Features
    model = models.CharField(max_length=150,blank=False,null=False,default='')
    feature1 = models.CharField(max_length=150,blank=False,null=False)
    feature2 = models.CharField(max_length=150,blank=False,null=False)
    feature3 = models.CharField(max_length=150,blank=False,null=False)
    feature4 = models.CharField(max_length=150,blank=False,null=False)
    generation = models.CharField(max_length=100,choices=generation_choices,null=True,blank=True)

    specs = models.JSONField()
    description = RichTextField()

    featured = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class Question(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='question')
    name = models.CharField(max_length=300,blank=False,null=False)
    question = models.TextField(blank=False,null=False)
    answer = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.product} - {self.name}'

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='review')
    name = models.CharField(max_length=300,blank=False,null=False)
    rating = models.IntegerField()
    review = models.TextField(blank=False,null=False)

    def __str__(self):
        return f'{self.name} - {self.rating}' 
    

class Cart(models.Model):
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='cart')

    @property
    def cartCount(self):
        cartItems = self.cartItems.filter(cart__customer=self.customer)
        total = 0
        for cartItem in cartItems:
            total += cartItem.quantity
        
        return total
    
    @property
    def TotalPrice(self):
        cartItems = self.cartItems.filter(cart__customer=self.customer)
        total = 0
        for cartItem in cartItems:
            total += cartItem.TotalPrice

        return total
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cartItems')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cartItem')
    quantity = models.IntegerField(default=0)
    
    @property
    def TotalPrice(self):
        return self.quantity * self.product.price


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='order')
    payment= models.BooleanField(default=False)
    
    @property
    def TotalPrice(self):
        orderItems = self.orderItems.filter(cart__customer=self.customer)
        total = 0
        for orderItem in orderItems:
            total += orderItem.TotalPrice

        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderItems')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='orderItem')
    quantity = models.IntegerField()

    @property
    def TotalPrice(self):
        return self.quantity * self.product.price

class OrderInfo(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name='orderInfo')
    name = models.CharField(max_length=250,null=False,blank=False)
    email = models.CharField(max_length=250,null=False,blank=False)
    phone = models.CharField(max_length=250,null=False,blank=False)
    address1 = models.CharField(max_length=250,null=False,blank=False)
    address2 = models.CharField(max_length=250,null=False,blank=False)
    message = models.TextField(null=True,blank=True)
    delivery = models.CharField(max_length=250,null=False,blank=False)

class PCBuilder(models.Model):

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='pcbuilder')
    processor = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderProcessor')
    cpu_cooler = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderCPUCooler')
    motherboard = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderMotherboard')
    ram = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderRam')
    storage = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderStorage')
    gpu = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderGPU')
    psu = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderPsu')
    casing = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderCasing')
    monitor = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderMonitor')
    casingCooler = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderCasingCooler')
    keyboard = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderKeyboard')
    mouse = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderMouse')
    antivirus = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderAntivirus')
    headphone = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderHeadphone')
    ups = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderUps')
    os = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='builderOs')

    generation = models.CharField(max_length=100,null=True,blank=True)
    ram_type = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f'{self.id}'