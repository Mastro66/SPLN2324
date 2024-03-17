### Criação/Atualização de um template jinja2 para o pyproject.toml

### UC - SPLN

### Autor

👤 **Fernando Daniel de Magalhães Pipa Alves - PG54470**

### Acerca do TPC

MakePyProject é um script Python projetado para gerar dinamicamente um arquivo `pyproject.toml` para projetos Python. Utiliza o pacote `flit_core` para construção e empacotamento de projetos Python e aproveita `jjcli` e `jinja2` para funcionalidades adicionais.

Desta forma, através de um `METADATA.json` (editado por mim), é atualizado o `pyproject.toml`

### Exemplo de comando de execução:

python3 makepyproject.py