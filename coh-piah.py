import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
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
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
            if freq[p] == 2:
                unicas -= 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

# Função que devolve a soma dos tamanhos de todas as palavras do texto
def tamanho_das_palavras_somadas(texto):
    tamanho_palavras = 0

    palavras = separa_palavras(texto)
    for palavra in palavras:
        tamanho_palavras += len(palavra)
    print(f"Tamanho total das palavras: {tamanho_palavras}")

    return tamanho_palavras






# Função que devolve o numero total de palavras do texto passado como parâmetro
def numero_total_palavras(texto_completo):   
    palavras = texto_completo.split()
    total_palavras = len(palavras)
    return total_palavras


# Função para devolver o tamanho médio de palavra
def tamanho_medio_palavra(texto):
    tamanho_palavras = len(separa_palavras(texto))
    total_palavras = numero_total_palavras(texto)
    resultado = tamanho_palavras / total_palavras if total_palavras > 0 else 0
    return resultado



# Função para definir a relação type-token
def relacao_type_token(texto):
    palavras = texto.split()
    type_token = n_palavras_diferentes(palavras) / numero_total_palavras(texto)
    return type_token

# Função para definir a Razão Hapax Legomana
def razao_hapax_legomana(texto):
    texto1 = texto.split()
    hapax_legomana = n_palavras_unicas(texto1) / numero_total_palavras(texto)
    print(hapax_legomana)
    return hapax_legomana


# Função para calcular o tamanho médio de sentença
def tamanho_medio_sentenca(texto):
    sentencas = separa_sentencas(texto)
    num_sentencas = len(sentencas)
    total_caracteres = sum(len(sentenca) for sentenca in sentencas)
    tamanho_medio = total_caracteres / num_sentencas

    return tamanho_medio

#  Função que retorna a complexidade de sentença
def complexidade_de_sentenca(texto):
    sentencas = separa_sentencas(texto)
    num_de_frases = 0
    for sentenca in sentencas:
        num_de_frases += len(separa_frases(sentenca))
    complexidade = num_de_frases / len(sentencas)
    return complexidade    

def tamanho_medio_frase(texto):
    sentencas = separa_sentencas(texto)
    num_caracteres_frase = 0
    num_frases = 0

    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        num_frases += len(frases)

        for frase in frases:
            num_caracteres_frase += len(frase)

    if num_frases > 0:
        tamanho_medio = num_caracteres_frase / num_frases
        return tamanho_medio
    else:
        return 0       

def compara_assinatura(as_a, as_b):
    '''Essa função recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    diferenca_absoluta = sum(abs(a - b) for a, b in zip(as_a, as_b))
    similaridade_ab = diferenca_absoluta / 6
    return similaridade_ab
   

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    tamMedioPalavra = tamanho_medio_palavra(texto)
    typeToken = relacao_type_token(texto)
    hapaxLegomana = razao_hapax_legomana(texto)
    tamMedioSentenca = tamanho_medio_sentenca(texto)
    complexSentenca = complexidade_de_sentenca(texto) 
    tamMedioFrase = tamanho_medio_frase(texto)

    return [tamMedioPalavra, typeToken, hapaxLegomana, tamMedioSentenca, complexSentenca,  tamMedioFrase ] 


def proximidade_numerica(num1, num2):
    diferenca_absoluta = abs(num1 - num2)

    intervalo_maximo = 100 

    pontuacao_maxima = 10
    
    pontuacao = pontuacao_maxima - (diferenca_absoluta / intervalo_maximo) * pontuacao_maxima
    
    pontuacao = max(1, min(10, pontuacao))
    
    return pontuacao

def avalia_textos(textos, ass_cp):
    '''Essa função recebe uma lista de textos e uma assinatura ass_cp e deve devolver o número (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    valores_das_assinaturas = []
    
    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura_texto, ass_cp)
        valores_das_assinaturas.append(similaridade)

    indice_mais_proximo = valores_das_assinaturas.index(min(valores_das_assinaturas)) + 1
    
    return indice_mais_proximo


    


    
def main():
    valores_conhecidos = le_assinatura()

    textos_a_comparar = le_textos()
    comparacao = avalia_textos(textos_a_comparar, valores_conhecidos)
    resultado = print("O autor do texto ", comparacao, " está infectado com COH-PIAH")
    return resultado
    

main()





           

    
