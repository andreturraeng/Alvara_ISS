from time import sleep
import colorama
from colorama import Fore, Style, Back
colorama.init()


def calculo_iss(area, valor_finalidade, valor_tipo):
    valor_iss = area * valor_finalidade * valor_tipo * aliq_iss
    return valor_iss


def calculo_alvara(area):
    valor_alvara = area * valor_m2_alvara
    return valor_alvara


def escolhe_finalidade(f):
    valor_finalidade = finalidade[(2 * f) - 1]
    return valor_finalidade


def escolhe_tipo(t):
    valor_tipo = tipo[(2 * t) - 1]
    return valor_tipo


def total(valor_alvara, valor_iss):
    total = valor_alvara + valor_iss
    return total


paraoucontinua = ''
while paraoucontinua != 'n':
    # PROGRAMA PRINCIPAL
    finalidade = ['residencial', 140, 'comercial', 108, 'industrial', 83, 'galpao', 56]
    tipo = ['alvenaria', 1, 'mista', 0.70, 'metalica', 0.60, 'madeira', 0.50]
    aliq_iss = 0.02
    valor_m2_alvara = 1.70


    titulo = (' ' * 12) + 'CALCULADORA DE ALVARÁ E ISS' + (' ' * 12)
    print(Fore.GREEN + ('*' * len(titulo)))
    print(titulo)
    print('*' * len(titulo) + Style.RESET_ALL)


    while True:
        print('\nPara inciar, escolha a "FINALIDADE" da construção:\n')
        f = input(f"Digite 1 para: {'Construção Residencial':-^35}\n"
                  f"Digite 2 para: {'Construção Comercial':-^35}\n"
                  f"Digite 3 para: {'Construção Industrial':-^35}\n"
                  f"Digite 4 para: {'Construção de Galpão':-^35}\n")
        if f in ('1', '2', '3', '4'):
            f = int(f)
            break
        else:
            print(Fore.RED + 'ERRO! Digite uma opção válida' + Style.RESET_ALL)

    while True:
        print('Agora escolha o "TIPO" de construção:\n')
        t = input(f"Digite 1 para: {'Alvenaria':-^35}\n"
                  f"Digite 2 para: {'Mista':-^35}\n"
                  f"Digite 3 para: {'Metálica':-^35}\n"
                  f"Digite 4 para: {'Madeira':-^35}\n")
        if t in ('1', '2', '3', '4'):
            t = int(t)
            break
        else:
            print(Fore.RED + 'ERRO! Digite uma opção válida' + Style.RESET_ALL)

    while True:
        try:
            area = float(input('Por fim, insira a "ÁREA CONSTRUÍDA": ').replace(',', '.'))
            if type(area) == float:
                break
        except:
            print(Fore.RED + '\nERRO! Valor inválido, tente novamente\n' + Style.RESET_ALL)

    escolhe_finalidade(f)
    escolhe_tipo(t)
    valor_finalidade = escolhe_finalidade(f)
    valor_tipo = escolhe_tipo(t)
    valor_iss = calculo_iss(area, valor_finalidade, valor_tipo)
    valor_alvara = calculo_alvara(area)

    print(Fore.GREEN + '\nCALCULANDO' + Style.RESET_ALL, end='')
    sleep(0.5)
    print(Fore.GREEN + '.' + Style.RESET_ALL, end='', flush=True)
    sleep(0.5)
    print(Fore.GREEN + '.' + Style.RESET_ALL, end='', flush=True)
    sleep(0.5)
    print(Fore.GREEN + '.' + Style.RESET_ALL, flush=True)
    sleep(0.5)
    print('\nO valor do ' + Fore.GREEN + 'ISS' + Style.RESET_ALL + ' fica em ' + Fore.GREEN + f'R$ {calculo_iss(area, valor_finalidade, valor_tipo):.2f}' + Style.RESET_ALL)
    print('O valor do ' + Fore.GREEN + 'ALVARÁ DE CONSTRUÇÃO' + Style.RESET_ALL + ' fica em ' + Fore.GREEN + f'R$ {calculo_alvara(area):.2f}' + Style.RESET_ALL)
    print('O valor total das ' + Fore.GREEN + 'TAXAS' + Style.RESET_ALL + ' fica em ' + Fore.GREEN + f'R$ {total(valor_alvara, valor_iss):.2f}\n' + Style.RESET_ALL)

    while True:
        paraoucontinua = input('Deseja fazer um novo cálculo? [S/N]').lower()
        if paraoucontinua not in 'sn':
            print(Fore.RED + '\nERRO! Digite S ou N\n' + Style.RESET_ALL)
        else:
            break
