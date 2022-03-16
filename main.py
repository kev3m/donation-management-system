
#Texto Introdutório
# import time
# time.sleep(2)
# print("Lorem ipsum dolor sit amet+ consectetur adipiscing elit+ sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam+ quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
# time.sleep(2)

# nomeDoDoador = input("Digite o nome do doador: ")
# classificacaoDoDoador = int(input("Digite a classificação da pessoa doadora:\n[Para pessoa Física digite 0]\n[Para pessoa Jurídica digite 1]: "))

novaDoacao = "S"
print("Uma nova doação será registrada")
#Verificar Válidade do Doador
# while classificacaoDoDoador < 0 or classificacaoDoDoador > 1:
#     print("Tipo inválido de doador")
#     classificacaoDoDoador = int(input("Digite a classificação da pessoa doadora:\n[Para pessoa Física digite 0]\n[Para pessoa Jurídica digite 1]: "))


itemExtra = 0
cestaCriada = 0

#Contadores
quantiaAcucar = 0
quantiaArroz = 0 
quantiaCafe = 0
quantiaExtrato = 0
quantiaMacarrao = 0
quantiaBolacha = 0
quantiaOleo = 0
quantiaFtrigo = 0
quantiaFeijao = 0
quantiaSal = 0

quantiaItensDoadorFisico = 0
quantiaItensDoadorJuridico = 0


while novaDoacao == "S":

    nomeDoDoador = input("Digite o nome do doador: ")
    classificacaoDoDoador = int(input("Digite a classificação da pessoa doadora:\n[Para pessoa Física digite 0]\n[Para pessoa Jurídica digite 1]: "))

    #Verificar Válidade do Doador
    while classificacaoDoDoador < 0 or classificacaoDoDoador > 1:
        print("Tipo inválido de doador")
        classificacaoDoDoador = int(input("Digite a classificação da pessoa doadora:\n[Para pessoa Física digite 0]\n[Para pessoa Jurídica digite 1]: "))
    acucar = float(input("Quantos quilogramas(kg) de açúcar foram doados? ")) #1 kg
    arroz = float(input("Quantos quilogramas(kg) de arroz foram doados? ")) #4 kg
    cafe = float(input("Quantos quilogramas(kg) de café foram doados? ")) #2 kg
    extrato = int(input("Quantas unidades de extrato de tomate foram doadas? ")) #2 un
    macarrao = int(input("Quantas unidades de macarrão foram doadas? ")) #3 un
    bolacha = int(input("Quantos pacotes de bolacha foram doados? ")) #1 pct
    oleo = float(input("Quantos litros(L) de óleo foram doados? ")) #1 l
    farinhaDeTrigo = float(input("Quantos quilogramas(kg) de farinha de trigo foram doados? ")) #1 kg
    feijao = float(input("Quantos quilogramas(kg) de feijão foram doados? ")) #4 kg
    sal = float(input("Quantos quilogramas(kg) de sal foram doados? ")) #1 kg
    extra = int(input("Quantos itens(outros) extras foram doados? "))
    novaDoacao = input("Deseja adicionar uma nova doação? (S/N)")
    novaDoacao.upper()

    #Contador de Itens Para Pessoas Fisicas e Juridicas
    if classificacaoDoDoador == 0:
        quantiaItensDoadorFisico = quantiaItensDoadorFisico + acucar + arroz + cafe + extrato + macarrao + bolacha + oleo + farinhaDeTrigo + feijao + sal
    elif classificacaoDoDoador == 1:
        quantiaItensDoadorJuridico = quantiaItensDoadorJuridico + acucar + arroz + cafe + extrato + macarrao + bolacha + oleo + farinhaDeTrigo + feijao + sal

    #Adicionar ao Contador de Itens
    if acucar or arroz or cafe or extra or macarrao or bolacha or oleo or farinhaDeTrigo or feijao or sal or extra > 0:
        quantiaAcucar += acucar 
        quantiaArroz += arroz
        quantiaCafe += cafe
        quantiaExtrato += extrato
        quantiaMacarrao += macarrao
        quantiaBolacha += bolacha
        quantiaOleo += oleo
        quantiaFtrigo += farinhaDeTrigo
        quantiaFeijao += feijao
        quantiaSal += sal
        itemExtra += extra
    #Criar a cesta
    while quantiaAcucar >= 1 and quantiaArroz >= 4 and quantiaCafe >= 2 and quantiaExtrato >= 2 and quantiaMacarrao >= 3 and quantiaBolacha >= 1 and quantiaOleo >= 1 and quantiaFtrigo >= 1 and quantiaFeijao >= 4 and quantiaSal >= 1:
        cestaCriada += 1 
        quantiaAcucar = quantiaAcucar - 1
        quantiaArroz = quantiaArroz - 4
        quantiaCafe = quantiaCafe - 2
        quantiaExtrato = quantiaExtrato - 2
        quantiaMacarrao = quantiaMacarrao - 3
        quantiaBolacha = quantiaBolacha - 1
        quantiaOleo = quantiaOleo - 1
        quantiaFtrigo = quantiaFtrigo - 1
        quantiaFeijao = quantiaFeijao - 4
        quantiaSal = quantiaSal - 1

#Contador de Itens Para Pessoas Fisicas e Juridicas
# if classificacaoDoDoador == 0:
#     quantiaItensDoadorFisico = quantiaItensDoadorFisico + acucar + arroz + cafe + extrato + macarrao + bolacha + oleo + farinhaDeTrigo + feijao + sal
# elif classificacaoDoDoador == 1:
#     quantiaItensDoadorJuridico = quantiaItensDoadorJuridico + acucar + arroz + cafe + extrato + macarrao + bolacha + oleo + farinhaDeTrigo + feijao + sal

if novaDoacao == "N":
    print("Acabou")

print(f"A quantidade de itens doados por doadores físicos foi: {quantiaItensDoadorFisico}")
print(f"A quantidade de itens doados por doadores jurídicos foi: {quantiaItensDoadorJuridico}")

print(quantiaAcucar)
print(quantiaSal)
print(cestaCriada)



# if acucar == 1:
#     cestaCriada += 1
# print(cestaCriada)

# def addItemExtra(extra):
#     if extra > 0:
#         itemExtra += 1




