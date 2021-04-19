from ninja import Schema
from pydantic import Field


class ClientOut(Schema):
    """
    Esquema usado internamente para a listagem de Clients de software autorizados, que será a entidade
    que consome os serviços da API.
    """
    id: int = Field(
        title='Identificador',
        description='ID do Client Software.'
    )
    client: str = Field(
        title='Nome',
        description='Nome para identificação do Client software.'
    )
    key: str = Field(
        title='Chave API',
        description='Chave API usada para conectar aos endpoints da API.'
    )


class ClientIn(Schema):
    """
    Esquema usado internamente para a criar APIKEY dos Clients de software autorizados, que será a entidade
    que consome os serviços da API.
    """
    client: str = Field(
        title='Nome',
        description='Nome para identificação do Client software.'
    )


class CategoryIn(Schema):
    """
    Esquema usado para o cadastro e edição das categorias do catálogo.
    """
    title: str = Field(
        title='Categoria',
        description='Título da categoria do calçado.'
    )


class CategoryOut(Schema):
    """
    Esquema usado para a listagem das categorias do catálogo.
    """
    detail: str = Field(
        'Success',
        title='Detalhe',
        description='Usado nos retornos das requisições.'
    )
    id: int = Field(
        None,
        title='Identificador',
        description='Identificador da categoria do calçado.'
    )
    title: str = Field(
        None,
        title='Categoria',
        description='Nome da categoria do calçado.'
    )

    client: ClientIn = Field(
        None,
        title='Entidade Client Software',
        description='Client Software dono da categoria.'
    )


class CollectionIn(Schema):
    """
    Esquema usado para o cadastro e edição das coleções do catálogo.
    """
    title: str = Field(
        title='Coleção',
        description='Título da coleção do calçado.'
    )


class CollectionOut(Schema):
    """
    Esquema usado para a listagem das coleções do catálogo.
    """
    detail: str = Field(
        'Success',
        title='Detalhe',
        description='Usado nos retornos das requisições.'
    )
    id: int = Field(
        None,
        title='Identificador',
        description='Identificador da coleção do calçado.'
    )
    title: str = Field(
        None,
        title='Coleção',
        description='Título da coleção do calçado.'
    )
    client: ClientIn = Field(
        None,
        title='Entidade Client Software',
        description='Client Software dono da coleção.'
    )


class SizeIn(Schema):
    """
    Esquema usado para o cadastro e edição do tamanho/grade dos calçados.
    """
    title: str = Field(
        title='Tamanho/Grade',
        description='Tamanho/Grade do calçado.'
    )


class SizeOut(Schema):
    """
    Esquema usado para a listagem do tamanho/grade dos calçados.
    """
    detail: str = Field(
        'Success',
        title='Detalhe',
        description='Usado nos retornos das requisições.'
    )
    id: int = Field(
        None,
        title='Identificador',
        description='Identificador do tamanho/grade.'
    )
    title: str = Field(
        None,
        title='Tamanho/grade',
        description='Título do tamanho/grade.'
    )
    client: ClientIn = Field(
        None,
        title='Entidade Client Software',
        description='Client Software dono do tamanho/grade.'
    )


class StatusIn(Schema):
    """
    Esquema usado para o cadastro e edição do status relacionado ao estoque dos calçados.
    """
    title: str = Field(
        title='Status do estoque',
        description='Status referente ao estoque do calçado.'
    )


class StatusOut(Schema):
    """
    Esquema usado para a listagem do status relacionado ao estoque dos calçados.
    """
    detail: str = Field(
        'Success',
        title='Detalhe',
        description='Usado nos retornos das requisições.'
    )
    id: int = Field(
        None,
        title='Identificador',
        description='Identificador do status.'
    )
    title: str = Field(
        None,
        title='Status do estoque',
        description='Status referente ao estoque do calçado.'
    )
    client: ClientIn = Field(
        None,
        title='Entidade Client Software',
        description='Client Software dono do status.'
    )


class ColorIn(Schema):
    """
    Esquema usado para o cadastro e edição das cores dos calçados.
    """
    name: str = Field(
        title='Cor(es) do calçado',
        description='Cor(es) referente aos calçados do catalogo.'
    )


class ColorOut(Schema):
    """
    Esquema usado para a listagem das cores dos calçados.
    """
    detail: str = Field(
        'Success',
        title='Detalhe',
        description='Usado nos retornos das requisições.'
    )
    id: int = Field(
        None,
        title='Identificador',
        description='Identificador da cor(es).'
    )
    title: str = Field(
        None,
        title='Cor(es) do calçado',
        description='Cor(es) do calçado.'
    )
    client: ClientIn = Field(
        None,
        title='Entidade Client Software',
        description='Client Software dono do status.'
    )


