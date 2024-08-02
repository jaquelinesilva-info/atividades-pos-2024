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

id_pergunta = int(input("Digite o número do prato para mais informações: "))
prato = pratos[id_pergunta-1]
print("---\n")

id_prato_attr = prato.getAttribute('id')
