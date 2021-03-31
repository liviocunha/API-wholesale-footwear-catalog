from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router
from ninja.security import django_auth, APIKeyQuery
from .models import Client, Category, Collection
from .schemas import ClientIn, ClientOut, CategoryIn, CategoryOut, CollectionIn, CollectionOut
from .utils import generate_api_key, str_upper, str_title


class ApiKey(APIKeyQuery):
    param_name = "api_key"

    def authenticate(self, request, key):
        try:
            return Client.objects.get(key=key)
        except Client.DoesNotExist:
            pass


router = Router()
api_key = ApiKey()


# Client
@router.post("/client", auth=django_auth, tags=["generate client api Key"])
def create_client(request, payload: ClientIn):
    new_key = False
    while not new_key:
        key = generate_api_key()
        try:
            get_client = Client.objects.get(key=key)
        except Client.DoesNotExist:
            new_key = True

    client = Client.objects.create(key=key, **payload.dict())
    return {"id": client.id, "client": client.client, "api_key": client.key}


@router.get("/client", response=List[ClientOut], auth=django_auth, tags=["generate client api Key"])
def list_client(request):
    qs = Client.objects.all()
    return qs


# Category
@router.post("/category", auth=api_key, tags=["category"])
def create_category(request, payload: CategoryIn):
    data = payload.dict()
    client = Client.objects.get(key=request.auth.key)
    try:
        categories = Category.objects.filter(client=client)
        get_category = categories.get(title=str_upper(data['title']))
        return {"detail": f"The {str_title(data['title'])} category already exists, please insert a new one."}
    except Category.DoesNotExist:
        category = Category.objects.create(client=client, title=str_upper(data['title']))
        return {"id": category.id, "title": category.title.title()}


@router.get("/category/{title}", response=CategoryOut, auth=api_key, tags=["category"])
def get_category(request, title: str):
    title = str_upper(title)
    try:
        client = Client.objects.get(key=request.auth.key)
        categories = Category.objects.filter(client=client)
        category_one = categories.get(title=str_upper(title))
        return category_one
    except Category.DoesNotExist:
        return {'id': None, 'client': None, 'title': None, 'detail': 'No categories for this client'}


@router.get("/category", response=List[CategoryOut], auth=api_key, tags=["category"])
def list_category(request):
    client = Client.objects.get(key=request.auth.key)
    categories = Category.objects.filter(client=client)
    return categories


# Collection
@router.post("/collection", auth=api_key, tags=["collection"])
def create_collection(request, payload: CollectionIn):
    data = payload.dict()
    client = Client.objects.get(key=request.auth.key)
    try:
        collections = Collection.objects.filter(client=client)
        get_collection = collections.get(title=str_upper(data['title']))
        return {"detail": f"The {str_title(data['title'])} collection already exists, please insert a new one."}
    except Collection.DoesNotExist:
        collection = Collection.objects.create(client=client, title=str_upper(data['title']))
        return {"id": collection.id, "title": str_title(collection.title)}


@router.get("/collection/{title}", response=CollectionOut, auth=api_key, tags=["collection"])
def get_collection(request, title: str):
    title = str_upper(title)
    try:
        client = Client.objects.get(key=request.auth.key)
        collections = Collection.objects.filter(client=client)
        collection_one = collections.get(title=str_upper(title))
        return collection_one
    except Collection.DoesNotExist:
        return {'id': None, 'client': None, 'title': None, 'detail': 'No collection for this client'}


@router.get("/collection", response=List[CollectionOut], auth=api_key, tags=["collection"])
def list_collection(request):
    client = Client.objects.get(key=request.auth.key)
    collections = Collection.objects.filter(client=client)
    return collections

