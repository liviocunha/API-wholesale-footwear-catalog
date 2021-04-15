from django.urls import path
from django.contrib import admin
from ninja import NinjaAPI
from catalog.core.api import router as catalog_router

api = NinjaAPI(
    version='1.0',
    csrf=True,
    title='API Wholesale Footwear Catalog',
    description='Este projeto é uma API RESTful que contém endpoints necessários para dar suporte a um '
                'aplicativo da web que permite que uma indústria de calçados exiba um catálogo de atacado.',
    urls_namespace='public_api',
)
api.add_router('/catalog/', catalog_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
