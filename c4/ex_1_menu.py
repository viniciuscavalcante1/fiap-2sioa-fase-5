"""Uma das frustrações mais comuns nos nossos primeiros programas é que eles acabam.
O cenário é quase sempre o mesmo: escrevemos um código, ficamos orgulhosos, testamos
e quando o funcionamento previsto termina, o programa se encerra.

Para solucionarmos esse problema, uma excelente solução é criar uma estrutura de menus,
na qual o usuário possa escolher se pretende continuar executando o programa ou se quer
finalizar o ciclo.

E quem pode nos ajudar nesse caso é o loop while!

Com esse loop, podemos estabelecer a lógica, enquanto o usuário não pressionar uma determinada
opção, o menu continua sendo exibido.

Para não perdermos tempo decidindo o que o menu conterá, vamos apenas exibir mensagens para cada
uma das opções, ok?"""

opcao = 0
while opcao != "4":
    print("Bem-vindo ao meu menu. O que o senhor deseja?")
    print("1 - Batata com carne")
    print("2 - Água com gás")
    print("3 - Coquinha gelada")
    print("4 - Sair")
    opcao = input("Informe sua opção: ")
    if opcao == "1":
        print("Uma batata com carne saindo direto do forno!")
    elif opcao == "2":
        print("Anotado! Uma aguinha com gás!")
    elif opcao == "3":
        print("Coquinha gelada pro chefe!")
print("Fechado campeão, já venho com tudo!")