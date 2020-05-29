from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import time
from bs4 import BeautifulSoup


def index(request):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'ROZKLADY_JEZYK=PL; ROZKLADY_AB=0; ROZKLADY_WIDTH=200; ROZKLADY_WIZYTA=27; ROZKLADY_OSTATNIA=1587647241',
        'Host': 'rozklady.mpk.krakow.pl',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    url = 'http://rozklady.mpk.krakow.pl/'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    hrefs = soup.select('table tr td a')
    numbers = []
    tram = []
    tram_replacement = []
    bus_city = []
    bus_suburban = []
    bus_suburban_fast = []
    bus_city_assist = []
    bus_city_fast = []
    bus_replacement = []
    for x in range(len(hrefs)):
        item = hrefs[x].get_text().strip()
        if item.isdigit():
            numbers.append(item)
    
    for x in range(len(numbers)):
        item = int(numbers[x])
        if item < 70:
            tram.append(item)

    for x in range(len(numbers)):
        item = int(numbers[x])
        if item >= 70 and item < 100:
            tram_replacement.append(item) 

    for x in range(len(numbers)):
        item = int(numbers[x])
        if item >= 100 and item < 200:
            bus_city.append(item)  

    for x in range(len(numbers)):
        item = int(numbers[x])
        if item >= 200 and item < 300:
            bus_suburban.append(item)  

    for x in range(len(numbers)):
        item = int(numbers[x])
        if item >= 300 and item < 400:
            bus_suburban_fast.append(item)  

    for x in range(len(numbers)):
        item = int(numbers[x])
        if item >= 400 and item < 500:
            bus_city_assist.append(item) 

    for x in range(len(numbers)):
        item = int(numbers[x])
        if item >= 500 and item < 600:
            bus_city_fast.append(item)  

    for x in range(len(numbers)):
        item = int(numbers[x])
        if item >= 700 and item < 800:
            bus_replacement.append(item)
    return JsonResponse([tram, tram_replacement], safe=False)

def info(request):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'ROZKLADY_JEZYK=PL; ROZKLADY_AB=0; ROZKLADY_WIDTH=200; ROZKLADY_WIZYTA=27; ROZKLADY_OSTATNIA=1587647241',
        'Host': 'rozklady.mpk.krakow.pl',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    url = 'http://rozklady.mpk.krakow.pl/'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    info = soup.select('table tr td')
    info2 = info[11].find_all('a')
    info_current = []
    info_next = []
    info_current.append(info2[0].get_text().strip())
    if len(info2) >= 1:
        for x in range(len(info2)):
            if x > 0:
                item = info2[x].get_text().strip()
                info_next.append(item)
    return JsonResponse([info_current, info_next], safe=False)

def lines(request):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'ROZKLADY_JEZYK=PL; ROZKLADY_AB=0; ROZKLADY_WIDTH=200; ROZKLADY_WIZYTA=27; ROZKLADY_OSTATNIA=1587647241',
        'Host': 'rozklady.mpk.krakow.pl',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    url = 'http://rozklady.mpk.krakow.pl/'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    hrefs = soup.select('table tr td a')
    numbers = []
    tram = []
    tram_replacement = []
    bus_city = []
    bus_suburban = []
    bus_suburban_fast = []
    bus_city_assist = []
    bus_city_fast = []
    bus_city_night = []
    bus_replacement = []
    bus_special = []
    bus_suburban_night = []
    info = soup.select('table tr td')
    info2 = info[11].find_all('a')
    #for x in range(len(hrefs)):
    #    print(hrefs[x].attrs.get('class'))
        
    info3 = []
    for x in range(len(info2)):
        item = info2[x].get_text().strip()
        info3.append(item)

    for x in range(len(hrefs)):
        item = hrefs[x].get_text().strip()
        item_class = hrefs[x].attrs.get('class')
        #print(item_class)
        if item.isdigit() and item_class != None:
            numbers.append({"number":item, "css":item_class[0]})
    
    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number < 70:
            tram.append(item)

    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 70 and line_number < 100:
            tram_replacement.append(item) 

    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 100 and line_number < 200:
            bus_city.append(item)  

    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 200 and line_number < 300:
            bus_suburban.append(item)  

    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 300 and line_number < 400:
            bus_suburban_fast.append(item)  

    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 400 and line_number < 500:
            bus_city_assist.append(item) 

    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 500 and line_number < 600:
            bus_city_fast.append(item)  

    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 600 and line_number < 700:
            bus_city_night.append(item) 

    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 700 and line_number < 800:
            bus_replacement.append(item)
    
    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 800 and line_number < 900:
            bus_special.append(item)

    for x in range(len(numbers)):
        item = numbers[x]
        line_number = int(item["number"])
        if line_number >= 900 and line_number <= 999:
            bus_suburban_night.append(item)

    return JsonResponse([tram, tram_replacement, bus_city, bus_suburban, bus_suburban_fast, bus_city_assist, bus_city_fast, bus_city_night, bus_replacement, bus_special, bus_suburban_night], safe=False)
