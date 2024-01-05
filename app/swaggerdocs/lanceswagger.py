SWAGGER_DOCS = {
    "SINGLE":{
        "GET": """
    Get Lance Details.

    ---
    tags:
      - Lance
    summary: Retrieve information about a lance.
    description: |
      This endpoint retrieves detailed information about a specific lance based on the provided lance ID.
    parameters:
      - name: id
        in: path
        description: ID of the lance to retrieve.
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Lance'
      404:
        description: Lance not found.
""",

"POST": """
    Create New Lance.

    ---
    tags:
      - Lance
    summary: Create a new lance.
    description: |
      This endpoint creates a new lance with the provided details.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            data:
              type: string
              description: Data of the lance. If not provided, the current date is used.
            valor:
              type: number
              description: Valor of the lance.
            cliente_id:
              type: integer
              description: ID of the cliente making the lance.
            leilao_id:
              type: integer
              description: ID of the leilao associated with the lance.
            produto_id:
              type: integer
              description: ID of the produto associated with the lance.
    responses:
      201:
        description: Lance created successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Lance'
      400:
        description: Validation error or specific error messages.
""",
"DELETE": """
    Delete lance.

    ---
    tags:
      - Lance
    summary: Delete a lance.
    description: |
      This endpoint deletes a specific conta based on the provided lance ID.
    parameters:
      - name: id
        in: path
        description: ID of the lance to delete.
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Lance deleted successfully.
      404:
        description: Lance not found.
"""

    },
    "LISTA":{
        "GET": """
    Get List of Lances for a Produto.

    ---
    tags:
      - Lance
    summary: Retrieve a list of lances for a specific produto.
    description: |
      This endpoint retrieves a list of lances for a specific produto based on the provided produto ID.
    parameters:
      - name: id
        in: path
        description: ID of the produto to retrieve lances for.
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: 'app/schemas/Lance'
"""
    }
}