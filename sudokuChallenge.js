/*
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

Rows:


There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers 
in any row. In other words, there can not be any rows that are identical.

In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in 
to complete the row.

Columns:


There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. 
Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the 
column.

Regions


A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not 
permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region.

Valid board example:


For those who don't know the game, here are some information about rules and how to play Sudoku: http://en.wikipedia.org/wiki/Sudoku and 
http://www.sudokuessentials.com/
*/

const doneOrNot = (board) => {
  //your code here
  let tempL = [];
  let tempL2 = [];
  let tempL3 = [];
  let tempL4 = [];
  let tempL5 = [];
  
  let tempL_0 = [];
  let tempL_1 = [];
  let tempL_2 = [];
  let tempL_3 = [];
  let tempL_4 = [];
  let tempL_5 = [];
  let tempL_6 = [];
  let tempL_7 = [];
  let tempL_8 = [];
  
  
  let beg1 = 0;
  let end1 = 2;
  let beg2 = 3;
  let end2 = 5;
  let beg3 = 6;
  let end3 = 8;
  
  let countInners = 0;
  
  for (let row in board) {
    for (let x in board[row]) {
      //checks vertical rows
      if (tempL.includes(board[row][x])) {
        return "Try again!";
      }
      tempL.push(board[row][x]);
      
      //checks 3x3 regions
      if (x >= beg1 && x <= end1) {
        if (tempL3.includes(board[row][x])) {
          return "Try again!";
        }
        tempL3.push(board[row][x]);
      }
      if (x >= beg2 && x <= end2) {
        if (tempL4.includes(board[row][x])) {
          return "Try again!";
        }
        tempL4.push(board[row][x]);
      }
      if (x >= beg3 && x <= end3) {
        if (tempL5.includes(board[row][x])) {
          return "Try again!";
        }
        tempL5.push(board[row][x]);
      }
      
      //checks horizontal rows
      if (x == 0) {
        if (tempL_0.includes(board[row][x])) {
          return "Try again!";
        }
        tempL_0.push(board[row][x]);
      } else if (x == 1) {
        if (tempL_1.includes(board[row][x])) {
          return "Try again!";
        }
        tempL_1.push(board[row][x]);
      } else if (x == 2) {
        if (tempL_2.includes(board[row][x])) {
          return "Try again!";
        }
        tempL_2.push(board[row][x]);
      } else if (x == 3) {
        if (tempL_3.includes(board[row][x])) {
          return "Try again!";
        }
        tempL_3.push(board[row][x]);
      } else if (x == 4) {
        if (tempL_4.includes(board[row][x])) {
          return "Try again!";
        }
        tempL_4.push(board[row][x]);
      } else if (x == 5) {
        if (tempL_5.includes(board[row][x])) {
          return "Try again!";
        }
        tempL_5.push(board[row][x]);
      } else if (x == 6) {
        if (tempL_6.includes(board[row][x])) {
          return "Try again!";
        }
        tempL_6.push(board[row][x]);
      } else if (x == 7) {
        if (tempL_7.includes(board[row][x])) {
          return "Try again!";
        }
        tempL_7.push(board[row][x]);
      } else if (x == 8) {
        if (tempL_8.includes(board[row][x])) {
          return "Try again!";
        }
        tempL_8.push(board[row][x]);
      }
    }
    tempL = [];
    countInners++;
    if (countInners == 3) {
      countInners = 0;
      tempL3 = [];
      tempL4 = [];
      tempL5 = [];
    }
  }
  
  return "Finished!"
}
