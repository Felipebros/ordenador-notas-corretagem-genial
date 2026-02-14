import os
import re
import argparse
from datetime import datetime

def rename_files(directory, pattern):
    """
    Renames files in a directory based on a regex pattern, 
    prefixing them with an ISO date extracted from the filename.
    """
    # Compile the regex pattern provided by the user
    try:
        regex = re.compile(pattern)
    except re.error as e:
        print(f"Erro na expressão regular: {e}")
        return

    # Check if directory exists
    if not os.path.isdir(directory):
        print(f"Diretório não encontrado: {directory}")
        return

    print(f"Iniciando processamento em: {directory}")
    
    files_processed = 0
    
    for filename in os.listdir(directory):
        # Match the filename against the user-provided regex
        match = regex.match(filename)
        
        if match:
            # Look for the date pattern DD-MM-YY in the filename
            # This regex specifically looks for two digits, dash, two digits, dash, two digits
            date_match = re.search(r'(\d{2})-(\d{2})-(\d{2})', filename)
            
            if date_match:
                day, month, year_short = date_match.groups()
                
                # Convert short year (YY) to full year (YYYY)
                # Assuming 20xx for years
                full_year = f"20{year_short}"
                
                # Construct the new prefix: YYYY-MM-DD
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
    parser = argparse.ArgumentParser(description="Ordenador de Notas de Corretagem: Renomeia arquivos prefixando a data no formato ISO para melhor organização.")
    
    # Argument for the regex pattern
    parser.add_argument(
        "pattern", 
        help="Expressão regular para filtrar os arquivos (ex: 'NotaCorretagem.*\.pdf')"
    )
    
    # Argument for the directory (defaults to current folder)
    parser.add_argument(
        "--dir", 
        default=".", 
        help="Diretório onde os arquivos estão localizados (padrão: pasta atual)"
    )

    args = parser.parse_args()
    
    rename_files(args.dir, args.pattern)
    