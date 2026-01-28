import email
import json
import random
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import razorpay
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.utils.timezone import now


''' ADMIN '''

# ADMIN_LOGIN

def admin_home(request):
    return render(request, 'macanda/Admin/admin_home.html')

def login_page(request):
    return render(request, "macanda/Admin/admin_login.html")


def login_form(request):
    if request.method == "POST":
        username = request.POST.get('txtname')
        password = request.POST.get('txtPassword')
        

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_home')
        else:
            return render(request, 'macanda/Admin/admin_login.html',{ 'error': 'User does not exist or password is wrong'})

    return redirect('login_page')

# MNAGE PRODUTS




def manage_products(request):
    products = Product.objects.all()
    return render(request,'macanda/Admin/manage_products.html',{'products': products})


def newproduct(request):
    return render(request, 'macanda/Admin/addproduct.html')


def addproduct(request):
    return render(request,'macanda/Admin/addproduct.html')


def createproduct(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('txtname'),
            price=request.POST.get('price'),
            description=request.POST.get('txtdescription'),
            category=request.POST.get('category'),
            mfg_date=request.POST.get('mfg_date'),
            pdt_image=request.FILES.get('pdt_image')
        )
    return redirect('manage_products')



def deletepdt(request,pdtid):
    pdt=Product.objects.get(id=pdtid)
    pdt.delete()
    return redirect('manage_products')

def editpdt(request, pdtid):
    pdt = Product.objects.get(id=pdtid)
    return render(request, 'macanda/Admin/edit_product.html', {'pdt': pdt})

def updatepdt(request, pdtid):
    pdt = Product.objects.get(id=pdtid)
    pdt.name = request.POST['txtname']
    pdt.price= request.POST['price']
    pdt.description = request.POST['txtdescription']
    pdt.category = request.POST['category']
    pdt.mfg_date = request.POST['mfg_date']
    if 'pdt_image' in request.FILES:
        pdt.pdt_image = request.FILES['pdt_image']
    pdt.save()
    return redirect('manage_products')


# MNAGE_OFFER

def manage_offer(request):
    offers=Offer.objects.all()
    return render (request, 'macanda/Admin/manage_offer.html',{'Offer':offers})

def newoffer(request):
    return render (request,'macanda/Admin/addoffer.html')


def addoffer(request):
    offers = Offer.objects.all()
    return render(request, 'macanda/Admin/addoffer.html', { 'Offer': offers})


