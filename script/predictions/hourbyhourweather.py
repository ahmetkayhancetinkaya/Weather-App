import json

import requests
from bs4 import BeautifulSoup


def getData(cityCode):
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
        page = requests.get(
                'https://weather.com/tr-TR/weather/hourbyhour/l/' + cityCode + '',
                headers=headers)
        tree =BeautifulSoup(page.text, 'html.parser')


        infoTag = tree.find_all('h1',attrs={ "class":"LocationPageTitle--PageHeader--1a5x1 HourlyForecast--CardHeader--2bpTn"})[0]# details sayısını artırdıkça artar
        cityValue = infoTag.find_all("span", attrs={"data-testid":"PresentationName", "class":"LocationPageTitle--PresentationName--1QYny"})[0].text


        updatedTimeTag = tree.find_all('div',attrs={ "class":"HourlyForecast--timestamp--MVnBF"})[0]# details sayısını artırdıkça artar
        updatedTimeValue = updatedTimeTag.text
        splitTimeArray = updatedTimeValue.split(":")


        day = tree.find_all('div',attrs={ "class":"HourlyForecast--DisclosureList--3CdxR"})[0]# details sayısını artırdıkça artar
        dayValue = day.find_all("h3", attrs={"id":"currentDateId0", "class":"HourlyForecast--longDate--1tdaJ"})[0].text


        ınfoDict = {"city" : cityValue,
                    "updateTime" : updatedTimeValue,
                    "day" : dayValue }
        contentDict = {}
        def HourlyWeather(index):

                weatherData = tree.find_all('details',attrs={ "id":"detailIndex" + str(index) + ""})[0]

                clockValue = weatherData.find_all('h2')[0].text
                tempValue = weatherData.find_all('span', attrs= {"class":"DetailsSummary--tempValue--1K4ka"})[0].text
                skyValue = weatherData.find_all('span', attrs= {"class":"DetailsSummary--extendedData--365A_"})[0].text
                chanceOfRain = weatherData.find_all('span', attrs= {"data-testid":"PercentageValue"})[0].text
                windSpeed = weatherData.find_all('span', attrs= {"data-testid":"Wind", "class":"Wind--windWrapper--3aqXJ undefined"})[0].text




                x ={
                         clockValue : {"hour" : clockValue, "temp":tempValue, "sky":skyValue, "chanceOfRain":chanceOfRain, "windSpeed":windSpeed}
                }
                contentDict.update(x)


        for i in range(0,(23-int(splitTimeArray[0]))):
                HourlyWeather(i)

        hourDict = {"content" : contentDict,
                    "info" : ınfoDict
                    }
        return hourDict


