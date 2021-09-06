nome = str(input("Nome completo : "))
primeiroNome = nome.split()[0]
ultimoNome = nome.split()[len(nome.split())-1]
print("Primeiro nome : ",primeiroNome,"\nUltimo nome : ",ultimoNome)