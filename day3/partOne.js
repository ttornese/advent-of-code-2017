const findClosestPerfectSquare = (input, increment) => {
  while (true) {
    let squareRoot = Math.sqrt(input);
    if (squareRoot % 1 == 0 && squareRoot % 2 != 0) {
      return input;
    }
    input = increment ? input + 1 : input - 1;
  }
};

const findManhattanDistance = (input) => {
  if (Math.sqrt(input) % 1 == 0) {
    return Math.sqrt(input) - 1;
  } else {
    const smallerSquare = findClosestPerfectSquare(input, false)
    const largerSquare = findClosestPerfectSquare(input, true)
    return Math.min(input - smallerSquare, largerSquare - input);
  }
};

export default (input) => {
  return findManhattanDistance(input);
};
