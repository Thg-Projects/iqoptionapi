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
    bot.send_message(mensagem.chat.id, "sua banca com get_balance() é: "+str(myBalance))

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /banca Fazer um pedido
     /balance Reclamar de um pedido
     /moeda Mandar um abraço pro Lira
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()
