using System;

/*
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
*/

public class Generic
{
  public string getText(int x)
    {
      return String.Format("{0:00}", x);
    }
}

public static class TimeFormat
{
    
    public static string GetReadableTime(int seconds)
    {
      Generic gen = new Generic();
      
      double x = seconds / 60.0 / 60.0;
      int hrs = (int)Math.Floor(x);
      
      x = seconds / 60.0;
      int min = (int)Math.Floor(x - (hrs * 60));

      int sec = (int)Math.Round((x - Math.Floor(x)) * 60);
      
      return $"{gen.getText(hrs)}:{gen.getText(min)}:{gen.getText(sec)}";
    }
}
