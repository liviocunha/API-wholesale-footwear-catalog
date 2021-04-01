from ninja import Schema


class ClientOut(Schema):
    id: int
    client: str
    key: str


class ClientIn(Schema):
    client: str


class CategoryIn(Schema):
    title: str


class CategoryOut(Schema):
    detail: str = 'Success'
    id: int = None
    title: str = None
    client: ClientIn = None


class CollectionIn(Schema):
    title: str


class CollectionOut(Schema):
    detail: str = 'Success'
    id: int = None
    title: str = None
    client: ClientIn = None


class SizeIn(Schema):
    title: str


class SizeOut(Schema):
    detail: str = 'Success'
    id: int = None
    title: str = None
    client: ClientIn = None