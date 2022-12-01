using System.Reflection;

namespace AdventOfCode
{
    public class _2022_00_0
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
            Console.WriteLine(input);
            
            Console.WriteLine(Common.GetPuzzleSolutionString(year, day, part, result));
        }
    }
}