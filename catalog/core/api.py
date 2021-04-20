import os
import shutil
from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router, File
from ninja.files import UploadedFile
from ninja.security import django_auth, APIKeyQuery
from .models import Client, Category, Collection, Size, Status, Color, Footwear, Photo
from .schemas import (
    ClientIn, ClientOut,
    CategoryIn, CategoryOut,
    CollectionIn, CollectionOut,
    SizeIn, SizeOut,
    StatusIn, StatusOut,
    ColorIn, ColorOut,
    FootwearIn, FootwearOut,
    PhotoIn, PhotoOut,
)

from .utils import generate_api_key, modified_dict_values_title, upload_image


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
@router.post("/client/create", auth=django_auth, tags=["generate client api Key"])
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


@router.get("/client/list", response=List[ClientOut], auth=django_auth, tags=["generate client api Key"])
def list_client(request):
    qs = Client.objects.all()
    return qs


# Category/Categoria
@router.post("/category/create", auth=api_key, tags=["categoria"], summary="Cadastrar nova categoria.")
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


@router.put("/category/update/{id}", auth=api_key, tags=["categoria"], summary="Atualizar categoria.")
def update_category(request, id: int, payload: CategoryIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    try:
        get_category = Category.objects.get(title__icontains=data['title'])
        return {"detail": f"The {data['title']} category already exists, please insert a new one."}
    except Category.DoesNotExist:
        category = get_object_or_404(Category, id=id)
        for attr, value in payload.dict().items():
            setattr(category, attr, value.title())
        category.save()
        new_title = category.title
        return {"new_title": new_title}


@router.get("/category/get/{id}", response=CategoryOut, auth=api_key, tags=["categoria"],
            summary="Buscar a categoria pelo ID.")
def get_category(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        categories = Category.objects.filter(client=client)
        category_one = categories.get(id=id)
        return category_one
    except Category.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No category for this Client"}


@router.get("/category/search/{title}", response=List[CategoryOut], auth=api_key, tags=["categoria"],
            summary="Buscar a categoria pelo título.")
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


@router.get("/category/list", response=List[CategoryOut], auth=api_key, tags=["categoria"],
            summary="Listar todas as categorias.")
def list_category(request):
    client = Client.objects.get(key=request.auth.key)
    categories = Category.objects.filter(client=client)
    if len(categories) > 0:
        return categories
    else:
        return [{"detail": "Categories empty"}]


@router.delete("/category/delete/{id}", auth=api_key, tags=["categoria"],
            summary="Apagar a categoria pelo ID.")
def delete_category(request, id: int):
    category = get_object_or_404(Category, id=id)
    title = category.title
    category.delete()
    return {"detail": f"Deleted category {title} with success"}


# Collection/Coleção
@router.post("/collection/create", auth=api_key, tags=["coleção"], summary="Cadastrar nova coleção.")
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


@router.put("/collection/update/{id}", auth=api_key, tags=["coleção"], summary="Atualizar coleção.")
def update_collection(request, id: int, payload: CollectionIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    try:
        get_collection = Collection.objects.get(title__icontains=data['title'])
        return {"detail": f"The {data['title']} collection already exists, please insert a new one."}
    except Collection.DoesNotExist:
        collection = get_object_or_404(Collection, id=id)
        for attr, value in payload.dict().items():
            setattr(collection, attr, value.title())
        collection.save()
        new_title = collection.title
        return {"new_title": new_title}


@router.get("/collection/get/{id}", response=CollectionOut, auth=api_key, tags=["coleção"],
            summary="Buscar coleção pelo ID.")
def get_collection(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        collections = Collection.objects.filter(client=client)
        collection_one = collections.get(id=id)
        return collection_one
    except Collection.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No collection for this Client"}


@router.get("/collection/search/{title}", response=List[CollectionOut], auth=api_key, tags=["coleção"],
            summary="Buscar coleção pelo título.")
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


@router.get("/collection/list", response=List[CollectionOut], auth=api_key, tags=["coleção"],
            summary="Listar todas coleções.")
def list_collection(request):
    client = Client.objects.get(key=request.auth.key)
    collections = Collection.objects.filter(client=client)
    if len(collections) > 0:
        return collections
    else:
        return [{"detail": "Collections empty"}]


@router.delete("/collection/delete/{id}", auth=api_key, tags=["coleção"],
            summary="Apagar a coleção pelo ID.")
def delete_collection(request, id: int):
    collection = get_object_or_404(Collection, id=id)
    title = collection.title
    collection.delete()
    return {"detail": f"Deleted collection {title} with success"}


# Size/Tamanho/grade
@router.post("/size/create", auth=api_key, tags=["tamanho/grade"], summary="Cadastrar novo tamanho/grade.")
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


@router.put("/size/update/{id}", auth=api_key, tags=["tamanho/grade"], summary="Atualizar tamanho/grade.")
def update_size(request, id: int, payload: SizeIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    try:
        get_size = Size.objects.get(title__icontains=data['title'])
        return {"detail": f"The {data['title']} size already exists, please insert a new one."}
    except Size.DoesNotExist:
        size = get_object_or_404(Size, id=id)
        for attr, value in payload.dict().items():
            setattr(size, attr, value.title())
        size.save()
        new_title = size.title
        return {"new_title": new_title}


@router.get("/size/get/{id}", response=SizeOut, auth=api_key, tags=["tamanho/grade"],
            summary="Buscar o tamanho/grade pelo ID.")
def get_size(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        sizes = Size.objects.filter(client=client)
        size_one = sizes.get(id=id)
        return size_one
    except Size.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No size for this Client"}


@router.get("/size/search/{title}", response=List[SizeOut], auth=api_key, tags=["tamanho/grade"],
            summary="Buscar o tamanho/grade pelo título.")
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


@router.get("/size/list", response=List[SizeOut], auth=api_key, tags=["tamanho/grade"],
            summary="Listar todos tamanhos/grades.")
def list_size(request):
    client = Client.objects.get(key=request.auth.key)
    sizes = Size.objects.filter(client=client)
    if len(sizes) > 0:
        return sizes
    else:
        return [{"detail": "Sizes empty"}]


@router.delete("/size/delete/{id}", auth=api_key, tags=["tamanho/grade"],
            summary="Apagar tamanho/grade pelo ID.")
def delete_size(request, id: int):
    size = get_object_or_404(Size, id=id)
    title = size.title
    size.delete()
    return {"detail": f"Deleted size {title} with success"}


# Status
@router.post("/status/create", auth=api_key, tags=["status"], summary="Cadastrar novo status.")
def create_status(request, payload: StatusIn):
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


@router.put("/status/update/{id}", auth=api_key, tags=["status"], summary="Atualizar status.")
def update_status(request, id: int, payload: StatusIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    try:
        get_status = Status.objects.get(title__icontains=data['title'])
        return {"detail": f"The {data['title']} status already exists, please insert a new one."}
    except Status.DoesNotExist:
        status = get_object_or_404(Status, id=id)
        for attr, value in payload.dict().items():
            setattr(status, attr, value.title())
        status.save()
        new_title = status.title
        return {"new_title": new_title}


@router.get("/status/get/{id}", response=StatusOut, auth=api_key, tags=["status"],
            summary="Buscar status pelo ID.")
def get_status(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        statuses = Status.objects.filter(client=client)
        status_one = statuses.get(id=id)
        return status_one
    except Status.DoesNotExist:
        return {"id": None, "client": None, "title": None, "detail": "No status for this Client"}


@router.get("/status/search/{title}", response=List[StatusOut], auth=api_key, tags=["status"],
            summary="Buscar status pelo título.")
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


@router.get("/status/list", response=List[StatusOut], auth=api_key, tags=["status"],
            summary="Listar todos os status.")
def list_status(request):
    client = Client.objects.get(key=request.auth.key)
    statuses = Status.objects.filter(client=client)
    if len(statuses) > 0:
        return statuses
    else:
        return [{"detail": "statuses empty"}]


@router.delete("/status/delete/{id}", auth=api_key, tags=["status"],
               summary="Apagar o status por ID.")
def delete_status(request, id: int):
    status = get_object_or_404(Status, id=id)
    title = status.title
    status.delete()
    return {"detail": f"Deleted status {title} with success"}


# Color/Cor
@router.post("/color/create", auth=api_key, tags=["cor"], summary="Cadastrar nova cor.")
def create_color(request, payload: ColorIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    client = Client.objects.get(key=request.auth.key)
    try:
        colors = Color.objects.filter(client=client)
        get_color = colors.get(name__icontains=data['name'])
        return {"detail": f"The {data['name']} color already status, please insert a new one."}
    except Color.DoesNotExist:
        color = Color.objects.create(client=client, name=data['name'])

        return {"id": color.id, "title": color.name}


@router.put("/color/update/{id}", auth=api_key, tags=["cor"], summary="Atualizar cor.")
def update_color(request, id: int, payload: ColorIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    try:
        get_color = Color.objects.get(name__icontains=data['name'])
        return {"detail": f"The {data['name']} color already exists, please insert a new one."}
    except Color.DoesNotExist:
        color = get_object_or_404(Color, id=id)
        for attr, value in payload.dict().items():
            setattr(color, attr, value.title())
        color.save()
        new_name = color.title
        return {"new_name": new_name}


@router.get("/color/get/{id}", response=ColorOut, auth=api_key, tags=["cor"], summary="Buscar cor pelo ID.")
def get_color(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        colors = Color.objects.filter(client=client)
        color_one = colors.get(id=id)
        return color_one
    except Color.DoesNotExist:
        return {"id": None, "client": None, "name": None, "detail": "No color for this Client"}


@router.get("/color/search/{name}", response=List[ColorOut], auth=api_key, tags=["cor"],
            summary="Buscar cor pelo nome.")
def search_color(request, name: str):
    try:
        client = Client.objects.get(key=request.auth.key)
        colors = Color.objects.filter(client=client)
        colors_search = colors.filter(name__icontains=name)
        if len(colors_search) > 0:
            return colors_search
        else:
            return [{"id": None, "client": None, "name": None, "detail": "No color for this search"}]
    except Color.DoesNotExist:
        return {"id": None, "client": None, "name": None, "detail": "No color for this Client"}


@router.get("/color/list", response=List[ColorOut], auth=api_key, tags=["cor"],
            summary="Listar todas as cores.")
def list_color(request):
    client = Client.objects.get(key=request.auth.key)
    colors = Color.objects.filter(client=client)
    if len(colors) > 0:
        return colors
    else:
        return [{"detail": "colors empty"}]


@router.delete("/color/delete/{id}", auth=api_key, tags=["cor"],
               summary="Apagar a cor pelo ID.")
def delete_color(request, id: int):
    color = get_object_or_404(Color, id=id)
    name = color.name
    color.delete()
    return {"detail": f"Deleted color {name} with success"}


# Footwear/Calçados
@router.post("/footwear/create", auth=api_key, tags=["calçados"], summary="Cadastrar novo calçado.")
def create_footwear(request, payload: FootwearIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    client = Client.objects.get(key=request.auth.key)
    try:
        footwears = Footwear.objects.filter(client=client)
        get_footwear = footwears.get(code__icontains=data['code'])
        return {"detail": f"The {data['code']} footwear already status, please insert a new one."}
    except Footwear.DoesNotExist:
        category = Category.objects.get(id=data['category'])
        collection = Collection.objects.get(id=data['collection'])
        size = Size.objects.get(id=data['size'])
        status = Status.objects.get(id=data['status'])
        color = Color.objects.get(id=data['color'])
        code = data['code'].upper()
        del data['category'], data['collection'], data['size'], data['status'], data['color'], data['code']

        footwear = Footwear.objects.create(client=client, category=category,
                                           collection=collection, size=size,
                                           status=status, color=color,
                                           code=code, **data)

        return {"id": footwear.id, "code": footwear.code, "name": footwear.name}


@router.put("/footwear/update/{id}", auth=api_key, tags=["calçados"], summary="Atualizar calçado.")
def update_footwear(request, id: int, payload: FootwearIn):
    data = payload.dict()
    data = modified_dict_values_title(data)
    footwear = get_object_or_404(Footwear, id=id)

    category = Category.objects.get(id=data['category'])
    collection = Collection.objects.get(id=data['collection'])
    size = Size.objects.get(id=data['size'])
    status = Status.objects.get(id=data['status'])
    color = Color.objects.get(id=data['color'])
    code = data['code'].upper()
    del data['category'], data['collection'], data['size'], data['status'], data['color'], data['code']

    data.update({'category': category})
    data.update({'collection': collection})
    data.update({'size': size})
    data.update({'status': status})
    data.update({'color': color})
    data.update({'code': code})

    for attr, value in data.items():
        setattr(footwear, attr, value)

    footwear.save()

    return {"detail": f"OK, footwear code {code} update!"}


@router.get("/footwear/get/{id}", response=FootwearOut, auth=api_key, tags=["calçados"], summary="Buscar o calçado "
                                                                                                 "pelo ID.")
def get_footwear(request, id: int):
    try:
        client = Client.objects.get(key=request.auth.key)
        footwears = Footwear.objects.filter(client=client)
        footwear_one = footwears.get(id=id)
        return footwear_one
    except Footwear.DoesNotExist:
        return {"id": None, "client": None, "code": None, "upper": None, "name": None,
                "outsole": None, "lining": None, "shoelaces": None, "insole": None,
                "abc_curve": None, "cost_price": None, "category": None, "collection": None,
                "size": None, "status": None, "color": None,
                "detail": "No footwear for this Client"}


@router.get("/footwear/search/{name}", response=List[FootwearOut], auth=api_key, tags=["calçados"],
            summary="Buscar calçados pelo nome.")
def search_footwear(request, name: str):
    try:
        client = Client.objects.get(key=request.auth.key)
        footwears = Footwear.objects.filter(client=client)
        footwear_search = footwears.filter(name__icontains=name)
        if len(footwear_search) > 0:
            return footwear_search
        else:
            return [{"id": None, "client": None, "code": None, "upper": None, "name": None,
                     "outsole": None, "lining": None, "shoelaces": None, "insole": None,
                     "abc_curve": None, "cost_price": None, "category": None, "collection": None,
                     "size": None, "status": None, "color": None,
                     "detail": "No footwear for this search"}]
    except Footwear.DoesNotExist:
        return {"id": None, "client": None, "code": None, "upper": None, "name": None,
                "outsole": None, "lining": None, "shoelaces": None, "insole": None,
                "abc_curve": None, "cost_price": None, "category": None, "collection": None,
                "size": None, "status": None, "color": None,
                "detail": "No footwear for this Client"}


@router.get("/footwear/list", response=List[FootwearOut], auth=api_key, tags=["calçados"],
            summary="Listar todos calçados.")
def list_footwear(request):
    client = Client.objects.get(key=request.auth.key)
    footwears = Footwear.objects.filter(client=client)
    if len(footwears) > 0:
        return footwears
    else:
        return [{"detail": "footwears empty"}]


@router.delete("/footwear/delete/{id}", auth=api_key, tags=["calçados"],
            summary="Apagar o calçado pelo ID.")
def delete_footwear(request, id: int):
    footwear = get_object_or_404(Footwear, id=id)
    code = footwear.code
    footwear.delete()
    return {"detail": f"Deleted footwear {code} with success"}


@router.post("/footwear/photos", auth=api_key, tags=["calçados"],
            summary="Subir fotos pelo código referência do calçado.")
def upload_many_photos(request, code_footwear: str, files: List[UploadedFile] = File(...)):
    code = code_footwear.upper()
    client = Client.objects.get(key=request.auth.key)
    try:
        footwear = Footwear.objects.get(code=code)
        photos = []
        i = 1
        for f in files:
            try:
                os.mkdir("photos")
                print(os.getcwd())
            except Exception as e:
                print(e)

            file_name = os.getcwd()+"/photos/"+f.name.replace(" ", "-")
            with open(file_name, 'wb+') as buffer:
                shutil.copyfileobj(f.file, buffer)

            name_photo = f"{code}-{i}"
            res = upload_image(file_name, name_photo)
            res_json = res.json()

            if os.path.exists(file_name):
                os.remove(file_name)
            else:
                print("The photo does not exist")

            url_image = res_json['data']['url']
            url_thumb = res_json['data']['thumb']['url']
            mime_image = res_json['data']['image']['mime']
            extension = res_json['data']['image']['extension']

            photo = Photo.objects.create(client=client, code_footwear=footwear, title=code,
                                         url=url_image, thumb=url_thumb,
                                         mime=mime_image, extension=extension)
            i += 1
            photos.append({"url_image": url_image, "url_thumb": url_thumb,
                           "MIME type": mime_image, "extension": extension})
        return [p for p in photos]
    except Footwear.DoesNotExist:
        return {"detail": f"The {code} footwear not exists"}






