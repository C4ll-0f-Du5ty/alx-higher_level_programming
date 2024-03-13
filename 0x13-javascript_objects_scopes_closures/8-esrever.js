#!/usr/bin/node
exports.esrever = function (list) {
  const k = list.length;
  for (let i = 0; i < k / 2; i++) {
    if (i === (k - 1 - i)) {
      break;
    }
    const c = list[i];
    list[i] = list[k - 1 - i];
    list[k - 1 - i] = c;
  }
  return list;
};
