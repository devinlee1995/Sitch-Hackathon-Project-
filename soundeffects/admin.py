from django.contrib import admin

from soundeffects.models import Categories, SoundEffect

# Register your models here.


class CatAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['category_name']}),
        ('category_info', {'fields': ['details']}),
    ]


admin.site.register(Categories, CatAdmin)

admin.site.register(SoundEffect)