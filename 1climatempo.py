#documentacao em: http://apiadvisor.climatempo.com.br/doc/index.html
import requests
import json #pip install json

iTOKEN = "Informe seu Token"
iCIDADE = "Informe o ID da cidade vinculada ao seu Token"

#Codigo do tipo da consulta
iTIPOCONSULTA = 1

#1=Tempo agora na cidade
if iTIPOCONSULTA == 1:
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + iCIDADE + "/current?token=" + iTOKEN
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    #print(iRETORNO_REQ)

    for iCHAVE in iRETORNO_REQ:
        print(iCHAVE + " : " + str(iRETORNO_REQ[iCHAVE]))

    for iCHAVE in iRETORNO_REQ['data']:
        print(iCHAVE + " : " + str(iRETORNO_REQ['data'][iCHAVE]) )

#2=Status do tempo no país
if iTIPOCONSULTA == 2:
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=" + iTOKEN
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    #print(iRETORNO_REQ)

    for iCHAVE in iRETORNO_REQ:
        print("Country: " + iCHAVE.get('country'))
        print("date: " + iCHAVE.get('date'))
        print("Text: " + iCHAVE.get('text') + "\n")

#3=Previsao para os proximas 15 dias
if iTIPOCONSULTA == 3:
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + iCIDADE + "/days/15?token=" + iTOKEN
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    #print(iRETORNO_REQ)
    print("\ncidade: " + str(iRETORNO_REQ.get('name')) + "-" + str(iRETORNO_REQ.get('state')))
    for iCHAVE in iRETORNO_REQ['data']:
        iDATA = iCHAVE.get('date_br')
        iCHUVA = iCHAVE['rain']['probability']
        iTEXTMORNING = iCHAVE['text_icon']['text']['phrase']['reduced']
        iTEMPERATURAMIN = iCHAVE['temperature']['min']
        iTEMPERATURAMAX = iCHAVE['temperature']['min']
        print("data: " + str(iDATA) + " chuva: " + str(iCHUVA) + "%" + " temp: min(" + str(iTEMPERATURAMIN) + ") max(" + str(iTEMPERATURAMAX) + ") resumo: " + str(iTEXTMORNING) + "\n")

#4=Previsao para os proximas 3 dias por regiao
if iTIPOCONSULTA == 4:
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/forecast/region/centro-oeste?token=" + iTOKEN
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    #print(iRETORNO_REQ)

    for iCHAVE in iRETORNO_REQ['data']:
        iDATA = iCHAVE.get('date_br')
        iTEXT = (iCHAVE.get('text'))
        if iTEXT == None:
            iTEXT = "sem dados para esta data"
        print("data: " + str(iDATA) + " texto: " + str(iTEXT) + "\n")

#5=Previsao para as proximas 72 horas
if iTIPOCONSULTA == 5:
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + iCIDADE + "/hours/72?token=" + iTOKEN
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    #print(iRETORNO_REQ)

    for iCHAVE in iRETORNO_REQ['data']:
        iDATA = iCHAVE.get('date_br')
        iTEMPERATURA = iCHAVE['temperature']['temperature']
        print("data:" + str(iDATA) + " " + str(iTEMPERATURA) + "º" + "\n")

#6=Pesquisa ID da Cidade
if iTIPOCONSULTA == 6:
    iCITY = input('Informe aqui o nome da cidade: ')
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + iCITY + "&token=" + iTOKEN
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    #print(iRETORNO_REQ)

    for iCHAVE in iRETORNO_REQ:
        iID = iCHAVE['id']
        iNAME = iCHAVE['name']
        iSTATE = iCHAVE['state']
        iCOUNTRY = iCHAVE['country']
        print("id:" + str(iID) + " - " + "stlocalesidate:" + str(iSTATE) + " - " + "country:" + str(iCOUNTRY) + " - " + "name:" + str(iNAME) + "\n") 

    iNEWCITY = input('Informe o ID da nova cidade ou 0(zero) para sair: ')
    if iNEWCITY != "0":
        iURL = "http://apiadvisor.climatempo.com.br/api-manager/user-token/"+ iTOKEN + "/locales" 
        payload="localeId[]=" + iNEWCITY
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        iRESPONSE = requests.request("PUT", iURL, headers=headers, data=payload)
        print(iRESPONSE.text)
    else:
        exit()

#7=Pesquisar o id da cidade vinculado ao seu Token
if iTIPOCONSULTA == 7:
    iURL = "http://apiadvisor.climatempo.com.br/api-manager/user-token/" + iTOKEN + "/locales" 
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    print("id: " + str(iRETORNO_REQ['locales']))

#8=Pesquisar a cidade por ID
if iTIPOCONSULTA == 8:
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/locale/city/" + iCIDADE + "?token=" + iTOKEN 
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    #print(iRETORNO_REQ)

    print("id: " + str(iRETORNO_REQ.get('id')))
    print("name: " + str(iRETORNO_REQ.get('name')))
    print("state: " + str(iRETORNO_REQ.get('state')))
    print("country: " + str(iRETORNO_REQ.get('country')) + "\n")

#9=Alterar o ID da cidade relacionada ao Token
if iTIPOCONSULTA == 9:
    iURL = "http://apiadvisor.climatempo.com.br/api-manager/user-token/"+ iTOKEN + "/locales" 
    payload="localeId[]=" + iCIDADE
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    iRESPONSE = requests.request("PUT", iURL, headers=headers, data=payload)
    print(iRESPONSE.text)