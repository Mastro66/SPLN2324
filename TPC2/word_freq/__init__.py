#!/usr/bin/env python3

# Documentação que fica guardada na variável __doc__
'''
NAME
   word_freq - Calculates word frequency in a text

SYNOPSIS
   word_freq [options] input_files
   options: 
        -m 20 : Show 20 most common
        -n : Order alfabetically
        -o : Change all Capital letters to lower case
Description'''


from jjcli import * 
from collections import Counter # Dicionario chave - nº ocorrencias (multi-set)
import re

__version__ = "0.0.1"

def tokeniza(texto):
    palavras = re.findall(r'\w+(?:\-\w+)?|[,;.:_?!—]+', texto)
    # (?: ...) agrupa mas não captura
    return palavras

def imprime(lista, opt):
    if opt == 'm':
        for palavra, n_ocorr in lista:
            print(f"{palavra}   {n_ocorr}")
    elif opt == 'n':
        for palavra, n_ocorr in lista:
            print(f"{n_ocorr}   {palavra}")
    elif opt == 'o':
        for palavra, n_ocorr in lista:
            print(f"{n_ocorr}   {palavra}")
def main():
    # "-m" recebe um argumento logo leva ":", ao contrário de "-n"
    cl=clfilter("nmo:", doc=__doc__)     ## option values in cl.opt dictionary

    for txt in cl.text():     ## process one file at the time
        lista_palavras = tokeniza(txt)
        ocorr = Counter(lista_palavras)

        if "-m" in cl.opt:
            imprime(ocorr.most_common(int(cl.opt.get("-m"))), 'm')
        elif "-n" in cl.opt:
            lista_palavras.sort()
            ocorr = Counter(lista_palavras)
            imprime(ocorr.items(), 'n')
        elif "-o" in cl.opt: # turn the capital letters into lower case
            lista_palavras.lower()
            ocorr = Counter(lista_palavras)
            imprime(ocorr.items(), 'o')
        else:
            imprime(ocorr.items(), 'm')


### TPC
# 1. Arranjar/procurar uma tabela padrão de frequenicas do portugues - Sugestão: no tio google perguntar tabela da frequencia das palavras portuguesas
# 2. Limpeza. Deitar palavras fora que são numeros (13h42m, limpar isto por exemplo) ou remover coisas que notamos que não sejam interessantes
# 3. Arranjar à mão uma fórmula que seja capaz de comparar racios de frequencias de palavras entre duas palavras



