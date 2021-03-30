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
    id: int
    client: ClientIn
    title: str
