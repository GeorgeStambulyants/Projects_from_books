package data_abstraction__1_2.code_examples;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;


public class Whitelist {
    public static void main(String[] args) {
        In in = new In(args[0]);
        int[] w = in.readAllInts();
        StaticSETofInts set = new StaticSETofInts(w);

        while (!StdIn.isEmpty()) {
            int key = StdIn.readInt();
            if (set.rank(key) == -1)
                StdOut.println(key);
        }
    }
}
