using System.Reflection;

namespace AdventOfCode
{
    public class _2022_01_2
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
            string[] items = File.ReadAllText(Common.GetInputPuzzleFilename(year, day)).Split("\n");
            int[] elves = new int[] {};
            int total = 0;
            foreach (var item in items)
            {
                bool isNumeric = int.TryParse(item, out _);
                if (isNumeric)
                {
                    total += Int32.Parse(item);
                } else {
                    elves = elves.Concat(new int[] {total}).ToArray();
                    total = 0;
                }
            }
            Array.Sort(elves);
            string result = (elves[elves.Length-1]+elves[elves.Length-2]+elves[elves.Length-3]).ToString();
            Console.WriteLine(Common.GetPuzzleSolutionString(year, day, part, result));
        }
    }
}