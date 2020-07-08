/*
    ALGORITHM 1.5 -- Union-find implementation 3 (weighted quick-union)
    -------------------------------------------------------------------
    Test as follows:
        java WeightedQuickUnionUF < (tiny|medium|large)UF.txt (files from algs4-data)
 */
package case_study_union_find__1_5.algorithms;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;


public class WeightedQuickUnionUF {
    private int[] id;  // parent link (site indexed)
    private int[] sz;  // size of component for roots (site indexed)
    private int count;  // number of components

    public WeightedQuickUnionUF(int N) {
        this.count = N;
        this.id = new int[N];
        this.sz = new int[N];

        for (int i = 0; i < N; i++) {
            this.id[i] = i;
            this.sz[i] = 1;
        }
    }

    public int count() {
        return this.count;
    }

    public boolean connected(int p, int q) {
        return this.find(p) == this.find(q);
    }

    private int find(int p) {
        // Follow links to find root
        while (p != this.id[p])
            p = this.id[p];
        return p;
    }

    public void union(int p, int q) {
        int i = this.find(p);
        int j = this.find(q);

        if (i == j)
            return;

        // Make smaller root point to larger one
        if (this.sz[i] < this.sz[j]) {
            this.id[i] = j;
            this.sz[j] += this.sz[i];
        }
        else {
            this.id[j] = i;
            this.sz[i] += this.sz[j];
        }

        count--;
    }

    public static void main(String[] args) {
        // Solve dynamic connectivity problem on StdIn
        int N = StdIn.readInt();  // Read number of sites
        WeightedQuickUnionUF uf = new WeightedQuickUnionUF(N);  // Initialize N components

        while (!StdIn.isEmpty()) {
            int p = StdIn.readInt();
            int q = StdIn.readInt();  // Read pair to connect

            // Ignore if connected
            if (uf.connected(p, q))
                continue;
            uf.union(p, q);  // Combine components
            StdOut.println(p + " " + q);  // and print connection
        }
        StdOut.println(uf.count() + " components");
    }
}
