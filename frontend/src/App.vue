<template>
<div class="container">
  <div id="inputDiv" class="container col-sm-4 col-md-4 col-lg-4 text-center" style="justify-content: center;">
      <InputCity/>
  </div>
</div>
<br>
<br>
<div class="container">
      <div id="pedictionDiv" class="container col-sm-6 col-md-6 col-lg-6 text-center" >
        <CurrentWeather :current-dict="currentDict"/>
      </div>
</div>
<br>
<div class="container">
    <div id="pedictionDiv" class="container col-sm-12 col-md-12 col-lg-12 atext-center" style="justify-content: center;">
      <Hourly :hourly-dict="hourlyDict"/>
    </div>
</div>
<br>
   
<div class="container">
  <div id="pedictionDiv" class="container col-sm-12 col-md-12 col-lg-12 align-items-center" style="justify-content: center;">
      <FourteenWeather :fourteenDay-dict="fourteenDayDict"/>/>
  </div>
</div>
</template>




<script>
import { h, onMounted} from 'vue'



import CurrentWeather from './components/currentWeather.vue';
import Hourly from './components/hourly.vue';
import FourteenWeather from './components/fourteenWeather.vue';
import InputCity from './components/inputCity.vue';
import weather from './service/weather';

export default {
      setup() {
    
     const {GelenIstek, currentDict,hourlyDict,fourteenDayDict} = weather()
    
     onMounted(() => {
       GelenIstek();
     });
     return {
       currentDict,hourlyDict,fourteenDayDict
     };
   },

    components: { CurrentWeather, Hourly, FourteenWeather, InputCity }
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #502c4e;
  margin-top: 60px;
}
#pedictionDiv{

  background-color: black;
  border-radius: 25px;
  color: rgb(245, 245, 245);
  padding: 10px;
  

}
#inputDiv{

  background-color: rgb(69, 21, 133);
  border-radius: 50px;
  color: rgb(251, 251, 251);
  padding: 10px;
  

}
.container{
  background: #ffffff;
}

 
  
  .hourDiv{
  color: rgb(15, 248, 34);
  background-image: linear-gradient(rgb(211, 39, 39), green);
   border-radius: 25px;
}
.dayDiv{
  color: rgb(15, 248, 34);
  background-image: linear-gradient(rgb(211, 39, 39), green);
   border-radius: 25px;
}

  #dataDiv { 
  border:3px solid rgb(1, 14, 1);
  display: flex;
  background: #0a0e9b;
  color: rgb(245, 245, 245);
  justify-content: center;
   padding: 10px;
  border-radius: 20px;
   
  }

  /* .hourByHourContentDiv{
    width: 250px;
    
    
  }
  .fourteenDayContentDiv{
    width: 350px;
  } */
  
  
</style>