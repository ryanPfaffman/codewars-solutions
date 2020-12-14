using System;
using System.Collections.Generic;

/*
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
*/

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
