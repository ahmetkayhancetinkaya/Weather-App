
import {ref} from 'vue'
import axios from 'axios'
export default function weather(){
    const currentDict = ref([]);
    const hourlyDict = ref([]);
    const fourteenDayDict = ref([]);

    
    const cityName = ref('')

    async function GelenIstek() {
      axios.get(" http://127.0.0.1:3000/weather", {
        headers: {
          "Access-Control-Allow-Origin": "*"
        }
      }).then(res => {
        console.log(res.data);
        currentDict.value.push(res.data.currentWeather)
        hourlyDict.value.push(res.data.hourByHourDict)
        fourteenDayDict.value.push(res.data.fourteendayDict)

      });
    }
    function cityWeather(){
        axios.post("http://localhost:3000/data",{
                cityName:cityName.value
            }).then(response => {
                if(response.status === 200){
                    currentCityWeather.value.push(response.data.currentWeather)
                    console.log("currentWeather", currentCityWeather)
                }
            })
    }

    return {currentDict,hourlyDict,fourteenDayDict, GelenIstek, cityName, cityWeather}
}