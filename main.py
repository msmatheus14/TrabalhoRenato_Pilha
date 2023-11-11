while True:

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
    
    def verificar_Top(pilha):

        if ver_vazia(pilha):

            return "Pilha vazia"
        
        return pilha[-1]    

    pilha_refazer = criarPilha()
    pilha_desfazer = criarPilha()
    

    print("1 - Abrir o arquivo")
    print("0 - Sair")

    op = int(input())



    if op == 0:

        break

    elif op == 1:

        nomearq = input("Entre com o nome do arquivo e extensão:")

        with open(nomearq, 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())

        while True:

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
                    arquivo.write(' ' + texto)
                
                comando = "1" + " " + str(texto)

                empilhar(pilha_desfazer, comando)
                
                

            elif op == 2:

                palavra = input("Digite a palavra que deseja substituir:")

                sub = input("Digite a nova palavra:")
                with open(nomearq, 'r', encoding="utf-8") as arquivo:
                    texto = arquivo.read()

                texto = texto.replace(palavra, sub)

                with open(nomearq, 'w', encoding='utf-8') as arquivo:
                    arquivo.write(texto)

                comando = "2" + " " + str(palavra) + " " +  str(sub)
                              
                empilhar(pilha_desfazer, comando)
                
                    
            elif op == 3:

                palavra = input("Digite a palavra que deseja remover:")
                with open(nomearq, 'r', encoding="utf-8") as arquivo:
                    texto = arquivo.read()

                texto = texto.replace(palavra, "")

                with open(nomearq, "w", encoding='utf-8') as arquivo:
                    arquivo.write(texto)

                comando = "3" + " " + str(palavra)

            elif op == 4:

                with open(nomearq, 'w', encoding='utf-8') as arquivo:
                    pass  # No need to write anything; the file is cleared

            elif op == 5: #Desfazer

                comando = verificar_Top(pilha_desfazer).split()
                print (comando)

                if comando[0] == "1":
                    print ("oi")

                    with open(nomearq, 'r', encoding="utf-8") as arquivo:

                        texto = arquivo.read()

                        texto = texto.replace(comando[1], "")

                    with open(nomearq, "w", encoding='utf-8') as arquivo:

                        arquivo.write(texto)

                    comando[0] = 3

                    elemento_empilhar = str(comando[0]) ," " , str(comando[1])

                    empilhar(pilha_refazer,elemento_empilhar)
                    desempilhar(pilha_desfazer)

                elif comando[0] == "2":

                    comando = verificar_Top(pilha_desfazer).split()

                    with open(nomearq, 'r', encoding="utf-8") as arquivo:
                        texto = arquivo.read()

                    texto = texto.replace(comando[2], comando[1])

                    with open(nomearq, 'w', encoding='utf-8') as arquivo:
                        arquivo.write(texto)

                    elemento_empilhar = str(comando[0]," ",comando[2], " ",comando[1])

                    empilhar(pilha_refazer, elemento_empilhar)

                    desempilhar(pilha_desfazer)

                elif comando[0] == "3":

                    comando = verificar_Top(pilha_desfazer).split()

                    with open(nomearq, 'a', encoding="utf-8") as arquivo:
                        arquivo.write(' ' + comando[1])

                    comando[0] = 1
                    elemento_empilhar = str(comando[0]," ",comando[1])

                    empilhar(pilha_refazer,elemento_empilhar)
                    desempilhar(pilha_desfazer)

            elif op == 6: #Refazer

                comando = verificar_Top(pilha_refazer).split()
                print (comando)

                if comando[0] == "1":

                    comando = verificar_Top(pilha_refazer).split()

                    with open(nomearq, 'r', encoding="utf-8") as arquivo:

                        texto = arquivo.read()

                        texto = texto.replace(comando[1], "")

                    with open(nomearq, "w", encoding='utf-8') as arquivo:

                        arquivo.write(texto)

                    comando[0] = 3

                    elemento_empilhar = comando[0]," ",comando[1]

                    empilhar(pilha_desfazer,elemento_empilhar)
                    desempilhar(pilha_refazer)

                elif comando[0] == "2":

                    comando = verificar_Top(pilha_refazer).split()

                    with open(nomearq, 'r', encoding="utf-8") as arquivo:
                        texto = arquivo.read()

                    texto = texto.replace(comando[2], comando[1])

                    with open(nomearq, 'w', encoding='utf-8') as arquivo:
                        arquivo.write(texto)

                    elemento_empilhar = str(comando[0]," ",comando[2], " ",comando[1])

                    empilhar(pilha_desfazer, elemento_empilhar)

                    desempilhar(pilha_refazer)

                elif comando[0] == "3":

                    comando = verificar_Top(pilha_refazer).split()

                    with open(nomearq, 'a', encoding="utf-8") as arquivo:
                        arquivo.write(' ' + comando[1])

                    comando[0] = 1
                    elemento_empilhar = str(comando[0]," ",comando[1])

                    empilhar(pilha_desfazer,elemento_empilhar)
                    desempilhar(pilha_refazer)