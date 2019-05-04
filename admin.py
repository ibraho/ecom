
from django.contrib import admin
from .models import *


'''Check the order of registering a ModelAdmin:
it’s the model class first, then the ModelAdmin class.'''

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ColorInline(admin.TabularInline):
    model = Color
    


class  TextChoiceInline(admin.TabularInline):

    model = TextChoice
 
class ImageInline(admin.TabularInline):
    model = Image

class RatingsAdmin(admin.ModelAdmin):
     list_display = ('profile','rate')

class ImageAdmin(admin.ModelAdmin):
     list_display = ('active','image')

     model = Image

class PostAdmin(admin.ModelAdmin):
    inlines = [
            ImageInline,ColorInline,TextChoiceInline,
        ]


    list_display = ('title',"price_before", 'price','out_of_stock', 'author', 'publish',
    'status','photo',)
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body','slug',)

    list_editable = ["price_before", 'out_of_stock', ]
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","photo",)





class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):

    #list_display = ('quantity','profile','order_time',)
    inlines = [OrderItemsInline]
   
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Ratings, RatingsAdmin)



