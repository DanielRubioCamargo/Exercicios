nome = str(input("Insira seu nome completo : ")).strip().title()
idade = int(input("Insira sua idade : "))
email = str(input("Insira seu email : ")).strip()
while email.find("@") == -1 or email.find(".com") == -1:
    email = str(input("Email incorreto! Insira novamente : ")).strip()
print("Olá {}, fico feliz em recebê-lo por aqui!\nSua idade é : {}\nSeu email é : {}".format(nome,idade,email))