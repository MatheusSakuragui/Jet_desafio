SWAGGER_DOCS = {
    "GET": """
    Get Eletronico Details.

    ---
    tags:
      - Eletronico
    summary: Retrieve information about an eletronico.
    description: |
      This endpoint retrieves detailed information about a specific eletronico based on the provided eletronico ID.
    parameters:
      - name: id
        in: path
        description: ID of the eletronico to retrieve.
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Eletronico'
      404:
        description: Eletronico not found.
""",

"POST": """
    Create New Eletronico.

    ---
    tags:
      - Eletronico
    summary: Create a new eletronico.
    description: |
      This endpoint creates a new eletronico with the provided details.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            voltagem:
              type: string
              description: Voltagem of the eletronico.
            produto_id:
              type: integer
              description: ID of the associated produto.
              example: 1
    responses:
      201:
        description: Eletronico created successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Eletronico'
      400:
        description: Validation error.
""",

"PUT": """
    Update Eletronico Details.

    ---
    tags:
      - Eletronico
    summary: Update information about an eletronico.
    description: |
      This endpoint updates the details of a specific eletronico based on the provided eletronico ID.
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
            voltagem:
              type: string
              description: Voltagem of the eletronico.
            produto_id:
              type: integer
              description: ID of the associated produto.
              example: 1
    responses:
      200:
        description: Eletronico updated successfully.
      404:
        description: Eletronico not found.
""",

"DELETE": """
    Delete Eletronico.

    ---
    tags:
      - Eletronico
    summary: Delete an eletronico.
    description: |
      This endpoint deletes a specific eletronico based on the provided eletronico ID.
    parameters:
      - name: id
        in: path
        description: ID of the eletronico to delete.
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Eletronico deleted successfully.
      404:
        description: Eletronico not found.
"""
}