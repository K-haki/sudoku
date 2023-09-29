<template>
    <div>
      <button @click="getData">Get Data</button>
      <p>输出：</p>
      <p>{{ responseData }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        responseData: ''
      };
    },
  
    methods: {
      getData() {
        axios.get('http://127.0.0.1:5000/data')
          .then(response => {
            this.responseData = response.data;
            console.log("response.data"); // 打印到控制台
          })
          .catch(error => {
            console.error('Error:', error);
          });
      }
    }
  };
  </script>