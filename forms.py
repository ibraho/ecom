from django import forms
from .models  import *
from django.contrib import admin


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','last_name','birth_date', 'location', 'zipcode',"phone",)
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)

'''class TopAdminForm(forms.ModelForm):
  class Meta:

    model = OrderItems
    widgets = {
            'shipping_address':ApproveStopWidget(),
        }
   '''