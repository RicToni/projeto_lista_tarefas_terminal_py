from datetime import datetime, date
import os

os.system('cls')
tarefas = []
TAREFA_CONCLUIDA = "✅"
TAREFA_NAO_CONCLUIDA = "❌"

def criar_tarefa():
    while True:
        os.system('cls')
        nome = input('Insira o nome da tarefa -> ')
        if not nome.strip():
            os.system('cls')
            print('O nome da tarefa não pode estar vazio!!')
            input('Pressione <ENTER> e tente novamente.')
            continue
        os.system('cls')
        while True:
            data_str = input('Insira a data da tarefa (DD/MM/AAAA) -> ')
            try:
                data = datetime.strptime(data_str, '%d/%m/%Y').date()
                break
            except ValueError:
                os.system('cls')
                print('Data inválida, insira no formato (DD/MM/AAAA)')
                input('Pressione <ENTER> e tene novamente.')
                continue
        while True:
            os.system('cls')
            horario_str = input('Insira o horário da tarefa -> ')
            try:
                horario = datetime.strptime(horario_str, '%H:%M').time()
                break
            except ValueError:
                os.system('cls')
                print('Horário inválido, insira no formato HH:MM')
                input('Pressione <ENTER> e tene novamente.')
                continue
        data_hora = datetime.combine(data, horario)
        while True:
            os.system('cls')
            descr = input('Descreva brevemente a tarefa -> ')
            if not descr.strip():
                os.system('cls')
                print('A descrição da tarefa não pode estar vazia!!')
                input('Pressione <ENTER> e tente novamente.')
                continue
            else:
                break
        while True:
            os.system('cls')
            prior_str = input('Defina a prioridade: [3]ALTA - [2]MEDIA - [1]BAIXA -> ')
            if prior_str not in ('1','2','3'):
                os.system('cls')
                print('Classificação inválida, escolha entre as seguintes opções: [3]ALTA - [2]MEDIA - [1]BAIXA ')
                input('Pressione <ENTER> e tente novamente.')
                continue
            else:
                break
        prior = int(prior_str)

        tarefa = dict(nome = nome, data = data_hora, descr = descr, priori = prior, sit = False)
        tarefas.append(tarefa)

        os.system('cls')
        print(f'Tarefa "{tarefa["nome"]}" criada com sucesso!!')
        input('Pressione <ENTER> pra voltar ao menu eanteriror!!')
        break

        
 
    
    # nome = dict(nome = nome, data = data, desc = desc, priori = priori)
    # pass

def listar_tarefas():
    os.system('cls')
    index = 1
    for tarefa in tarefas:
        status = TAREFA_CONCLUIDA if tarefa['sit'] else TAREFA_NAO_CONCLUIDA
        print(f'''
Tarefa {index}: {status}
--------------------------------
Nome: {tarefa["nome"]}
Data/Hora: {tarefa["data"]}
Descrição: {tarefa["descr"]}
Prioridade: {tarefa["priori"]}
''')
        index += 1
    if len(tarefas) == 0:
        print('Você aiinda não adicionou nenhuma tarefa a lista!')
    input('\nPRESSIONE <ENTER> PARA VOLTAR AO MENU ANTERIOR!')

def remover_tarefa():
    os.system('cls')
    listar_tarefas()
    while True:
        try:
            opcao = int(input('Escolha qual tarefa deseja excluir(número da tarefa)? -> '))
            tarefa_excluida = tarefas.pop(opcao - 1)
            os.system('cls')
            print(F'A tarefa {opcao}:{tarefa_excluida["nome"]} foi removida!!')
            break
        except IndexError:
            os.system('cls')
            input('Índice inválido, digite <ENTER> e tente novamente!!!')
        except ValueError:
            os.system('cls')
            input('Entrada inválida! Digite apenas números. pressione <ENTER> e tente novamente!!')  

