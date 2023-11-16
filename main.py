#Matheus Andrade e Gabriel Alves



def criarPilha():
        #retorna a pilha criada.
        pilha = []
        return pilha
    
    
def ver_vazia(pilha):
        #verifica se a pilha esta vazia e retorna um valor booleano.
        return len(pilha) == 0

def empilhar(pilha, item):
        #adicona um item na pilha e exibe mensagem de confirmação.
        pilha.append(item)


def desempilhar (pilha):
        #remove elemento do top da pilha
        if (ver_vazia(pilha)):
            return "Pilha vazia"
        
        return pilha.pop()
      




while True:

    print("1 - Abrir o arquivo")
    print("0 - Sair")

    op = int(input())



    if op == 0:

        break

    elif op == 1:

        pilha_refazer = criarPilha()
        pilha_desfazer = criarPilha()
        
        nomearq = input("Entre com o nome do arquivo e extensão:")

        with open(nomearq, 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())

        while True:

            anterior = "*"

            print("1 - Adicionar texto")
            print("2 - Substituir palavra no texto")
            print("3 - Remover palavra do texto")
            print("4 - Remover texto todo")
            print("5 - Desfazer")
            print("6 - Refazer")
            print("0 - Sair")


            op = int(input(">>"))

            if op == 0:
                break

            elif op == 1:

                print("Digite o texto a ser inserido:")
                texto = input(">>")

                with open(nomearq, 'a', encoding="utf-8") as arquivo:
                    arquivo.write(" " + texto)
                
                empilhar_elemento = "1" + " " + str(texto)

                empilhar(pilha_desfazer, empilhar_elemento)
                
                

            elif op == 2:

                palavra = input("Digite a palavra que deseja substituir:")

                sub = input("Digite a nova palavra:")
                with open(nomearq, 'r', encoding="utf-8") as arquivo:
                    texto = arquivo.read()

                texto = texto.replace(palavra, sub)

                with open(nomearq, 'w', encoding='utf-8') as arquivo:
                    arquivo.write(texto)

                empilhar_elemento = "2" + " " + str(palavra) + " " +  str(sub)
                              
                empilhar(pilha_desfazer, empilhar_elemento)
                
                    
            elif op == 3:

                palavra_removida = input("Digite a palavra que deseja remover:")

                with open(nomearq, 'r', encoding="utf-8") as arquivo:

                    texto = arquivo.read()

                texto = texto.split()

                for i in range(0,len(texto)-1):
                    
                    if texto[i] == palavra_removida:
                        if i > 0:
                            anterior = texto[i - 1]

                texto.remove(palavra_removida)

                texto2 = " ".join(texto)

                with open(nomearq, "w", encoding='utf-8') as arquivo:

                    arquivo.write(texto2)
                

                empilhar_elemento = "3" + " " + str(anterior) + " " + str(palavra_removida)

                empilhar(pilha_desfazer, empilhar_elemento)

            elif op == 4:

                with open(nomearq, 'r', encoding="utf-8") as arquivo:
                    texto = arquivo.read()

                empilhar_elemento = "4" + " "+ str(texto)
                empilhar(pilha_desfazer,empilhar_elemento)

                with open(nomearq, 'w', encoding='utf-8') as arquivo:
                    pass  # No need to write anything; the file is cleared



            elif op == 5: #Desfazer

                if (ver_vazia(pilha_desfazer)==True):
                    print ("Pilha desfazer vazia!")

                else:

                    comando = pilha_desfazer[-1]
                    comando = comando.split()
                    
                    if comando[0] == "1":

                        with open(nomearq, 'r', encoding="utf-8") as arquivo:
                            texto = arquivo.read()

                        texto = texto.replace(comando[1], "")

                        
                        with open(nomearq, 'w', encoding='utf-8') as arquivo:
                            arquivo.write(texto)
                       

                        elemento_empilhar = str(comando[0]) + " " + str(comando[1])

                        empilhar(pilha_refazer,elemento_empilhar)
                        desempilhar(pilha_desfazer)

                    elif comando[0] == "2":

                        with open(nomearq, 'r', encoding="utf-8") as arquivo:
                            texto = arquivo.read()

                        texto = texto.replace(comando[2], comando[1])

                        with open(nomearq, 'w', encoding='utf-8') as arquivo:
                            arquivo.write(texto)

                        elemento_empilhar = str(comando[0]) + " " + str(comando[2]) +  " " + comando[1]

                        empilhar(pilha_refazer, elemento_empilhar)

                        desempilhar(pilha_desfazer)

                    elif comando[0] == "3":

                        if comando[1] != "*":

                            with open(nomearq, 'r', encoding="utf-8") as arquivo:

                                texto = arquivo.read()

                            texto = texto.split()

                            for i in range(0,len(texto)-1):
                                
                                if texto[i] == comando[1]:
                                    texto.insert(i+1, comando[2])

                            texto = " ".join(texto)

                            with open(nomearq, 'w', encoding="utf-8") as arquivo:
                                arquivo.write(texto)


                        else:

                            with open(nomearq, 'r', encoding="utf-8") as arquivo:

                                texto = arquivo.read()

                            texto = texto.split()

                            texto.insert(0,comando[2])

                            texto = " ".join(texto)

                            with open(nomearq, 'w', encoding="utf-8") as arquivo:

                                arquivo.write(texto)

                        elemento_empilhar = str(comando[0]) + " " + str(comando[1]) + " " + str(comando[2])

                        empilhar(pilha_refazer,elemento_empilhar)
                        desempilhar(pilha_desfazer)

                    elif comando[0] == "4":
                        
                        for i in range(1,len(comando)):

                            with open(nomearq, 'a', encoding="utf-8") as arquivo:
                                arquivo.write(' ' + comando[i])
                        
                        empilhar(pilha_refazer, pilha_desfazer[-1])
                        desempilhar(pilha_desfazer)


            elif op == 6: #Refazer

                if ver_vazia(pilha_refazer) == True:
                    print ("Pilha Refazer Vazia!")

                else:

                    comando = pilha_refazer[-1]
                    comando = comando.split()

                    if comando[0] == "1":
                        
                        with open(nomearq, "a", encoding='utf-8') as arquivo:

                            arquivo.write(comando[1] + " ")

                        elemento_empilhar = str(comando[0]) + " " + str(comando[1])

                        empilhar(pilha_desfazer,elemento_empilhar)
                        desempilhar(pilha_refazer)

                    elif comando[0] == "2":


                        with open(nomearq, 'r', encoding="utf-8") as arquivo:
                            texto = arquivo.read()

                        texto = texto.replace(comando[2], comando[1])

                        with open(nomearq, 'w', encoding='utf-8') as arquivo:
                            arquivo.write(texto)

                        elemento_empilhar = str(comando[0]) + " " + str(comando[2]) +  " " + str(comando[1])

                        empilhar(pilha_desfazer, elemento_empilhar)

                        desempilhar(pilha_refazer)

                    elif comando[0] == "3":

                        
                        with open(nomearq, 'r', encoding="utf-8") as arquivo:
                            texto = arquivo.read()

                        texto = texto.split()

                        texto.remove(comando[2])

                        texto2 = " ".join(texto)

                        with open(nomearq, 'w', encoding="utf-8") as arquivo:
                            arquivo.write(texto2)

                        elemento_empilhar = str(comando[0]) + " " + str(comando[1]) + " " + str(comando[2])

                        empilhar(pilha_desfazer,elemento_empilhar)

                        desempilhar(pilha_refazer)

                    elif comando[0] == "4":
                        
                        with open(nomearq, 'r', encoding="utf-8") as arquivo:
                            texto = arquivo.read()

                        empilhar_elemento = "4" + " "+ str(texto)
                        empilhar(pilha_desfazer,empilhar_elemento)
                        desempilhar(pilha_refazer)

                        with open(nomearq, 'w', encoding='utf-8') as arquivo:
                            pass  # No need to write anything; the file is cleared