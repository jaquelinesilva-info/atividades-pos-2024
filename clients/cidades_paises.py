import requests
from xml.dom.minidom import parseString


def get_capital_city(country_code):
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
    x = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://www.oorsprong.org/websamples.countryinfo/CapitalCity"
    }
    
    exibir = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{country_code}</sCountryISOCode>
        </CapitalCity>
      </soap:Body>
    </soap:Envelope>"""
    
    response = requests.post(url, data=exibir, headers=x)
    
    print( response.content.decode())
    
    dom = parseString(response.content)
    
    # verifica se  existe
    capitaisEncontradas = dom.getElementsByTagName("m:CapitalCityResult")
    if capitaisEncontradas:
        capital = capitaisEncontradas[0].childNodes[0].data
        return capital
    else:
        return "'CapitalCityResult' não  foi encontrado"


nz_capital = get_capital_city("NZ")
print(f"A capital da Nova Zelândia é {nz_capital}")
