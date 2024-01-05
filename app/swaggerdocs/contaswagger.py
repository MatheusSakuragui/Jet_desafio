SWAGGER_DOCS = {
    "GET": """
    Get Conta Details.

    ---
    tags:
      - Conta
    summary: Retrieve information about a conta.
    description: |
      This endpoint retrieves detailed information about a specific conta based on the provided conta ID.
    parameters:
      - name: id
        in: path
        description: ID of the conta to retrieve.
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: ID of the conta.
                agencia:
                  type: string
                  description: Agência of the conta.
                conta_corrente:
                  type: string
                  description: Número da conta.
                financeiro_id:
                  type: integer
                  description: ID of the associated financeiro.
                  example: 1
      404:
        description: Conta not found.
""",

"POST": """
    Create New Conta.

    ---
    tags:
      - Conta
    summary: Create a new conta.
    description: |
      This endpoint creates a new conta with the provided details.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            agencia:
              type: string
              description: Agência of the conta.
            conta_corrente:
              type: string
              description: Número da conta.
            financeiro_id:
              type: integer
              description: ID of the associated financeiro.
              example: 1
    responses:
      201:
        description: Conta created successfully.
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: ID of the created conta.
                agencia:
                  type: string
                  description: Agência of the created conta.
                conta_corrente:
                  type: string
                  description: Número da conta of the created conta.
                financeiro_id:
                  type: integer
                  description: ID of the associated financeiro.
                  example: 1
      400:
        description: Validation error.
""",

"PUT": """
    Update Conta Details.

    ---
    tags:
      - Conta
    summary: Update information about a conta.
    description: |
      This endpoint updates the details of a specific conta based on the provided conta ID.
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID of the conta to retrieve.
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            agencia:
              type: string
              description: Agência of the conta.
            conta_corrente:
              type: string
              description: Número da conta.
            financeiro_id:
              type: integer
              description: ID of the associated financeiro.
              example: 1
    responses:
      200:
        description: Conta updated successfully.
      404:
        description: Conta not found.
""",

"DELETE": """
    Delete Conta.

    ---
    tags:
      - Conta
    summary: Delete a conta.
    description: |
      This endpoint deletes a specific conta based on the provided conta ID.
    parameters:
      - name: id
        in: path
        description: ID of the conta to delete.
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Conta deleted successfully.
      404:
        description: Conta not found.
"""
}