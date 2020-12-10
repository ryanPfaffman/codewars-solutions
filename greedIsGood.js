const score = (dice) => {
  const count = (string, target) => {
    let count = 0;
    for (let x in string) {
      if (string[x] === target) {
        count ++;
      }
    }
    return count;
  }

  const diceS = dice.join('');

  const moneyDigits = ['1', '5'];

  let checkArray = [];

  let points = 0;

  for (let x in diceS) {
    if (moneyDigits.includes(diceS[x])) {
      let countMoney = count(diceS, diceS[x]);
      if (countMoney >= 3 && checkArray.includes(diceS[x]) === false) {
        if (diceS[x] === '1') {
          points += 1000 + (100 * (countMoney % 3))
        } else {
          points += 500 + (50 * (countMoney % 3))
        }
        checkArray.push(diceS[x]);
      } else if (countMoney < 3 && checkArray.includes(diceS[x]) === false) {
        if (diceS[x] === "1") {
          points += 100 * countMoney;
        } else {
          points += 50 * countMoney;
        }
        checkArray.push(diceS[x]);
      }
    } else {
      let countOther = count(diceS, diceS[x]);
      if (countOther >= 3 && checkArray.includes(diceS[x]) === false) {
        points += parseInt(diceS[x]) * 100;
        checkArray.push(diceS[x]);
      }
    }
  }
  return points;
}
