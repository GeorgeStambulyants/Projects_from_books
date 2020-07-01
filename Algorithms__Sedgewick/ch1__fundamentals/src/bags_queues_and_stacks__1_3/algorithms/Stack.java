/*
    ALGORITHM 1.2 -- Pushdown stack (linked-list implementation)
    ------------------------------------------------------------
    This generic Stack implementation is based on a linked-list data
    structure. It can be used to create stacks containing any type of data.
 */
package bags_queues_and_stacks__1_3.algorithms;

import java.util.Iterator;


public class Stack<Item> implements Iterable<Item> {
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

    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public Item next() {
            Item item = current.item;
            current = current.next;

            return item;
        }

        public void remove() {}
    }
}
