/*
* All exercise solutions of the 1.1 paragraph
* TODO: rewrite this heading
* */

import edu.princeton.cs.algs4.StdOut;

public class Exercises {
    public static void transposition(int[][] array, int M, int N) {
        /*
            Prints transposition of a two-dimensional array
            with M rows and N columns
         */
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++){
                StdOut.print(array[j][i] + " ");
            }
            StdOut.println();
        }
    }

    public static int lg(int N) {
        /* TODO
            Returns the largest int not larger
            than the base-2 logarithm of N. Can not use Math
         */
        return 1;
    }

    public static void main(String[] args) {
        
    }
}
