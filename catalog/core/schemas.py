from ninja import Schema


class ClientSchema(Schema):
    id: int
    client: str
    key: str


class CategoryIn(Schema):
    client: int
    title: str


class CategoryOut(Schema):
    id: int
    client: ClientSchema
    title: str
