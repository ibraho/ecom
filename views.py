from django.shortcuts import render ,get_object_or_404,redirect,render_to_response
from django.http import  HttpResponse
from.models import *
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import *
from django.db.models import Q
from django.http import JsonResponse
from taggit.models import Tag
from django.urls import reverse
from django.db.models import Count
from django.db.models import Count, Min, Sum, Avg,Max
from django.db.models import F
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.shortcuts import render, redirect
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from decimal import Decimal
from datetime import datetime

def search (request):
    query=request.GET.get('search')
    cate=Category.objects.all()

    if query:
       posts=Post.objects.all().filter(out_of_stock=False )
       queries=posts.filter(
            Q(title__icontains=query)|
            Q(category__name__icontains=query)).distinct()
       posts=queries
       pik=posts

    if pik:
        papi=pik.aggregate(Min('price'),Max('price'))
    paginator=Paginator(posts,8)
    page= request.GET.get('page')
    post=paginator.get_page(page)
    dic={'post':post,'page':page ,'papi':papi,'cate':cate}

    return render (request, 'home.html',dic)
def index(request):

    cart = Cart(request)
    query=request.GET.get('search')
    cate=Category.objects.all()
    if query:
        return all_products(request)
    posts=Post.objects.all().filter(out_of_stock=False )
    cate=Category.objects.all()
    dic={'posts':posts,'cate':cate,'cart':cart,}


    return render (request, 'index.html',dic)




def payment_process(request):
    cate=Category.objects.all()
    cart = Cart(request)
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    orders =Order.objects.filter(id=order_id)
    host = request.get_host()
    paypal_dict = {
             'business': settings.PAYPAL_RECEIVER_EMAIL,
             'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
             'item_name': 'Order {}'.format(order.id),
             'invoice': str(order.id),
             'currency_code': 'USD',
             'notify_url': 'http://{}{}'.format(host,
             reverse('paypal-ipn')),
             
             'return_url': 'http://{}{}'.format(host,
             reverse('ecom:all_products')),
             'cancel_return': 'http://{}{}'.format(host,
             reverse('ecom:delete_unpaid_order')),   }
    form = PayPalPaymentsForm(initial=paypal_dict)
    dic={'order': order, 'orders':orders,'form':form,'cate':cate,'cart':cart}
    return render(request,'process.html',dic)


def retry_payment(request,order_id):
    cate=Category.objects.all()
    cart = Cart(request)

    order_id=order_id
    order = get_object_or_404(Order, id=order_id)
    orders =Order.objects.filter(id=order_id)
    host = request.get_host()
    paypal_dict = {
             'business': settings.PAYPAL_RECEIVER_EMAIL,
             'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
             'item_name': 'Order {}'.format(order.id),
             'invoice': str(order.id),
             'currency_code': 'USD',
             'notify_url': 'http://{}{}'.format(host,
             reverse('paypal-ipn')),
             
             'return_url': 'http://{}{}'.format(host,
             reverse('ecom:all_products')),
             'cancel_return': 'http://{}{}'.format(host,
             reverse('ecom:delete_unpaid_order')),   }
    form = PayPalPaymentsForm(initial=paypal_dict)
    dic={'order': order, 'orders':orders,'form':form,'cate':cate,'cart':cart,}
    return render(request,'payment/process.html',dic)


def delete_unpaid_order(request):

    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect(reverse('ecom:all_products'))

def delete_order(request, id):
    if request.is_ajax():
        order = get_object_or_404(Order, id=id)
        
        order.delete()
        
        data={
        'message':'Order is deleted'
        }
        return JsonResponse(data)  

def create_order(request):
    cart = Cart(request)
    profile_form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        order=Order.objects.create(profile=request.user.profile,shipping_address=profile_form)
        
        for item in cart:
            rat=Ratings.objects.create(profile=request.user.profile,feedback=None,order=order,rate=0,posti=item['post'])
            OrderItems.objects.create(profile=request.user.profile,order=order,product=item['post'],
                price=item['price'],rated=rat, quantity=item['quantity'], color=item['color'], extra=item['extra'])
    #cart.clear()


        request.session['order_id'] = order.id
    
    return redirect(reverse('ecom:payment_process'))




