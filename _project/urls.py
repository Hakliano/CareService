from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from nejlepsiProjekt.views import (
    partner_list, add_partner, register, index, cards, partner_detail,
    partners_by_category_and_city, get_cities_for_region, filter_partners
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),  # Hlavní stránka
    path('partners/', partner_list, name='partner_list'),  # Výpis partnerů
    path('add-partner/', add_partner, name='add_partner'),  # Přidání partnera
    path('register/', register, name='register'),  # Registrace uživatele
    path('cards/', cards, name='cards'),  # Statická stránka karet
    path('reality/', filter_partners, name='reality'),  # Filtrace partnerů
    path('partner/<int:partner_id>/', partner_detail, name='partner_detail'),  # Detail partnera
    path('partners/filter/', partners_by_category_and_city, name='partners_by_category_and_city'),  # Další filtrace
    path('get-cities-for-region/', get_cities_for_region, name='get_cities_for_region'),  # AJAX pro města
]

# Pro statické a mediální soubory během vývoje
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
