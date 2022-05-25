<template>
  <div>
    <h2>Saatlik Hava Durumu</h2>
  </div>
  <div class="hourByHourInfoDiv" v-for="(item, index) in hourlyDict" :key="item">
    <div class="infoDiv">
      <span>{{ item.info.city }}</span>
    </div>
    <div class="infoDiv">
      <span>{{ item.info.day }}</span>
    </div>
    <div class="infoDiv">
      <span>{{ item.info.updateTime }}</span>
    </div>
    <br />

    <div class="row justify-content-center">
      <div v-for="itemhour in item.content">
        <div>
          <div class="hourByHourContentDiv">
            <div class="hourDiv">{{ itemhour.hour }}</div>
            <div id="dataDiv" class="chanceofRainDiv">Yağmur İhtimali : {{ itemhour.chanceOfRain }}</div>
            <br />
            <div id="dataDiv" class="skyDiv">Gökyüzü : {{ itemhour.sky }}</div>
            <br />
            <div id="dataDiv" class="tempDiv">Sıcaklık : {{ itemhour.temp }}</div>
            <br />
            <div id="dataDiv" class="windSpeedDiv">Rüzgar : {{ itemhour.windSpeed }}</div>
          </div>
        </div>
        <br />
      </div>
    </div>
  </div>
</template>

<script>
import { h, onMounted, ref } from 'vue'
import weather from '../service/weather';
export default {

  props : {
    hourlyDict:Object
  }
}
</script>

