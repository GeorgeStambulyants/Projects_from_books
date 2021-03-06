/*
    An abstract data type for a fixed-capacity stack of strings
 */

package bags_queues_and_stacks__1_3.code_examples;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;


public class FixedCapacityStackOfStrings {
    private String[] a;  // stack entries
    private int N;  // size
    private int capacity;

    public FixedCapacityStackOfStrings(int cap) {
        capacity = cap;
        a = new String[cap];
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public int size() {
        return N;
    }

    public void push(String item) {
        a[N++] = item;
    }

    public String pop() {
        return a[--N];
    }

    public boolean isFull() {
        return capacity == N + 1;
    }

    public static void main(String[] args) {
        // Test Client
        FixedCapacityStackOfStrings s;
        s = new FixedCapacityStackOfStrings(100);
        while (!StdIn.isEmpty()) {
            String item = StdIn.readString();
            if (!item.equals("-"))
                s.push(item);
            else if (!s.isEmpty())
                StdOut.print(s.pop() + " ");
        }
        StdOut.println("(" + s.size() + " left on stack)");
    }
}
