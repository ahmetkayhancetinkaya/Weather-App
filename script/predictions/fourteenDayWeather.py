import json

import requests
from bs4 import BeautifulSoup

def getData(cityCode):
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
        page = requests.get(
                'https://weather.com/tr-TR/weather/tenday/l/' + cityCode + '',
                headers=headers)
        tree =BeautifulSoup(page.text, 'html.parser')

        cityValue = tree.find_all('span', attrs={"data-testid":"PresentationName" ,"class":"LocationPageTitle--PresentationName--1QYny"})[0].text # details sayısını artırdıkça artar
        updatedTimeValue = tree.find_all('div', attrs={ "class":"DailyForecast--timestamp--22ExT"})[0].text

        infoDict = {
                "city" : cityValue,
                "updatedTimeValue" : updatedTimeValue
        }
        contentDict = {}
        def fourteenWeather(index):

                dataDetail = tree.find_all('details',attrs={ "id":"detailIndex" + str(index) + ""})[0]#details içini değiştir
                dayValue = dataDetail.find_all('h2')[0].text
                hıTemp = dataDetail.find_all('span', attrs={"data-testid":"TemperatureValue", "class":"DetailsSummary--highTempValue--3Oteu"})[0].text
                loTemp = dataDetail.find_all('span', attrs={"data-testid":"TemperatureValue", "class":"DetailsSummary--lowTempValue--3H-7I"})[0].text
                skyValue = dataDetail.find_all('span', attrs={ "class":"DetailsSummary--extendedData--365A_"})[0].text
                chanceOfRain = dataDetail.find_all('span', attrs={"data-testid":"PercentageValue"})[0].text
                windSpeed = dataDetail.find_all('span', attrs={"data-testid":"Wind", "class":"Wind--windWrapper--3aqXJ undefined"})[0].text


                x = {
                        dayValue: {"day": dayValue,
                                   "hıTemp": hıTemp,
                                   "loTemp": loTemp,
                                   "sky": skyValue,
                                   "chanceOfRain": chanceOfRain,
                                   "windSpeed": windSpeed}
                }
                contentDict.update(x)

        for i in range(0,15):
                fourteenWeather(i)

        fourteenDayDict = {
                "info" : infoDict,
                "content" : contentDict
        }
        return fourteenDayDict

