SWAGGER_DOCS = {
    "SINGLE":{
        "GET": """
    Get details of a specific TipoProduto.

    ---
    tags:
      - Tipo de produto
    summary: Retrieve details of a TipoProduto.
    description: |
      This endpoint retrieves details of a specific TipoProduto based on the provided ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the TipoProduto.
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/TipoProduto'
      404:
        description: TipoProduto not found.
""",
"POST": """
    Create a new TipoProduto.

    ---
    tags:
      - Tipo de produto
    summary: Create a new TipoProduto.
    description: |
      This endpoint creates a new TipoProduto with the provided information.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            descricao:
              type: string
              description: Descrição do produto.
            eletronico_veiculo:
              type: string
              description: Tipo do produto (eletronico/veiculo).
    responses:
      201:
        description: TipoProduto created successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/TipoProduto'
      400:
        description: Validation error.
""",
"PUT": """
    Update details of a TipoProduto.

    ---
    tags:
      - Tipo de produto
    summary: Update details of a TipoProduto.
    description: |
      This endpoint updates the details of a specific TipoProduto based on the provided ID.
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID of the TipoProduto.
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            descricao:
              type: string
              description: Descrição do produto.
            eletronico_veiculo:
              type: string
              description: Tipo do produto (eletronico/veiculo).
    responses:
      200:
        description: TipoProduto updated successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/TipoProduto'
      404:
        description: TipoProduto not found.
      400:
        description: Validation error.
""",
"DELETE": """
    Delete a TipoProduto.

    ---
    tags:
      - Tipo de produto
    summary: Delete a TipoProduto.
    description: |
      This endpoint deletes a specific TipoProduto based on the provided ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the TipoProduto.
    responses:
      204:
        description: TipoProduto deleted successfully.
      404:
        description: TipoProduto not found.
"""
    },
    "LISTA":{
        "GET": """
    Get a list of TipoProdutos.

    ---
    tags:
      - Tipo de produto
    summary: Retrieve a list of TipoProdutos.
    description: |
      This endpoint retrieves a list of all TipoProdutos available in the system.
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: 'app/schemas/TipoProduto'
"""

    }
}