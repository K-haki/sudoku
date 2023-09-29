<template>
    <el-dialog title="错误提示" :visible="visible" @close="handleClose">
      <p>{{ errorMessage }}</p>
    </el-dialog>
  </template>
  
  <script>
  export default {
    props: {
      errorMessage: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        visible: true
      };
    },
    methods: {
      handleClose() {
        this.visible = false;
      }
    }
  };
  </script>