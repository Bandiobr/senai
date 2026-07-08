print("RADAR de TRÂNSITO")
velocidade = int(input("Informe a velocidade do carro"))

limite = 80

if velocidade > limite:
    print("Você ta correndo muito")
elif velocidade == limite:
    print ("Você esta na velocidade certa")

