<template>
  <div class="wrapper-main">
    <div class="maincontent">
      <router-view></router-view>
    </div>
    <div class="tab">
      <div class="tab-item" @click="changeToHome">
        <img src="./assets/icons/clock.png" alt="" style="width: 6vw;height: 6vw;">
        <p>闹钟</p>
      </div>
      <div class="tab-item" @click="changeToGlobal">
        <img src="./assets/icons/global.png" alt="" style="width: 6vw;height: 6vw;">
        <p>世界时钟</p>
      </div>
      <div class="tab-item" @click="changeToSecond">
        <img src="./assets/icons/bm.png" alt="" style="width: 6vw;height: 6vw;">
        <p>秒表</p>
      </div>
      <div class="tab-item" @click="changeToCountDown">
        <img src="./assets/icons/countdown.png" alt="" style="width: 6vw;height: 6vw;">
        <p>计时器</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {useRouter} from 'vue-router';

const router = useRouter()
const changeToHome = () => {
  router.push({
    name: 'clockpage'
  })
}
const changeToSecond = () => {
  router.push({
    name: 'secondclock'
  })
}
const changeToGlobal = () => {
  router.push({
    name: 'worldclock'
  })
}
const changeToCountDown = () => {
  router.push({
    name: 'countdown'
  })
}
</script>

<style scoped>
.wrapper-main {
  height: 100%;
  width: 100%;
}

.tab {
  width: 100%;
  position: fixed;
  bottom: 0;
  left: 0;
  height: 16vw;
  border: 1px solid #DDD;
  background-color: #DDD;
  display: flex;
  flex-direction: row;
}

.tab-item {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  background-color: whitesmoke;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-top: 4.5vw;
}

.tab-item:hover {
  background-color: transparent;
  transition: 0.25s;
}

.tab-item p {
  font-size: 0.8em;
  /* text-align: center; */
  color: #555;
}

.maincontent {
  width: 100%;
  height: 100vh;
  /* margin-bottom: 16vw; */
}
</style>