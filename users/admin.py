from __future__ import unicode_literals
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MyUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email']

    password1 = None
    password2 = None

    def clean_password2(self):
        pass

    def _post_clean(self):
        pass

    def save(self, commit=True):
        user = super(forms.ModelForm, self).save(commit=False)

        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        user.email = email
        user.first_name = first_name
        user.last_name = last_name


        if commit:
            user.save()
        return user

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        exclude = []


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    fieldsets = (
        (None, {'fields' : ('email', 'password')}),
        (_('Personal info'), {'fields' : ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields' : ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ( 'first_name', 'last_name','email'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


