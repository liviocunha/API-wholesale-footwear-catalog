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


class StatusIn(Schema):
    title: str


class StatusOut(Schema):
    detail: str = 'Success'
    id: int = None
    title: str = None
    client: ClientIn = None


class ColorIn(Schema):
    name: str


class ColorOut(Schema):
    detail: str = 'Success'
    id: int = None
    name: str = None
    client: ClientIn = None


class FootwearIn(Schema):
    code: str
    upper: str
    name: str
    outsole: str
    lining: str
    shoelaces: str
    insole: str
    abc_curve: str
    cost_price: float
    category: int
    collection: int
    size: int
    status: int
    color: int


class FootwearOut(Schema):
    id: int
    client: ClientIn = None
    code: str
    upper: str
    name: str
    outsole: str
    lining: str
    shoelaces: str
    insole: str
    abc_curve: str
    cost_price: float
    category: CategoryIn = None
    collection: CollectionIn = None
    size: SizeIn = None
    status: StatusIn = None
    color: ColorIn = None


class PhotoIn(Schema):
    photo: int
    # title: int
    # url: str
    # thumb: str
    # mime: str
    # extension: str


class PhotoOut(Schema):
    code_footwear: FootwearIn = None
    title: int
    url: str
    thumb: str
    mime: str
    extension: str