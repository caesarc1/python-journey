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
        total_vendas = self._calcular_total()
        venda_dinheiro = total_vendas - sum(
            [
                self.debito,
                self.credito,
                self.alelo,
                self.ticket,
                self.sodexo,
                self.ben,
                self.pix,
            ]
        )

        self._exibir_resultados(total_vendas, venda_dinheiro)

    def _calcular_total(self):
        return (
            sum(
                [
                    self.sobra_dinheiro,
                    self.saida,
                    self.fundo_caixa,
                    self.debito,
                    self.credito,
                    self.alelo,
                    self.ticket,
                    self.sodexo,
                    self.ben,
                    self.pix,
                ]
            )
        ) - self.caixa_ontem

    def _exibir_resultados(self, total_vendas, venda_dinheiro):
        print(
            f"Total de vendas: {total_vendas}\n"
            f"Vendas em Dinheiro: {venda_dinheiro}\n"
            f"Vendas no Débito: {self.debito}\n"
            f"Vendas no Crédito: {self.credito}\n"
            f"Vendas no Alelo: {self.alelo}\n"
            f"Vendas no Ticket: {self.ticket}\n"
            f"Vendas no Sodexo: {self.sodexo}\n"
            f"Vendas no Ben: {self.ben}\n"
            f"Vendas no Pix: {self.pix}"
        )


try:
    sobra_dinheiro = input("Insira quanto sobrou em dinheiro: ").replace(",", ".")
    sobra_dinheiro = float(sobra_dinheiro)

    saida = input("Insira quanto saiu do caixa: ").replace(",", ".")
    saida = float(saida)

    fundo_caixa = input(
        "Insira quanto você deixou pro caixa do dia seguinte: "
    ).replace(",", ".")
    fundo_caixa = float(fundo_caixa)

    debito = input("Insira quanto vendeu em Débito: ").replace(",", ".")
    debito = float(debito)

    credito = input("Insira quanto vendeu em Crédito: ").replace(",", ".")
    credito = float(credito)

    alelo = input("Insira quanto vendeu em Alelo: ").replace(",", ".")
    alelo = float(alelo)

    ticket = input("Insira quanto vendeu em Ticket: ").replace(",", ".")
    ticket = float(ticket)

    sodexo = input("Insira quanto vendeu em Sodexo: ").replace(",", ".")
    sodexo = float(sodexo)

    ben = input("Insira quanto vendeu em Ben: ").replace(",", ".")
    ben = float(ben)

    pix = input("Insira quanto vendeu no Pix: ").replace(",", ".")
    pix = float(pix)

    caixa_ontem = input("Insira o valor do caixa de ontem: ").replace(",", ".")
    caixa_ontem = float(caixa_ontem)

    caixa = Caixa(
        sobra_dinheiro=sobra_dinheiro,
        saida=saida,
        fundo_caixa=fundo_caixa,
        debito=debito,
        credito=credito,
        alelo=alelo,
        ticket=ticket,
        sodexo=sodexo,
        ben=ben,
        pix=pix,
        caixa_ontem=caixa_ontem,
    )
except ValueError:
    print("Entrada inválida. Certifique-se de inserir um número válido.")

caixa.fechar_caixa()
