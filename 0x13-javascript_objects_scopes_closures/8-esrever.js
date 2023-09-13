#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];

  for (let i = 0; i < list.length; i++) {
    revList[list.length - i - 1] = list[i];
  }

  return revList;
};
