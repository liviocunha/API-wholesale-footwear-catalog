from django.urls import path
from django.contrib import admin
from ninja import NinjaAPI
from catalog.core.api import router as catalog_router

api = NinjaAPI(
    version='1.0',
    csrf=True,
    title='API Wholesale Footwear Catalog',
    description='This project contains backend REST APIs needed to support a web application that allows '
                'a footwear industry to display wholesale catalog.',
    urls_namespace='public_api',
)
api.add_router('/catalog/', catalog_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
