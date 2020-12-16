using System;
using System.Linq;
/*
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
*/

namespace Solution
{
  public class GenericStuff
    {
        public int Count(int[] seq, int target)
        {
            int total = 0;

            for (int x = 0; x <= seq.Length - 1; x++)
            {
                if (seq[x] == target)
                {
                    total++;
                }
            }

            return total;
        }
    }
  
  class Kata
    {
    
    public static int find_it(int[] seq) 
      {
      
      int returnValue = 0;
      
      GenericStuff gen = new GenericStuff();
      
      for (int x = 0; x <= seq.Length - 1; x++) {
        if (gen.Count(seq, seq[x]) % 2 != 0) {
          returnValue = seq[x];
          return returnValue;
          }
        }
      return returnValue;
      }
    }
}
// time taken: 2205 ms;
/*

 public static int find_it(int[] seq)
    {
        return seq.ToList()
                  .GroupBy(x => x) //Group by each element in the array
                  .Where(x => (x.Count() % 2) != 0) //Find grouped odd numbers
                  .Select(x => x.First())
                  .FirstOrDefault(); //since array will only contain 1 odd number, get first one
      }
       
    }

^^^ 
Time taken: 2440 ms;

First, and Where, and Select -- all new to me.

First pulls out the first element in a sequence. There can be conditions written in to the First method. All of this is mad to be readable,
but I think it is the same as seq.ToList().GroupBy(x => x).Where(x => (x.Count() % 2 != 0).Select(x => x.First()).FirstOrDefault();

Where - Filters a sequence of values based on a predicate (x). Each element's index is used in the logic of the predicate function.
*/
