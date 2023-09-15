#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 1 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let c = 0; c < this.width; c++) line += 'X';
      console.log(line);
    }
  }
};
