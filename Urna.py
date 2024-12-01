import tkinter as tk
from tkinter import messagebox
import pickle
import csv
import os


class UrnaEletronica:
    def __init__(self, master):
        self.master = master
        self.master.title("Urna Eletrônica")
        self.master.geometry("400x500")
        self.master.resizable(False, False)

        # Dados
        self.candidatos = self.carregar_dados("candidatos.csv")
        self.eleitores = self.carregar_dados("eleitores.csv")
        self.votos = self.carregar_votos("votos.pkl")
        self.eleitor_atual = None

        # Interface inicial
        self.create_login_interface()

    def carregar_dados(self, arquivo):
        """Carrega os dados de eleitores ou candidatos de um arquivo CSV ou PKL."""
        if not os.path.exists(arquivo):
            messagebox.showerror("Erro", f"Arquivo {arquivo} não encontrado.")
            self.master.destroy()
            return {}

        if arquivo.endswith(".csv"):
            try:
                with open(arquivo, newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    dados = {linha["id"]: linha["nome"] for linha in reader}
                    print(f"Dados carregados de {arquivo}: {dados}")  # Debug
                    return dados
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar {arquivo}: {str(e)}")
                self.master.destroy()
                return {}

    def carregar_votos(self, arquivo):
        """Carrega os votos armazenados ou cria uma nova estrutura."""
        if os.path.exists(arquivo):
            with open(arquivo, "rb") as f:
                return pickle.load(f)
        return {"branco": 0, "inválido": 0, **{nome: 0 for nome in self.candidatos.values()}}

    def salvar_votos(self, arquivo):
        """Salva os votos no arquivo .pkl."""
        with open(arquivo, "wb") as f:
            pickle.dump(self.votos, f)

    def create_login_interface(self):
        """Interface inicial para o login do eleitor."""
        self.clear_interface()

        tk.Label(self.master, text="Digite o título de eleitor", font=("Helvetica", 14)).pack(pady=10)
        self.titulo_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.titulo_entry.pack(pady=10)

        tk.Button(self.master, text="Confirmar", font=("Helvetica", 12), bg="green", fg="white", command=self.validar_eleitor).pack(pady=10)
