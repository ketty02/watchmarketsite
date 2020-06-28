from django.contrib import admin
from market.models.watch import Watch
from market.models.type import Type

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        queryset = queryset.filter(owner=request.user)

        return queryset

    def get_fields(self, request, obj=None):
        all_fields = super().get_fields(request, obj)

        if not request.user.is_superuser:
            all_fields.remove('owner')

        return all_fields

    def save_model(self, request, obj, form, change):
         if not obj.pk:
             owner = form.cleaned_data.get('owner')

             if not owner:
                 obj.owner = request.user

         super().save_model(request, obj, form, change)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        queryset = queryset.filter(watch__in=request.user.watches.all())

        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'watches':
                kwargs['queryset'] = Watch.objects.filter(owner=request.user)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)



