﻿using System;

public static class ResistorColor
{
    public static int ColorCode(string color)
    {
        return Colors(color);
    }

    public static string[] Colors(string color)
    {

        enum Color
        {
            Black = 0,
            Brown = 1,
            Red = 2,
            Orange = 3,
            Yellow = 4,
            Green = 5,
            Blue = 6,
            Violet = 7,
            Grey = 8,
            White = 9
        };
        return Color.color;
    }
}
