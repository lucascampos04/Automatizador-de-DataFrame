import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk
import pandas as pd

df = None

def file_df():
    global df
    open_df = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
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

def calculate_statistics():
    if df is not None:
        print('\nEstatísticas do DataFrame:')
        print('Média:', df.mean())
        print('Mediana:', df.median())
        print('Desvio Padrão:', df.std())
    else:
        print("Nenhum DataFrame foi encontrado.")

def save_df():
    if df is not None:
        save_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
        df.to_csv(save_path, index=False)
        print("DataFrame salvo com sucesso.")

janela = tk.Tk()
janela.title("Automatizador de DataFrame")
janela.geometry('500x400')
janela.configure(bg='lightgray')

# Estilização dos botões
style = ttk.Style()
style.configure('TButton', font=('Arial', 10, 'bold'), foreground='blue')

style.map('TButton',
          background=[('active', 'darkblue'), ('disabled', 'grey')],
          foreground=[('disabled', 'lightgrey')])

# Painel esquerdo com os botões
left_frame = tk.Frame(janela, bg='lightgray')
left_frame.pack(side='left', padx=10, pady=10)

# ABRINDO ARQUIVO
open_button = ttk.Button(left_frame, text='Abrir', command=lambda: file_df())
open_button.pack(pady=10)

# EXIBIR INFORMAÇÕES
info_button = ttk.Button(left_frame, text='Informações', command=display_info)
info_button.pack(pady=10)

# LIMPAR OS DADOS
clean_button = ttk.Button(left_frame, text='Limpeza', command=clean_df)
clean_button.pack(pady=10)

# RENOMEAR COLUNA
rename_button = ttk.Button(left_frame, text='Renomear Coluna', command=rename_coluna)
rename_button.pack(pady=10)

# APAGAR COLUNA
result_button = ttk.Button(left_frame, text='Apagar coluna', command

=drop_columns)
result_button.pack(pady=10)

# CALCULAR ESTATÍSTICAS
statistics_button = ttk.Button(left_frame, text='Estatísticas', command=calculate_statistics)
statistics_button.pack(pady=10)

# SALVAR DATAFRAME
save_button = ttk.Button(left_frame, text='Salvar DataFrame', command=save_df)
save_button.pack(pady=10)

# Painel direito para exibir resultados
result_frame = tk.Frame(janela, bg='white')
result_frame.pack(side='right', padx=10, pady=10, fill='both', expand=True)

# Etiqueta para mostrar a limpeza do DataFrame
clean_label = tk.Label(result_frame, text="Limpeza do DataFrame", font=('Arial', 12, 'bold'))
clean_label.pack(pady=10)

# Texto para exibir a limpeza do DataFrame
clean_text = tk.Text(result_frame, height=20, width=40)
clean_text.pack()

janela.mainloop()