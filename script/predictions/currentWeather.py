import json

import requests
from bs4 import BeautifulSoup

def getData(cityCode):
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
        page = requests.get(
                'https://weather.com/tr-TR/weather/today/l/' + cityCode + '',
                headers=headers)
        tree =BeautifulSoup(page.text, 'html.parser')

        currentDict = {}

        infoTag = tree.find_all('div',attrs={ "class":"CurrentConditions--header--27uOE"})[0]# details sayısını artırdıkça artar
        cityValue = infoTag.find_all("h1", attrs={"class":"CurrentConditions--location--kyTeL"})[0].text
        updatedTimeValue = infoTag.find_all("span", attrs={"class":"CurrentConditions--timestamp--23dfw"})[0].text

        currentTag = tree.find_all('div', attrs={"class": "CurrentConditions--primary--2SVPh"})[0]  # details sayısını artırdıkça artar
        currentTemp = currentTag.find_all("span", attrs={"class":"CurrentConditions--tempValue--3a50n"})[0].text
        skyValue = currentTag.find_all("div", attrs={"class":"CurrentConditions--phraseValue--2Z18W"})[0].text



        infoDict = {"city" : cityValue,
                    "updateTime" : updatedTimeValue,
                       }
        contentDict={}

        dailyDetailInfo = tree.find_all('div',attrs={"id":"todayDetails", "class":"removeIfEmpty"})[0]# details sayısını artırdıkça artar
        feelTemp = dailyDetailInfo.find_all("span", attrs={ "data-testid":"TemperatureValue", "class":"TodayDetailsCard--feelsLikeTempValue--Cf9Sl"})[0].text
        hıLoTemp = dailyDetailInfo.find_all("div", attrs={ "data-testid":"wxData", "class":"WeatherDetailsListItem--wxData--2s6HT"})[0].text
        humidity = dailyDetailInfo.find_all("span", attrs={ "data-testid":"PercentageValue"})[0].text
        pressureValue = dailyDetailInfo.find_all("span", attrs={ "data-testid":"PressureValue"})[0].text
        windSpeed = dailyDetailInfo.find_all("span", attrs={ "data-testid":"Wind"})[0].text


        x = {
                "currentTemp": currentTemp,
                "sky": skyValue,
                "feelTemp": feelTemp,
                "hıLoTemp": hıLoTemp,
                "humidity": humidity,
                "pressureValue": pressureValue,
                "windSpeed": windSpeed

        }
        contentDict.update(x)
        currentDict = {
                "info" : infoDict,
                "content" : contentDict
        }

        return  currentDict



