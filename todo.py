def adicionar_tarefa(tarefas, descricao):
    """
    Adiciona uma nova tarefa à lista.
    Uma tarefa é um dicionário com 'descricao', 'concluida' e 'prioridade'.
    """
    if descricao:
        prioridade = input("Digite a prioridade da tarefa (Alta, Média ou Baixa): ").strip().capitalize()

        if prioridade not in ["Alta", "Média", "Media", "Baixa"]:
            print("⚠️ Prioridade inválida. Definido como 'Baixa'.")
            prioridade = "Baixa"

        if prioridade == "Media":
            prioridade = "Média"

        nova_tarefa = {
            "descricao": descricao,
            "concluida": False,
            "prioridade": prioridade
        }
        tarefas.append(nova_tarefa)
        print(f"\n✅ Tarefa '{descricao}' com prioridade '{prioridade}' adicionada com sucesso!")
    else:
        print("\n❌ A descrição da tarefa não pode ser vazia.")

def listar_tarefas(tarefas):
    """Lista todas as tarefas, mostrando o status, descrição e prioridade."""
    print("\n--- Sua Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa na lista. Adicione uma!")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "✅" if tarefa["concluida"] else "◻️"
            prioridade = tarefa.get("prioridade", "Baixa")
            print(f"{i + 1}. {status} {tarefa['descricao']} (Prioridade: {prioridade})")
    print("--------------------------")

def marcar_como_concluida(tarefas, indice):
    """Marca uma tarefa como concluída com base no seu índice na lista."""
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        if tarefas[indice_real]["concluida"]:
            print(f"\n⚠️ A tarefa '{tarefas[indice_real]['descricao']}' já estava marcada como concluída.")
        else:
            tarefas[indice_real]["concluida"] = True
            print(f"\n✅ Tarefa '{tarefas[indice_real]['descricao']}' marcada como concluída!")
    else:
        print("\n❌ Índice inválido. Por favor, escolha um número da lista.")

def remover_tarefa(tarefas, indice):
    """Remove uma tarefa da lista com base no seu índice."""
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        tarefa_removida = tarefas.pop(indice_real)
        print(f"\n🗑️ Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
    else:
        print("\n❌ Índice inválido. Por favor, escolha um número da lista.")

def editar_tarefa(tarefas):
    if not tarefas:
        print("\n⚠️ Nenhuma tarefa para editar.")
        return

    print("\n--- Editar Tarefa ---")
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa['descricao']} (Prioridade: {tarefa.get('prioridade', 'Baixa')})")

    try:
        indice = int(input("Digite o número da tarefa que deseja editar: "))
        if 1 <= indice <= len(tarefas):
            tarefa = tarefas[indice - 1]
            print(f"\nDescrição atual: {tarefa['descricao']}")
            nova_descricao = input("Digite a nova descrição (ou ENTER para cancelar): ").strip()
            if nova_descricao == "":
                print("Edição cancelada.")
            else:
                tarefa['descricao'] = nova_descricao
                print(f"\n✅ Descrição da tarefa atualizada com sucesso!")
        else:
            print("\n❌ Número inválido.")
    except ValueError:
        print("\n❌ Entrada inválida. Digite um número válido.")

    if not tarefas:
        print("\n⚠️ Nenhuma tarefa para editar.")
        return

    print("\n--- Editar Tarefa ---")
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa['descricao']} (Prioridade: {tarefa.get('prioridade', 'Baixa')})")

    try:
        indice = int(input("Digite o número da tarefa que deseja editar: "))
        if 1 <= indice <= len(tarefas):
            tarefa = tarefas[indice - 1]
            print(f"\nDescrição atual: {tarefa['descricao']}")
            nova_descricao = input("Digite a nova descrição (ou ENTER para cancelar): ").strip()
            if nova_descricao == "":
                print("Edição cancelada.")
            else:
                tarefa['descricao'] = nova_descricao
                print(f"\n✅ Descrição da tarefa atualizada com sucesso!")
        else:
            print("\n❌ Número inválido.")
    except ValueError:
        print("\n❌ Entrada inválida. Digite um número válido.")

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MENU ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Editar Tarefa")
    print("0. Sair")

def main():
    """Função principal que executa o loop do programa."""
    lista_de_tarefas = []

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(lista_de_tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(lista_de_tarefas)
        elif escolha == '3':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para marcar como concluída: "))
                marcar_como_concluida(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite um número.")
        elif escolha == '4':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para remover: "))
                remover_tarefa(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite um número.")
        elif escolha == '5':
            editar_tarefa(lista_de_tarefas)
        elif escolha == '0':
            print("\nObrigado por usar o Gerenciador de Tarefas. Até mais!")
            break
        else:
            print("\n❌ Opção inválida. Por favor, tente novamente.")

    """Função principal que executa o loop do programa."""
    lista_de_tarefas = []

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(lista_de_tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(lista_de_tarefas)
        elif escolha == '3':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para marcar como concluída: "))
                marcar_como_concluida(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite um número.")
        elif escolha == '4':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para remover: "))
                remover_tarefa(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite um número.")
        elif escolha == '5':
            print("\n🔧 Funcionalidade de edição de tarefa ainda em desenvolvimento.")
        elif escolha == '0':
            print("\nObrigado por usar o Gerenciador de Tarefas. Até mais!")
            break
        else:
            print("\n❌ Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