def timetable(request):
    if (request.GET.get('line') == None):
        return JsonResponse({'error':'no line'})
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'ROZKLADY_JEZYK=PL; ROZKLADY_AB=0; ROZKLADY_WIDTH=200; ROZKLADY_WIZYTA=27; ROZKLADY_OSTATNIA=1587647241',
        'Host': 'rozklady.mpk.krakow.pl',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    line_number = request.GET.get('line')
    variant_number = request.GET.get('variant')
    stop_number = request.GET.get('stop')
    url = ''
    if stop_number is None and variant_number is None:
        url = 'http://rozklady.mpk.krakow.pl/?lang=PL&linia=' + line_number
    elif stop_number is None:
        url = 'http://rozklady.mpk.krakow.pl/?lang=PL&linia=' + line_number + '__' + variant_number
    else:
        url = 'http://rozklady.mpk.krakow.pl/?lang=PL&linia=' + line_number + '__' + variant_number + '__' + stop_number
    #url = 'http://rozklady.mpk.krakow.pl/?lang=PL&linia=' + line_number + '__' + variant_number + '__' + stop_number
    #print(url)
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    hrefs = soup.select('table tbody tr td table tr td table')
    basic_info = hrefs[1].find_all('p')
    available_routes = hrefs[1].find_all('a')
    stops = hrefs[4].find_all('tr')
    basic_info_parsed = {}
    available_routes_parsed = []
    stops_parsed = []
    html_ttdata = str(hrefs[5])
    #for x in (range(len(basic_info))):
    basic_info_parsed.update({"lineNumber":basic_info[0].get_text().strip(), "from":basic_info[1].get_text().strip()[4:len(basic_info[1].get_text().strip())], "to":basic_info[2].get_text().strip()[4:len(basic_info[2].get_text().strip())]})
    for x in (range(len(available_routes))):
        q1 = urllib.parse.parse_qs(urllib.parse.urlparse(available_routes[x].get('href')).query)
        q2 = q1["linia"][0].split("__")
        available_routes_parsed.append({"name":available_routes[x].get_text().strip(), "href":q2})
    for row in stops:
        col = row.find_all('td')
        #print(len(col))
        if (len(col)) > 1:
            if col[1].get_text().strip() == 'NZ':
                href = urllib.parse.parse_qs(urllib.parse.urlparse(col[0].find_all('a')[0].get('href')).query)
                href2 = href["linia"][0].split("__")
                stop_id = urllib.parse.parse_qs(urllib.parse.urlparse(col[2].find_all('a')[0].get('href')).query)
                stop_id2 = stop_id["przystanek"]
                stops_parsed.append({"name":col[0].get_text().strip(), "hrefs":href2, "requestStop":True, "stopID":stop_id2[0]})
            elif len(col[0].find_all('a')) > 0:
                href = urllib.parse.parse_qs(urllib.parse.urlparse(col[0].find_all('a')[0].get('href')).query)
                href2 = href["linia"][0].split("__")
                stop_id = urllib.parse.parse_qs(urllib.parse.urlparse(col[2].find_all('a')[0].get('href')).query)
                stop_id2 = stop_id["przystanek"]
                stops_parsed.append({"name":col[0].get_text().strip(), "hrefs":href2, "requestStop":False, "stopID":stop_id2[0]})
            else:
                stops_parsed.append({"name":col[0].get_text().strip(), "ends":True, "requestStop":False})
        else:
            stops_parsed.append({"border":True})
