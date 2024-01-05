SWAGGER_DOCS = {
    "GET":"""
        Retorna as informações do cliente.

        ---
        tags:
          - Cliente
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: ID do cliente
        responses:
          200:
            description: Successful response
            content:
              application/json:
                schema:
          404:
            description: Client not found
        """,
    "POST":"""
        Criar novo cliente.

        ---
        consumes:
          - application/json  # Specify that the request consumes JSON
        tags:
          - Cliente
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              properties:
                nome:
                  type: string
                  description: Nome do cliente
                email:
                  type: string
                  description: Email do cliente
                senha:
                  type: string
                  description: Senha do cliente
                telefone:
                  type: string
                  description: Telefone do cliente
                cpf:
                  type: string
                  description: CPF do cliente
        responses:
          201:
            description: Client criado com sucesso
            content:
              application/json:
                schema:
          400:
            description: Validation error
    """,
    "PUT":"""
        Atualizar as informações do cliente.

        ---
        tags:
          - Cliente
        parameters:
          - in: path
            name: id
            type: integer
            required: true
            description: ID do cliente para atualizar as informações
          - in: body
            name: body
            required: true
            schema:
              type: object
              properties:
                nome:
                  type: string
                  description: Nome do cliente
                email:
                  type: string
                  description: Email do cliente
                senha:
                  type: string
                  description: Senha do cliente
                telefone:
                  type: string
                  description: Telefone do cliente
                cpf:
                  type: string
                  description: CPF do cliente
        responses:
          200:
            description: Cliente atualizado com sucesso
            content:
              application/json:
                schema:
          404:
            description: Client not found
        """,
    "DELETE":"""
        Deletar um cliente.

        ---
        tags:
          - Cliente
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: ID do cliente para deletá-lo
        responses:
          204:
            description: Cliente deletado com sucesso
          404:
            description: Client not found
        """
}