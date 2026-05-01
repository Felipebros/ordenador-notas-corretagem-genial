# Ordenador de Notas de Corretagem e Negociação (Corretora Genial e XP Investimentos)

Este script Python organiza automaticamente as notas de corretagem e de negociação da Genial e XP Investimentos, prefixando o nome do arquivo com a data no formato ISO (`YYYY-MM-DD`). Isso garante que seus arquivos fiquem ordenados cronologicamente e organizados no explorador de arquivos.

### 🚀 Formas de Execução:

#### 1. Interface Visual (Recomendado para Windows, Linux ou macOS)
A forma mais simples de usar. Basta dar um clique duplo no arquivo:
- **`interface_visual.pyw`**

> [!NOTE]
> **Compatibilidade:** No Windows e macOS funciona nativamente com o Python instalado. No **Linux**, caso a janela não abra, instale o suporte ao Tkinter com o comando: `sudo apt install python3-tk`.

Ele abrirá uma janela avisando que o processamento começou e mostrará um resumo do que foi renomeado ao final. 
> [!TIP]
> Por padrão, ele busca tanto por **Notas de Corretagem** quanto por **Notas de Negociação** na mesma pasta onde o script está salvo.

#### 2. Execução Rápida (Windows)
- Dê um clique duplo no arquivo **`executar_ordenacao.bat`**. 
- Ele executará o script via terminal e manterá a janela aberta no final para você conferir os resultados antes de fechar.

#### 3. Via Terminal (Avançado)
Se você deseja personalizar a pasta ou o padrão de busca:
```bash
# Executa com os padrões automáticos
python ordenador.py

# Especifica uma pasta diferente
python ordenador.py --dir "/caminho/para/meus/pdfs"

# Define um padrão de busca personalizado (Regex)
python ordenador.py "NotaCustomizada_.*\.pdf"
```

---

### 🧠 O que o script faz:

* **Filtro Inteligente**: Identifica arquivos que começam com `NotaCorretagem_` ou `NotaNegociacao-`.
* **Extração de Data**: Localiza automaticamente a data no nome do arquivo (formatos `DD-MM-YY` ou `DD-MM-YYYY`).
* **Conversão ISO**: Transforma datas como `30-01-26` em `2026-01-30`.
* **Renomeação**: Adiciona o prefixo de data mantendo o nome original (ex: `2026-01-30_NotaCorretagem_...pdf`).

### 🛠️ Requisitos:
* **Python 3.x** instalado.
* Não é necessário instalar nenhuma biblioteca externa (usa apenas bibliotecas padrão do Python).
