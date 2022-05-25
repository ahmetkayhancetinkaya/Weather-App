<template>
    
        <div class="inputTextDiv">
            <div class="form-group">
                <label for="city">Şehir</label>
                <input type="text" id="city" class="form-control" v-model="cityName"/><br>
                <button v-on:click="cityWeather()">Ara</button>
            </div>
        </div>
    
</template>

<script>
import weather from "../service/weather"
export default{
    setup() {
        const {cityName, cityWeather} = weather()

        return {cityName, cityWeather}
    }
    
}
</script>