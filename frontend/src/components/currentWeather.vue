<template>
  <div>
    <h2>Anlık Hava Durumu</h2>
  </div>
  <div class="currentMainDiv" v-for="(item, index) in currentDict" :key="index">
    <div class="infoDiv">
      <span>{{ item.info.city }}</span>
    </div>
    <div class="infoDiv">
      <span>{{ item.info.updateTime }}</span>
    </div>

    <div id="dataDiv" class="tempDiv">
      Anlık Sıcaklık:
      <span>{{ item.content.currentTemp }}</span>
    </div>
    <br />
    <div id="dataDiv" class="feelTempDiv">
      Hissedilen Sıcaklık:
      <span>{{ item.content.feelTemp }}</span>
    </div>
    <br />
    <div id="dataDiv" class="humidityDiv">
      Nem:
      <span>{{ item.content.humidity }}</span>
    </div>
    <br />
    <div id="dataDiv" class="hıLoTempDiv">
      En Yüksek/En Düşük:
      <span>{{ item.content.hıLoTemp }}</span>
    </div>
    <br />
    <div id="dataDiv" class="pressureDiv">
      Basınç:
      <span>{{ item.content.pressureValue }}</span>
    </div>
    <br />
    <div id="dataDiv" class="skyDiv">
      Gökyüzü:
      <span>{{ item.content.sky }}</span>
    </div>
    <br />
    <div id="dataDiv" class="windSpeedDiv">
      Rüzgar:
      <span>{{ item.content.windSpeed }}</span>
    </div>
  </div>
</template>

<script>

export default {
  props : {
    currentDict:Object
  }

}
</script>

