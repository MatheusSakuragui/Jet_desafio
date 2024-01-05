SWAGGER_DOCS = {
    "GET": """
    Get details of a Veiculo.

    ---
    tags:
      - Veiculo
    summary: Retrieve details of a Veiculo.
    description: |
      This endpoint retrieves details of a Veiculo based on the provided ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the Veiculo.
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Veiculo'
      404:
        description: Veiculo not found.
""",
"POST": """
    Create a new Veiculo.

    ---
    tags:
      - Veiculo
    summary: Create a new Veiculo.
    description: |
      This endpoint creates a new Veiculo based on the provided data.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            placa:
              type: string
              description: Placa do veículo
            ano:
              type: string
              description: Ano do veículo
            qtd_portas:
              type: string
              description: Quantidade de portas do veículo
            produto_id:
              type: integer
              description: ID do produto associado ao veículo
    responses:
      201:
        description: Veiculo created successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Veiculo'
      400:
        description: Validation error.
""",
"PUT": """
    Update details of a Veiculo.

    ---
    tags:
      - Veiculo
    summary: Update details of a Veiculo.
    description: |
      This endpoint updates the details of a Veiculo based on the provided ID and data.
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID of the Veiculo to be updated.
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            placa:
              type: string
              description: Placa do veículo
            ano:
              type: string
              description: Ano do veículo
            qtd_portas:
              type: string
              description: Quantidade de portas do veículo
            produto_id:
              type: integer
              description: ID do produto associado ao veículo
    responses:
      200:
        description: Veiculo updated successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Veiculo'
      404:
        description: Veiculo not found.
""",
"DELETE": """
    Delete a Veiculo.

    ---
    tags:
      - Veiculo
    summary: Delete a Veiculo.
    description: |
      This endpoint deletes a Veiculo based on the provided ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the Veiculo to be deleted.
    responses:
      200:
        description: Veiculo deleted successfully.
        content:
          application/json:
            schema:
              $ref: 'app/schemas/Veiculo'
      404:
        description: Veiculo not found.
"""

}