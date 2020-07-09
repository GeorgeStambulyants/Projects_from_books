/*
    Exercise 1.1.14.
    ---------------
    Write a static method lg() that takes an int value N as argument and
    returns the largest int not larger than base-2 logarithm of N.
    Do not use Math.
 */
package basic_programming_model__1_1.exercises;


public class Exercise__1_1_14 {
    public static int pow(int X, int Y) {
        int result = X;
        // X >= 0 and Y >= 0
        if (X == 0)
            return 0;
        if (Y == 0)
            return 1;

        for (int i = 1; i < Y; i++) {
            result *= X;
        }

        return result;
    }

    public static int lg(int N) {
        int X = 1;
        while (Exercise__1_1_14.pow(2, X) < N) {
            X++;
        }
        return X - 1;
    }
}
