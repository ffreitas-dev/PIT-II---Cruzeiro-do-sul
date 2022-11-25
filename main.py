import requests
import boot
import lista
from chatterbot import ChatBot
import PySimpleGUI as sg


# Menu sair já ok
def menu_sair(jn_principal):
    #jn_principal.close()
    jn_sair = [
        [sg.Text("Até logo")],
    ]

    jn_sair = sg.Window("Saindo...", jn_sair)
    while True:
        evento, valores = jn_sair.read()
        if evento == sg.WIN_CLOSED:
            break

    jn_sair.close()


# Menu apagar já ok
def menu_apagar(jn_principal, chatbot):
    #jn_principal.close()
    chatbot.storage.drop()
    jn_apagar = [
        [sg.Text("Me treine novamente")],
    ]

    jn_sair = sg.Window("Saindo...", jn_apagar)
    while True:
        evento, valores = jn_sair.read()
        if evento == sg.WIN_CLOSED:
            break


# Menu treinar já ok
def menu_treinar(jn_principal, chatbot):
    #jn_principal.close()
    boot.treinar(chatbot)
    jn_treinar = [
        [sg.Text("Banco de dados atualizado!")],
    ]

    jn_treinar = sg.Window("Treinado...", jn_treinar)
    while True:
        evento, valores = jn_treinar.read()
        if evento == sg.WIN_CLOSED:
            break

    jn_treinar.close()


# Menu adicionar ok! Testar se ta realmente add informação apos treinamento
def menu_adicionar(jn_principal):
    #jn_principal.close()
    jn_adicionar = [
        [sg.Text("Me ensine mais!")],
        [sg.Text("Insira a Pergunta:"), sg.InputText(key="pergunta")],
        [sg.Text("Insira a Resposta:"), sg.InputText(key="resposta")],
        [sg.Button("Adicionar o aprendizado!"), sg.Button("TREINAR NOVAMENTE!")]
    ]

    jn_adicionar = sg.Window("Treinado...", jn_adicionar)
    while True:
        evento, valores = jn_adicionar.read()
        if evento == sg.WIN_CLOSED:
            break
        if evento == "Adicionar o aprendizado!":
            pergunta = valores["pergunta"]
            resposta = valores["resposta"]
            if (pergunta and resposta) != '':
                lista.adicionar(pergunta)
                lista.adicionar(resposta)
                jn_adicionar["pergunta"].update('')
                jn_adicionar["resposta"].update('')
                lista.imprimir()
                # lista.dados.append(pergunta)
                # lista.dados.append(resposta)
                # print("Add")
        if evento == "TREINAR NOVAMENTE!":
            boot.treinar(chatbot)
    jn_adicionar.close()


def menu_testar(jn_principal):
    #jn_principal.close()
    jn_testar = [
        [sg.Text("Olá, eu sou o DaniChat! Sobre o que gostaria de saber?")],
        [sg.Text("Insira sua pergunta:"), sg.InputText(key="pergunta")],
        [sg.Text("Resposta"), sg.Text(key="resposta")],
        [sg.Button("OK")]
    ]

    jn_testar = sg.Window("DaniChat", jn_testar)
    while True:
        evento, valores = jn_testar.read()
        if evento == sg.WIN_CLOSED:
            break
        if evento == "OK":
            pergunta = valores["pergunta"]
            resposta = chatbot.get_response(pergunta)
            jn_testar["resposta"].update(resposta)

    jn_testar.close()


def menu_principal(menu_pr, chatbot):
    win_prinicipal = [
        [sg.Text(menu_pr)],
        [sg.Button("Treinar"), sg.Button("Apagar Banco")],
        [sg.Button("Adicionar Informações"), sg.Button("Testar Chat")],
        [sg.Button("Sair")],
    ]

    jn_principal = sg.Window(menu_pr, win_prinicipal)
    while True:
        evento, valores = jn_principal.read()
        if evento == "Sair":
            menu_sair(jn_principal)
            break
        elif evento == "Apagar Banco":
            menu_apagar(jn_principal, chatbot)
            #break
        elif evento == "Treinar":
            menu_treinar(jn_principal, chatbot)
            #break
        elif evento == "Adicionar Informações":
            menu_adicionar(jn_principal)
            #break
        else:
            menu_testar(jn_principal)
            break

    jn_principal.close()


# Inicio do programa
if __name__ == '__main__':
    from spacy.cli import download


    class ENGSM:
        ISO_639_1 = 'en_core_web_sm'


    try:
        chatbot = ChatBot("Dani chat", tagger_language=ENGSM)
        menu_principal('Menu Principal', chatbot)
    except:  # evita baixar o tempo todo a biblioteca encore apos fazer uso a primeira vez
        download("en_core_web_sm")
        chatbot = ChatBot("Dani chat", tagger_language=ENGSM)
        menu_principal('Menu Principal', chatbot)
