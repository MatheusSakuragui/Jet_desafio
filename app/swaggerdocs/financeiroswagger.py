SWAGGER_DOCS = {
    "GET": """
    Get Financeiro Details.

    ---
    tags:
      - Financeiro
    summary: Retrieve information about a financeiro.
    description: |
      This endpoint retrieves detailed information about a specific financeiro based on the provided financeiro ID.
    parameters:
      - name: id
        in: path
        description: ID of the financeiro to retrieve.
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Financeiro'
      404:
        description: Financeiro not found.
""",

"POST": """
    Create New Financeiro.

    ---
    tags:
      - Financeiro
    summary: Create a new financeiro.
    description: |
      This endpoint creates a new financeiro with the provided details.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            banco:
              type: string
              description: Banco of the financeiro.
    responses:
      201:
        description: Financeiro created successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Financeiro'
      400:
        description: Validation error.
""",

"PUT": """
    Update Financeiro Details.

    ---
    tags:
      - Financeiro
    summary: Update information about a financeiro.
    description: |
      This endpoint updates the details of a specific financeiro based on the provided financeiro ID.
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID of the financeiro to update.
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            banco:
              type: string
              description: Banco of the financeiro.
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              banco:
                type: string
                description: Updated banco of the financeiro.
    responses:
      200:
        description: Financeiro updated successfully.
      404:
        description: Financeiro not found.
""",

"DELETE": """
    Delete Financeiro.

    ---
    tags:
      - Financeiro
    summary: Delete a financeiro.
    description: |
      This endpoint deletes a specific financeiro based on the provided financeiro ID.
    parameters:
      - name: id
        in: path
        description: ID of the financeiro to delete.
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Financeiro deleted successfully.
      404:
        description: Financeiro not found.
"""

}