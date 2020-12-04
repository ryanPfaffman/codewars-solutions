const isInteresting = (number, awesomePhrases) => {
  let numberL = [];
  let numberL1 = [];
  let numberL2 = [];
  const number1 = number + 1;
  const number2 = number + 2;

  const numberS = number.toString();
  const numberS1 = number1.toString();
  const numberS2 = number2.toString();

  const isPalindrome = (array) => {
    if (array.length < 3) {
      return false;
    }
    let y = array.length - 1;
    for (let x = 0; x <= array.length - 1; x++) {
      if (array[x] != array[y]) {
        return false;
        break;
      }
      y -= 1;
    }
    return true;
  }

  const isSequentialI = (array) => {
    if (array.length < 3) {
      return false;
    }
    const testArray = [1,2,3,4,5,6,7,8,9,0];
    let checkValue1 = 0;
    let checkValue2 = 0;
    let checkValue3 = 0;

    let checkValue = testArray.indexOf(array[0]);
    console.log(checkValue);

    for (let x = 1; x <= array.length - 1; x++) {
      let tempCheck = testArray.indexOf(array[x]);
      if (tempCheck === checkValue + 1) {
        checkValue = tempCheck
      } else {
        return false;
        break;
      }
    }
    return true;
}

  const isSequentialD = (array) => {
    if (array.length < 3) {
      return false;
    }
    const testArray = [9,8,7,6,5,4,3,2,1,0]

    let checkValue = testArray.indexOf(array[0]);
    console.log(checkValue)

    for (let x = 1; x <= array.length - 1; x++) {
      let tempCheck = testArray.indexOf(array[x]);
      if (tempCheck === checkValue + 1) {
        checkValue = tempCheck
      } else {
        return false;
        break;
      }
    }
    return true;
  }

  const isSame = (array) => {
    if (array.length < 3) {
      return false;
    }
    let checker = array[0];

    for (let x in array) {
      if (array[x] != checker) {
        return false;
        break;
      }
    }
    return true;
  }

  for (let x = 0; x <= numberS.length - 1; x++) {
    numberL.push(parseInt(numberS[x]));
    numberL1.push(parseInt(numberS1[x]));
    numberL2.push(parseInt(numberS2[x]));
  }

  console.log(numberL);
  console.log(numberL1);
  console.log(numberL2);

  if (number < 98) {
    return 0;
  } else if (numberS.slice(-2) === "00") {
    return 2;
  } else if (numberS.length <= 1) {
    return 0;
  } else if (isPalindrome(numberL)) {
    return 2;
  } else if (isSequentialI(numberL)) {
    return 2;
  } else if (isSequentialD(numberL)) {
    return 2;
  } else if (isSame(numberL)) {
    return 2;
  } else if (awesomePhrases.includes(number)) {
    return 2;
  } else if (numberS1.slice(-2) === "00" || numberS2.slice(-2) === "00") {
    return 1;
  } else if (isPalindrome(numberL1) || isPalindrome(numberL2)) {
    return 1;
  } else if (isSequentialI(numberL1) || isSequentialI(numberL2)) {
    return 1;
  } else if (isSequentialD(numberL1) || isSequentialD(numberL2)) {
    return 1;
  } else if (isSame(numberL1) || isSame(numberL2)) {
    return 1;
  } else if (awesomePhrases.includes(number1) || awesomePhrases.includes(number2)) {
    return 1;
  } else {
    return 0
  }
}
