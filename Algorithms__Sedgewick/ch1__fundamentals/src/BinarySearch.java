/*
    class BinarySearch must be tested with test data.
    It can be find at https://algs4.cs.princeton.edu/code/
    -------------------------------------------------------
    Test with following files:
        * tinyW.txt and tinyT.txt
        * largeW.txt and largeT.txt
    Testing format after compilation:
        1) $ java BinarySearch tinyW.txt < tinyT.txt
            output:
                50
                99
                13
        2) $ java BinarySearch largeW.txt < largeT.txt
            output is very long and omitted here
 */

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

import java.util.Arrays;

/*
  The class provides a static method for binary
  searching for an integer in a sorted array of integers.

  The indexOf operations takes logarithmic time in the worst case.
 */

public class BinarySearch {

    // This class should not be instantiated
    private BinarySearch() { }

    public static int indexOf(int key, int[] a) {
        int lo = 0;
        int hi = a.length - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (key < a[mid])
                hi = mid - 1;
            else if (key > a[mid])
                lo = mid + 1;
            else
                return mid;
        }
        return -1;
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        int[] allowList = in.readAllInts();

        Arrays.sort(allowList);

        while (!StdIn.isEmpty()) {
            // Read key, print if not in whitelist
            int key = StdIn.readInt();
            if (BinarySearch.indexOf(key, allowList) < 0)
                StdOut.println(key);
        }
    }
}
