from django.contrib import admin
from .models import User, Product, Category, Favorite, Image
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Fields',
            {
                'fields': (
                    'user_type',
                    'phone_number',
                    'street',
                    'city',
                    'zip_code',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)


class PropertyImageInline(admin.TabularInline):
    model = Image
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, ]


admin.site.register(Product, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Image)