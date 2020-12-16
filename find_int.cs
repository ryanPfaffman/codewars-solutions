public static int find_it(int[] seq)
        {
            var groups = seq.GroupBy(x => x);

            int returnVal = 0;

            foreach (var value in groups)
            {
                if (value.Count() % 2 != 0)
                {
                    returnVal = value.Key;
                }
            }
            return returnVal;
        }
