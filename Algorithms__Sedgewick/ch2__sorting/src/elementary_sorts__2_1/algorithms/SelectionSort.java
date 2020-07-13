/*
    Algorithm 2.1 -- Selection sort
    See Example.java.
    -------------------------------
    For each i, this implementation puts the ith smallest item
    in a[i]. The entries to the left of position i are the i
    smallest items in the array and are not examined again.

    Selection sort uses ~ N^2/2 compares and N exchanges
    to sort an array of length N.
 */
package elementary_sorts__2_1.algorithms;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;


public class SelectionSort {
    public static void sort(Comparable[] a) {
        // Sort a[] into increasing order
        int N = a.length;

        for (int i = 0; i < N; i++) {
            // Exchange a[i] with smallest entry in a[i+1...N]
            int min = i;  // index of minimal entry

            for (int j = i + 1; j < N; j++)
                if (SelectionSort.less(a[j], a[min]))
                    min = j;

            SelectionSort.exch(a, i, min);
        }
    }

    private static boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }

    private static void exch(Comparable[] a, int i, int j) {
        Comparable t = a[i];

        a[i] = a[j];
        a[j] = t;
    }

    private static void show(Comparable[] a) {
        // Print the array, on a single line
        for (int i = 0; i < a.length; i++)
            StdOut.print(a[i] + " ");

        StdOut.println();
    }

    public static boolean isSorted(Comparable[] a) {
        // Test weather the array entries are in order
        for (int i = 1; i < a.length; i++)
            if (SelectionSort.less(a[i], a[i - 1]))
                return false;
        return true;
    }

    public static void main(String[] args) {
        // Read strings from standard input, sort them, and print
        String[] a = StdIn.readAllStrings();
        SelectionSort.sort(a);
        assert SelectionSort.isSorted(a);
        SelectionSort.show(a);
    }
}
