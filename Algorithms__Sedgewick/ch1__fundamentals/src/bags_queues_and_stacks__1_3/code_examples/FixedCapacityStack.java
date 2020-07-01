/*
    An abstract data type for a fixed-capacity generic stack
 */
package bags_queues_and_stacks__1_3.code_examples;


import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;


public class FixedCapacityStack<Item> {
    private Item[] a;  // stack entries
    private int N;  // size

    public FixedCapacityStack(int cap) {
        a = (Item[]) new Object[cap];
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public int size() {
        return N;
    }

    public void push(Item item) {
        a[N++] = item;
    }

    public Item pop() {
        return a[--N];
    }

    public static void main(String[] args) {
        // Test Client
        FixedCapacityStack<String> s;
        s = new FixedCapacityStack<String>(100);
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
