from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router
from ninja.security import django_auth, APIKeyQuery
from .models import Client, Category, Collection, Size, Status
from .schemas import (
    ClientIn, ClientOut,
    CategoryIn, CategoryOut,
    CollectionIn, CollectionOut,
    SizeIn, SizeOut,
    StatusIn, StatusOut,
)

from .utils import generate_api_key, modified_dict_values_title


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
    data = modified_dict_values_title(data)
    client = Client.objects.get(key=request.auth.key)
    try:
        categories = Category.objects.filter(client=client)
        get_category = categories.get(title__icontains=data['title'])

        return {"detail": f"The {data['title']} category already exists, please insert a new one."}
    except Category.DoesNotExist:
        category = Category.objects.create(client=client, title=data['title'])

        return {"id": category.id, "title": category.title}


@router.get("/category/{id}", response=CategoryOut, auth=api_key, tags=["category"])
def get_category(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        categories = Category.objects.filter(client=client)
        category_one = categories.get(id=id)
        return category_one
    except Category.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No category for this Client"}


@router.get("/category/search/{title}", response=List[CategoryOut], auth=api_key, tags=["category"])
def search_category(request, title: str):
    try:
        client = Client.objects.get(key=request.auth.key)
        categories = Category.objects.filter(client=client)
        categories_search = categories.filter(title__icontains=title)
        if len(categories_search) > 0:
            return categories_search
        else:
            return [{"id": None, "client": None, "title": None, "detail": "No category for this search"}]
    except Category.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No category for this Client"}


@router.get("/category", response=List[CategoryOut], auth=api_key, tags=["category"])
def list_category(request):
    client = Client.objects.get(key=request.auth.key)
    categories = Category.objects.filter(client=client)
    if len(categories) > 0:
        return categories
    else:
        return [{"detail": "Categories empty"}]


@router.delete("/category/{id}", auth=api_key, tags=["category"])
def delete_category(request, id: int):
    category = get_object_or_404(Category, id=id)
    title = category.title
    category.delete()
    return {"detail": f"Deleted category {title} with success"}


# Collection
@router.post("/collection", auth=api_key, tags=["collection"])
def create_collection(request, payload: CollectionIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    client = Client.objects.get(key=request.auth.key)
    try:
        collections = Collection.objects.filter(client=client)
        get_collection = collections.get(title__icontains=data['title'])

        return {"detail": f"The {data['title']} collection already exists, please insert a new one."}
    except Collection.DoesNotExist:
        collection = Collection.objects.create(client=client, title=data['title'])

        return {"id": collection.id, "title": collection.title}


@router.get("/collection/{id}", response=CollectionOut, auth=api_key, tags=["collection"])
def get_collection(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        collections = Collection.objects.filter(client=client)
        collection_one = collections.get(id=id)
        return collection_one
    except Collection.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No collection for this Client"}


@router.get("/collection/search/{title}", response=List[CollectionOut], auth=api_key, tags=["collection"])
def search_collection(request, title: str):
    try:
        client = Client.objects.get(key=request.auth.key)
        collections = Collection.objects.filter(client=client)
        collections_search = collections.filter(title__icontains=title)
        if len(collections_search) > 0:
            return collections_search
        else:
            return [{"id": None, "client": None, "title": None, "detail": "No collection for this search"}]
    except Collection.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No collection for this Client"}


@router.get("/collection", response=List[CollectionOut], auth=api_key, tags=["collection"])
def list_collection(request):
    client = Client.objects.get(key=request.auth.key)
    collections = Collection.objects.filter(client=client)
    if len(collections) > 0:
        return collections
    else:
        return [{"detail": "Collections empty"}]


@router.delete("/collection/{id}", auth=api_key, tags=["collection"])
def delete_collection(request, id: int):
    collection = get_object_or_404(Collection, id=id)
    title = collection.title
    collection.delete()
    return {"detail": f"Deleted collection {title} with success"}


# Size
@router.post("/size", auth=api_key, tags=["size"])
def create_size(request, payload: SizeIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    client = Client.objects.get(key=request.auth.key)
    try:
        sizes = Size.objects.filter(client=client)
        get_size = sizes.get(title__icontains=data['title'])
        return {"detail": f"The {data['title']} size already exists, please insert a new one."}
    except Size.DoesNotExist:
        size = Size.objects.create(client=client, title=data['title'])

        return {"id": size.id, "title": size.title}


@router.get("/size/{id}", response=SizeOut, auth=api_key, tags=["size"])
def get_size(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        sizes = Size.objects.filter(client=client)
        size_one = sizes.get(id=id)
        return size_one
    except Size.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No size for this Client"}


@router.get("/size/search/{title}", response=List[SizeOut], auth=api_key, tags=["size"])
def search_size(request, title: str):
    try:
        client = Client.objects.get(key=request.auth.key)
        sizes = Size.objects.filter(client=client)
        sizes_search = sizes.filter(title__icontains=title)
        if len(sizes_search) > 0:
            return sizes_search
        else:
            return [{"id": None, "client": None, "title": None, "detail": "No size for this search"}]
    except Size.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No size for this Client"}


@router.get("/size", response=List[SizeOut], auth=api_key, tags=["size"])
def list_size(request):
    client = Client.objects.get(key=request.auth.key)
    sizes = Size.objects.filter(client=client)
    if len(sizes) > 0:
        return sizes
    else:
        return [{"detail": "Sizes empty"}]


@router.delete("/size/{id}", auth=api_key, tags=["size"])
def delete_size(request, id: int):
    size = get_object_or_404(Size, id=id)
    title = size.title
    size.delete()
    return {"detail": f"Deleted size {title} with success"}


# Status
@router.post("/status", auth=api_key, tags=["status"])
def create_status(request, payload: SizeIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    client = Client.objects.get(key=request.auth.key)
    try:
        statuses = Status.objects.filter(client=client)
        get_status = statuses.get(title__icontains=data['title'])
        return {"detail": f"The {data['title']} size already status, please insert a new one."}
    except Status.DoesNotExist:
        status = Status.objects.create(client=client, title=data['title'])

        return {"id": status.id, "title": status.title}


@router.get("/status/{id}", response=StatusOut, auth=api_key, tags=["status"])
def get_status(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        statuses = Status.objects.filter(client=client)
        status_one = statuses.get(id=id)
        return status_one
    except Status.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No status for this Client"}


@router.get("/status/search/{title}", response=List[StatusOut], auth=api_key, tags=["status"])
def search_status(request, title: str):
    try:
        client = Client.objects.get(key=request.auth.key)
        statuses = Status.objects.filter(client=client)
        statuses_search = statuses.filter(title__icontains=title)
        if len(statuses_search) > 0:
            return statuses_search
        else:
            return [{"id": None, "client": None, "title": None, "detail": "No status for this search"}]
    except Status.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No status for this Client"}


@router.get("/status", response=List[StatusOut], auth=api_key, tags=["status"])
def list_status(request):
    client = Client.objects.get(key=request.auth.key)
    statuses = Status.objects.filter(client=client)
    if len(statuses) > 0:
        return statuses
    else:
        return [{"detail": "statuses empty"}]


@router.delete("/status/{id}", auth=api_key, tags=["status"])
def delete_status(request, id: int):
    status = get_object_or_404(Status, id=id)
    title = status.title
    status.delete()
    return {"detail": f"Deleted status {title} with success"}