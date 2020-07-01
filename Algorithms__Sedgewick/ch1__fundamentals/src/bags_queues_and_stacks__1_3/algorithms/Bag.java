/*
    ALGORITHM 1.4 -- Bag
    --------------------
    This Bag implementation maintains a linked list of the items
    provided in calls to add().
 */
package bags_queues_and_stacks__1_3.algorithms;


import java.util.Iterator;


public class Bag<Item> implements Iterable<Item> {
    private Node first;  // first node in list
    private int N;  // number of items in Bag

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

    public void add(Item item) {
        Node old_first = first;

        first = new Node();
        first.item = item;
        first.next = old_first;

        N++;
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
