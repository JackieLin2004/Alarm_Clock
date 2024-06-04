<script setup lang="ts">
import {ref, onMounted, onBeforeUnmount} from 'vue';

// 获取指针
const sec = ref<HTMLElement | null>(null);
const min = ref<HTMLElement | null>(null);
const hour = ref<HTMLElement | null>(null);

// 动画函数
function toTime() {
  // 获取实时时间
  const date = new Date();
  const iSec = date.getSeconds();
  const iMin = date.getMinutes() + iSec / 60;
  const iHour = date.getHours() + iMin / 60;
  // 赋样式
  if (sec.value && min.value && hour.value) {
    sec.value.style.transform = `translate(-50%, -50%) rotate(${iSec * 6}deg)`;
    min.value.style.transform = `translate(-50%, -50%) rotate(${iMin * 6}deg)`;
    hour.value.style.transform = `translate(-50%, -50%) rotate(${iHour * 30}deg)`;
  }
}

// 定时器调用
let intervalId: number | undefined;

onMounted(() => {
  intervalId = setInterval(toTime, 1000);
  toTime(); // 初始化时钟位置
});

onBeforeUnmount(() => {
  if (intervalId) {
    clearInterval(intervalId);
  }
});

// 闹钟功能
const alarmTime = ref('');
const alarmTimeout = ref<number | null>(null);
const alarmClock = ref<HTMLAudioElement | null>(null);

function setAlarm() {
  if (!alarmTime.value) {
    alert('请选择闹钟时间！');
    return;
  }

  const now = new Date();
  const [hour, minute] = alarmTime.value.split(':');
  const alarm = new Date(now.getFullYear(), now.getMonth(), now.getDate(), parseInt(hour), parseInt(minute));
  const timeDiff = alarm.getTime() - now.getTime();

  if (timeDiff > 0) {
    alarmTimeout.value = window.setTimeout(() => {
      console.log('alarming!')
      if (alarmClock.value) {
        alarmClock.value.play();
      }
    }, timeDiff);
    alert('闹钟设置成功！');
  } else {
    alert('请选择未来的时间！');
  }
}

function closeAlarm() {
  if (alarmClock.value) {
    alarmClock.value.pause();
    alarmClock.value.load();
  }
  if (alarmTimeout.value !== null) {
    window.clearTimeout(alarmTimeout.value);
    alarmTimeout.value = null;
  }
}
</script>

<template>
  <div class="wrapper">
    <div class="clock">
      <div class="box">
        <!--刻度线-->
        <div class="line line0"></div>
        <div class="line line1"></div>
        <div class="line line2"></div>
        <div class="line line3"></div>
        <div class="line line4"></div>
        <div class="line line5"></div>

        <div class="line line00"></div>
        <div class="line line11"></div>
        <div class="line line22"></div>
        <div class="line line33"></div>
        <div class="line line44"></div>
        <div class="line line55"></div>

        <!--指针-->
        <div class="pointer hour" ref="hour"></div>
        <div class="pointer min" ref="min"></div>
        <div class="pointer sec" ref="sec"></div>

        <!--螺丝-->
        <div class="dot"></div>
      </div>

      <!--添加阴影-->
      <div class="box1"></div>
    </div>
    <!-- 闹钟设置 -->
    <div class="alarm-clock">
      <br>
      <div class="show-time">
        <label for="alarm-time"><strong>闹钟时间：</strong></label>
        <input type="time" v-model="alarmTime" id="alarm-time">
      </div>
      <br>
      <button class="set-alarm" @click="setAlarm">设置闹钟</button>
      <audio controls ref="alarmClock" id="alarm-clock" style="display: none">
        <source src="../assets/music.mp3" type="audio/mpeg">
      </audio>
      <br>
      <button class="close-alarm" @click="closeAlarm">关闭闹钟</button>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  width: 100vw;
  height: 100vh;
  background-image: linear-gradient(to right bottom, #e6899d, #2caae1);
}

.clock {
  width: 100%;
  height: 45%;
  display: flex;
  justify-content: center;
  align-items: center;
  scale: 0.8;
}

.clock .box {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  border: 7px solid #999999;
  box-shadow: 0 23px 15px rgba(0, 0, 0, 0.7);
  position: relative;
}

.clock .box1 {
  position: absolute;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  border: 7px solid #999999;
  box-shadow: inset 0 23px 15px rgba(0, 0, 0, 0.7);
}

.clock .line {
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  top: 0;
  width: 5px;
  height: 30px;
  background-color: #412d2d;
  transform-origin: 3px 150px;
}

.clock .line1 {
  transform: translate(-50%) rotate(30deg);
}

.clock .line2 {
  transform: translate(-50%) rotate(60deg);
}

.clock .line3 {
  transform: translate(-50%) rotate(90deg);
}

.clock .line4 {
  transform: translate(-50%) rotate(120deg);
}

.clock .line5 {
  transform: translate(-50%) rotate(150deg);
}

.clock .line11 {
  transform: translate(-50%) rotate(-30deg);
}

.clock .line22 {
  transform: translate(-50%) rotate(-60deg);
}

.clock .line33 {
  transform: translate(-50%) rotate(-90deg);
}

.clock .line44 {
  transform: translate(-50%) rotate(-120deg);
}

.clock .line55 {
  transform: translate(-50%) rotate(-150deg);
}

.clock .line00 {
  transform: translate(-50%) rotate(180deg);
}

.clock .pointer {
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  transform-origin: center bottom;
}

.clock .hour {
  width: 9px;
  height: 60px;
  top: 120px;
  background-color: #000;
}

.clock .min {
  width: 7px;
  height: 90px;
  top: 108px;
  background-color: #000;
}

.clock .sec {
  width: 3px;
  height: 110px;
  top: 93px;
  background-color: red;
}

.clock .dot {
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background-color: #000;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.alarm-clock {
  width: 100%;
  height: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.alarm-clock .show-time {
  display: flex;
  width: 60%;
  justify-content: center;
  align-items: center;
}

.alarm-clock button {
  width: 80%;
  height: 10vw;
  border: none;
  outline: none;
  border-radius: 4px;
  background-color: #60adc7;
  color: #fff;
  font-size: 4vw;
}
</style>
