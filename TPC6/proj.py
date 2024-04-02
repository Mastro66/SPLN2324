import spacy
from collections import defaultdict

# Carregar modelo de língua portuguesa
nlp = spacy.load("pt_core_news_lg")

def calcular_amizades(texto):
    # Processar o texto com o modelo Spacy
    doc = nlp(texto)
    
    # Dicionário para armazenar as contagens de amizades
    amizades = defaultdict(int)
    
    # Lista para armazenar os nomes próprios no texto
    nomes_proprios = [ent.text for ent in doc.ents if ent.label_ == "PER"]
    
    # Iterar sobre as frases no documento
    for sent in doc.sents:
        # Verificar se há nomes próprios na frase
        nomes_na_frase = [token.text for token in sent if token.text in nomes_proprios]
        # Atualizar as contagens de amizades
        for nome1 in nomes_na_frase:
            for nome2 in nomes_na_frase:
                if nome1 != nome2:
                    # Ordenar os nomes alfabeticamente para evitar repetição
                    par_ordenado = tuple(sorted([nome1, nome2]))
                    amizades[par_ordenado] += 1
    
    return amizades

def guardar_resultado(tabela_amizades, output_path, palavras_indesejadas=None):
    if palavras_indesejadas is None:
        palavras_indesejadas = set()  # Criar um conjunto vazio se não for fornecido
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("Tabela de Amizades:\n")
        f.write("----------------------\n")
        for amizade, contagem in tabela_amizades.items():
            nome1, nome2 = amizade
            # Verificar se algum dos nomes está na lista de palavras indesejadas
            if nome1 not in palavras_indesejadas and nome2 not in palavras_indesejadas:
                f.write(f"{nome1} e {nome2}: {contagem}\n")

# Função para ler o texto de um arquivo
def ler_arquivo(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

# Lista de palavras indesejadas que você deseja remover do resultado
palavras_indesejadas = {"rapaz", "Coisinha", "Murmuravam","Porquê","Acha","Pedi-a","Er","Tinham","jardinzinhos","gordíssimo",
                        "Parecia","Safadinho","Querido","lho","Podiam","mr","Vivia","Vai","Espicaça-o","Pai",
                        "Olharam","BOOOOOM","Trazia","Desculpe","Fui","Sonhei","Hum","Ir-te","Ouviram","Vamos",
                        "Maldições","lha","embrulhos","Cala-te","P.","Herdei","És","Imensa","Gryffindor","Hufflepuff",
                        "Slyverin","Ravenclaw","GRYFFINDOR","barman","abençoado","Madame","Esperava","Abanou", "dou-te","bludger"
                        ,"Devem","Atrás","bramiu","Julgo","Bebe","Consegues","Aterraram","Absoluta","Estavam","Certo","seroes","Adeus",
                        "Mal","Terei","Pôs-lhes","Apontando-o","Meteu","Importas-te","Louco","Difícil","Cruel","Achaste"}

# Arquivo de entrada e saída
file_path = "HP.txt"
output_path = "output.txt"

# Ler o texto do arquivo
texto = ler_arquivo(file_path)

# Calcular amizades no texto
tabela_amizades = calcular_amizades(texto)

# Salvar o resultado no arquivo de saída, removendo palavras indesejadas
guardar_resultado(tabela_amizades, output_path, palavras_indesejadas)

print("Resultado salvo com sucesso em:", output_path)