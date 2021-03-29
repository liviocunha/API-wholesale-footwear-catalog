from django.urls import path
from django.contrib import admin
from ninja import NinjaAPI
from catalog.core.api import router as catalog_router

api = NinjaAPI()
api.add_router('/catalog/', catalog_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
