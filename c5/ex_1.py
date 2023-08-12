# estrutura de menu
opcao = -1

notas = []
while opcao != 4:
    print("1 - Cadastrar nota")
    print("2 - Exibir notas")
    print("3 - Calcular média")
    print("4 - Sair")
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        notas.append(float(input("Por favor, informe a nota do aluno: ")))
    elif opcao == 2:
        print("As notas da turma são: ")
        for nota in notas:
            print(nota)
    elif opcao == 3:
        # soma = 0
        # for nota in notas:
        #    soma = soma + nota
        media = sum(notas) / len(notas)
        print(media)
    elif opcao == 4:
        print("Saindo!")
    else:
        print("Opção inválida!")