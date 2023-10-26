import csv
import json
from unidecode import unidecode

data = {}

def parse_number(s):
    # Substitua os pontos que separam os milhares por uma string vazia
    return int(s.replace('.', ''))

with open('02003.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Pula o cabeçalho
    for row in reader:
        total_nacional = unidecode(row[0])
        comunidad = unidecode(row[1])
        mes = unidecode(row[2])
        sexo = unidecode(row[3])
        valor = parse_number(row[4])  # Use a função para remover pontos e converter para inteiro
        
        if total_nacional not in data:
            data[total_nacional] = {}
        if comunidad not in data[total_nacional]:
            data[total_nacional][comunidad] = {}
        if mes not in data[total_nacional][comunidad]:
            data[total_nacional][comunidad][mes] = {}
        data[total_nacional][comunidad][mes][sexo] = valor

json_data = json.dumps(data, indent=4, ensure_ascii=False)

# Você pode imprimir o JSON ou salvá-lo em um arquivo, por exemplo:
with open('dados3.json', 'w', encoding='utf-8') as jsonfile:
    jsonfile.write(json_data)

print(json_data)
