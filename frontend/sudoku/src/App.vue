<template>
  <div id="app">
<!--    <div class="number-container">-->
<!--      <div class="select-number" v-for="(number,i) in numbers">{{number}}</div>-->
<!--    </div>-->
    <el-loading fullscreen class="my-loading"></el-loading> 
    <el-input v-model="timer" readonly></el-input>
    <div calss="game-board">
      <div v-for="ii of list" class="game-row">
        <div v-for="item of list" class="sudoku-board">
          {{  "数独" + (item + (ii - 1) * 3 - 1) }}
          <div v-for="(row,i) in responseData[item + (ii - 1) * 3 - 1]" class="board-row">
            <input v-for="(grid,j) in row" class="board-grid" :value="grid" @input="inputChange($event,i,j,(item + (ii - 1) * 3 - 1))"/>
          </div>
        </div>
      </div>
    </div>
    <button class="button" style="top: 40%;" @click="output">新的游戏</button>
    <el-select style="position: absolute;left:80%;top: 52%;" v-model="value1" multiple placeholder="请选择：数独号，行，列" clearable="true">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    <button style="top: 20%;" class="button" @click="b_solve">并发求解</button>
    <button style="top: 60%;" class="button" @click="tips">提示</button>
    <button style="top: 70%;" class="button" @click="hand_in">提交</button>
    <button style="top: 80%;" class="button" @click="look_ans">查看答案</button>
    <!--    <button style="top: 35%;" class="button" @click="reset">难度选择</button>-->

      <div class="dropdown-container">
        <!--    <label for="fruit">选择难度：</label>-->
        <select id="difficulty" v-model="selecteddiff" class="dropdown">
          <option value="none">难度选择</option>
          <option value="easy">Easy</option>
          <option value="medium">Middle</option>
          <option value="hard">Difficult</option>
        </select>
        <!--    <p>你选择的难度是：{{ selecteddiff }}</p>-->
      </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'app',
  components: {
  },
  data() {
    return {
      responseData: '',
      responsetip: [],
      response_solve: [],
      board: [[[]]],
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      list: [1, 2, 3],
      selecteddiff: '', // 绑定选中的难度
      timer: 0,  
      intervalId: null,
      value1: [],
      t0: '',
      t1: '',
      t2: '',
      value2: [],
      options: [{
          value: '1',
          label: '1'
        }, {
          value: '2',
          label: '2'
        }, {
          value: '3',
          label: '3'
        }, {
          value: '4',
          label: '4'
        }, {
          value: '5',
          label: '5'
        }, {
          value: '6',
          label: '6'
        }, {
          value: '7',
          label: '7'
        }, {
          value: '8',
          label: '8'
        }, {
          value: '9',
          label: '9'
        }],
    };
  },
  created (){
    this.openFullScreen();
  },
  methods: {
    output() {
      if (this.selecteddiff == 'none') {
        this.$alert('请选择难度！否则无法开始游戏！', '警告！小朋友要听话哟！', {
          confirmButtonText: '好嘞',
        });
      } else {
          axios.get('http://127.0.0.1:5000/data', {
            params: {
              difficulty: this.selecteddiff
            }
          })
          .then(response => {
            this.responseData = response.data;
            //console.log(response.data); // 打印到控制台
            for (let i = 0; i < 9; i++){
              this.board[i] = this.responseData[i];
            }
            this.timer = 0;
            this.startTimer();
            //this.board = response.data;
          })
          .catch(error => {
            console.error('Error:', error);
          });
        }
    },
    judge() {
      if(this.responseData == this.board) {
        this.$alert(' 您的解题用时为：' + this.timer + 's', '恭喜你，答对了！', {
          confirmButtonText: '好嘞',
        });
      } else {
        this.$alert('您的解题用时为：' + this.timer + 's', '很遗憾，答错了！', {
          confirmButtonText: '好嘞',
        });
      }
      for (let i = 0; i < 9; i++){
        this.board[i] = this.responseData[i];
      }
    },
    look_ans() {
      this.$alert('您的解题用时为：' + this.timer + 's' + '\n但是你没解出来（嘲笑！）', '偷看答案是吧！逮到你了', {
        confirmButtonText: '好嘞',
      });
      this.stopTimer();
      axios.get('http://127.0.0.1:5000/solution')
      .then(response => {
        this.responseData = response.data;
        for (let i = 0; i < 9; i++){
          this.board[i] = this.responseData[i];
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    b_solve() {
      this.$alert('正在为您并发求解数独，请稍等...', {
        confirmButtonText: '好嘞',
      });
      this.stopTimer();
      axios.get('http://127.0.0.1:5000/solve')
      .then(response => {
        this.responseData = response.data;
        this.$alert('已经成功求解数独，请查看！', {
          confirmButtonText: '好嘞',
        });
        for (let i = 0; i < 9; i++){
          this.board[i] = this.responseData[i];
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    get_ans() {
      axios.get('http://127.0.0.1:5000/solution')
      .then(response => {
        this.responseData = response.data;
        this.judge();
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    hand_in() {
      this.stopTimer();
      for (let num = 0; num < 9; num++){
        for (let i = 0; i < 9; i++){
          for (let j = 0; j < 9; j++){
            if (this.board[num][i][j] == ''){
              this.$alert('请填写完整后再提交！', '警告！小朋友要听话哟！', {
                confirmButtonText: '好嘞',
              });
              this.startTimer();
              return;
            }
          }
        }
      }
      this.get_ans();
    },
    inputChange($event, i, j, num) {
      const value = Number($event.target.value);
      if (isNaN(value)) {
        this.$set(this.board[num][i], j, '');
        this.$alert('请输入1-9中的某个数字！', '警告！小朋友要听话哟！', {
          confirmButtonText: '好嘞',
        });
      } else if (value == 0) {
        this.$set(this.board[num][i], j, '');
        this.$alert('请输入1-9中的某个数字！', '警告！小朋友要听话哟！', {
          confirmButtonText: '好嘞',
        });
      } else if ((value < 10) && (value > 0)) {
        this.$set(this.board[num][i], j, value);
      } else {
        // eslint-disable-next-line max-len
        this.$set(this.board[num][i], j, Number(String(value).substring(String(value).length - 1, String(value).length)));
      }
    },
    tips() {
      this.t0 = this.value1[0]
      this.t1 = this.value1[0]
      this.t2 = this.value1[0]
      axios.get('http://127.0.0.1:5000/solution')
      .then(response => {
        this.responsetip = response.data;
        this.$alert('你所选位置的提示：' + this.responsetip[this.t0][this.t1][this.t2], '偷偷告诉你', {
        confirmButtonText: '好嘞',
      });
      })
      .catch(error => {
        console.error('Error:', error);
      });
      
    },
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
    },
    openFullScreen() {
      const loading = this.$loading({
        lock: true,
        text: 'Hk 和 Chen 正在赶来为你打开数独游戏哦！请稍等片刻......',
        spinner: 'el-icon-loading',
        background: 'rgba(255, 255, 255, 1)',
        customClass: 'my-loading'
      });
      setTimeout(() => {
        loading.close();
      }, 1000);
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
  left: 90%;
  top: 50%;
  transform: translate(-50%,50%);
}

body {  
  background-image: url('./back.jpg'); /* 替换为你的背景图片路径 */  
  background-repeat: no-repeat;  
  background-size: cover; /* 背景图片填充整个页面 */  
}

.dropdown-container {
  position: absolute;
  left: 90%;
  top: 30%;
  transform: translate(-50%,50%);
  
}

.dropdown {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(88, 87, 87, 0.596);
}

.my-loading {  
  /* 设置背景图片 */  
  background-image: url('./loading.gif');  
  
  /* 设置背景图片大小 */  
  background-size: 70px 70px;  
  
  /* 设置背景图片位置 */  
  background-position: 50.5% 220px;
  background-repeat: no-repeat;
}
</style>
