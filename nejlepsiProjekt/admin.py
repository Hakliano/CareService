from django.contrib import admin
from .models import (
    Partner, Contact, Payment, Category, Portfolium, PortfoliumType, Content,
    Customer, Review, Staff, StaffRule, Post, OpeningHours, Feature, PartnerFeature, PriceList, Gallery, 
    Region, City
)

# Inline editor pro Content
class ContentInline(admin.StackedInline):
    model = Content
    extra = 1

# Inline editor pro Gallery
class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1

# Inline editor pro OpeningHours
class OpeningHoursInline(admin.TabularInline):
    model = OpeningHours
    extra = 1

# Inline editor pro PriceList
class PriceListInline(admin.TabularInline):
    model = PriceList
    extra = 1

# Inline editor pro PartnerFeature
class PartnerFeatureInline(admin.TabularInline):
    model = PartnerFeature
    extra = 1

# Nastavení adminu pro Region
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Nastavení adminu pro City
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')  # Zobrazení názvu města a příslušného regionu
    search_fields = ('name', 'region__name')  # Vyhledávání podle názvu města a regionu
    list_filter = ('region',)  # Filtr podle regionu

# Nastavení adminu pro Partner
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'category', 'coints', 'city')
    search_fields = ('name', 'email', 'category__name', 'city__name')
    list_filter = ('category', 'city',)
    ordering = ('-coints',)
    inlines = [ContentInline, GalleryInline, OpeningHoursInline, PriceListInline, PartnerFeatureInline]

# Nastavení adminu pro OpeningHours
class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ('partner', 'day', 'open_time', 'close_time')
    list_filter = ('partner', 'day')
    ordering = ('partner', 'day')

# Nastavení adminu pro Feature
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)

# Nastavení adminu pro PartnerFeature
class PartnerFeatureAdmin(admin.ModelAdmin):
    list_display = ('partner', 'feature')
    list_filter = ('partner', 'feature')
    search_fields = ('partner__name', 'feature__name')

# Nastavení adminu pro PriceList
class PriceListAdmin(admin.ModelAdmin):
    list_display = ('partner', 'service_name', 'price')
    search_fields = ('service_name', 'partner__name')
    list_filter = ('partner',)

# Nastavení adminu pro Gallery
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('partner', 'image')
    list_filter = ('partner',)

# Admin pro Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Registrace ostatních modelů
admin.site.register(Partner, PartnerAdmin)
admin.site.register(OpeningHours, OpeningHoursAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(PartnerFeature, PartnerFeatureAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Contact)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Portfolium)
admin.site.register(PortfoliumType)
admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Staff)
admin.site.register(StaffRule)
