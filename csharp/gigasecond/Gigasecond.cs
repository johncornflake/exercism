using System;

public static class Gigasecond
{
    public static DateTime Add(DateTime moment)
    {
        return moment.AddSeconds(System.Math.Pow(10.00, 9.00));
    }
}
