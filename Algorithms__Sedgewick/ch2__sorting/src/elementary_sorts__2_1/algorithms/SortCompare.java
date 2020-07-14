/*
    Comparing two sorting algorithms
    --------------------------------
    This client runs the two sorts named in the first
    two command-line arguments on arrays of
    N (the third command-line argument) random Double values
    between 0.0 and 1.0, repeating the experiment
    T (the fourth command-line argument) times, then
    prints the ratio of the total running times.

    Test as follows:
        $ java SortCompare Insertion Selection 1000 100
 */
package elementary_sorts__2_1.algorithms;

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.Stopwatch;


public class SortCompare {
    public static double time(String alg, Double[] a) {
        Stopwatch timer = new Stopwatch();
        if (alg.equals("Insertion"))
            InsertionSort.sort(a);
        else if (alg.equals("Selection"))
            SelectionSort.sort(a);

        return timer.elapsedTime();
    }

    public static double timeRandomInput(String alg, int N, int T) {
        // Use alg to sort T random arrays of length N
        double total = 0.0;
        Double[] a = new Double[N];

        for (int t = 0; t < T; t++) {
            // Perform one experiment (generate and sort an array)
            for (int i = 0; i < N; i++)
                a[i] = StdRandom.uniform();
            total += SortCompare.time(alg, a);
        }
        return total;
    }

    public static void main(String[] args) {
        String alg1 = args[0];
        String alg2 = args[1];
        int N = Integer.parseInt(args[2]);
        int T = Integer.parseInt(args[3]);
        double t1 = SortCompare.timeRandomInput(alg1, N, T);  // total for alg1
        double t2 = SortCompare.timeRandomInput(alg2, N, T);  // total for alg2

        StdOut.printf("For %d random Doubles\n  %s is", N, alg1);
        StdOut.printf(" %.1f times faster than %s\n", t2/t1, alg2);
    }
}
