<template>
  <div id="app">
<!--    <div class="number-container">-->
<!--      <div class="select-number" v-for="(number,i) in numbers">{{number}}</div>-->
<!--    </div>-->
    <div calss="game-board">
      <div v-for="i of list" class="game-row">
        <div v-for="item of list" class="sudoku-board">
          {{  "数独" + item * i }}
          <div v-for="(row,i) in board" class="board-row">
            <input v-for="(grid,j) in row" class="board-grid" :value="grid" @input="inputChange($event,i,j)"/>
          </div>
        </div>
      </div>
    </div>
    <button class="button" @click="output">新的游戏</button>
    <button style="top: 35%;" class="button" @click="reset">难度选择</button>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';


export default {
  name: 'app',
  components: {
  },
  data() {
    return {
      board: [[1, 0, 2, 0, 5, 0, 7, 0, 0], [0, 6, 3, 8, 0, 5, 0, 0, 7], [7, 0, 1, 0, 0, 4, 3, 9, 0],
        [0, 4, 0, 0, 6, 9, 0, 8, 0], [0, 0, 6, 1, 7, 0, 2, 0, 0], [0, 8, 0, 6, 0, 1, 5, 2, 0],
        [0, 0, 4, 6, 0, 7, 0, 5, 0], [0, 6, 0, 2, 0, 0, 7, 0, 0], [1, 0, 5, 8, 0, 6, 0, 9, 0]],
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      list: [1, 2, 3],
    };
  },
  methods: {
    output() {
      //console.log(this.board);
      // 读取本地文件  
      axios.get('/download')  
        .then(response => {  
          console.log(response.data);  
          // 在这里你可以处理文件数据  
        })  
        .catch(error => {  
          console.error('Error:', error);  
        });
      /*
      // POST /someUrl
      this.$http.post(window.RestfulSudoku, {
        data: this.board,
        header: { 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Access-Control-Allow-Origin': '*' },
      }).then((response) => {
        this.board = response.data.data;
      }, (response) => {
        alert(response);
      });
      */
    },
    reset() {
      // eslint-disable-next-line max-len
      this.board = [[1, 0, 2, 0, 5, 0, 7, 0, 0], [0, 6, 3, 8, 0, 5, 0, 0, 7], [7, 0, 1, 0, 0, 4, 3, 9, 0],
        [0, 4, 0, 0, 6, 9, 0, 8, 0], [0, 0, 6, 1, 7, 0, 2, 0, 0], [0, 8, 0, 6, 0, 1, 5, 2, 0],
        [0, 0, 4, 6, 0, 7, 0, 5, 0], [0, 6, 0, 2, 0, 0, 7, 0, 0], [1, 0, 5, 8, 0, 6, 0, 9, 0]];
    },
    inputChange($event, i, j) {
      const value = Number($event.target.value);
      if (isNaN(value)) {
        this.$set(this.board[i], j, '');
      } else if ((value < 10) && (value > 0)) {
        this.$set(this.board[i], j, value);
      } else {
        // eslint-disable-next-line max-len
        this.$set(this.board[i], j, Number(String(value).substring(String(value).length - 1, String(value).length)));
      }
    },
  },
};
</script>

<style>
#app {
}

.game-board{
  display: grid;
  grid-template-columns: repeat(3, 1rem); /* 创建3个等宽的列 */  
  grid-template-rows: repeat(3, 1rem); /* 创建3个等高的行 */  

}

.game-row {
  width: 100%;
  height: 16rem;
  display: flex;
  justify-content: center;
}

.sudoku-board{
  display: grid;
  width: 16rem;
  height: 100%;
  /*
  height: 27rem;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
  border: black 1px solid;
  */

}

.board-row {
  width: 100%;
  height: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.board-grid {
  width: 1.5rem;
  height: 100%;
  text-align: center;
  font-size: 1.2rem;
  line-height: 2.8rem;
  justify-content: center;
  align-items: center;
  border: #95a8b1 1px solid;
  background-color: rgba(33, 63, 122, 0.596);
}

.selected {
  border: #42b983 1px solid;
}

.number-container {
  display: flex;
  position: absolute;
  left: 50%;
  top: 8%;
  -webkit-transform: translate(-50%);
  -moz-transform: translate(-50%);
  -ms-transform: translate(-50%);
  -o-transform: translate(-50%);
  transform: translate(-50%);
}

.select-number {
  width: 3rem;
  height: 3rem;
  border: aqua 1px solid;
  border-radius: 50%;
  text-align: center;
  line-height: 3rem;
}

.button {
  position: absolute;
  left: 85%;
  top: 50%;
  transform: translate(-50%,50%);
}

body {  
  background-image: url('./back.jpg'); /* 替换为你的背景图片路径 */  
  background-repeat: no-repeat;  
  background-size: cover; /* 背景图片填充整个页面 */  
}
</style>
