import time




# def benchmark_new(function):
#     def inner():
#         print('Antes')
#         function()
#     return inner

def benchmark_old(function):
    print('TIME')
    function()
    
def benchmark(function):
    def inner_function():
        print("TIME FROM INNER")
        function()
    
    return inner_function

@benchmark
def dizer_ola():
    print('Olá!')

# def exibir_mensagem(callback, *args):
#     print("hello world")
#     print(time.time())
#     retorno = callback(args)
#     print(time.time())
#     return retorno

# def somar(values):
    # resultado = 0
    
    # for valor in values:
    #     resultado += valor
        
    # return resultado

if __name__ == "__main__":
    # resultado = exibir_mensagem(somar, 3, 6)
    # print(f'O resultado é: {resultado}')
    dizer_ola()