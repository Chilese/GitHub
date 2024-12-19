## Descrição do Projeto
O Sistema de Ponto de Venda (PDV) é uma aplicação desktop desenvolvida em Python e Tkinter. Ele é projetado para ajudar pequenas empresas a gerenciar suas vendas, estoque de produtos, fornecedores e categorias de produtos de forma eficiente e intuitiva. Com uma interface amigável, o PDV permite aos usuários registrar vendas, adicionar novos produtos, atualizar informações do produto, e visualizar o estoque disponível. Além disso, oferece recursos para gerenciar fornecedores e categorias de produtos.

## Funcionalidades Principais
- **Cadastro de Produtos:** Adicione novos produtos ao estoque com informações detalhadas, como nome, descrição, preço de compra, preço de venda, quantidade, data de entrada, fornecedor, categoria e notas.
- **Edição de Produtos:** Atualize facilmente os detalhes dos produtos existentes.
- **Gestão de Estoque:** Monitore o estoque disponível e receba alertas quando os níveis estiverem baixos.
- **Cadastro de Fornecedores:** Mantenha um registro dos fornecedores com informações de contato.
- **Cadastro de Categorias:** Organize os produtos em categorias para facilitar a gestão.
- **Gestão de Usuários:** Controle o acesso ao sistema com diferentes níveis de permissão.
- **Gestão de Vendas:** Registre e acompanhe as vendas realizadas.
- **Dashboard com Gráficos:** Visualize o desempenho das vendas e o status do estoque através de gráficos.

## Requisitos
- Python 3.x
- Tkinter
- SQLite
- bcrypt
- logging

## Instalação
1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/projeto-pdv.git
    cd projeto-pdv
    ```

2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

3. Inicialize o banco de dados:
    ```sh
    python init_db.py
    ```

4. Execute o PDV:
    ```bash
    python main.py
    ```

## Uso
1. Execute o aplicativo:
    ```sh
    python main.py
    ```

2. Navegue pela interface gráfica para utilizar as funcionalidades do PDV.

## Estrutura do Banco de Dados
### Tabela `products`
- `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `name` (TEXT, NOT NULL)
- `price` (REAL, NOT NULL)
- `stock` (INTEGER, NOT NULL)

### Tabela `users`
- `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `username` (TEXT, NOT NULL)
- `password` (TEXT, NOT NULL)

## Exemplo de Uso
### Cadastro de Produto
1. Abra o aplicativo.
2. Navegue até a seção de cadastro de produtos.
3. Insira os detalhes do produto e clique em "Salvar".

### Realização de Venda
1. Abra o aplicativo.
2. Navegue até a seção de vendas.
3. Selecione os produtos e finalize a venda.

## Contribuição
Contribuições são bem-vindas! Por favor, siga estas etapas:
1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.