using System;
using System.Collections.Generic;

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

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete 
the column.

Regions


A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not 
permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region.

Valid board example:


For those who don't know the game, here are some information about rules and how to play Sudoku: http://en.wikipedia.org/wiki/Sudoku and 
http://www.sudokuessentials.com/
*/

public class Sudoku
{
  public static string DoneOrNot(int[][] board)
  {
    List<int> tempL = new List<int>();
    List<int> tempL2 = new List<int>();
    List<int> tempL3 = new List<int>();
    List<int> tempL4 = new List<int>();
    List<int> tempL5 = new List<int>();
  
  
    List<int> tempL_0 = new List<int>();
    List<int> tempL_1 = new List<int>();
    List<int> tempL_2 = new List<int>();
    List<int> tempL_3 = new List<int>();
    List<int> tempL_4 = new List<int>();
    List<int> tempL_5 = new List<int>();
    List<int> tempL_6 = new List<int>();
    List<int> tempL_7 = new List<int>();
    List<int> tempL_8 = new List<int>();
  
    int beg1 = 0;
    int end1 = 2;
    int beg2 = 3;
    int end2 = 5;
    int beg3 = 6;
    int end3 = 8;
  
    int countInners = 0;
  
  
    for (int x = 0; x <= board.Length - 1; x++)
    {
      for (int y = 0; y <= board[x].Length - 1; y++)
      {
        if (String.Join("", tempL).Contains(board[x][y].ToString()))
        {
            return "Try again!";
        }
        tempL.Add(board[x][y]);

        if (y >= beg1 && y <= end1)
        {
          if (String.Join("", tempL3).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL3.Add(board[x][y]);
        }
        if (y >= beg2 && y <= end2)
        {
          if (String.Join("", tempL4).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL4.Add(board[x][y]);
        }
        if (y >= beg3 && y <= end3)
        {
          if (String.Join("", tempL5).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL5.Add(board[x][y]);
        }
        
        //checks horizontal rows
        if (y == 0)
        {
          if (String.Join("", tempL_0).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL_0.Add(board[x][y]);
        }
        else if (y == 1)
        {
          if (String.Join("", tempL_1).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL_1.Add(board[x][y]);
        }
        else if (y == 2)
        {
          if (String.Join("", tempL_2).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL_2.Add(board[x][y]);
        }
        else if (y == 3)
        {
          if (String.Join("", tempL_3).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL_3.Add(board[x][y]);
        }
        else if (y == 4)
        {
          if (String.Join("", tempL_4).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL_4.Add(board[x][y]);
        }
        else if (y == 5)
        {
          if (String.Join("", tempL_5).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL_5.Add(board[x][y]);
        }
        else if (y == 6)
        {
          if (String.Join("", tempL_6).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL_6.Add(board[x][y]);
        }
        else if (y == 7)
        {
          if (String.Join("", tempL_7).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL_7.Add(board[x][y]);
        }
        else if (y == 8)
        {
          if (String.Join("", tempL_8).Contains(board[x][y].ToString()))
          {
              return "Try again!";
          }
          tempL_8.Add(board[x][y]);
        }
      }
      tempL.Clear();
      countInners++;
      if (countInners == 3)
      {
          countInners = 0;
          tempL3.Clear();
          tempL4.Clear();
          tempL5.Clear();

      }
    }
    return "Finished!";
  }
}
