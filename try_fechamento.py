import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class CaixaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fechamento de Caixa")

        self.labels = [
            "Sobra de dinheiro",
            "Saída do caixa",
            "Fundo de caixa",
            "Débito",
            "Crédito",
            "Alelo",
            "Ticket",
            "Sodexo",
            "Ben",
            "Pix",
            "Caixa de ontem",
        ]
        self.entries = []

        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12))
        style.configure("TEntry", font=("Arial", 12))

        for i, label_text in enumerate(self.labels):
            label = ttk.Label(master, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(master)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)
            if i == len(self.labels) - 1:  # Último campo de entrada
                entry.bind("<Return>", lambda event: self.fechar_caixa())

        self.submit_button = ttk.Button(
            master, text="Fechar Caixa", command=self.fechar_caixa
        )
        self.submit_button.grid(row=len(self.labels), columnspan=2, pady=10)

    def focus_next_entry(self, event, entry):
        next_index = (self.entries.index(entry) + 1) % len(self.entries)
        self.entries[next_index].focus()
        
    def fechar_caixa(self):
        try:
            valores = [float(entry.get().replace(",", ".")) for entry in self.entries]
            caixa = Caixa(*valores)
            (
                total_vendas,
                venda_dinheiro,
                self.debito,
                self.credito,
                self.alelo,
                self.ticket,
                self.sodexo,
                self.ben,
                self.pix,
            ) = caixa.fechar_caixa()
            messagebox.showinfo(
                "Resultado",
                f"Total de vendas: {total_vendas}\n"
                f"Vendas em Dinheiro: {venda_dinheiro}\n"
                f"Vendas no Débito: {self.debito}\n"
                f"Vendas no Crédito: {self.credito}\n"
                f"Vendas no Alelo: {self.alelo}\n"
                f"Vendas no Ticket: {self.ticket}\n"
                f"Vendas no Sodexo: {self.sodexo}\n"
                f"Vendas no Ben: {self.ben}\n"
                f"Vendas no Pix: {self.pix}",
            )
        except ValueError:
            messagebox.showerror(
                "Erro", "Entrada inválida. Certifique-se de inserir um número válido."
            )


class Caixa:
    def __init__(
        self,
        sobra_dinheiro,
        saida,
        fundo_caixa,
        debito,
        credito,
        alelo,
        ticket,
        sodexo,
        ben,
        pix,
        caixa_ontem,
    ):
        self.sobra_dinheiro = sobra_dinheiro
        self.saida = saida
        self.fundo_caixa = fundo_caixa
        self.debito = debito
        self.credito = credito
        self.alelo = alelo
        self.ticket = ticket
        self.sodexo = sodexo
        self.ben = ben
        self.pix = pix
        self.caixa_ontem = caixa_ontem

    def fechar_caixa(self):
        total_vendas = (
            self.sobra_dinheiro
            + self.saida
            + self.fundo_caixa
            + self.debito
            + self.credito
            + self.alelo
            + self.ticket
            + self.sodexo
            + self.ben
            + self.pix
            - self.caixa_ontem
        )

        venda_dinheiro = (
            total_vendas
            - self.debito
            - self.credito
            - self.alelo
            - self.ticket
            - self.sodexo
            - self.ben
            - self.pix
        )

        return (
            total_vendas,
            venda_dinheiro,
            self.debito,
            self.credito,
            self.alelo,
            self.ticket,
            self.sodexo,
            self.ben,
            self.pix,
        )


root = tk.Tk()
caixa_gui = CaixaGUI(root)
root.mainloop()