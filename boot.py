from chatterbot.trainers import ListTrainer

import lista

def treinar(chatbot):

    treiner = ListTrainer(chatbot)
    treiner.train(lista.dados)


