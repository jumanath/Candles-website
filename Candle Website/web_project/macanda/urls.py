from django.urls import re_path
from . import views

urlpatterns = [

# ADMIN

    # ADMIN_LOGIN
    re_path(r'admin_home', views.admin_home, name='admin_home'),
    re_path(r'login_page',views.login_page,name='login_page'),
    re_path(r'login_form',views.login_form,name='login_form'),


    # MANAGE_PRODUCT

    re_path(r'^manage_products/$', views.manage_products, name='manage_products'),
    re_path(r'^newproduct/$', views.newproduct, name='newproduct'),
    re_path(r'^addproduct/$', views.addproduct, name='addproduct'),
    re_path(r'^createproduct/$', views.createproduct, name='createproduct'),
    re_path(r'^deletepdt/(\d+)/$',views.deletepdt,name='deletepdt'),
    re_path(r'^editpdt/(\d+)/$',views.editpdt,name='editpdt'),
    re_path(r'^updatepdt/(\d+)/$',views.updatepdt,name='updatepdt'),
    
    # MANAGE_OFFER
    re_path(r'manage_offer',views.manage_offer,name='manage_offer'),
    re_path(r'newoffer',views.newoffer,name='newoffer'),
    re_path(r'addoffer',views.addoffer,name='addoffer'),
    re_path(r'createoffer',views.createoffer,name='createoffer'),
    re_path(r'deleteoffer/(\d+)/$',views.deleteoffer,name='deleteoffer'),
    re_path(r'edit_offer/(\d+)/$',views.edit_offer,name='edit_offer'),
    re_path(r'updateoffer/(\d+)/$',views.updateoffer,name='updateoffer'),

    # MANAGE_IMAGES
    re_path(r'fileupload/', views.fileupload_view, name='fileupload'), 
    re_path(r'viewfile/', views.viewfile_view, name='viewfile'),
    re_path(r'deleteimage/(\d+)/$', views.deleteimage, name='deleteimage'),
    re_path(r'updateimg/(\d+)/$', views.updateimg, name='updateimg'),
    re_path(r'editimg/(\d+)/$', views.editimg, name='editimg'),


    # MANAGE_CARAOUSAL

    re_path(r'manage_carousal',views.manage_carousal,name='manage_carousal'),
    re_path(r'newcarousalimage',views.newcarousalimage,name='newcarousalimage'),
    re_path(r'addcarousal',views.addcarousal,name='addcarousal'),
    re_path(r'createcarousalimage',views.createcarousalimage,name='createcarousalimage'),
    re_path(r'deletecarousal/(\d+)/$',views.deletecarousal,name='deletecarousal'),
    re_path(r'editcarousal/(\d+)/$',views.editcarousal,name='editcarousal'),
    re_path(r'updatecarousal/(\d+)/$',views.updatecarousal,name='updatecarousal'),

    # MANAGE_ORDERS&CUSTOMERS

    re_path(r'manage_orders_customers',views.manage_orders_customers,name='manage_orders_customers'),

    
# USER
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^$', views.mainscreen, name='mainscreen'),

    # MANGE_LOGIN
    re_path(r'user_login',views.user_login,name='user_login'),
    re_path(r'register',views.register,name='register'),
    re_path(r'logout',views.logout_view,name='logout'),

    # WISHLIST
    re_path(r'^wishlist/add/(\d+)/$', views.add_to_wishlist, name='add_to_wishlist'),
    re_path(r'^wishlist/$', views.wishlist_view, name='wishlist'),
    re_path(r'^wishlist/remove/(\d+)/$', views.remove_wishlist, name='remove_wishlist'),

    # CART
    re_path(r'^cart/$', views.cart_page, name='cart'),
    re_path(r'^add_to_cart/(\d+)/$', views.add_to_cart, name='add_to_cart'),
    re_path(r'^remove_cart/(\d+)/$', views.remove_cart, name='remove_cart'),

# MANAGER

    # PAYMENT
    re_path(r'create-order/', views.create_order, name='create_order'),
    re_path(r'^payment/(\d+)/$', views.payment_page, name='payment_page'),
    re_path(r"save-order", views.save_order, name="save_order"),

    # MANAGER 
    re_path(r'^manager/$', views.manager, name='manager'),
    re_path(r'^manager_login/$', views.manager_login, name='manager_login'),
    re_path(r'^manager_form/$', views.manager_form, name='manager_form'),

    re_path(r'payment_options/$',views.payment_options,name='payment_options'),
    re_path(r'paid-orders/$',views.paid_orders,name='paid_orders'),
    re_path(r'cod-orders/$',views.cod_orders,name='cod_orders'),

    re_path(r'deliveryman_register',views.deliveryman_register,name='deliveryman_register'),
    re_path(r'view_deliveryman',views.view_deliveryman,name='view_deliveryman'),

# DELIVERYMAN
    re_path(r'deliveryman_login',views.deliveryman_login,name='deliveryman_login')
 





]
