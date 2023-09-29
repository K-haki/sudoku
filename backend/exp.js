const express = require('express');  
const app = express();  
const path = require('path');  
const fs = require('fs');  
  
// 定义路由  
app.get('/download', (req, res) => {  
  const file1 = `${__dirname}/shudu.txt`;  
  const file2 = `${__dirname}/solution.txt`;  
  
  // 检查文件是否存在  
  fs.access(file1, fs.constants.F_OK, (err) => {  
    if (err) {  
      console.error('文件不存在:', file1);  
      res.status(404).send('文件不存在');  
      return;  
    }  
  
    fs.access(file2, fs.constants.F_OK, (err) => {  
      if (err) {  
        console.error('文件不存在:', file2);  
        res.status(404).send('文件不存在');  
        return;  
      }  
  
      // 设置响应头，指定文件名和内容类型  
      res.setHeader('Content-Disposition', 'attachment; filename=file1.txt');  
      res.setHeader('Content-Type', 'text/plain');  
  
      // 创建可读流并将文件内容发送到响应  
      const stream1 = fs.createReadStream(file1);  
      stream1.pipe(res);  
  
      // 下载完第一个文件后，开始下载第二个文件  
      stream1.on('end', () => {  
        res.setHeader('Content-Disposition', 'attachment; filename=file2.txt');  
        res.setHeader('Content-Type', 'text/plain');  
  
        const stream2 = fs.createReadStream(file2);  
        stream2.pipe(res);  
      });  
    });  
  });  
});  
  
// 启动服务器  
app.listen(3000, () => {  
  console.log('服务器已启动，监听端口 3000');  
});