SWAGGER_DOCS = {
    "SINGLE":{
        "GET": """
    Get details of a Leilao.

    ---
    tags:
      - Leilao
    summary: Retrieve details of a specific Leilao.
    description: |
      This endpoint retrieves details of a specific Leilao based on the provided Leilao ID.
    parameters:
      - name: id
        in: path
        description: ID of the Leilao to retrieve details for.
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Leilao'
""",

"PUT": """
    Update details of a Leilao.

    ---
    tags:
      - Leilao
    summary: Update details of a specific Leilao.
    description: |
      This endpoint updates details of a specific Leilao based on the provided Leilao ID.
    parameters:
      - in: path
        name: id
        description: ID of the Leilao to update details for.
        required: true
        schema:
          type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              description: Nome do leilao
            data_futura:
              type: string
              format: date-time  # Adjust the format based on your requirements
              description: Data futura do leilao
            data_visitacao:
              type: string
              format: date-time  # Adjust the format based on your requirements
              description: Data de visitacao do leilao
            detalhes:
              type: string
              description: Detalhes do leilao
            qtd_produtos:
              type: integer
              description: Quantidade de produtos do leilao
            status:
              type: string
              default: "EM ABERTO"
              description: Status do leilao
            conta:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: ID da conta associada ao leilao
    responses:
      201:
        description: Leilao updated successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Leilao'
      400:
        description: Validation error.
""",

"POST": """
    Create a new Leilao.

    ---
    tags:
      - Leilao
    summary: Create a new Leilao.
    description: |
      This endpoint creates a new Leilao based on the provided data.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              description: Nome do leilao
            data_futura:
              type: string
              format: date-time  # Adjust the format based on your requirements
              description: Data futura do leilao
            data_visitacao:
              type: string
              format: date-time  # Adjust the format based on your requirements
              description: Data de visitacao do leilao
            detalhes:
              type: string
              description: Detalhes do leilao
            qtd_produtos:
              type: integer
              description: Quantidade de produtos do leilao
            status:
              type: string
              default: "EM ABERTO"
              description: Status do leilao
            conta:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: ID da conta associada ao leilao
    responses:
      201:
        description: Leilao created successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Leilao'
      400:
        description: Validation error.
""",

"DELETE": """
    Delete a Leilao.

    ---
    tags:
      - Leilao
    summary: Delete a specific Leilao.
    description: |
      This endpoint deletes a specific Leilao based on the provided Leilao ID.
    parameters:
      - name: id
        in: path
        description: ID of the Leilao to delete.
        required: true
        schema:
          type: integer
    responses:
      201:
        description: Leilao deleted successfully.
      404:
        description: Leilao not found.
"""
    },
    "LISTA":{
        "GET": """
    Get a list of all Leilao.

    ---
    tags:
      - Leilao
    summary: Retrieve a list of all Leilao.
    description: |
      This endpoint retrieves a list of all Leilao available in the system.
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: 'app/schemas/Leilao'
"""
    }
}