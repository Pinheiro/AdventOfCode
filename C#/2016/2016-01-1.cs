using System.Numerics;
using System.Reflection;

namespace AdventOfCode
{
    public class _2016_01_1
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
            string input = File.ReadAllText(Common.GetInputPuzzleFilename(year, day));
            string[] sequence = input.Split(", ");
            Complex position = new Complex(0, 0);
            Complex direction = new Complex(0, 1);
            Complex turn_left = new Complex(0, 1);
            Complex turn_right = new Complex(0, -1);
            foreach (var step in sequence)
            {
                if (step.Substring(0, 1) == "L") 
                    direction *= turn_left;
                else 
                direction *= turn_right;
                for (int i = 0; i < Int32.Parse(step.Substring(1, step.Length - 1)); i++) 
                    position += direction;
            }
            string result = Convert.ToString(Math.Abs(position.Real) + Math.Abs(position.Imaginary));
            Console.WriteLine(Common.GetPuzzleSolutionString(year, day, part, result));
        }
    }
}