<template>
  <div class="timer">
    <div class="display">{{ formattedTime }}</div>
    <div class="controls">
      <div class="time-inputs">
        <input type="number" v-model.number="hours" @input="validateInput('hours')" placeholder="小时"
          :disabled="running" />
        <input type="number" v-model.number="minutes" @input="validateInput('minutes')" placeholder="分钟"
          :disabled="running" />
        <input type="number" v-model.number="seconds" @input="validateInput('seconds')" placeholder="秒"
          :disabled="running" />
      </div>
      <div class="buttons">
        <button @click="startTimer" :disabled="running">开始</button>
        <button @click="pauseTimer" :disabled="!running">暂停</button>
        <button @click="resetTimer">重置</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue';

export default {
  setup() {
    const hours = ref(0);
    const minutes = ref(0);
    const seconds = ref(0);
    const totalTime = ref(0);
    const timeRemaining = ref(0);
    const running = ref(false);
    let timer = null;

    const validateInput = (type) => {
      if (type === 'hours' && hours.value < 0) hours.value = 0;
      if (type === 'minutes' && minutes.value < 0) minutes.value = 0;
      if (type === 'seconds' && seconds.value < 0) seconds.value = 0;
    };

    watch([hours, minutes, seconds], () => {
      totalTime.value = (hours.value * 3600 + minutes.value * 60 + seconds.value) * 1000;
      timeRemaining.value = totalTime.value;
    });

    const formattedTime = computed(() => {
      const hours = Math.floor(timeRemaining.value / 3600000);
      const minutes = Math.floor((timeRemaining.value % 3600000) / 60000);
      const seconds = Math.floor((timeRemaining.value % 60000) / 1000);
      const milliseconds = Math.floor((timeRemaining.value % 1000) / 10);
      return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}:${String(milliseconds).padStart(2, '0')}`;
    });

    const startTimer = () => {
      if (!running.value && timeRemaining.value > 0) {
        running.value = true;
        timer = setInterval(() => {
          if (timeRemaining.value > 0) {
            timeRemaining.value -= 10;
          } else {
            clearInterval(timer);
            alert("时间到！")
            running.value = false;
          }
        }, 10);
      }
    };

    const pauseTimer = () => {
      if (running.value) {
        clearInterval(timer);
        running.value = false;
      }
    };

    const resetTimer = () => {
      clearInterval(timer);
      timeRemaining.value = totalTime.value;
      running.value = false;
    };

    return {
      hours,
      minutes,
      seconds,
      formattedTime,
      running,
      startTimer,
      pauseTimer,
      resetTimer,
      validateInput
    };
  },
};
</script>

<style scoped>
.timer {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Arial, sans-serif;
  background-image: linear-gradient(to right bottom, #e6899d, #2caae1);
}

.display {
  font-size: 3rem;
  margin: 20px 0;
}

.controls {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.time-inputs {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.time-inputs input {
  margin: 5px;
  padding: 10px;
  font-size: 1rem;
  width: 80px;
  text-align: center;
}

.buttons button {
  margin: 5px;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
}
</style>