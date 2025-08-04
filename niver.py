
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
import sys

CONTATOS_ARQUIVO = "aniversarios.txt"

# Caminho para a pasta Startup do usuário
STARTUP_PATH = os.path.join(os.getenv("APPDATA"), r"Microsoft\\Windows\\Start Menu\\Programs\\Startup")
SCRIPT_PATH = os.path.abspath(sys.argv[0])
BAT_PATH = os.path.join(STARTUP_PATH, "niver_startup.bat")

def adicionar_ao_startup():
    if not os.path.exists(BAT_PATH):
        with open(BAT_PATH, "w") as bat_file:
            bat_file.write(f'start "" python "{SCRIPT_PATH}"\n')

def carregar_contatos():
    contatos = {}
    if os.path.exists(CONTATOS_ARQUIVO):
        with open(CONTATOS_ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha and not linha.startswith("#"):
                    try:
                        nome, data_str = linha.split(",")
                        data_nasc = datetime.strptime(data_str, "%d/%m/%Y")
                        contatos[nome] = data_nasc
                    except ValueError:
                        print(f"Formato inválido na linha: {linha}")
    return contatos

def verificar_aniversario():
    hoje = datetime.now()
    contatos = carregar_contatos()
    aniversariantes = []

    for nome, data_nasc in contatos.items():
        if data_nasc.day == hoje.day and data_nasc.month == hoje.month:
            idade = hoje.year - data_nasc.year
            aniversariantes.append(f"{nome} está fazendo {idade} anos, nascido em {data_nasc.year}")

    return aniversariantes

def exibir_aviso(aniversariantes):
    root = tk.Tk()
    root.withdraw()
    if aniversariantes:
        mensagem = "Hoje é o aniversário de:\n\n" + "\n".join(aniversariantes)
        messagebox.showinfo("Lembrete de aniversário!", mensagem)
    root.destroy()

def criar_arquivo_contatos():
    if not os.path.exists(CONTATOS_ARQUIVO):
        with open(CONTATOS_ARQUIVO, "w", encoding="utf-8") as arquivo:
            arquivo.write("# Formato: Nome,DD/MM/AAAA\n")
            arquivo.write("Exemplo,01/01/2000\n")

def main():
    criar_arquivo_contatos()
    aniversariantes = verificar_aniversario()
    if aniversariantes:
        exibir_aviso(aniversariantes)
    adicionar_ao_startup()

if __name__ == "__main__":
    main()
