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