def createoffer(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        discount_percent = request.POST.get('discount_percent')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if not product_id:
            return render(request, 'macanda/Admin/addoffer.html', {'error': 'Product ID is required' })

        product_id = Product.objects.filter(id=product_id).first()

        if product_id is None:
            return render(request, 'macanda/Admin/addoffer.html', {'error': 'Invalid Product ID'})

        Offer.objects.create(
            product_id=product_id,
            discount_percent=discount_percent,
            start_date=start_date,
            end_date=end_date
        )

        return redirect('manage_offer')

def deleteoffer(request,offerid):
    offer=Offer.objects.get(id=offerid)
    offer.delete()
    return redirect('manage_offer')

def edit_offer(request, offerid):
    offer = Offer.objects.get(id=offerid)
    return render(request, 'macanda/Admin/edit_offer.html', {'offer': offer})

def updateoffer(request, offerid):
    offer = Offer.objects.get(id=offerid)
    offer.discount_percent = request.POST['discount_percent']
    offer.start_date=request.POST['start_date']
    offer.end_date=request.POST['end_date']
    offer.save()
    return redirect('manage_offer')

# MANAGE_IMAGES

def viewfile_view(request):
    images = fileupload.objects.all()
    return render(request, 'macanda/Admin/viewfile.html', {'images': images})

def fileupload_view(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            fileupload.objects.create(image=image)
            return redirect('viewfile')
    return render(request, 'macanda/Admin/fileupload.html')

def deleteimage(request,imgid):
    image = fileupload.objects.get(id=imgid)
    image.delete()
    return redirect('viewfile')

def editimg(request,imgid):
    image=fileupload.objects.get(id=imgid)
    return render (request, 'macanda/Admin/edit_img.html',{'image':image})


def updateimg(request, offerid):
    image = fileupload.objects.get(id=offerid)

    if request.method == "POST":
        if 'image' in request.FILES:
            image.image = request.FILES['image']
            image.save()

    return redirect('viewfile')



# MANAGE_CAROUSAL

def manage_carousal(request):
    carousal_image=carousalimage.objects.all()
    return render (request,'macanda/Admin/manage_carousal.html',{'carousalimage':carousal_image})

def newcarousalimage(request):
    return render (request, 'macanda/Admin/addcarousal.html')


def addcarousal(request):
    carousal = carousalimage.objects.all()
    return render(request, 'macanda/Admin/addcarousal.html', { 'carousalimage': carousal})


def createcarousalimage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        carousalimage.objects.create(
           image=image
        )

        return redirect('manage_carousal')

def deletecarousal(request,carousalid):
    image=carousalimage.objects.get(id=carousalid)
    image.delete()
    return redirect('manage_carousal')

def editcarousal(request, carousalid):
    image=carousalimage.objects.get(id=carousalid)
    return render(request, 'macanda/Admin/edit_carousal.html', {'carousal': image})

def updatecarousal(request, carousalid):
    image_obj = carousalimage.objects.get(id=carousalid)

    if request.method == 'POST':
        if 'image' in request.FILES:
            image_obj.image = request.FILES['image']
            image_obj.save()

    return redirect('manage_carousal')


# MANAGE_ORDERS&CUSTOMERS

def manage_orders_customers(request):
    users = User.objects.filter(is_staff=False)
    orders = Order.objects.select_related('user', 'product').order_by('-id')

    return render(
        request,
        'macanda/manager/manage_customers.html',
        {
            'users': users,
            'orders': orders
        }
    )




''' USER '''

def home(request):
    images = fileupload.objects.all()[:5]
    products = Product.objects.all()
    one_image = fileupload.objects.order_by('-id').first() 
    carousal_images = carousalimage.objects.all()  
    return render(request, 'macanda/User/home.html', {
        'one_image':one_image,
        'images': images,
        'products': products,
        'carousalimage':carousal_images
    })

# USER_LOGIN

def mainscreen(request):
    return render(request,'macanda/User/mainscreen.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('txtname')
        password = request.POST.get('txtPassword')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            LoginCustomer.objects.create(user=user)

            return redirect('home')
        else:
            return render(request, 'macanda/User/user_login.html', {
                'error': 'User does not exist or password is wrong'
            })

    return render(request, 'macanda/User/user_login.html')

# USER_REGISTER

def register(request):
    if request.method == "POST":
        username = request.POST.get('txtname')
        password = request.POST.get('txtPassword')
        cpassword = request.POST.get('txtconfirmpassword')

        if password != cpassword:
            return render(request, 'macanda/User/register.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'macanda/User/register.html', {
                'error': 'User already exists'
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('user_login')

    return render(request, 'macanda/User/register.html')


# """"""""LOGOUT"""""""

def logout_view(request):
    logout(request)
    return redirect('user_login')

# """"""""ADD_TO_WISHLIST"""""""

@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)

    Wishlist.objects.create(
        user=request.user,
        product=product
    )

    return redirect('wishlist')

@login_required
def wishlist_view(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'macanda/User/wishlist.html', {'items': items})

@login_required
def remove_wishlist(request, item_id):
    Wishlist.objects.filter(id=item_id, user=request.user).delete()
    return redirect('/wishlist/')


# """"""""ADD_TO_CART"""""""

@login_required
def add_to_cart(request, product_id):
    cart_item = cart.objects.filter(
        user=request.user,
        product_id=product_id
    ).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart.objects.create(
            user=request.user,
            product_id=product_id,
            quantity=1
        )

    return redirect('cart')

@login_required
def cart_page(request):
    cart_items = cart.objects.filter(user=request.user)

    return render(
        request,
        'macanda/User/cart.html',
        {
            'cart_items': cart_items   
        }
    )


@login_required
def remove_cart(request, cart_id):
    cart.objects.filter(id=cart_id, user=request.user).delete()
    return redirect('cart')



''' MANAGER MODULE'''

def manager_login(request):
    return render(request, "macanda/manager/manager_login.html")


def manager_form(request):
    if request.method == "POST":
        username = request.POST.get('txtname')
        password = request.POST.get('txtPassword')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('manager')
        else:
            return render(
                request,
                'macanda/manager/manager_login.html',
                {'error': 'User does not exist or password is wrong'}
            )

    return redirect('manager_login')


@login_required(login_url='manager_login')
def manager(request):
    return render(request, 'macanda/manager/manager.html')


# """"""""PAYMENT"""""""


client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)

def create_order(request):
    amount = int(request.GET.get('amount')) * 100  # rupees → paise

    order = client.order.create({
        'amount': amount,
        'currency': 'INR',
        'payment_capture': 1
    })

    return JsonResponse({
        'order_id': order['id'],
        'amount': amount,
        'key': settings.RAZORPAY_KEY_ID
    })
def payment_page(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'macanda/manager/payment.html', {
        'product': product,
        'amount': int(product.price * 100),  # paise for Razorpay
        'razorpay_key': settings.RAZORPAY_KEY_ID,
    })



@login_required
def save_order(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    try:
        data = json.loads(request.body)

        product = Product.objects.get(id=data["product_id"])
        payment_method = data["payment_method"]
        payment_status = data["payment_status"]

        # 🔐 Server-side validation
        if payment_method == "COD":
            payment_status = "Pending"
            order_status = "Confirmed"
        elif payment_method == "Online":
            payment_status = "Paid"
            order_status = "Confirmed"
        else:
            return JsonResponse({"error": "Invalid payment method"}, status=400)

        Order.objects.create(
            user=request.user,
            product=product,
            amount=product.price,  
            payment_method=payment_method,
            payment_status=payment_status,
            status=order_status
        )

        return JsonResponse({
            "success": True,
            "redirect_url": reverse("home")
        })

    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def payment_options(request):
    return render(request, 'macanda/manager/payment_options.html')

def paid_orders(request):
    orders = Order.objects.filter(payment_status="Paid")
    return render(
        request,
        'macanda/manager/paid_orders.html',
        {'orders': orders}
    )


def cod_orders(request):
    orders = Order.objects.filter(payment_method="COD")
    return render(
        request,
        'macanda/manager/cod_orders.html',
        {'orders': orders}
    )
    
def deliveryman_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        vehicle_no = request.POST.get('vehicle_no')

        DeliveryMan.objects.create(
            name=name,
            email=email,
            phone=phone,
            vehicle_no=vehicle_no,
        )

        request.session['deliveryman_email'] = email  # 🔑 KEY LINE

        return redirect('otp_verification')

    return render(request, 'macanda/manager/deliveryman_register.html')


def edit_deliveryman(request, did):
    delivery_man = DeliveryMan.objects.get(id=did)

    if request.method == 'POST':
        delivery_man.phone = request.POST.get('phone')
        delivery_man.vehicle_no = request.POST.get('vehicle_no')

        email = request.POST.get('email')
        if email:  # 🔑 critical line
            delivery_man.email = email

        delivery_man.save()
        return redirect('view_deliveryman')

    return render(
        request,
        'macanda/manager/edit_deliveryman.html',
        {'boy': delivery_man}
    )


def delete_deliveryman(request, did):
    delivery_man = DeliveryMan.objects.get(id=did)
    delivery_man.delete()
    return redirect('view_deliveryman')

def view_deliveryman(request):
    delivery_boys = DeliveryMan.objects.all()
    return render(
        request,
        'macanda/manager/view_deliveryman.html',
        {'delivery_boys': delivery_boys}
    )
def otp_verification(request):
    email = request.session.get('deliveryman_email')
    if not email:
        return redirect('deliveryman_register')

    if request.method == "POST":
        otp = random.randint(100000, 999999)

        deliveryman = DeliveryMan.objects.get(email=email)
        deliveryman.otp = otp
        deliveryman.save()

        send_mail(
            'OTP Verification',
            f'Your OTP is {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return redirect('view_deliveryman')

    return render(request, 'macanda/manager/otp_verification.html')

 

''' MANAGER MODULE'''

def deliveryman_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        otp = request.POST.get('otp')

        try:
            deliveryman = DeliveryMan.objects.get(email=email, otp=otp)
            request.session['deliveryman_id'] = deliveryman.id
            return redirect('deliveryman_dashboard')
        except DeliveryMan.DoesNotExist:
            return render(request, 'macanda/deliveryman/deliveryman_login.html', {
                'error': 'Invalid email or OTP'
            })

    return render(request, 'macanda/deliveryman/deliveryman_login.html')


def deliveryman_dashboard(request):
    today = now().date()

    orders = Order.objects.filter(
        created_at__date=today
    ).order_by('-created_at')

    return render(
        request,
        'macanda/deliveryman/deliveryman_dashboard.html',
        {'orders': orders}
    )



                  

           



            