class FootwearIn(Schema):
    """
    Esquema usado para o cadastro e edição dos calçados.
    """
    code: str = Field(
        None,
        title='Código referência',
        description='Código referência do calçado usado pela marca.'
    )
    upper: str = Field(
        None,
        title='Cabedal',
        description='Material do cabedal do calçado, parte superior do calçado.'
    )
    name: str = Field(
        None,
        title='Modelo',
        description='Nome do modelo do calçado usado pela marca.'
    )
    outsole: str = Field(
        None,
        title='Sola',
        description='Material da sola do calçado, solado ou sola exterior.'
    )
    lining: str = Field(
        None,
        title='Forro',
        description='Material do forro interno do calçado.'
    )
    closure: str = Field(
        None,
        title='Tipo de fechamento ou fecho',
        description='Material ou tipo de fechamento ou fecho do calçado.'
    )
    insole: str = Field(
        None,
        title='Palmilha',
        description='Material da palmilha do calçado.'
    )
    abc_curve: str = Field(
        None,
        title='Curva ABC',
        description='Método de categorização de estoques Curva ABC, análise de Pareto ou regra 80/20.'
    )
    cost_price: float = Field(
        None,
        title='Preço de custo do par',
        description='Preço de custo do par do calçado para a marca.'
    )
    category: int = Field(
        None,
        title='Categoria',
        description='Categoria do calçado.'
    )
    collection: int = Field(
        None,
        title='Coleção',
        description='Coleção do catalogo.'
    )
    size: int = Field(
        None,
        title='Tamanho/Grade',
        description='Tamanho ou grade do calçado.'
    )
    status: int = Field(
        None,
        title='Status de estoque',
        description='Status de estoque do calçado.'
    )
    color: int = Field(
        None,
        title='Cor(es) do calçado',
        description='Cor(es) do calçado.'
    )
    gender: str = Field(
        None,
        title='Gênero',
        description='Gênero do calçado.'
    )


class FootwearOut(Schema):
    """
    Esquema usado para a listagem dos calçados.
    """
    id: int = Field(
        None,
        title='Identificador',
        description='Identificador do calçado armazenado no banco de dados.'
    )
    client: ClientIn = Field(
        None,
        title='Entidade Client Software',
        description='Client Software dono do calçado.'
    )
    code: str = Field(
        None,
        title='Código referência',
        description='Código referência do calçado usado pela marca.'
    )
    upper: str = Field(
        None,
        title='Cabedal',
        description='Material do cabedal do calçado, parte superior do calçado.'
    )
    name: str = Field(
        None,
        title='Modelo',
        description='Nome do modelo do calçado usado pela marca.'
    )
    outsole: str = Field(
        None,
        title='Sola',
        description='Material da sola do calçado, solado ou sola exterior.'
    )
    lining: str = Field(
        None,
        title='Forro',
        description='Material do forro interno do calçado.'
    )
    closure: str = Field(
        None,
        title='Tipo de fechamento ou fecho',
        description='Material ou tipo de fechamento ou fecho do calçado.'
    )
    insole: str = Field(
        None,
        title='Palmilha',
        description='Material da palmilha do calçado.'
    )
    abc_curve: str = Field(
        None,
        title='Curva ABC',
        description='Método de categorização de estoques Curva ABC, análise de Pareto ou regra 80/20.'
    )
    cost_price: float = Field(
        None,
        title='Preço de custo do par',
        description='Preço de custo do par do calçado para a marca.'
    )
    category: CategoryIn = Field(
        None,
        title='Categoria',
        description='Categoria do calçado.'
    )
    collection: CollectionIn = Field(
        None,
        title='Coleção',
        description='Coleção do catalogo.'
    )
    size: SizeIn = Field(
        None,
        title='Tamanho/Grade',
        description='Tamanho ou grade do calçado.'
    )
    status: StatusIn = Field(
        None,
        title='Status de estoque',
        description='Status de estoque do calçado.'
    )
    color: ColorIn = Field(
        None,
        title='Cor(es) do calçado',
        description='Cor(es) do calçado.'
    )
    gender: str = Field(
        None,
        title='Gênero',
        description='Gênero do calçado.'
    )


class PhotoIn(Schema):
    """
    Implementação futura
    """
    photo: int
    # title: int
    # url: str
    # thumb: str
    # mime: str
    # extension: str


class PhotoOut(Schema):
    """
    Implementação futura
    """
    code_footwear: FootwearIn = None
    title: int
    url: str
    thumb: str
    mime: str
    extension: str