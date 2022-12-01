using System.Reflection;

namespace AdventOfCode
{
    public class _2016_02_1
    {
        public static void Solve()
        {
            string year = "YYYY";
            string day = "DD";
            string part = "P";
            string? className = MethodBase.GetCurrentMethod()?.DeclaringType?.Name;
            if (className is not null)
            {
                year = className.Substring(1,4);
                day = className.Substring(6,2);
                part = className.Substring(9,1);
            }
            string result = "";
            string input = File.ReadAllText(Common.GetInputPuzzleFilename(year, day));
            string[] instructions = input.Split("\n");
            int[,] keypad = new int[3,3]{{1,2,3}
                                       , {4,5,6}
                                       , {7,8,9}};
            int row = 1;
            int col = 1;
            foreach (var line in instructions)
            {
                foreach (var direction in line)
                {
                    Console.WriteLine(direction);
                    if (direction.Equals("U")) {Console.WriteLine("U");}
                    if ((direction.Equals("U")) && (row > 0)) {row--;}
                    if ((direction.Equals("D")) && (row < 2)) {row++;}
                    if ((direction.Equals("L")) && (col > 0)) {col--;}
                    if ((direction.Equals("R")) && (col < 2)) {col++;}
                }
                result += Convert.ToString(keypad[row,col]);
            }
            Console.WriteLine(Common.GetPuzzleSolutionString(year, day, part, result));
        }
    }
}