import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys
import threading

def run_process(root):
    # Pega o diretório atual onde o script está
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, "ordenador.py")
    
    # Usa o executável python atual
    python_exe = sys.executable
    
    # Força a saída do subprocesso a ser UTF-8 (corrige problema de acentos no Windows)
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    
    try:
        # Executa o comando em segundo plano
        # Explicitamente forçamos o diretório atual (--dir base_dir e cwd=base_dir) 
        # Isso corrige um bug do Windows onde arquivos .pyw podem iniciar em C:\Windows\System32
        result = subprocess.run(
            [python_exe, script_path, "--dir", base_dir],
            cwd=base_dir,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            env=env
        )
        
        # Assim que terminar, envia o resultado de volta para a interface gráfica
        root.after(0, show_result, root, result)
            
    except Exception as e:
        root.after(0, show_error, root, str(e))

def show_result(root, result):
    # Essa função roda na interface gráfica para mostrar os alertas
    if result.returncode == 0:
        messagebox.showinfo(
            "Processo Concluído", 
            f"A ordenação dos arquivos terminou com sucesso!\n\nLogs:\n{result.stdout}",
            parent=root
        )
    else:
        messagebox.showerror(
            "Erro na Execução", 
            f"Ocorreu um erro durante a execução.\n\nLogs:\n{result.stdout}\n{result.stderr}",
            parent=root
        )
    # Fecha o programa inteiro assim que o alerta for fechado
    root.destroy()

def show_error(root, error_msg):
    messagebox.showerror("Erro Inesperado", f"Não foi possível executar o script:\n{error_msg}", parent=root)
    root.destroy()

def main():
    # Cria a janela principal do Tkinter para aparecer na barra de tarefas
    root = tk.Tk()
    root.title("Ordenador de Notas")
    
    # Configura o tamanho da janela e a centraliza na tela
    window_width = 300
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False) # Impede de redimensionar
    
    # Adiciona uma mensagem de aguarde
    lbl = tk.Label(root, text="Processando arquivos...\nPor favor, aguarde.", font=("Helvetica", 11))
    lbl.pack(expand=True)
    
    # Roda o processamento em uma "Thread" (segundo plano real) para não travar a janela visual
    threading.Thread(target=run_process, args=(root,), daemon=True).start()
    
    # Mantém a janela aberta e interativa
    root.mainloop()

if __name__ == "__main__":
    main()
