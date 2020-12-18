using System;
using System.Collections.Generic;

/*
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
*/

public class Generic
{
  public string SubArrayString(string[] sLst, int beginning, int end)
  { 
    List<string> list = new List<string>();
    
    for (int x = 0; x <= sLst.Length - 1; x++)
    {
      if (x >= beginning && x <= end)
      {
        list.Add(sLst[x]);
      }
    }
    
    return String.Join("", list);
  }
}

public class LongestConsecutives 
{
    public static String LongestConsec(string[] strarr, int k) 
    {
        // your code
      
      Generic gen = new Generic();
      
      string returnS = "";
      int c = strarr.Length - 1;
      
      int kCheck = strarr.Length;
      
      if (k > kCheck || k <= 0)
      {
        return "";
      }
      
      int end = k - 1;
      
      float longestLen = Single.NegativeInfinity;
      
      for (int x = 0; x <= c; x++)
      {
        string tempS = gen.SubArrayString(strarr, x, end);
        int tempSLen = tempS.Length;
        
        if (tempSLen > longestLen)
        {
          longestLen = tempSLen;
          returnS = tempS;
        }
        end ++;
      }
      return returnS;
    }
}
