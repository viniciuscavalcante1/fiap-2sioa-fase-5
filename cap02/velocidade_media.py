# Pedir a distância da viagem
distancia = float(input("Por favor, digite a distância percorrida: "))

# Pedir o tempo da viagem
tempo = float(input("Por favor, informe o tempo necessário para a viagem, em horas: "))

# Dividir a distância pelo tempo
velocidade_media = distancia / tempo

# Exibir o resultado para o usuário
print(f"A velocidade média foi de {velocidade_media:.2f}km/h.")