def editar_tarefa():
    while True:
        os.system('cls')
        if not tarefas:
            print("Nenhuma tarefa cadastrada para editar.")
            input("Pressione <ENTER> para voltar ao menu.")
            break

        listar_tarefas()
        try:
            escolha_tarefa = input('Escolha a tarefa a ser editada!!')
            escolha_int = int(escolha_tarefa)

            if escolha_int < 1 or escolha_int > len(tarefas):
               os.system('cls')
               input('Opção inválida, escolha o número da tarefa entre as listadas.\nPressione <ENTER> e tente novamente!')
               continue

            tarefa = tarefas[escolha_int - 1]
            os.system('cls')
            print(f'Editando a tarefa: {tarefa}')   ## Formatar a saída para o usuário. 

            os.system('cls')
            novo_nome = input(f'Nome: {tarefa["nome"]} - Insira o novo nome ou pressione <ENTER> para manter o atual -> ') 
            if novo_nome.strip():
                tarefa["nome"] = novo_nome
            
            os.system('cls')
            nova_data = input(f"Data atual: {tarefa['data'].strftime('%d/%m/%Y')}) - Insira nova data ou pressiona <ENTER>para manter a atual -> ").strip()
            if nova_data:
                try:
                    tarefa['data'] = datetime.strptime(nova_data, '%d/%m/%Y').date()
                except ValueError:
                    print("Data inválida, mantendo a anterior.")
            
            os.system('cls')
            novo_horario = input(f"Horário atual: {tarefa['data'].strftime('%H:%M')} - Insira o novo horário ou pressione <ENTER> para manter o atual -> ")
            if novo_horario:
                try:
                    tarefa['data'] = datetime.combine(
                        tarefa['data'], datetime.strptime(novo_horario, '%H:%M').time()
                    )
                except ValueError:
                    print("Horário inválido, mantendo o anterior.")
            
            os.system('cls')
            nova_descr = input(f"Descrição atual: {tarefa['descr']} - Digite uma nova descrição ou pressione <ENTER> para manter a atual  -> ").strip()
            if nova_descr:
                tarefa['descr'] = nova_descr   
            
            os.system('cls')
            nova_prioridade = input(f"Nova prioridade (atual: {tarefa['priori']}) [1, 2, 3] -> ").strip()
            if nova_prioridade in ('1', '2', '3'):
                tarefa['priori'] = int(nova_prioridade)

            os.system('cls')
            print("Tarefa editada com sucesso!")
            input("Pressione <ENTER> para voltar ao menu.")
            break                  
                
        except IndexError:
            print("Número inválido. Escolha um número correspondente a uma tarefa existente.")
            input("Pressione <ENTER> para tentar novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            input("Pressione <ENTER> para tentar novamente.")

def concluir_tarefa():
    while True:
        os.system('cls')
        if not tarefas:
           print("Nenhuma tarefa cadastrada para editar.")
           input("Pressione <ENTER> para voltar ao menu.")
           break
       
        listar_tarefas()
        escolha_tarefa = input('Escolha a tarefa a ser concluida!!').strip()
    
        try:
            escolha_int = int(escolha_tarefa)
            if escolha_int < 1 or escolha_int > len(tarefas):
                os.system('cls')
                input('Opção inválida, escolha o número da tarefa entre as listadas.\nPressione <ENTER> e tente novamente!')
                continue
            tarefa = tarefas[escolha_int - 1]
            if tarefa['sit'] == True:
                input('A tarefa escolhida já está marcada como cocnluida! Pressiona <ENTER> para retornar ao menu!')
                break
            else:
                tarefa['sit'] = True
                print(f'A tarefa {tarefa["nome"]} foi marcada como concluída!')
                input('Pressione <ENTER> para voltar ao menu anterior!')
                break

        except IndexError:
            print("Número inválido. Escolha um número correspondente a uma tarefa existente.")
            input("Pressione <ENTER> para tentar novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            input("Pressione <ENTER> para tentar novamente.")

def exibir_menu():
    os.system('cls')
    print('''
===== GERENCIADOR DE TAREFAS =====
1) - Adicionar tarefa.
2) - Listar tarefas.
3) - Remover tarefa.
4) - Editar tarefa.
5) - Finalizar tarefa .                  
----------------------------------- ''')
    opcao = input('->')
    if opcao not in ('1','2','3','4','5'):
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
        
    elif opcao == '1':
        criar_tarefa()
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        remover_tarefa()
    elif opcao == '4':
        editar_tarefa()
    elif opcao == '5':
        concluir_tarefa()
    