game = True
while game==True:
    import random
    valor = random.randint(10,50)
    nome1 = input("nome: ")
    nome2 = input("nome: ")
    
    if valor % 2 != 0 and valor >= 15 or valor % 2 != 0 and valor < 15:
        print("Não foi dessa vez!")
    elif valor % 2 == 0 and valor < 15:
        print("Deu match!!Um beijo no rosto!")
    else:
        print("Um abraco, apenas amizade!")