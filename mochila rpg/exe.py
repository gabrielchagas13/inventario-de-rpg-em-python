#dicionario
inventario= {
    'mochila': ['violão', 'plantinha de dormir', 'foto da mamae pato'],
    'ouro': 150
}

#importações
import time
import os


#historinha
print ("Olá, bem vindo a DuckWorld ! Você é um pato, que vive tranquilamente na lagoa azul")
time.sleep(1.5)
print ("\nUm mundo no qual os patos vivem em amornia")
time.sleep(1.5)
print ("\nAté a chegada dos gansos, a comunidade patoviska esta desesperada")
time.sleep(1.5)
print ("\nVocê assume a liderança e tem a temida missão de enfrentar os gansos")
time.sleep(1.5)
print("\nMas antes disso, você tem que nadar pela lagoa para recolher recursos antes de ir a batalha")
time.sleep(1.5)
print (f"\nMestre Duck, o velho ancião da vila te da uma mochila, na qual seu invetario esta assim: antes de começar essa sua grande aventura \n")
time.sleep(1.5)

#printar inventario
for chave, valor in inventario.items():
        print ('%s: %s' %(chave, inventario))
time.sleep(3.5)
os.system('clear')



while True:
    if inventario["ouro"] >= 0:

        #codigo
        alimento = input("Olha só, quem é que está ali ! Na arvore mais antiga do lago, o seu amigo quati, ele esta vendendo alguns kiwis por 10 ouros, você quer comprar para não passar fome no caminho? \n")

        #alimento
        if alimento == "Sim":
            inventario['alimento'] = 'Kiwi'
            inventario["ouro"] -= 10
            print (f"\nQue legal, agora sua mochila tem comida.")
            time.sleep(3.5)
            os.system('clear')
        elif alimento == "Não":
            print ("Poxa, que pena. O kiwi do quati é o melhor da região")    
            time.sleep(3.5)
            os.system('clear')
        else:
            print ("Por favor, digite novamente")
            continue
        
        #pos compra ou nao
        print (f"Bravo ! Veja como ficou sua mochila agora")
        time.sleep(2.5)
        for chave, valor in inventario.items():
                print ('%s: %s' %(chave, inventario))
                time.sleep(3.5)
                os.system('clear')

        #armadura
        print("Agora vamos no equipar !")
        time.sleep(1.5)
        print("Porco Otavio esta vendendo armadura logo ao lado, qual armadura você gostaria de comprar?")
        time.sleep(1.5)
        print ("A de 1 - diamante, que é 50 ouros, 2 - prata 30 ouros e 3 - bronze 15 ouros")
        time.sleep(1.5)
        armadura = int(input("Qual você quer comprar? "))

        #codigo armadura
        if armadura == 1:
            inventario['armadura'] = 'Diamante'
            inventario["ouro"] -= 50
            print (f"\nTa podendo ein, de dima.")
            time.sleep(3.5)
            os.system('clear')
        elif armadura == 2:
            inventario['armadura'] = 'Prata'
            inventario["ouro"] -= 30
            print (f"\nFerro entao.")
            time.sleep(3.5)
            os.system('clear')
        elif armadura == 3:
            inventario['armadura'] = 'Bronze'
            inventario["ouro"] -= 50
            print (f"\nTa pobre né.")
            time.sleep(3.5)
            os.system('clear')
        else: 
            print("Por favor escreva de novo")
            continue

        #soldados codigo
        print("Agora vamos partir em direção ao combate !")
        time.sleep(1.5)
        print("Quati e Porco Otavio toparam te ajudar, o peixe-boi Love esta oferecendo ajuda tambem")
        time.sleep(1.5)
        print ("Porem so os 4 não vão conseguir combater o exercito de gansos")
        time.sleep(1.5)
        print("Alguns patinhos guerreiros se disponibilizam a ajudar vocês nessa temida missão")
        time.sleep(1.5)
        print (" seu inventario ficou assim para a missão:")
        for chave, valor in inventario.items():
                print ('%s: %s' %(chave, inventario))
                time.sleep(3.5)
    else:
        print ("Você não tem dinheiro para isso")