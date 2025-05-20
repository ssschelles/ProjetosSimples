# Organizador de Tarefas sem funções e sem try/except

tarefas = []
while True:
    # Listar ações possiveis
    print("\n=== Organizador de Tarefas ===")
    print('\n1- Adicionar nova tarefa \n2- Remover uma tarefa \n3- Listar tarefas \n4- Sair\n')
    acao = input('Escolha uma opção: ') 

    # Adicionar nova tarefa
    if acao=='1':
        tarefa = input('Adicione uma nova tarefa: ')
        tarefas.append(tarefa)
        print('Nova tarefa adicionada com sucesso!')
    
    #Remover tarefas 
    elif acao=='2':
        if not tarefas:
            print('Não existem tarefas na sua lista!')

        else:    
            print("\n=== Lista de Tarefas ===")
            for i in range(len(tarefas)):
                print(i+1,"- ", tarefas[i])
            
            indice_valido = False
            while not indice_valido:
                remover = input('Digite o número da tarefa que deseja remover: ')
                if remover.isdigit():
                    remover = int(remover)
                    if 1<= remover <= len(tarefas):
                        indice_valido=True
                        tarefas.pop(remover-1)
                        print('Tarefa removida com sucesso!')
                    else:
                        print('Número inválido! Por favor, insira um número dentro do intervalo.')
                else:
                    print("Entrada inválida! Por favor, insira um número.")
            

    # Listar tarefas
    elif acao=='3':
        if not tarefas:
            print('Não existem tarefas na sua lista!')
        else:
            print('Aqui estão suas tarefas:')
            for i in range(len(tarefas)):
                print(i+1,'- ',tarefas[i])
        
    # Sair 
    elif acao=='4':
        print("Saindo do Organizador de Tarefas. Até mais!")
        break

    else:
      print("Opção inválida! Por favor, escolha uma opção válida.")  
