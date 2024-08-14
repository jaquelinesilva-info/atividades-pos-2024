from xml.dom.minidom import parse

dom = parse("xml/imobiliaria.xml")

imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName("imovel")

print("Imóveis disponíveis:")
for i, imovel in enumerate(imoveis):
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue
    print(f"{i + 1} - {descricao}")

id_imovel = int(input("Digite o número do imóvel para mais informações: ")) - 1

if 0 <= id_imovel < len(imoveis):
    imovel = imoveis[id_imovel]
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue
    proprietario_nome = imovel.getElementsByTagName("nome")[0].firstChild.nodeValue
    emails = imovel.getElementsByTagName("email")
    telefones = imovel.getElementsByTagName("telefone")
    rua = imovel.getElementsByTagName("rua")[0].firstChild.nodeValue
    bairro = imovel.getElementsByTagName("bairro")[0].firstChild.nodeValue
    cidade = imovel.getElementsByTagName("cidade")[0].firstChild.nodeValue
    numero = imovel.getElementsByTagName("numero")
    tamanho = imovel.getElementsByTagName("tamanho")[0].firstChild.nodeValue
    numQuartos = imovel.getElementsByTagName("numQuartos")[0].firstChild.nodeValue
    numBanheiros = imovel.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue
    valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue
    
    print("----- Detalhes do Imóvel -----")
    print(f"Descrição: {descricao}")
    print(f"Proprietário: {proprietario_nome}")
    
    if emails:
        print("--- Emails ---")
        for email in emails:
            print(f"  {email.firstChild.nodeValue}")
    
    if telefones:
        print("--- Telefones ---")
        for telefone in telefones:
            print(f" {telefone.firstChild.nodeValue}")
    
    print("--- Endereço ---")
    print(f" Rua: {rua}")
    print(f" Bairro: {bairro}")
    print(f" Cidade: {cidade}")
    
    if numero:
        print(f" Número: {numero[0].firstChild.nodeValue}")
    
    print("---- Características ----")
    print(f" Tamanho: {tamanho}")
    print(f" Número de Quartos: {numQuartos}")
    print(f" Número de Banheiros: {numBanheiros}")
    print(f"Valor: {valor}")
    
else:
    print("Esse imóvel não existe.")
