namespace AdventOfCode
{
    public class Common
    {
        public static string GetInputPuzzleFilename(string year, string day)
        {
            return $"../_Input/{year}-{day}.txt";
        }
        public static string GetPuzzleSolutionString(string year, string day, string part, string result)
        {
            return $"AoC++ {year} Day {day} Part {part} Solution = {result}";
        }
    }
}