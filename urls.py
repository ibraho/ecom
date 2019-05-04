

from django.urls import path,re_path
from .import views 
from django.views.generic import ListView
app_name="ecom"
urlpatterns=[
  path('retry-payment/<order_id>', views.retry_payment, name='retry_payment'),
  path('process-payment/', views.payment_process, name='payment_process'),


  #path('', views.show_cat, name='show_cat',),
  path('accounts/profile/', views.profile, name='profile',),
  path('search/', views.search, name='search',),
  path('all/<category_slug>/', views.all_products, name='all_products',),
  path('subcat/<sub_category_slug>/', views.all_products, name='all_products',),
  path('all/<query>/', views.all_products, name='all_products',),
  path('all/', views.all_products, name='all_products',),
  path('delete-unpaid/', views.delete_unpaid_order, name='delete_unpaid_order',),
  path('rate_order/<rated_id>/',views.rate,name='rate'),
  path('', views.index, name='index'),

  path('add_wish/<id>',views.add_wish,name='add_wish'),
  path('delete-order/<id>',views.delete_order,name='delete_order'),

  path('remove_wish/<id>',views.remove_wish,name='remove_wish'),
  path('create_order/',views.create_order,name='create_order'),
  path('product/<id>/<slug>/',views.post_detail,name='post_detail'),
  path('one_order/<post_id>/<color>/<extra>/',views.one_order,name='one_order'),
  path('one_order/<post_id>/',views.one_orders,name='one_orders'),

  path('delete-one_order/<order_id>',views.remove_order,name='remove_order'),


    
 ]