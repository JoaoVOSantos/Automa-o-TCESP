import os
from tkinter import Tk, filedialog
from datetime import datetime

def rename_pdfs():
    # Obter a data de hoje no formato desejado
    today = datetime.now().strftime("%d-%m-%y")
    
    # Configurar a interface de seleção de arquivos
    root = Tk()
    root.withdraw()  # Ocultar a janela principal do Tkinter
    root.title("Selecione arquivos PDF")
    
    # Abrir janela para selecionar múltiplos arquivos PDF
    file_paths = filedialog.askopenfilenames(
        title="Selecione os arquivos PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    
    # Verificar se algum arquivo foi selecionado
    if not file_paths:
        print("Nenhum arquivo selecionado.")
        return

    # Renomear os arquivos
    for file_path in file_paths:
        directory, original_name = os.path.split(file_path)
        name, ext = os.path.splitext(original_name)
        
        # Criar o novo nome com a data
        new_name = f"{name} - {today}{ext}"
        new_path = os.path.join(directory, new_name)
        
        try:
            os.rename(file_path, new_path)
            print(f"Renomeado: {original_name} -> {new_name}")
        except Exception as e:
            print(f"Erro ao renomear {original_name}: {e}")
    
    print("Processo concluído!")

if __name__ == "__main__":
    rename_pdfs()
