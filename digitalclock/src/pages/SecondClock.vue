<template>
  <div class="timer">
    <div class="display">{{ formattedTime }}</div>
    <div class="controls">
      <button @click="startTimer" :disabled="running">开始</button>
      <button @click="pauseTimer" :disabled="!running">暂停</button>
      <button @click="resetTimer">重置</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      time: 0,
      timer: null,
      running: false,
    };
  },
  computed: {
    formattedTime() {
      const minutes = Math.floor(this.time / 60000);
      const seconds = Math.floor((this.time % 60000) / 1000);
      const milliseconds = Math.floor((this.time % 1000) / 10);
      return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}:${String(milliseconds).padStart(2, '0')}`;
    },
  },
  methods: {
    startTimer() {
      if (!this.running) {
        this.running = true;
        this.timer = setInterval(() => {
          this.time += 10;
        }, 10);
      }
    },
    pauseTimer() {
      if (this.running) {
        clearInterval(this.timer);
        this.running = false;
      }
    },
    resetTimer() {
      clearInterval(this.timer);
      this.time = 0;
      this.running = false;
    },
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

.controls button {
  margin: 5px;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
}
</style>