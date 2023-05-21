import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk
import pandas as pd

df = None

def file_df():
    global df
    open_df = filedialog.asksaveasfilename(filetypes=[('CSV Files', '*.csv')])
    df = pd.read_csv(open_df)
    print("Dataframe aberto com sucesso.")

def display_info():
    if df is not None:
        print(df.info())
        print('\n', df.head())
    else:
        print("Nenhum DataFrame foi encontrado.")

def clean_df():
    if df is not None:
        df.dropna(inplace=True)
        print("DataFrame limpado")
    else:
        print("Nenhum dataFrame foi carregado.")

def rename_coluna():
    old_name = simpledialog.askstring('Renomear Coluna', 'Digite o nome da Coluna a ser renomeada:')
    new_name = simpledialog.askstring('Renomear Coluna', 'Digite o novo nome da coluna:')
    df.rename(columns={old_name : new_name}, inplace=True)

def end_result():
    print('\nResultado Final do DataFrame:')
    print(df)

def drop_columns():
    if df is not None:
        columns_name = simpledialog.askstring("Apagar Coluna:", "Digite o nome da coluna a ser deletada: ")
        if columns_name in df.columns:
            df.drop(columns_name, axis=1, inplace=True)
            print(f'A coluna {columns_name}, foi deletada com sucesso')
        else:
            print(f'A coluna {columns_name}, não existe no dataframe')
            
janela = tk.Tk()
janela.title("Automatizador de DataFrame")
janela.geometry('300x300')
janela.configure(bg='lightgray')

# Estilização dos botões
style = ttk.Style()
style.configure('TButton', font=('Arial', 10, 'bold'), foreground='blue')

style.map('TButton',
          background=[('active', 'darkblue'), ('disabled', 'grey')],
          foreground=[('disabled', 'lightgrey')])

# ABRINDO ARQUIVO
open_button = ttk.Button(janela, text='Abrir',
                         command=lambda: file_df())
open_button.pack(pady=10)

# EXIBIR INFORMAÇÕES
info_button = ttk.Button(janela, text='Informações',
                         command=display_info)
info_button.pack(pady=10)

# LIMPAR OS DADOS
clean_button = ttk.Button(janela, text='Limpeza',
                          command=clean_df)
clean_button.pack(pady=10)

# RENOMEAR COLUNA
rename_button = ttk.Button(janela, text='Renomear Coluna',
                           command=rename_coluna)
rename_button.pack(pady=10)

# APAGAR COLUNA
result_button = ttk.Button(janela, text='Apagar coluna',
                           command=drop_columns)
result_button.pack(pady=10)

# MOSTRAR RESULTADO FINAL
result_button = ttk.Button(janela, text='Mostrar Resultado',
                           command=end_result)
result_button.pack(pady=10)




janela.mainloop()
