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

def soma_elementos(valores):
    return sum(valores)


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

def n_palavras_unicas(lista_palavras.split()):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras que aparecem uma única vez'''
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
def tamanho_das_palavras_somadas(texto_completo):
    palavras = texto_completo.split()
    tamanho_palavras = 0
    for palavra in palavras:
        tamanho_palavras += len(palavra)
    return tamanho_palavras


# Função que devolve o numero total de palavras do texto passado como parâmetro
def numero_total_palavras(texto_completo):   
    palavras = texto_completo.split()
    total_palavras = len(palavras)
    return total_palavras


# Função para devolver o tamanho médio de palavra
def tamanho_medio_palavra(texto):
    tamanho_medio = tamanho_das_palavras_somadas(texto) / numero_total_palavras(texto)
    return tamanho_medio


# Função para definir a relação type-token
def relacao_type_token(texto):
    type_token = n_palavras_diferentes(texto) / numero_total_palavras(texto)
    return type_token

# Função para definir a Razão Hapax Legomana
def razao_hapax_legomana(texto):
    hapax_legomana = n_palavras_unicas(texto.split()) / numero_total_palavras(texto)
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
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    diferenca_absoluta = sum(abs(calcula_assinatura(as_a) - calcula_assinatura(as_b)))
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
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    textos_a_avaliar = [textos]
    valores_das_assinaturas = []
    for texto in textos_a_avaliar:
        valores_das_assinaturas.append(calcula_assinatura(texto))
        for valor in valores_das_assinaturas:
            numero_mais_proximo = proximidade_numerica(valor, ass_cp)
            if numero_mais_proximo < 6:
                pass
            else:
                return numero_mais_proximo

    

# def main():
#     tracos_linguisticos = le_assinatura()
#     assinatura_conhecida = soma_elementos(tracos_linguisticos)

#     textos = le_textos()
#     resultado = avalia_textos(textos, assinatura_conhecida)
    
texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
resultado = n_palavras_unicas(texto)
print(resultado)

            

    
# exemplo = "oi tudo bem com voce"
# lista_palavras = exemplo.split()
# resultado =  n_palavras_unicas(lista_palavras)
# print(resultado)   