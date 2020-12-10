const primeFactors = (n) => {
  let primeFactorization = 1;
  let denominator = 2;
  let count = 0;

  let numToDivide = n;

  let returnS = '';

  while (primeFactorization != n) {
    if (numToDivide % denominator === 0) {
      numToDivide /= denominator;
      primeFactorization *= denominator;
      count ++;
    } else {
      returnS += count ? "(" + (count > 1 ? + denominator + "**" + count + ")": + denominator + ")") : "";
      count = 0;
      denominator ++;
    }
  }
  returnS += count ? "(" + (count > 1 ? + denominator + "**" + count + ")": + denominator + ")") : ""

  return returnS;
}

/*
My first solution was finding the answers, but I couldn't get it to pass because
it was running too long.
My first solution:
const primeFactors = (n) => {
  const isItAPrimeNumber = (n) => {
    for (let x = 2; x < parseInt(n / 2); x++) {
      if (n % x === 0) {
        return false;
        break;
      }
    }
    return true;
  }

  const findNextDenominator = (n, numToDivide) => {
    let returnN = n + 1;
    let boolean = isItAPrimeNumber(returnN)
    while (boolean === false || numToDivide % returnN != 0) {
      returnN += 1;
      boolean = isItAPrimeNumber(returnN);
    }
    return returnN
  }

  let primeFactorization = 1;
  let denominator = 2;
  let count = 0;

  let numToDivide = n;

  let returnS = '';

  while (primeFactorization != n) {
    if (numToDivide % denominator === 0) {
      numToDivide /= denominator;
      primeFactorization *= denominator;
      count += 1;
    } else {
      if (count > 1) {
        returnS += "(" + denominator + "**" + count + ")";
      } else if (count === 1) {
        returnS += "(" + denominator + ")";
      }
      count = 0;
      denominator = findNextDenominator(denominator, numToDivide);
    }
  }
  if (count > 1) {
    returnS += "(" + denominator + "**" + count + ")";
  } else if (count === 1) {
    returnS += "(" + denominator + ")";
  }
  return returnS;
}

So eventually, I gave up, and I found this solution:

const primeFactors = (n) => {
  let returnS = '';
  let count = 0;

  for (let i = 2; i <= n; i++) {
    count = 0;
    while (n % i === 0) {
      count++;
      n /= i;
    }
    returnS += count ? "(" + (count > 1 ? i + "**" + count + ")" : i + ")") : "";
  }

  return returnS || "(" + n + ")";
}

That solution told me that I didn't actually have to check for the prime numbers,
and I could just count the denominator up by 1. I guess it works due to some-
thing in the way that prime number work.
Also, I got some practice with ternary operators, which are actually awesome.
*/
