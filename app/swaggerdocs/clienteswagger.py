SWAGGER_DOCS = {
    "GET":"""
        Retorna as informações do cliente.

        ---
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
                  $ref: 'clientes'
          404:
            description: Client not found
        """,
    "POST":"""
        Criar novo cliente.

        ---
        parameters:
          - name: nome
            in: formData
            type: string
            required: true
            description: Nome do cliente
          - name: email
            in: formData
            type: string
            required: true
            description: Email do cliente
          - name: senha
            in: formData
            type: string
            required: true
            description: Senha do cliente
          - name: telefone
            in: formData
            type: string
            required: true
            description: Telefone do cliente
          - name: cpf
            in: formData
            type: string
            required: true
            description: CPF do cliente
        responses:
          201:
            description: Client criado com sucesso
            content:
              application/json:
                schema:
                  $ref: '/clientes'
          400:
            description: Validation error
        """,
    "PUT":"""
        Atualizar as informações do cliente.

        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: ID do cliente para atualizar as informações
          - name: nome
            in: formData
            type: string
            required: true
            description: Nome do cliente
          - name: email
            in: formData
            type: string
            required: true
            description: Email do cliente
          - name: senha
            in: formData
            type: string
            required: true
            description: Senha do cliente
          - name: telefone
            in: formData
            type: string
            required: true
            description: Telefone do cliente
          - name: cpf
            in: formData
            type: string
            required: true
            description: CPF do cliente
        responses:
          200:
            description: Cliente atualizado com sucesso
            content:
              application/json:
                schema:
                  $ref: '/clientes'
          404:
            description: Client not found
        """,
    "DELETE":"""
        Deletar um cliente.

        ---
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