#ChatBot Básico com perguntas e respostas para que você possa me conhecer um pouquinho mais. ♥

import os

def processar_respostas(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, eu sou proficiente em Python, além de ter conhecimentos em HTML5 e CSS3.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, obtive formação em Análise e Desenvolvimento de Sistemas.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, para me manter atualizada sobre as tendências e novas tecnologias em programação,faço uso de uma variedade de recursos, cursos online, participação em comunidades de desenvolvimento, além de acompanhar blogs e sites especializados. Também gosto de participar de eventos e conferências da área, onde posso interagir com outros profissionais e aprender com suas experiências e perspectivas.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, considero-me uma programadora de nível intermediário em termos de experiência.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')

def start ():
    #Me apresentar pelo ChatBot
    print('Óla! Bem-vindo(a)')
    #Pedir o nome
    nome = input('Digite seu nome:')
    #Pedir o email
    email = input ('Digite seu email:')
    while True:
        #Oferecer o menu de opções de perguntas
        resposta = input(
        f'O que gostaria de saber sobre mim?'
        f'{os.linesep}[1] - Quais linguagens de programação você domina?'
        f'{os.linesep}[2] - Qual é a sua formação acadêmica em programação?'
        f'{os.linesep}[3] - Como você costuma se manter atualizado sobre as tendências e novas tecnologias em programação?'
        f'{os.linesep}[4] - Qual é o seu nível de experiência em programação?{os.linesep}')
        #Processar a resposta enviada
        processar_respostas(resposta, nome) 

if __name__=='__main__' :
    start()