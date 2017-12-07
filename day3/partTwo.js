// GLOBALS
let spiral, i, j, currentDirection, currentValue, steps, directions;
directions = {
  right: 1,
  up: 1,
  left: 2,
  down: 2
};
spiral = [[1]];
i = j = 0;
currentDirection = "right";
currentValue = 1;

const getRightValue = () => {
  let surrounding_sum = 0;

  if (spiral[i-1]) {
    surrounding_sum = surrounding_sum +
      (spiral[i-1][j-1] ? spiral[i-1][j-1] : 0) +
      (spiral[i-1][j] ? spiral[i-1][j] : 0) +
      (spiral[i-1][j+1] ? spiral[i-1][j+1] : 0);
  }

  surrounding_sum = surrounding_sum +
    (spiral[i][j-1] ? spiral[i][j-1] : 0);

  return surrounding_sum;
};

const moveRight = () => {
  steps = directions["right"];
  while (steps > 0) {
    j += 1;
    currentValue = getRightValue();
    spiral[i].push(currentValue);
    steps -= 1;
  }
  directions["right"] += 2;
  currentDirection = "up";
};

const getUpValue = () => {
  let surrounding_sum = 0;

  if (spiral[i-1]) {
    surrounding_sum = surrounding_sum +
      (spiral[i-1][j-1] ? spiral[i-1][j-1] : 0);
  }

  if (spiral[i]) {
    surrounding_sum = surrounding_sum +
      (spiral[i][j] ? spiral[i][j] : 0) +
      (spiral[i][j-1] ? spiral[i][j-1] : 0);
  }

  if (spiral[i-2]) {
    surrounding_sum = surrounding_sum +
      (spiral[i-2][j-1] ? spiral[i-2][j-1] : 0);
  }

  return surrounding_sum;
};

const moveUp = () => {
  steps = directions["up"];
  while (steps > 0) {
    currentValue = getUpValue();
    i -= 1;
    if (spiral[i]) {
      spiral[i].push(currentValue);
    } else {
      spiral.unshift([currentValue]);
    }
    steps -= 1;
  }
  directions["up"] += 2;
  currentDirection = "left";
};

const getLeftValue = () => {
  let surrounding_sum = 0;

  return spiral[i][0] +
    (spiral[i+1][j-1] ? spiral[i+1][j-1] : 0) +
    (spiral[i+1][j-2] ? spiral[i+1][j-2] : 0) +
    (spiral[i+1][j-3] ? spiral[i+1][j-3] : 0);
};

const moveLeft = () => {
  steps = directions["left"];
  i = 0;
  j = steps;
  while (steps > 0) {
    currentValue = getLeftValue();
    j -= 1;
    spiral[i].unshift(currentValue);
    steps -= 1;
  }
  directions["left"] += 2;
  currentDirection = "down";
};

const getDownValue = () => {
  let surrounding_sum = 0;

  if (spiral[i-1]) {
    surrounding_sum = spiral[i-1][0] + spiral[i-1][1];
  }

  if (spiral[i]) {
    surrounding_sum += spiral[i][0];
  }

  if (spiral[i+1]) {
    surrounding_sum += spiral[i+1][0];
  }

  return surrounding_sum;
};

const moveDown = () => {
  steps = directions["down"];
  while (steps > 0) {
    i += 1;
    currentValue = getDownValue();
    if (spiral[i]) {
      spiral[i].unshift(currentValue);
    } else {
      spiral.push([currentValue]);
    }
    steps -= 1;
  }
  directions["down"] += 2;
  currentDirection = "right";
};

export default (data) => {
  while (currentValue < data) {
    switch (currentDirection) {
      case "right":
        moveRight();
        break;
      case "up":
        moveUp();
        break;
      case "left":
        moveLeft();
        break;
      case "down":
        moveDown();
        break;
    }
  }

  return spiral;
}