def one_order(request,post_id,color,extra):
    profile_form = ProfileForm(instance=request.user.profile)
    item=request.GET.get('item')
    post=get_object_or_404(Post,id=post_id)
    if request.method == 'POST'and 'one_order' in request.POST:
        order=Order.objects.create(profile=request.user.profile,shipping_address=profile_form)
        rate=Ratings.objects.create(profile=request.user.profile,feedback=None,order=order,posti=post)
        OrderItems.objects.create(profile=request.user.profile,order=order,
             product=post,price=post.price,rated=rate, quantity=1,color=color,extra=extra)
    
        request.session['order_id'] = order.id

    return redirect(reverse('ecom:payment_process'))
def one_orders(request,post_id):
    profile_form = ProfileForm(instance=request.user.profile)
    item=request.GET.get('item')
    post=get_object_or_404(Post,id=post_id)
    if request.method == 'POST'and 'one_order' in request.POST:
        order=Order.objects.create(profile=request.user.profile,shipping_address=profile_form)
        rate=Ratings.objects.create(profile=request.user.profile,feedback=None,order=order,posti=post)
        OrderItems.objects.create(profile=request.user.profile,order=order,
             product=post,price=post.price,rated=rate, quantity=1,)
    
        request.session['order_id'] = order.id

    return redirect(reverse('ecom:payment_process'))



def rate(request,rated_id):

    #if request.is_ajax():
    rated= Ratings.objects.get(id=rated_id)
    star=request.GET.get('star')
    feed=request.GET.get('feedback')
    

    if request.is_ajax():
        Ratings.objects.filter(id=rated_id).update(rate=star,feedback=feed)

            


        data={
        'message':'This order item is rated'
        }
        return JsonResponse(data)



def remove_order(request,order_id):

    #if request.is_ajax():
 
    order=Order.objects.get(id=order_id)
    order.delete()

       

    return HttpResponse("Multiple objects created")




@login_required
@transaction.atomic
def profile(request  ):
    profile_id=request.user.profile
    my_orders = Order.objects.filter(profile=request.user.profile)
    my_feedback = Ratings.objects.filter(profile=request.user.profile)

    the_tim=int(datetime.now().strftime('%d'))-3
    my_orders = Order.objects.filter(profile=request.user.profile)
    for orde in  my_orders:
        if int(orde.order_time.strftime('%d')) <= the_tim and orde.paid == False:
            orde.delete()
        
        
      
            
    fav=Profile.objects.all()
    cart = Cart(request)
    cart_product_form = CartAddProductForm()
    post=Post.objects.all().filter(out_of_stock=False )
    query=request.GET.get('search')
    cate=Category.objects.all()
    if query:
        return search(request)
    if request.method == 'POST' and 'btnform2' in request.POST:
        photo_form = PhotoForm(request.POST,request.FILES, instance=request.user.profile)
        if photo_form.is_valid():
            photo_form.save()
    else:

        photo_form=PhotoForm(instance=request.user.profile)

    if request.method == 'POST' and 'btnform1' in request.POST:

        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        
        if profile_form.is_valid():
          
            
            profile_form.save() 
           
    else:
        
        profile_form = ProfileForm(instance=request.user.profile)
    wish=Profile.objects.all()
        
    dic={
     "photo_form":photo_form,
     "profile_form":profile_form ,'cate':cate,'query':query,
     "wish":wish,"post":post,"cart":cart,'fav':fav,  'cart_product_form':cart_product_form,
     "my_orders":my_orders,'my_feedback':my_feedback,}
    return render(request, 'profile.html' ,dic)




   

