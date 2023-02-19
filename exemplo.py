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