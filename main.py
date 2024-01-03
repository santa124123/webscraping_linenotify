import requests
from bs4 import BeautifulSoup

def main(run):
    url = "https://www.investing.com/currencies/chf-thb"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    inputs = soup.find('span', {'class': 'text-2xl'})
    str(inputs)
    CHF = str(inputs).split(">")[1].split("<")[0]

    line_url = 'https://notify-api.line.me/api/notify'
    token = 'cT9Neprwc3j7g0qO5SoHDjaDbG2A70GdaPqyIekrJbc'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

    if float(CHF) != 40.881:
        msg = CHF
        r = requests.post(line_url, headers=headers, data = {'message':msg})
        run = False