# Pesquisa de Opinião - TudoWeb
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0
# Teste com 10 entrevistados
for i in range(1, 11):
    print("Entrevistado:", i)
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("1: EXCELENTE")
    print("2: BOM")
    print("3: RUIM")
    opiniao = int(input("Digite a opinião (1, 2 ou 3): "))

    # Validação apenas da opinião com while e operador or
    while opiniao < 1 or opiniao > 3:
        print("Opção inválida! Escolha 1, 2 ou 3.")
        opiniao = int(input("Digite sua opinião novamente (1, 2 ou 3): "))

# Estrutura de decisão para contagem
    if opiniao == 1:
        qtd_excelente = qtd_excelente + 1
    elif opiniao == 2:
        qtd_bom = qtd_bom + 1
    elif opiniao == 3:
        qtd_ruim = qtd_ruim + 1

    print()
# Exibição dos resultados finais solicitados
print("Resultado da pesquisa:")
print("Quantidade de respostas EXCELENTE:", qtd_excelente)
print("Quantidade de respostas RUIM:", qtd_ruim) 