using System;
using System.Collections.Generic;

public static class Kata
{
  public static bool IsPangram(string str)
  {
      string[] letters = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" };

      List<string> lettersList = new List<string>(letters);

      for (int x = 0; x <= str.Length - 1; x++)
      {
          string tempS = Convert.ToString(str[x]).ToLower();
        
          if (string.Join("", lettersList).Contains(tempS))
          {
              lettersList.Remove(tempS);
          }
      }

      if (lettersList.Count == 0)
      {
          return true;
      } else
      {
          return false;
      }

   }
}
