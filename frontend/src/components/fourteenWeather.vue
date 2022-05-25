<template>
 <div>
    <h2>14 Günlük Hava Durumu</h2>
  </div>
  <div class="fourteenDayInfoDiv" v-for="(item, index) in fourteenDayDict" :key="item">
  <div class="infoDiv">
      <span>{{ item.info.city }}</span>
    </div>
    <div class="infoDiv">
      <span>{{ item.info.updatedTimeValue }}</span>
    </div>
    <br />
        
      <div class="row justify-content-center">
        <div v-for="itemday in item.content">
          <div>
            <div class="fourteenDayContentDiv">
              <div class="dayDiv">{{ itemday.day }}</div>
              <div id="dataDiv" class="chanceofRainDiv">Yağmur İhtimali : {{ itemday.chanceOfRain }}</div>
            <br />
            <div id="dataDiv" class="skyDiv">Gökyüzü : {{ itemday.sky }}</div>
            <br />
            <div id="dataDiv" class="tempDiv">En Yüksek/En Düşük : {{itemday.hıTemp}}/{{itemday.loTemp}}</div>
            <br />
            <div id="dataDiv" class="windSpeedDiv">Rüzgar : {{ itemday.windSpeed }}</div>
            </div>
          </div>
         <br>
        </div>
        
      </div>
    
  </div>
</template>

<script>

export default {

    props : {
    fourteenDayDict:Object
  }
    
  
}
</script>

