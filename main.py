'''*******************************************************************************
Autor: Keven Coutinho Crisostomo
Componente Curricular: MI - Algoritmos I
Concluido em: 09/04/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************'''

novaDoacao = "S"
print("Uma nova doação será registrada")

cestaCriada = 0
itemExtra = 0

#Contadores Variáveis
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
quantiaExtra = 0

#Contadores Totais
totalAcucar = 0
totalArroz = 0 
totalCafe = 0
totalExtrato = 0
totalMacarrao = 0
totalBolacha = 0
totalOleo = 0
totalFtrigo = 0
totalFeijao = 0
totalSal = 0

quantiaItensDoadorFisico = 0
quantiaItensDoadorJuridico = 0

while novaDoacao == "S":
    
    nomeDoDoador = input("Digite o nome do doador: ")
    classificacaoDoDoador = int(input('''Digite a classificação da pessoa doadora:\n
    [Para pessoa Física digite 0]\n
    [Para pessoa Jurídica digite 1]: '''))

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

    novaDoacao = input("Deseja adicionar uma nova doação? (S/N)").upper()[0]
    
    #Contador de Itens Para Pessoas Fisicas e Juridicas
    if classificacaoDoDoador == 0:
        quantiaItensDoadorFisico = quantiaItensDoadorFisico + acucar + arroz + cafe + extrato + macarrao + bolacha + oleo + farinhaDeTrigo + feijao + sal + extra
    elif classificacaoDoDoador == 1:
        quantiaItensDoadorJuridico = quantiaItensDoadorJuridico + acucar + arroz + cafe + extrato + macarrao + bolacha + oleo + farinhaDeTrigo + feijao + sal + extra

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
        quantiaExtra += extra
        itemExtra += extra
        totalAcucar += acucar
        totalArroz += arroz 
        totalCafe += cafe
        totalExtrato += extrato
        totalMacarrao += macarrao
        totalBolacha += bolacha
        totalOleo += oleo
        totalFtrigo += farinhaDeTrigo
        totalFeijao += feijao
        totalSal += sal
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
        quantiaExtra = quantiaExtra - 1

if novaDoacao == "N":
    print("O programa foi finalizado.")
    print("O relatório será apresentado.")

print('---------------------------------------------------------------------')
print(f"Foram recebidos {totalAcucar:.1f} kg de açucar")
print(f"Foram recebidos {totalArroz:.1f} kg de arroz")
print(f"Foram recebidos {totalCafe:.1f} kg de café")
print(f"Foram recebidos {totalExtrato:.1f} un de extrato")
print(f"Foram recebidos {totalMacarrao:.1f} un de macarrão")
print(f"Foram recebidos {totalBolacha:.1f} pct de bolacha")
print(f"Foram recebidos {totalOleo:.1f} L de óleo")
print(f"Foram recebidos {totalFtrigo:.1f} kg de farinha de trigo")
print(f"Foram recebidos {totalFeijao:.1f} kg de feijão")
print(f"Foram recebidos {totalSal:.1f} kg de sal")
print(f"Foram recebidos {itemExtra:.1f} itens extras")
print('---------------------------------------------------------------------')
print(f"Foram recebidas {totalAcucar + totalArroz + totalCafe + totalExtrato + totalMacarrao + totalBolacha + totalOleo + totalFtrigo + totalFeijao + totalSal + itemExtra} doações")
print(f"A quantidade de itens doados por doadores físicos foi: {quantiaItensDoadorFisico}")
print(f"A quantidade de itens doados por doadores jurídicos foi: {quantiaItensDoadorJuridico}")
print('---------------------------------------------------------------------')
print(f"{cestaCriada} cestas foram formadas")
print('---------------------------------------------------------------------')
if itemExtra > cestaCriada:
    print(f"{cestaCriada} cestas receberam itens extras, ou seja, todas.")
elif itemExtra < cestaCriada:
    print(f"{itemExtra} cestas receberam itens extras")
    print(f"{cestaCriada - itemExtra } cestas não receberam itens extras")

print('---------------------------------------------------------------------')
if quantiaAcucar > 0:
    print(f"Sobraram {quantiaAcucar:.1f} kg de açucar")
if quantiaArroz > 0:
    print(f"Sobraram {quantiaArroz:.1f} kg de arroz")
if quantiaCafe > 0:
    print(f"Sobraram {quantiaCafe:.1f} kg de café")
if quantiaExtrato > 0:
    print(f"Sobraram {quantiaExtrato} un de extrato")
if quantiaMacarrao > 0:
    print(f"Sobraram {quantiaMacarrao} un de macarrão")
if quantiaBolacha > 0:
    print(f"Sobraram {quantiaBolacha} pct de bolacha")
if quantiaOleo > 0:
    print(f"Sobraram {quantiaOleo:.1f} L de óleo")
if quantiaFtrigo > 0:
    print(f"Sobraram {quantiaFtrigo:.1f} kg de farinha de trigo")
if quantiaFeijao > 0:
    print(f"Sobraram {quantiaFeijao:.1f} kg de feijão")
if quantiaSal > 0:
    print(f"Sobraram {quantiaSal:.1f} kg de sal")
if quantiaExtra > 0:
    print(f"Sobraram {quantiaExtra} itens extras")
print('--------------------------------------------------------------------')

    


