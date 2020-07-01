/*
    ALGORITHM 1.3 -- FIFO queue
    ---------------------------
 */
package bags_queues_and_stacks__1_3.algorithms;


import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Queue<Item> {
    private Node first;  // link to least recently added node
    private Node last;  // link to most recently added node
    private int N;  // number of items on the queue

    private class Node {
        // nested class to define nodes
        Item item;
        Node next;
    }

    public boolean isEmpty() {
        return first == null;  // or N == 0
    }

    public int size() {
        return N;
    }

    public void enqueue(Item item) {
        // Add item to the end of the list
        Node old_last = last;

        last = new Node();
        last.item = item;
        last.next = null;

        if (this.isEmpty())
            first = last;
        else
            old_last.next = last;

        N++;
    }

    public Item dequeue() {
        // Remove item from the beginning of the list
        Item item = first.item;

        first = first.next;

        if (this.isEmpty())
            last = null;

        N--;

        return item;
    }

    public static void main(String[] args) {
        // Create a queue and enqueue/dequeue strings
        Queue<String> q = new Queue<String>();

        while(!StdIn.isEmpty()) {
            String item = StdIn.readString();
            if (!item.equals("-"))
                q.enqueue(item);
            else if (!q.isEmpty())
                StdOut.print(q.dequeue() + " ");
        }
        StdOut.println("(" + q.size() + " left on queue)");
    }
}
