import telebot
import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("sobralface@gmail.com","facebook123@")
Iq.connect() #conectar
goal="EURUSD"
print("get candles")
# print(Iq.get_candles(goal,60,111,time.time()))

print("BALANCE Seu Teste:   ")
print(Iq.get_balance())


print("você vai verificar qual moeda você usa:   ")
print(Iq.get_currency())

CHAVE_API = "5865616008:AAElJsLWJcEALxuhNIZPi0u0jJeqOvJkOHg"

bot = telebot.TeleBot(CHAVE_API)
 
    

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza pra sua casa: Tempo de espera em 20min")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10min chega ai")

@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem salada não, clique aqui para iniciar: /iniciar")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /pizza Pizza
    /hamburguer Hamburguer
    /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamação@balbalba.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! Lira mandou um abraço de volta")
    
@bot.message_handler(commands=["balance"])
def balance(mensagem):
    myBalance = Iq.get_balance()
    bot.send_message(mensagem.chat.id, "sua banca com get_balance() é: "+myBalance)

@bot.message_handler(commands=["moeda"])
def moeda(mensagem):
    myMoeda = Iq.get_currency()
    bot.send_message(mensagem.chat.id, "a moeda que você usa com get_currency() é: "+myMoeda)

@bot.message_handler(commands=["banca"])
def banca(mensagem):
    myBalance = Iq.get_balance()
    bot.send_message(mensagem.chat.id, "sua banca com get_balance() é: "+myBalance)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Fazer um pedido
     /opcao2 Reclamar de um pedido
     /opcao3 Mandar um abraço pro Lira
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()
