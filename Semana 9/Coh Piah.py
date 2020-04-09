import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas [-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()
    
def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower ()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower ()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    somatorio = 0
    indice = 0
    while indice < len(as_a):
       somatorio += abs(as_a[indice] - as_b[indice])
       indice += 1
    similaridade = (somatorio / 6)

    return similaridade

def separador_listas(lista):
    aux = []
    for i in lista:
        for j in i:
            aux.append(j)

    return aux

def contador_caracteres(lista):
    caracteres = 0
    for i in lista:
        for j in i:
            caracteres += 1

    return caracteres

def calcula_assinatura(texto):
    aux_palavras = []
    aux_frases = []
    letras = 0
      
    sentencas = separa_sentencas(texto)
    qtde_sentencas = len(sentencas)
    caracteres_sentencas = contador_caracteres(sentencas)
    

    for i in sentencas:
        aux_frases.append(separa_frases(i))
    frases = separador_listas(aux_frases)
    qtde_frases = len(frases)
    caracteres_frases = contador_caracteres(frases)
    
    for i in frases:
        aux_palavras.append(separa_palavras(i))
    palavras = separador_listas(aux_palavras)
    qtde_palavras = len(palavras)

    qtde_palavras_unicas = n_palavras_unicas(palavras)
    
    qtde_palavras_diferentes = n_palavras_diferentes(palavras)
    
    for i in palavras:
        letras += len(i)
       
    wal = letras / qtde_palavras
    ttr = qtde_palavras_diferentes / qtde_palavras
    hlr = qtde_palavras_unicas / qtde_palavras
    sal = caracteres_sentencas / qtde_sentencas
    sac = qtde_frases / qtde_sentencas
    pal = caracteres_frases / qtde_frases

    ass = [wal, ttr, hlr, sal, sac, pal]

    return ass
    
def avalia_textos(textos, ass_cp):
    cohpiah = 10000
    for i in textos:
        ass = calcula_assinatura(i)
        semelhanca = compara_assinatura(ass_cp, ass)
        if semelhanca < cohpiah:
            cohpiah = int(semelhanca)

    return cohpiah


    
