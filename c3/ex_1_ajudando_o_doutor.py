"""O doutor Henry Jones Junior estabeleceu uma regra com os seus alunos da
disciplina de Arqueologia: todos os que obtiverem nota maior do que 8,5
na sua prova semestral serão convidados para uma visita de campo na
América do Sul.

O nosso programa deve solicitar o e-mail e a nota do aluno, exibindo
a mensagem "ENVIANDO CONVITE" caso a nota do aluno satisfaça a condição
proposta."""

email_aluno = input("Informe o e-mail do aluno: ")
nota_aluno = float(input("Informe a nota do aluno: "))

if nota_aluno > 8.5:
    print(f"ENVIANDO CONVITE PARA {email_aluno.upper()}")