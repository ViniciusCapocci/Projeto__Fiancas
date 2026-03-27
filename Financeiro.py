import time

# Bloco 0: Deposito
ValoresEntrada = []
Valores_despesa_fixa = []
Valores_despesa_variavel = []

nome = input('Por favor, informe seu nome: ')
print(f'\nOlá {nome}, seja bem-vinda à sua planilha financeira!')
print('Vamos começar!!!')
time.sleep(0.5)

# BLOCO 1: ENTRADAS 
while True:
    pergunta = input('\nTem mais de uma ENTRADA esse mês? Sim ou Não: ').upper().strip()
    if pergunta == 'SIM':
        while True:
            try:
                qtd = int(input('Digite a quantidade de entradas: '))
                break
            except ValueError:
                print('Erro: Digite um número inteiro para a quantidade.')
        
        i = 0
        while i < qtd:
            try:
                valor = float(input(f'Digite o {i+1}º valor recebido: ').replace(',', '.'))
                ValoresEntrada.append(valor)
                i += 1
            except ValueError:
                print('Erro: Valor inválido. Use apenas números.')
        break
    elif pergunta in ['NÃO', 'NAO', 'N']:
        while True:
            try:
                valor = float(input('Digite o valor que foi recebido: ').replace(',', '.'))
                ValoresEntrada.append(valor)
                break
            except ValueError:
                print('Erro: Valor inválido.')
        break
    else:
        print('Erro: Digite apenas "Sim" ou "Não".')

print(40*'_')

# BLOCO 2: DESPESAS FIXAS
while True:
    pergunta = input('E de DESPESAS FIXAS, tem mais de uma? Sim ou Não: ').upper().strip()
    if pergunta == 'SIM':
        while True:
            try:
                qtd = int(input('Digite a quantidade de despesas fixas: '))
                break
            except ValueError:
                print('Erro: Digite um número inteiro.')
        
        i = 0
        while i < qtd:
            try:
                valor = float(input(f'Digite o valor da {i+1}ª despesa fixa: ').replace(',', '.'))
                Valores_despesa_fixa.append(valor)
                i += 1
            except ValueError:
                print('Erro: Valor inválido.')
        break
    elif pergunta in ['NÃO', 'NAO', 'N']:
        while True:
            try:
                valor = float(input('Digite o valor da despesa fixa: ').replace(',', '.'))
                Valores_despesa_fixa.append(valor)
                break
            except ValueError:
                print('Erro: Valor inválido.')
        break
    else:
        print('Erro: Digite apenas "Sim" ou "Não".')

print(40*'_')

# BLOCO 3: DESPESAS VARIÁVEIS
while True:
    pergunta = input('Tem mais de uma DESPESA VARIÁVEL? Sim ou Não: ').upper().strip()
    if pergunta == 'SIM':
        while True:
            try:
                qtd = int(input('Quantas despesas variáveis: '))
                break
            except ValueError:
                print('Erro: Digite um número inteiro.')
        
        i = 0
        while i < qtd:
            try:
                valor = float(input(f'Digite o valor da {i+1}ª despesa variável: ').replace(',', '.'))
                Valores_despesa_variavel.append(valor)
                i += 1
            except ValueError:
                print('Erro: Valor inválido.')
        break
    elif pergunta in ['NÃO', 'NAO', 'N']:
        while True:
            try:
                valor = float(input('Digite o valor da despesa variável: ').replace(',', '.'))
                Valores_despesa_variavel.append(valor)
                break
            except ValueError:
                print('Erro: Valor inválido.')
        break
    else:
        print('Erro: Digite apenas "Sim" ou "Não".')

# 4. CÁLCULOS FINAIS
total_entrada = sum(ValoresEntrada)
total_despesas_fixa = sum(Valores_despesa_fixa)
total_variaveis = sum(Valores_despesa_variavel)
total_geral_despesas = total_despesas_fixa + total_variaveis
saldo_final = total_entrada - total_geral_despesas

print("\n" + 40*'=')
if saldo_final <= 0:
    print('CUIDADO! Você está gastando demais ou está no limite!')
else:
    print('Parabéns, suas finanças estão em ordem!')

print(f'\nTotal de Entradas:      R${total_entrada:.2f}')
print(f'Total Despesas Fixas:   R${total_despesas_fixa:.2f}')
print(f'Total Despesas Variáveis: R${total_variaveis:.2f}')
print(f'SALDO FINAL:            R${saldo_final:.2f}')
print(40*'=')

# 5. GRAVAÇÃO NO ARQUIVO
try:
    with open('dados.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(f'Relatório de {nome}\n')
        arquivo.write("-" * 50 + "\n")
        arquivo.write(f"{'Entradas':<15} | {'Fixas':<15} | {'Variáveis':<15}\n")
        arquivo.write(f"R${total_entrada:<13.2f} | R${total_despesas_fixa:<13.2f} | R${total_variaveis:<13.2f}\n")
        arquivo.write("-" * 50 + "\n")
        arquivo.write(f'Saldo Final que irá sobrar: R${saldo_final:.2f}\n')
    print("\nOs dados foram salvos com sucesso em 'dados.txt'!")
except Exception as e:
    print(f"\nErro ao salvar o arquivo: {e}")
