class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def alterarValor(self, valor):
        self.valorLitro = valor

    def alterarCombustivel(self, combustivel):
        self.tipoCombustivel = combustivel
    
    def alterarQuantidadeCombustivel(self, valor):
        self.quantidadeCombustivel = valor

    def mostrarQuantidade(self):
        print(f"A quantidade de combustivel atual é: {self.quantidadeCombustivel:.1f}L")

    def abastecerPorValor(self, valor):
        totaLitros = valor/self.valorLitro
        print(f"A quantidade abastecida foi: {totaLitros:.1f}L")
        self.quantidadeCombustivel+=totaLitros

    def abastecerPorLitro(self, litro):
        totalLitros = litro
        precoTotal = totalLitros*self.valorLitro
        print(f"O total a ser pago é: {precoTotal:.1f}R$")
        self.quantidadeCombustivel+=totalLitros

class Carro:
    def __init__(self, consumoGasolina):
        self.consumo = consumoGasolina
        self.combustivel = 0

    def adicionarGasolina(self, valor):
        self.combustivel+=valor
        print(f"você adicionou: {valor:.1f}L")
    
    def andar(self, km):
        litrosGastos = km/self.consumo
        self.combustivel-=litrosGastos
        print(f'Você andou {km}km e gastou {litrosGastos}')
    
    def obterGasolina(self):
        print(f"A quantidade de gasolina atual é: {self.combustivel:.1f}")

fusca = Carro(15)
fusca.obterGasolina()

fusca.adicionarGasolina(20)
fusca.obterGasolina()

fusca.andar(100)
fusca.obterGasolina()