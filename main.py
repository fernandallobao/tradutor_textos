#Crie em Python, um tradutor, e envie o link do repositório.
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='auto', target='pt')

while True:

    texto = input('Informe o texto a ser traduzida: ')
    texto_traduzido = tradutor.translate(texto)
    print(texto_traduzido)

    op = input('Deseja traduzir outro texto (s/n)?').lower()
    if op == "s":
        continue
    else:
        break
print('Progama encerrado!')
