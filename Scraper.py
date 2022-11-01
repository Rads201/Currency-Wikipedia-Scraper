import requests
from bs4 import BeautifulSoup
import zmq
import time


def wiki_scrape(curr_code):

    url = "https://en.wikipedia.org/wiki/"

    if curr_code == "PHP":
        url += "Philippine_peso"
    elif curr_code == "HRK":
        url += "Croatian_kuna"
    elif curr_code == "PLN":
        url += "Polish złoty"
    elif curr_code == "ISK":
        url += "Icelandic_króna"
    elif curr_code == "JPY":
        url += "Japanese_yen"
    elif curr_code == "IDR":
        url += "Indonesian_rupiah"
    elif curr_code == "EUR":
        url += "Euro"
    elif curr_code == "CZK":
        url += "Czech_koruna"
    elif curr_code == "THB":
        url += "Thai_baht"
    elif curr_code == "SGD":
        url += "Singapore_dollar"
    elif curr_code == "LTL":
        url += "Lithuanian_litas"
    elif curr_code == "EEK":
        url += "Estonian_kroon"
    elif curr_code == "NOK":
        url += "Norwegian_krone"
    elif curr_code == "CHF":
        url += "Swiss_franc"
    elif curr_code == "USD":
        url += "United_States_dollar"
    elif curr_code == "CNY":
        url += "Renminbi"
    elif curr_code == "MTL":
        url += "Maltese_lira"
    elif curr_code == "TRY":
        url += "Turkish_lira"
    elif curr_code == "RON":
        url += "Romanian_leu"
    elif curr_code == "MYR":
        url += "Malaysian_ringgit"
    elif curr_code == "CAD":
        url += "Canadian_dollar"
    elif curr_code == "BGN":
        url += "Bulgarian_lev"
    elif curr_code == "BRL":
        url += "Brazilian_real"
    elif curr_code == "CYP":
        url += "Cypriot_pound"
    elif curr_code == "AUD":
        url += "Australian_dollar"
    elif curr_code == "KRW":
        url += "South_Korean_won"
    elif curr_code == "NZD":
        url += "New_Zealand_dollar"
    elif curr_code == "ILS":
        url += "Israeli_new_shekel"
    elif curr_code == "ZAR":
        url += "South_African_rand"
    elif curr_code == "MXN":
        url += "Mexican_peso"
    elif curr_code == "RUB":
        url += "Russian_ruble"
    elif curr_code == "LVL":
        url += "Latvian_lats"
    elif curr_code == "SKK":
        url += "Slovak_koruna"
    elif curr_code == "INR":
        url += "Indian_rupee"
    elif curr_code == "SIT":
        url += "Slovenian_tolar"
    elif curr_code == "SEK":
        url += "Swedish_krona"
    elif curr_code == "HUF":
        url += "Hungarian_forint"
    elif curr_code == "HKD":
        url += "Hong_Kong_dollar"
    elif curr_code == "DKK":
        url += "Danish_krone"
    elif curr_code == "GBP":
        url += "Pound_sterling"

    response = requests.get(
        url,
    )
    soup = BeautifulSoup(response.text, features="html.parser")

    paragraph = soup.find("p").find_next("p")
    return paragraph.text


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:3000")

while True:
    #  Wait for next request from client
    code = socket.recv_string()
    print(code)
    sentence = str(wiki_scrape(code))

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string(sentence)
