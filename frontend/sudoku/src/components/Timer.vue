<template>  
    <div>  
      <el-button @click="startTimer">开始</el-button>  
      <el-button @click="stopTimer">停止</el-button>  
      <el-input v-model="timer" readonly></el-input>  
    </div>  
  </template>  
    
  <script>  
  export default {  
    data() {  
      return {  
        timer: 0,  
        intervalId: null  
      }  
    },  
    methods: {  
      startTimer() {  
        if (this.intervalId === null) {  
          this.intervalId = setInterval(() => {  
            this.timer++;  
          }, 1000)  
        }  
      },  
      stopTimer() {  
        clearInterval(this.intervalId)  
        this.intervalId = null  
      }  
    }  
  }  
  </script>