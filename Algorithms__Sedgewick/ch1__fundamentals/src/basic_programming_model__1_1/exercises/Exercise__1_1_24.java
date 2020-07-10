/*
    Exercise 1.1.25
    ---------------
    Give the sequence of values of p and q that are computed
    when Euclid'd algorithm is used to compute the greatest
    common divisor of 105 and 24. Extend the code given on
    page 4 to develop a program Euclid that takes two
    integers from the command line and computes their
    greatest common divisor, printing out the two
    argument for each call on the recursive method. Use program
    to compute the greatest common divisor of 1111111 and 1234567
 */

package basic_programming_model__1_1.exercises;

import edu.princeton.cs.algs4.StdOut;


public class Exercise__1_1_24 {
    public static int gcd(int p, int q) {
        StdOut.println("p: " + p + " q: " + q);

        if (q == 0) {
            StdOut.print("Result: ");
            return p;
        }
        int r = p % q;
        return gcd(q, r);
    }

    public static void main(String[] args) {
        int p = Integer.parseInt(args[0]);
        int q = Integer.parseInt(args[1]);
        StdOut.println(Exercise__1_1_24.gcd(p, q));
    }
}
