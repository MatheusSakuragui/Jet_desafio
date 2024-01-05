SWAGGER_DOCS = {
    "SINGLE":{"GET": """
    Get information about a specific Produto.

    ---
    tags:
      - Produto
    summary: Retrieve information about a Produto.
    description: |
      This endpoint retrieves information about a specific Produto, including details about the associated Leilao and TipoProduto.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the Produto to retrieve information for.
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              type: object
              properties:
                # Define the properties of the Produto response here.
                id:
                  type: integer
                marca:
                  type: string
                modelo:
                  type: string
                descricao:
                  type: string
                lance_inicial:
                  type: float
                lance_adicional:
                  type: float
                vendido:
                  type: boolean
                leilao_data:
                  type: string
                  format: date-time
                leilao_detalhes:
                  type: string
                leilao_status:
                  type: string
                tipo_produto_info:
                  type: string
                tipo_produto_descricao:
                  type: string
      404:
        description: Produto not found.
""",
"POST": """
    Create a new Produto.

    ---
    tags:
      - Produto
    summary: Create a new Produto.
    description: |
      This endpoint creates a new Produto based on the provided data.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              description: Nome do produto
            marca:
              type: string
              description: Marca do produto
            modelo:
              type: string
              description: Modelo do produto
            descricao:
              type: string
              description: Descrição do produto
            lance_inicial:
              type: float
              description: Lance inicial do produto
            lance_adicional:
              type: float
              description: Lance adicional do produto
            vendido:
              type: boolean
              description: Flag indicating if the produto is sold
            leilao_id:
              type: integer
              description: ID do leilao associado ao produto
            tipo_produto_id:
              type: integer
              description: ID do tipo de produto associado
    responses:
      201:
        description: Produto created successfully.
        content:
          application/json:
            schema:
              type: object
              properties:
                # Define the properties of the created Produto response here.
                id:
                  type: integer
                marca:
                  type: string
                modelo:
                  type: string
                descricao:
                  type: string
                lance_inicial:
                  type: float
                lance_adicional:
                  type: float
                vendido:
                  type: boolean
                leilao_data:
                  type: string
                  format: date-time
                leilao_detalhes:
                  type: string
                leilao_status:
                  type: string
                tipo_produto_info:
                  type: string
                tipo_produto_descricao:
                  type: string
      400:
        description: Validation error.
""",
"PUT": """
    Update information about a specific Produto.

    ---
    tags:
      - Produto
    summary: Update information about a Produto.
    description: |
      This endpoint updates information about a specific Produto based on the provided data.
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID of the Produto to update.
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              description: Nome do produto
            marca:
              type: string
              description: Marca do produto
            modelo:
              type: string
              description: Modelo do produto
            descricao:
              type: string
              description: Descrição do produto
            lance_inicial:
              type: float
              description: Lance inicial do produto
            lance_adicional:
              type: float
              description: Lance adicional do produto
            vendido:
              type: boolean
              description: Flag indicating if the produto is sold
            leilao_id:
              type: integer
              description: ID do leilao associado ao produto
            tipo_produto_id:
              type: integer
              description: ID do tipo de produto associado
    responses:
      200:
        description: Produto updated successfully.
        content:
          application/json:
            schema:
              type: object
              properties:
                # Define the properties of the updated Produto response here.
                id:
                  type: integer
                marca:
                  type: string
                modelo:
                  type: string
                descricao:
                  type: string
                lance_inicial:
                  type: float
                lance_adicional:
                  type: float
                vendido:
                  type: boolean
                leilao_data:
                  type: string
                  format: date-time
                leilao_detalhes:
                  type: string
                leilao_status:
                  type: string
                tipo_produto_info:
                  type: string
                tipo_produto_descricao:
                  type: string
      400:
        description: Validation error.
""",
"DELETE": """
    Delete a specific Produto.

    ---
    tags:
      - Produto
    summary: Delete a Produto.
    description: |
      This endpoint deletes a specific Produto based on the provided ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the Produto to delete.
    responses:
      200:
        description: Produto deleted successfully.
        content: {}
      404:
        description: Produto not found.
"""},"LISTA":{
    "GET": """
    Get a list of filtered Produtos.

    ---
    tags:
      - Produto
    summary: Retrieve a list of filtered Produtos.
    description: |
      This endpoint retrieves a list of Produtos based on the provided filters.
    parameters:
      - name: min
        in: query
        type: integer
        description: Minimum lance_inicial value.
      - name: max
        in: query
        type: integer
        description: Maximum lance_inicial value.
      - name: leilaoid
        in: query
        type: integer
        description: ID of the associated Leilao.
      - name: tipoproduto
        in: query
        type: string
        description: TipoProduto filter (eletronico_veiculo).
      - name: nome
        in: query
        type: string
        description: Filter Produtos by name (descricao).
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  # Define the properties of each Produto in the list here.
                  id:
                    type: integer
                  marca:
                    type: string
                  modelo:
                    type: string
                  descricao:
                    type: string
                  lance_inicial:
                    type: float
                  lance_adicional:
                    type: float
                  vendido:
                    type: boolean
                  leilao_data:
                    type: string
                    format: date-time
                  leilao_detalhes:
                    type: string
                  leilao_status:
                    type: string
                  tipo_produto_info:
                    type: string
                  tipo_produto_descricao:
                    type: string
      400:
        description: Validation error.
"""
}

}