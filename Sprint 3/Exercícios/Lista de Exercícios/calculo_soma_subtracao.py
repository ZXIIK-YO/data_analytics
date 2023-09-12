# Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
# Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).
# Utilize os valores abaixo para testar seu exercício:

# x = 4 
# y = 5
# imprima:

# Somando: 4+5 = 9
# Subtraindo: 4-5 = -1

class Calculo:
    def somar(self, x, y):
        resultado = x + y
        return resultado

    def subtrair(self, x, y):
        resultado = x - y
        return resultado

# Valores para teste
x = 4
y = 5

# Cria uma instância da classe Calculo
calculadora = Calculo()

# Realiza a soma e a subtração usando os métodos da classe
soma = calculadora.somar(x, y)
subtracao = calculadora.subtrair(x, y)

# Imprime os resultados
print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")
