
Cria arquivo JSON utilizando FAKER no formato ideal para ser adicionado no Banco de Dados usando loaddata.

1    Primeiro é necessário instalar o faker. pip install faker

2    Com o faker instalado execute o programa script.py python3 script.py

3    Será criado um arquivo no formato JSON ideal para ser adicionado em qualquer banco de dados.

4    No meu caso, como estou usando DJANGO e MYSQL o comando para adicionar o JSON é: python3 manage.py loaddata nomedoarquivojson.json

5    Verifique se as linhas foram adicionadas ao seu banco de dados.