def all_products(request,category_slug=None,sub_category_slug=None):
    fav=Profile.objects.all()

    cart = Cart(request)
    cart_product_form = CartAddProductForm()
    cate=Category.objects.all()
    sub=SubCategory.objects.all()
    #sub=None

    posts=None
    posts=Post.objects.all().filter(out_of_stock=False )
    query=request.GET.get('search')
    pik=None
    papi=None
    query=request.GET.get('search')
    pox = Post.objects.all().filter(out_of_stock=False)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        posts=posts.filter(category=category)
        #sub=SubCategory.objects.all().filter(category__in=category)
        pik=posts
    if sub_category_slug:
        sub_category=get_object_or_404(SubCategory,slug=sub_category_slug)
        posts=posts.filter(subo_category=sub_category)
        #sub=SubCategory.objects.all().filter(category__in=category)
        pik=posts

    if query:
       posts=Post.objects.all().filter(out_of_stock=False )
       queries=posts.filter(
            Q(title__icontains=query)).distinct()
       posts=queries
       pik=posts
    reduced=request.GET.get('reduced')# get the reduced price from the "reduced" name on form
    if reduced:   
        posts=posts.filter(out_of_stock=False ,price_before__gte=F('price')).exclude(price_before__isnull=reduced )

        
    high=request.GET.get('high')# get the high price from the "high" name on form
    if high:
        high="-price"
        posts=posts.order_by("-price")
    low=request.GET.get('low')# get the low price from the "low" name on form
    if low:
        posts=posts.order_by("price")
    
    min_price=request.GET.get('mini')# get the min price from the "min" name on form
    max_price=request.GET.get('maxi')# get the max price from the "maxi" name on form
    if min_price and max_price:
        posts=posts.filter(price__range=(min_price, max_price))
    if pik:
        papi=pik.aggregate(Min('price'),Max('price'))
    number=request.GET.get('number')# get the high price from the "high" name on form
    if number:
        paginator=Paginator(posts,number)

    else:
        paginator=Paginator(posts,4)
    
    page= request.GET.get('page')
    pisa=Post.objects.all()
    post=paginator.get_page(page)

    dic={'post':post,'page':page,'pisa':pisa,"cate":cate,
    'cart_product_form':cart_product_form,
    'min_price':min_price,'max_price':max_price, 'papi':papi,'cart':cart,
    'fav':fav,'sub':sub,
    }
    return render (request, 'home.html',dic)


@login_required
def add_wish(request, id):
    if request.is_ajax():
        wishi = Post.objects.get(id=id)
        profile = Profile.objects.get(user=request.user)
        profile.wish.add(wishi)
        

        return render (request, 'home.html')

@login_required
def remove_wish(request, id):
    if request.is_ajax():
        wishi = Post.objects.get(id=id)
        profile = Profile.objects.get(user=request.user)
        profile.wish.remove(wishi)
        
 
        return render (request, 'home.html')


def post_detail(request,slug,id):
    cart = Cart(request)
    cart_product_form = CartAddProductForm()
    query=request.GET.get('search')
    cate=Category.objects.all()


    if query:
        return search(request)
    pis=Post.objects.all()
    post=get_object_or_404(Post,slug=slug,id=id)
    feedback = Ratings.objects.filter(posti=post).exclude(posti__isnull=True)
    color=post.post_color.all()
    extra_choice=post.post_text.all()

    image=post.post_image.all()
    post_ids = post.category.values_list('id', flat=True)
    similar_post = Post.objects.filter(category__in=post_ids)\
     .exclude(id=post.id)
    similar_post = similar_post.annotate(same_category=Count('category'))\
     .order_by('-same_category','title',)[:10]
    #postp=post.filter(out_of_stock=False)
    dic={'cate':cate,
    'post': post,
    'image':image,
    'similar_post':similar_post,
    'pis':pis,
     'cart_product_form': cart_product_form,
  'cart':cart,'feedback':feedback,'extra_choice':extra_choice,'color':color,
    }
    return render(request,'detail.html',dic)

