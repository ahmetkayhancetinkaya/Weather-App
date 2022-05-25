import sys
import json


from predictions import fourteenDayWeather, hourbyhourweather, currentWeather

def weatherScript(city):


    allDict= {"currentWeather" : currentWeather.getData(city),
              "hourByHourDict" : hourbyhourweather.getData(city),
              "fourteendayDict" : fourteenDayWeather.getData(city) }

    myJson = json.dumps(allDict, indent=5, ensure_ascii=True, sort_keys=True) # Dicti JSON'açevirme
    
    print(myJson)
    return myJson

if __name__=="__main__":
    city = sys.argv[1]
    weatherScript(city)



