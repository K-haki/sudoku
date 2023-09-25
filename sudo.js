// 读取数独题目文件
fetch('shudu.txt')
  .then(response => response.text())
  .then(puzzleData => {
    // 解析数独题目数据
    const puzzles = parseSudokuData(puzzleData);

    // 读取数独答案文件
    fetch('solution.txt')
      .then(response => response.text())
      .then(answerData => {
        // 解析数独答案数据
        const answers = parseSudokuData(answerData);

        // 进行数独游戏相关的处理
        handleSudokuGame(puzzles, answers);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  })
  .catch(error => {
    console.error('Error:', error);
  });

// 解析数独题目和答案数据
function parseSudokuData(data) {
  const puzzles = [];
  const lines = data.trim().split('\n\n'); // 使用空行分隔题目
  for (let i = 0; i < lines.length; i++) {
    const puzzleData = lines[i].split('\n');
    const puzzle = puzzleData.map(row => row.trim().split(' '));
    puzzles.push(puzzle);
  }
  return puzzles;
}

// 生成一个数独格子
function generateSudokuCell(value) {
  const cell = document.createElement('input');
  cell.className = 'sudoku-cell';
  cell.type = 'text';
  cell.maxLength = 1;
  cell.size = 1;
  cell.value = value === '0' ? '' : value;
  cell.addEventListener('input', handleCellInput);
  return cell;
}

// 处理数独格子的输入事件
function handleCellInput(event) {
  const input = event.target;
  const value = input.value;

  if (value !== '') {
    const intValue = parseInt(value, 10);
    if (isNaN(intValue) || intValue < 1 || intValue > 9) {
      input.value = '';
    }
  }
}

// 进行数独游戏相关的处理
function handleSudokuGame(puzzles, answers) {
  const gameContainer = document.getElementById('game-container');

  for (let i = 0; i < 9; i++) {
    const puzzle = puzzles[i];
    const answer = answers[i];

    const gameWrapper = document.createElement('div');
    gameWrapper.className = 'game-wrapper';

    const puzzleHeading = document.createElement('h2');
    puzzleHeading.textContent = `Puzzle ${i + 1}`;
    gameWrapper.appendChild(puzzleHeading);

    const sudokuBoard = generateSudokuBoard(puzzle);
    gameWrapper.appendChild(sudokuBoard);

    const checkButton = document.createElement('button');
    checkButton.textContent = 'Check';
    checkButton.addEventListener('click', () => {
      const inputs = sudokuBoard.getElementsByTagName('input');
      const userSolution = [];

      for (let j = 0; j < inputs.length; j++) {
        const value = inputs[j].value.trim();
        userSolution.push(value === '' ? '0' : value);
      }

      if (validateSudokuAnswer(puzzle, userSolution)) {
        alert('Correct solution!');
      } else {
        alert('Incorrect solution!');
      }
    });

    gameWrapper.appendChild(checkButton);

    gameContainer.appendChild(gameWrapper);
  }
}

// 验证答案
function validateSudokuAnswer(puzzle, answer) {
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (puzzle[i][j] !== answer[i][j]) {
        return false;
      }
    }
  }
  return true;
}