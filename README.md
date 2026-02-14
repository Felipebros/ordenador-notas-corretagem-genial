# Ordenador de Notas de Corretagem (Genial)

Este script Python organiza as notas de corretagem da Genial, prefixando o nome do arquivo com a data no formato ISO (`YYYY-MM-DD`). Isso garante que os arquivos fiquem ordenados cronologicamente no explorador de arquivos do computador.

### Como usar o script:

1. **Instalação**: Certifique-se de ter o Python instalado. Não são necessárias bibliotecas externas.
2. **Execução**: Você pode usar o arquivo `.bat` para uma execução rápida ou rodar via terminal.
3. **Exemplo de comando (Via Terminal)**:
```bash
python ordenador.py "NotaCorretagem_.*\.pdf"
```
*Se os arquivos estiverem em outra pasta:*
```bash
python ordenador.py "NotaCorretagem_.*\.pdf" --dir "/caminho/para/meus/pdfs"
```

4. **Execução Rápida (Windows)**:
   - Basta dar um clique duplo no arquivo `executar_ordenacao.bat`. Ele já está configurado para buscar arquivos que comecem com "NotaCorretagem_".

**O que o script faz:**

* Filtra os arquivos usando o **Regex** que você passar.
* Extrai a primeira data que encontrar no nome (`DD-MM-YY`).
* Transforma `30-01-26` em `2026-01-30`.
* Renomeia o arquivo original adicionando o prefixo (ex: `2026-01-30_NotaCorretagem_...pdf`).
