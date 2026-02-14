import argparse
import os
import re


def rename_files(directory, pattern):
    """
    Renomeia arquivos em um diretório com base em um padrão de regex,
    prefixando-os com uma data ISO extraída do nome do arquivo.
    """
    # Compila o padrão de expressão regular fornecido pelo usuário
    try:
        regex = re.compile(pattern)
    except re.error as e:
        print(f"Erro na expressão regular: {e}")
        return

    # Verifica se o diretório existe
    if not os.path.isdir(directory):
        print(f"Diretório não encontrado: {directory}")
        return

    print(f"Iniciando processamento em: {directory}")

    files_processed = 0

    for filename in os.listdir(directory):
        # Compara o nome do arquivo com a regex fornecida pelo usuário
        match = regex.match(filename)

        if match:
            # Procura pelo padrão de data DD-MM-AA no nome do arquivo
            # Esta regex procura especificamente por dois dígitos, traço, dois dígitos, traço, dois dígitos
            date_match = re.search(r"(\d{2})-(\d{2})-(\d{2})", filename)

            if date_match:
                day, month, year_short = date_match.groups()

                # Converte o ano curto (AA) para o ano completo (AAAA)
                # Assumindo 20xx para os anos
                full_year = f"20{year_short}"

                # Constrói o novo prefixo: AAAA-MM-DD
                iso_date = f"{full_year}-{month}-{day}"
                new_name = f"{iso_date}_{filename}"

                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)

                try:
                    os.rename(old_path, new_path)
                    print(f"Sucesso: {filename} -> {new_name}")
                    files_processed += 1
                except Exception as e:
                    print(f"Erro ao renomear {filename}: {e}")
            else:
                print(f"Aviso: Padrão de data não encontrado em '{filename}'")

    print(f"\nConcluído. Total de arquivos renomeados: {files_processed}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ordenador de Notas de Corretagem: Renomeia arquivos prefixando a data no formato ISO para melhor organização."
    )

    # Argumento para o padrão de regex
    parser.add_argument(
        "pattern",
        help="Expressão regular para filtrar os arquivos (ex: 'NotaCorretagem.*\.pdf')",
    )

    # Argumento para o diretório (o padrão é a pasta atual)
    parser.add_argument(
        "--dir",
        default=".",
        help="Diretório onde os arquivos estão localizados (padrão: pasta atual)",
    )

    args = parser.parse_args()

    rename_files(args.dir, args.pattern)