#        for col in row.find_all('td'):
#            stops_parsed.append(col[1].get_text().strip())
    def current_stop_filter(stop):
        print(stop)
        if stop.get("hrefs") is not None and stop["hrefs"][2] == stop_number:
            return True
        else:
            return False 
    current_stop = list(filter(current_stop_filter, stops_parsed))[0]
    basic_info_parsed["currentStop"] = current_stop
    return JsonResponse({"info":basic_info_parsed, "routes":available_routes_parsed, "stops":stops_parsed, "html":html_ttdata}, safe=False)
    

def get_line_type(request):
    if (request.GET.get('line') == None):
        return JsonResponse({'error':'no line'})
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'ROZKLADY_JEZYK=PL; ROZKLADY_AB=0; ROZKLADY_WIDTH=200; ROZKLADY_WIZYTA=27; ROZKLADY_OSTATNIA=1587647241',
        'Host': 'rozklady.mpk.krakow.pl',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    line_number = request.GET.get('line')
    url = 'http://rozklady.mpk.krakow.pl/'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    hrefs = soup.select('table tr td a')
    css = {}
    for x in range(len(hrefs)):
        item = hrefs[x].get_text().strip()
        item_class = hrefs[x].attrs.get('class')
        #print(item_class)
        if item.isdigit() and item_class != None and item == line_number:
            css['type'] = item_class[0]
    return JsonResponse(css, safe=False)

def get_variant_stops(request):
    if (request.GET.get('line') == None or request.GET.get('variant') == None):
        return JsonResponse({'error':'no line/variant'})
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'ROZKLADY_JEZYK=PL; ROZKLADY_AB=0; ROZKLADY_WIDTH=200; ROZKLADY_WIZYTA=27; ROZKLADY_OSTATNIA=1587647241',
        'Host': 'rozklady.mpk.krakow.pl',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    line_number = request.GET.get('line')
    variant_number = request.GET.get('variant')
    url = 'http://rozklady.mpk.krakow.pl/?lang=PL&linia=' + line_number + '__' + variant_number
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    hrefs = soup.select('table tbody tr td table tr td table')
    basic_info = hrefs[1].find_all('p')
    stops = hrefs[4].find_all('tr')
    basic_info_parsed = {}
    stops_parsed = []
    #for x in (range(len(basic_info))):
    basic_info_parsed.update({"lineNumber":basic_info[0].get_text().strip(), "from":basic_info[1].get_text().strip()[4:len(basic_info[1].get_text().strip())], "to":basic_info[2].get_text().strip()[4:len(basic_info[2].get_text().strip())]})
    for row in stops:
        col = row.find_all('td')
        #print(len(col))
        if (len(col)) > 1:
            if col[1].get_text().strip() == 'NZ':
                href = urllib.parse.parse_qs(urllib.parse.urlparse(col[0].find_all('a')[0].get('href')).query)
                href2 = href["linia"][0].split("__")
                stop_id = urllib.parse.parse_qs(urllib.parse.urlparse(col[2].find_all('a')[0].get('href')).query)
                stop_id2 = stop_id["przystanek"]
                stops_parsed.append({"name":col[0].get_text().strip(), "hrefs":href2, "requestStop":True, "stopID":stop_id2})
            elif len(col[0].find_all('a')) > 0:
                href = urllib.parse.parse_qs(urllib.parse.urlparse(col[0].find_all('a')[0].get('href')).query)
                href2 = href["linia"][0].split("__")
                stop_id = urllib.parse.parse_qs(urllib.parse.urlparse(col[2].find_all('a')[0].get('href')).query)
                stop_id2 = stop_id["przystanek"]
                stops_parsed.append({"name":col[0].get_text().strip(), "hrefs":href2, "requestStop":False, "stopID":stop_id2})
            else:
                stops_parsed.append({"name":col[0].get_text().strip(), "ends":True, "requestStop":False})
        else:
            stops_parsed.append({"border":True})
#        for col in row.find_all('td'):
#            stops_parsed.append(col[1].get_text().strip())
    return JsonResponse({"info":basic_info_parsed, "stops":stops_parsed}, safe=False)