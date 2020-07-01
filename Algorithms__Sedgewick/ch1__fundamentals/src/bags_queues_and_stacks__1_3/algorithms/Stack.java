/*
    ALGORITHM 1.2 -- Pushdown stack (linked-list implementation)
    ------------------------------------------------------------
    This generic Stack implementation is based on a linked-list data
    structure. It can be used to create stacks containing any type of data.
 */
package bags_queues_and_stacks__1_3.algorithms;


import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Stack<Item> {
    private Node first;  // top of stack (most recently added node)
    private int N;  // number of items

    private class Node {
        Item item;
        Node next;
    }

    public boolean isEmpty() {
        return first == null;  // Or: N == 0;
    }

    public int size() {
        return N;
    }

    public void push(Item item) {
        // Add item to top of stack
        Node old_first = first;
        first = new Node();

        first.item = item;
        first.next = old_first;

        N++;
    }

    public Item pop() {
        // Remove item from top of stack
        Item item = first.item;

        first = first.next;
        N--;

        return item;
    }

    public static void main(String[] args) {
        // Test Client
        Stack<String> s;
        s = new Stack<String>();
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
