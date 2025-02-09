def aumentar(n):
    p = (n/100) *10
    sa = n + p
    return sa


def diminuir(n):
    p = (n/100) *13
    sd = n - p 
    return sd


def dobro(n):
    sdo = n * 2
    return sdo


def metade(n):
    sme = n / 2
    return sme


def moeda(preco = 0, moeda = 'R$'):
    return print(f'{moeda}{preco:.2f}'.replace('.', ','))

