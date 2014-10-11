import httplib, urllib,urllib2,socket
from BeautifulSoup import BeautifulSoup
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib

timeout = 20
socket.setdefaulttimeout(timeout)

# ------------------------- get -----------------------

req = urllib2.Request('https://servicos.min-saude.pt/sico/faces/estatisticas.jsp')
req.add_header('Accept-Encoding',"gzip, deflate")
req.add_header('Accept-Language',"pt-pt,pt;q=0.8,en;q=0.5,en-us;q=0.3")
req.add_header('Content-type', 'application/x-www-form-urlencoded')
req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
req.add_header('User-agent', 'Mozilla/5.0')
req.add_header('Host','servicos.min-saude.pt')
req.add_header('Connection',"keep-alive")
req.add_header('Referer','https://servicos.min-saude.pt/sico/faces/estatisticas.jsp')

response = urllib2.urlopen(req)

data = response.read()
soup = BeautifulSoup(data)
numObitosCausaNaoNatural = soup.find('input', {'id':'numObitosCausaNaoNatural'}).get('value')

print numObitosCausaNaoNatural

print "fiz o primeiro get"

# ------------------------- post ----------------------

cookies = response.headers.get('Set-Cookie')

numObitosCausaNatural = soup.find('input', {'id':'numObitosCausaNatural'}).get('value')
numObitosCausaNaoNatural = soup.find('input', {'id':'numObitosCausaNaoNatural'}).get('value')
numObitosSujeitoInvestigacao = soup.find('input', {'id':'numObitosSujeitoInvestigacao'}).get('value')
numAcidenteTrabalho = soup.find('input', {'id':'numAcidenteTrabalho'}).get('value')
numAcidenteTransito = soup.find('input', {'id':'numAcidenteTransito'}).get('value')
numEventualSuicidio = soup.find('input', {'id':'numEventualSuicidio'}).get('value')
numEventualHomicidio = soup.find('input', {'id':'numEventualHomicidio'}).get('value')
numOutrosAcidentes = soup.find('input', {'id':'numOutrosAcidentes'}).get('value')
numIgnorado = soup.find('input', {'id':'numIgnorado'}).get('value')
id = soup.find('input', {'name':'oracle.adf.faces.STATE_TOKEN'}).get('value')

columnInfoMoth = soup.find('input', {'id':'columnInfoMoth'}).get('value')
columnInfoWeek = soup.find('input', {'id':'columnInfoWeek'}).get('value')
columnInfoTotal = soup.find('input', {'id':'columnInfoTotal'}).get('value')
obitosSemanaInfo = soup.find('input', {'id':'columnInfoTotal'}).get('value')
obitosDiarioInfo = soup.find('input', {'id':'obitosDiarioInfo'}).get('value')

values = {
'oracle.adf.faces.STATE_TOKEN':id,
'source':'_id0:anterior',
'oracle.adf.faces.FORM':'_id0',
'event':'update',
'selectedRow':'4',
'_id0:tabelaVersoes:selected':'4',
'_id0:tabelaVersoes:rangeStart':'0',
'numObitosCausaNatural':'',
'columnInfoMoth': columnInfoMoth.replace(" ", "+"),
'columnInfoWeek': columnInfoWeek.replace(" ", "+")+'-',
'columnInfoTotal': columnInfoTotal.replace(" ", "+")+'-',
'numObitosCausaNatural': numObitosCausaNatural.replace(" ", "+"),
'numObitosCausaNaoNatural': numObitosCausaNatural.replace(" ", "+"),
'numObitosSujeitoInvestigacao': numObitosSujeitoInvestigacao.replace(" ", "+"),
'numAcidenteTrabalho': numAcidenteTrabalho.replace(" ", "+"),
'numAcidenteTransito': numAcidenteTransito.replace(" ", "+"),
'numEventualSuicidio': numEventualSuicidio.replace(" ", "+"),
'numEventualHomicidio': numEventualHomicidio.replace(" ", "+"),
'numOutrosAcidentes': numOutrosAcidentes.replace(" ", "+"),
'numIgnorado': numIgnorado.replace(" ", "+"),
'obitosSemanaInfo': obitosSemanaInfo.replace(" ", "+"),
'obitosDiarioInfo':obitosDiarioInfo.replace(" ", "+")+'-'
}

data = urllib.urlencode(values)
req = urllib2.Request('https://servicos.min-saude.pt/sico/faces/estatisticas.jsp', data)
req.add_header('Cookie', cookies)
req.add_header('Accept-Encoding',"gzip, deflate")
req.add_header('Accept-Language',"pt-pt,pt;q=0.8,en;q=0.5,en-us;q=0.3")
req.add_header('Content-type', 'application/x-www-form-urlencoded')
req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
req.add_header('User-agent', 'Mozilla/5.0')
req.add_header('Host','servicos.min-saude.pt')
req.add_header('Connection',"keep-alive")
req.add_header('Referer','https://servicos.min-saude.pt/sico/faces/estatisticas.jsp')

class MyHTTPErrorProcessor(urllib2.HTTPErrorProcessor):

    def http_response(self, request, response):
        code, msg, hdrs = response.code, response.msg, response.info()

        # only add this line to stop 302 redirection.
        if code == 302:
        	return response

        if not (200 <= code < 300):
            response = self.parent.error(
                'http', request, response, code, msg, hdrs)
        return response

    https_response = http_response

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), MyHTTPErrorProcessor)

urllib2.install_opener(opener)

response = urllib2.urlopen(req)

data = response.read()
#cookies = response.headers.get('Set-Cookie')
print 'fiz um post depois'

# ------------------------- get -----------------------
req = urllib2.Request('https://servicos.min-saude.pt/sico/faces/estatisticas.jsp')
req.add_header('Cookie', cookies)
req.add_header('Accept-Encoding',"gzip, deflate")
req.add_header('Accept-Language',"pt-pt,pt;q=0.8,en;q=0.5,en-us;q=0.3")
req.add_header('Content-type', 'application/x-www-form-urlencoded')
req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
req.add_header('User-agent', 'Mozilla/5.0')
req.add_header('Host','servicos.min-saude.pt')
req.add_header('Connection',"keep-alive")
req.add_header('Referer','https://servicos.min-saude.pt/sico/faces/estatisticas.jsp')

response = urllib2.urlopen(req)

data = response.read()
soup = BeautifulSoup(data)
print "fiz o segundo get"

numObitosCausaNaoNatural = soup.find('input', {'id':'numObitosCausaNaoNatural'}).get('value')

print numObitosCausaNaoNatural