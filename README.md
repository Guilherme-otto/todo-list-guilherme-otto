# Projeto: Gerenciador de Tarefas v2.0

## 1. Visão Geral

Este é um projeto de um Gerenciador de Tarefas via terminal, desenvolvido em Python. A base do projeto oferece funcionalidades para adicionar, listar, concluir e remover tarefas. O objetivo deste trabalho é estender a funcionalidade do sistema e demonstrar um fluxo de trabalho de desenvolvimento profissional utilizando Git e GitHub.

## 2. Configuração Inicial

1.  **Fork:** Realize um fork deste repositório para a sua conta pessoal no GitHub.
2.  **Clone:** Clone o repositório que você criou (o seu fork) para o seu ambiente de desenvolvimento local.
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
    ```

## 3. Especificações da Tarefa

Você deve implementar as **duas** novas funcionalidades descritas abaixo.

### Funcionalidade 1: Prioridade de Tarefas

* **Estrutura de Dados:** A estrutura de dados de cada tarefa deve ser alterada para incluir um campo `prioridade`.
* **Adicionar Tarefa:** A função de adição deve ser modificada para solicitar ao usuário um nível de prioridade (`Alta`, `Média`, `Baixa`). Uma entrada inválida deve resultar na prioridade padrão `Baixa`.
* **Listar Tarefas:** A função de listagem deve ser atualizada para exibir a prioridade de cada tarefa.

### Funcionalidade 2: Edição de Descrição da Tarefa

* **Menu:** Uma nova opção para "Editar Tarefa" deve ser adicionada ao menu principal.
* **Implementação:** Deve ser criada uma função que permita ao usuário:
    1.  Selecionar uma tarefa existente pelo seu índice.
    2.  Visualizar a descrição atual.
    3.  Inserir uma nova descrição para substituí-la.
* **Feedback:** O sistema deve informar ao usuário se a operação foi bem-sucedida.

## 4. Requisitos de Entrega e Fluxo de Trabalho

A avaliação levará em conta a organização do seu repositório e o uso correto das ferramentas.

* **README.md:** Este arquivo deve ser atualizado com a seção "Minhas Contribuições" devidamente preenchida.
* **`.gitignore`:** O repositório precisa conter um arquivo `.gitignore` configurado adequadamente para projetos Python, ignorando arquivos e pastas como `__pycache__` e `venv/`.
* **Fluxo com Branches:** Cada uma das duas funcionalidades deve ser desenvolvida em uma *feature branch* separada (ex: `feature/task-priority` e `feature/edit-task-description`). Após a finalização, cada branch deve ser mesclada (`merge`) de volta à branch `main`.
* **Histórico de Commits:** É exigido um histórico com um mínimo de **8 a 10 commits atômicos**. As mensagens de commit devem ser claras e refletir o trabalho realizado em cada etapa.

## 5. Critérios de Avaliação

* **README:** Clareza e detalhamento da seção "Minhas Contribuições".
* **Git:** Qualidade das mensagens de commit e demonstração do fluxo de trabalho com branches e merges.
* **Funcionalidade:** Implementação correta e funcional das modificações solicitadas.
* **Código:** Legibilidade, organização e qualidade geral do código implementado.

---

## (Template para o Aluno)

## Minhas Contribuições

* **Nome:** `[Seu Nome Completo]`
* **GitHub:** `[Link para seu perfil no GitHub]`

### Modificação 1: Prioridade de Tarefas

**Lógica Implementada:**
A função adicionar_tarefa foi modificada para permitir ao usuário definir a prioridade da tarefa no momento da criação.

O usuário pode escolher entre as opções: "Alta", "Média" ou "Baixa".

Caso a prioridade digitada não seja reconhecida, o sistema atribui automaticamente a prioridade "Baixa" e informa o usuário.

O campo prioridade foi adicionado ao dicionário de cada tarefa.

A função listar_tarefas foi atualizada para exibir a prioridade ao lado da descrição de cada tarefa.

**Como Testar:**
Execute o programa.

Escolha a opção 1 - Adicionar Tarefa.

Digite uma descrição e, em seguida, a prioridade desejada (Alta, Média ou Baixa).

Em seguida, escolha a opção 2 - Listar Tarefas para visualizar se a prioridade foi registrada corretamente.

Teste também inserir uma prioridade inválida (como "Urgente") para verificar se o valor padrão "Baixa" é atribuído.

### Modificação 2: Editar Descrição da Tarefa

**Lógica Implementada:**
Foi criada a função editar_tarefa, que lista todas as tarefas e permite ao usuário selecionar uma delas para editar a descrição.

A função exibe a descrição atual e solicita uma nova descrição. Se o campo for deixado em branco, a edição é cancelada.

Uma mensagem de confirmação é exibida ao final da edição.

**Como Testar:**
Execute o programa.

Adicione pelo menos uma tarefa.

Escolha a opção 5 - Editar Tarefa.

Selecione o número correspondente à tarefa que deseja editar.

Digite a nova descrição e confirme.

Liste as tarefas novamente com a opção 2 para verificar se a descrição foi atualizada corretamente.

Repita e pressione apenas ENTER para confirmar o cancelamento da edição.