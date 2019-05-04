from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
import os 
from django.utils.safestring import mark_safe 

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True)
    
    
    class Meta:
        ordering=('name',)
        verbose_name ='Sub category'
        verbose_name_plural='Sub categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ecom:list_category',args=[self.slug])
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True)
    sub_category = models.ManyToManyField(SubCategory)
    class Meta:
        ordering=('name',)
        verbose_name ='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ecom:list_category',args=[self.slug])





class Post(models.Model):
    status_choices=(
         ('draft','Draft'),('published','Published')
        )
    title=models.CharField(max_length=20)
    slug=models.SlugField(max_length=200,unique_for_date='publish',)
    category = models.ManyToManyField(Category)
    subo_category = models.ManyToManyField(SubCategory)
    discription1=RichTextField()
    discription2=RichTextField()
    out_of_stock=models.BooleanField(default=False)
    price_before=models.DecimalField( max_digits=5, decimal_places=2, blank=True, null=True)
    price=models.DecimalField( max_digits=5, decimal_places=2)
    author=models.ForeignKey(User,related_name='blog_posts', on_delete=models.CASCADE)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=10,choices=status_choices,default='draft')
    photo=models.ImageField(upload_to='documents',blank=True)
    #tags = TaggableManager()



    class Meta:
        ordering=('-publish',)
        index_together = (('id', 'slug'),) 
        verbose_name_plural ='Items'
        verbose_name ='Items'
    def __str__(self):
        return self.title.replace(' ','-')





    def get_absolute_url(self):
        return reverse('ecom:post_detail', args=[self.id,self.slug])

@receiver(post_delete, sender=Post)
def photo_post_delete_handler(sender, **kwargs):
    photos = kwargs['instance']
    storage, path = photos.photo.storage, photos.photo.path
    storage.delete(path)



class Image(models.Model):
    image = models.ImageField(upload_to='documents')
    post = models.ForeignKey(Post,related_name='post_image',on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

@receiver(post_delete, sender=Image)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

class Color(models.Model):
    color_choices=(
         ('red','Red'),('green','Green'),
         ('black','Black'),('yellow','Yellow'),

         ('blue','Blue'),('brown','Brown'),
         ('orange','Orange'),('white','White'),
         ('grey','Grey'),('pink','Pink'),

        )
    color = models.CharField(max_length=10,blank=True,null=True,choices=color_choices,default=None)
    post = models.ForeignKey(Post,related_name='post_color',on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.color

class TextChoice(models.Model):

    product_extra_choice = models.CharField(max_length=10,default=None)
    post = models.ForeignKey(Post,related_name='post_text',on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.product_extra_choice

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=30, blank=True)   
    location = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone=models.CharField(max_length=30,null=True,blank=True)
    photo=models.ImageField(upload_to='documents/profile',blank=True,null=True ,default='/documents/profile/oneuser.jpg')
    wish=models.ManyToManyField(Post, related_name='wished' ,blank=True)

    def get_profile_picture(self):

        if self.photo:
            return photo_url
        else:
            return '/documents/profile/oneuser.jpg/'
    def __str__(self):
        return 'Profile: {}'.format(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
   


@receiver(post_delete, sender=Profile)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.photo.storage, photos.photo.path
    storage.delete(path)

@receiver(models.signals.pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).photo
    except sender.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

class Order(models.Model):
    profile = models.ForeignKey(Profile,default="", related_name='items', on_delete=models.CASCADE)
    order_time=models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)

    shipping_address=RichTextField()

    class Meta:

        ordering = ('-order_time',)
    def __str__(self):
        return 'Order {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all() )


class Ratings(models.Model):
    profile = models.ForeignKey(Profile, related_name='rate_profile',  on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)
    feedback=models.CharField(max_length=300,null=True, blank=True)
    order=models.ForeignKey(Order, default="", on_delete=models.SET_NULL, null=True,)
    posti=models.ForeignKey(Post,related_name='ra_items',  on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}'.format(self.id)

        
class OrderItems(models.Model):
    profile = models.ForeignKey(Profile, related_name='item', on_delete=models.CASCADE)
    rated=models.ForeignKey(Ratings,related_name='rate_items',   on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Post,default="",related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    order_time=models.DateTimeField(default=timezone.now)
    quantity = models.PositiveIntegerField(default=1)
    color=models.CharField(max_length=300,null=True, blank=True)
    extra=models.CharField(max_length=300,null=True, blank=True)

    order=models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    def __str__(self):
        return '{}'.format(self.id)


    def get_cost(self):
        return self.price * self.quantity


