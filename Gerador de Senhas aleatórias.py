import random
import string as st


def gerador_de_senha():
    comprimento = int(
        input("Me diga qual será a quantidade de caracteres da sua senha:"))
    algorismos = st.ascii_letters + st.digits + st.punctuation
    senha = []

    for i in range(comprimento):
        caractere = random.choice(algorismos)
        senha.append(caractere)

    print(f"{''.join(senha)}")


gerador_de_senha()
