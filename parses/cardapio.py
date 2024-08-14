from xml.dom.minidom import parse
 
dom = parse ("xml/cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

id_prato = 0

for prato in pratos:
    id_prato += 1
    id_prato_attr = prato.getAttribute('id')
    nome_elemento = prato.getElementsByTagName('nome')[0]
    nome = nome_elemento.firstChild.nodeValue
    print(f"{id_prato} - {id_prato_attr}: {nome}")

id_pergunta = input("Digite o número do prato para mais informações: ")


for prato in pratos:
    id_prato_attr = prato.getAttribute('id')
    if id_pergunta == id_prato_attr:
        nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
        descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue
        ingredientes = prato.getElementsByTagName('ingrediente')
        preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
        moeda = prato.getElementsByTagName('preco')[0].getAttribute('moeda')
        calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
        tempo_preparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue


        print(f"ID: {id_prato}")
        print(f"Nome: {nome}")
        print(f"Descrição: {descricao}")
        for ingrediente in ingredientes:
            ingrediente_value = ingrediente.firstChild.nodeValue
            print(f" {ingrediente_value}")
        print(f"Preço: {preco} ({moeda})")
        print(f"Calorias: {calorias}")
        print(f"Tempo de Preparo: {tempo_preparo}")
        break

else:
    print("Esse prato nao existe.")




