import pyperclip
from unidecode import unidecode
import re

EMOJI_A = ord('🇦')
QUADRADO1 = '0️⃣'[1]
QUADRADO2 = '0️⃣'[2]

while True:
    texto = input("Frase: ")
    texto = texto.lower()
    lista_palavras = list()
    #divide o texto pelo espaços em branco
    for palavra in texto.split(' '):
        emote_regex = re.compile(r':.*:')
        match = emote_regex.match(palavra)
        if match:
            lista_palavras.append(palavra)
        else:
            emojis = str()
            for caracter in palavra:
                #retira acentos
                caracter = unidecode(caracter)
                #verifica se é uma letra de A a Z
                if caracter.isalpha() and ord(caracter) >= 97 and ord(caracter) <= 122:
                    #o emoji é formado apartir do numero da tabela ascii dele
                    #por exemplo 🇧 é formado somando o numero da tabela ascii de 🇦 com  
                    #o numero da tabela ascii de b menos 97(que é o numero da tabela ascii de a) 
                    emojis += chr(EMOJI_A + ord(caracter) - 97)+" "
                #verifica se é numero ou * ou #
                elif caracter.isdigit() or caracter == '*' or caracter == '#':
                    #por exemplo 0️⃣ é a união de 0 com ️ e com ⃣
                    emojis += f'{caracter}{QUADRADO1}{QUADRADO2}'
                elif caracter == '?':
                    emojis += ':question:'
                else:
                    emojis += caracter
            lista_palavras.append(emojis)
    if len(lista_palavras) > 1:
        texto_emojis = ':null:'.join(lista_palavras)
    else:
        texto_emojis = lista_palavras[0]
    pyperclip.copy(texto_emojis)