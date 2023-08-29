from django.contrib import admin
from .models import Advertisiment
class AdvertisimentAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "auction", "created_date", "user", "image", "minimage"]
    list_filter = ["price", "auction", "create_at"]
    actions = ["make_auction_as_true", "make_auction_as_false"]
    fieldsets = (
        ("Общие", {
            "fields": ("title", "description", "user", "image")
        }),
        ("Финансы", {
            "fields": ("price", "auction"),
            "classes": ["collapse"]
        })
    )
    @admin.action(description="Добвить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction = True)
    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)


admin.site.register(Advertisiment, AdvertisimentAdmin)