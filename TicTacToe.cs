public class Solution {
    public string Tictactoe(int[][] moves)
    {
        //even odd checker
        //check grid for completion
        //if x is even then A
        //if x in odd then B
        //if over then
        //1,4,7
        //2,5,8
        //3,6,9
        //1,2,3
        //4,5,6
        //7,8,9
        //1,5,9
        Dictionary<int, string> checkerD = new Dictionary<int, string>();
        checkerD.Add(1,"C");
        checkerD.Add(2,"D");
        checkerD.Add(3,"E");
        checkerD.Add(4,"F");
        checkerD.Add(5,"G");
        checkerD.Add(6,"H");
        checkerD.Add(7,"I");
        checkerD.Add(8,"J");
        checkerD.Add(9,"K");

        Dictionary<string, int> testD = new Dictionary<string, int>();
        testD.Add("0,0", 1);
        testD.Add("0,1", 2);
        testD.Add("0,2", 3);
        testD.Add("1,0", 4);
        testD.Add("1,1", 5);
        testD.Add("1,2", 6);
        testD.Add("2,0", 7);
        testD.Add("2,1", 8);
        testD.Add("2,2", 9);

        for (int x = 0; x < moves.Length; x++)
        {
            if (x % 2 == 0)
            {
                //A
                checkerD[testD[String.Join(",", moves[x])]] = "A";
            } else
            {
                //B
                checkerD[testD[String.Join(",", moves[x])]] = "B";
            }

            if (isGameOver(checkerD))
            {
                if (x % 2 == 0)
                {
                    return "A";
                } else
                {
                    return "B";
                }
            }

            //Console.WriteLine(String.Join(",", checkerD));
        }

        if (moves.Length == 9)
        {
            return "Draw";
        } else
        {
            return "Pending";
        }

        //Console.WriteLine(isGameOver(checkerD));

        return "";
    }

    public static bool isGameOver(Dictionary<int, string> checkDic)
    {
        //1,4,7
        //2,5,8
        //3,6,9
        //1,2,3
        //4,5,6
        //7,8,9
        //1,5,9
        if ((checkDic[1] == checkDic[4]) && (checkDic[4] == checkDic[7]))
        {
            return true;
        } else if ((checkDic[2] == checkDic[5]) && (checkDic[5] == checkDic[8]))
        {
            return true;
        } else if ((checkDic[3] == checkDic[6]) && (checkDic[6] == checkDic[9]))
        {
            return true;
        } else if ((checkDic[1] == checkDic[2]) && (checkDic[2] == checkDic[3]))
        {
            return true;
        } else if ((checkDic[4] == checkDic[5]) && (checkDic[5] == checkDic[6]))
        {
            return true;
        } else if ((checkDic[7] == checkDic[8]) && (checkDic[8] == checkDic[9]))
        {
            return true;
        } else if ((checkDic[1] == checkDic[5]) && (checkDic[5] == checkDic[9]))
        {
            return true;
        } else if ((checkDic[3] == checkDic[5]) && (checkDic[5] == checkDic[7]))
        {
            return true;
        } else
        {
            return false;
        }

        //return false;
    }
}
