const maxSequence = (arr) => {
  if (arr.length === 0) {
    return 0;
  }

  const getMax = (list) => {
    let total = 0;
    for (let x in list) {
      total += list[x];
    }
    return total
  }

  const getSubArraysOfIndex = (list, index) => {
    let tempL = [];
    let tempTotal = 0;
    let returnTotal = Number.NEGATIVE_INFINITY;

    for (let x = index; x < list.length; x++) {
      let count = x;
      while (count < list.length) {
        tempTotal = getMax(list.slice(x, count + 1))
        if (tempTotal > returnTotal) {
          returnTotal = tempTotal
        }
        tempTotal = 0
        count += 1
      }
    }
    return returnTotal
  }

  let listOfSubArrays = [];

  let count = 0;
  let tempTotal = 0;
  let returnTotal = Number.NEGATIVE_INFINITY

  while (count < arr.length) {
    tempTotal = getSubArraysOfIndex(arr, count)
    if (tempTotal > returnTotal) {
      returnTotal = tempTotal;
    }
    tempTotal = 0;
    count += 1
  }

  if (returnTotal < 0) {
    return 0
  } else {
    return returnTotal
  }
}
