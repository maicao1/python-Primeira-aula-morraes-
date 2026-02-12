print("--------")
print("\nseja bem vindo ao jogo de adivinhacao")
print("--------")

n_secreto = 68

entrada = input("digite um valor numerico: ")

print(f"você digitou o numero: {entrada}")

if(entrada == n_secreto):
    print(f"Parabens, você acertou o numero secreto")
else:
    if(entrada > n_secreto):
    print("o numero digitado foi maior que o numero secreto")
    
    if(entrada < n_secreto):
     print("o numero digitado foi menor que o numero secreto")

print("fim de jogo!")
