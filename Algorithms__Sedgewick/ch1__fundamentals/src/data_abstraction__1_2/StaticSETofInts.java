package data_abstraction__1_2;

import java.util.Arrays;


public class StaticSETofInts {
    private int[] a;

    public StaticSETofInts(int[] keys) {
        this.a = new int[keys.length];

        for (int i = 0; i < keys.length; i++)
            this.a[i] = keys[i];
        Arrays.sort(a);
    }

    public boolean contains(int key) {
        return this.rank(key) != -1;
    }

    public int rank(int key) {
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
}
