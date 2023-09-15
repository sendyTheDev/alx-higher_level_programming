#!/usr/bin/node

const SquareSuperClass = require('./5-square');

module.exports = class Square extends SquareSuperClass {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
	for (let j = 0; j < this.width; j++) line += c;
        console.log(line);
      }
    } else {
      this.print();
    }
  }
};
