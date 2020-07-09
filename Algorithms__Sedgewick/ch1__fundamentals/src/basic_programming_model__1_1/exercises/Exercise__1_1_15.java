/*
    Exercise 1.1.15
    ---------------
    Write a static method histogram() that takes an array a[]
    of int values and an integer M as argument and returns
    an array of length M whose ith entry is the number
    of times integer i appeared in the argument array.
    If the values in a[] are all between 0 and M - 1,
    the sum of values in returned array should be
    equal to a.length.
 */

package basic_programming_model__1_1.exercises;


public class Exercise__1_1_15 {
    public static int[] histogram(int[] a, int M) {
        int[] N = new int[M];

        for (int i = 0; i < N.length; i++)
            N[i] = 0;

        for (int value : a) {
            if (value < N.length)
                N[value] += 1;
        }

        return N;
    }
}
