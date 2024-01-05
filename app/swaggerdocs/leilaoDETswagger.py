SWAGGER_DOCS = {
    "GET": """
    Get detailed information about a specific Leilao.

    ---
    tags:
      - Leilao
    summary: Retrieve detailed information about a Leilao.
    description: |
      This endpoint retrieves detailed information about a specific Leilao, including historical data for each product.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the Leilao to retrieve details for.
    responses:
      200:
        description: Successful response.
        content:
          application/json:
            schema:
      404:
        description: Leilao not found.
"""

}