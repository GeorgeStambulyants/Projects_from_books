/*
    ALGORITHM 1.3 -- Union-find implementation #2
    with quick-union. See union() instance method.
    ------------------------------------------
    Test as follows:
        java UFQuickUnion < (tiny|medium|large)UF.txt (files from algs4-data)
 */
package case_study_union_find__1_5.algorithms;


import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class UFQuickUnion {
    private int[] id; // access to component id (site indexed)
    private int count;  // number of components

    public UFQuickUnion(int N) {
        // Initialize component id array
        this.count = N;
        this.id = new int[N];

        for (int i = 0; i < N; i++)
            id[i] = i;
    }

    public int count() {
        return count;
    }

    public boolean connected(int p, int q) {
        return this.find(p) == this.find(q);
    }

    public int find(int p) {
        // Find component name
        while (p != this.id[p])
            p = this.id[p];
        return p;
    }

    public void union(int p, int q) {
        // Give p and q the same root
        int pRoot = this.find(p);
        int qRoot = this.find(q);

        if (pRoot == qRoot)
            return;

        id[pRoot] = qRoot;

        count--;
    }

    public static void main(String[] args) {
        // Solve dynamic connectivity problem on StdIn
        int N = StdIn.readInt();  // Read number of sites
        UFQuickUnion uf = new UFQuickUnion(N);  // Initialize N components

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
