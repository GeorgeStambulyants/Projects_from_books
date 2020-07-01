/*
    ALGORITHM 1.1 -- Pushdown (LIFO) stack (resizing array implementation)
    ----------------------------------------------------------------------
    This generic, iterable implementation of Stack API
    is a model for collection ADTs that keeps items in array.
    It resizes the array to keep the array size within a constant
    factor of the stack size
 */
package bags_queues_and_stacks__1_3.algorithms;

import java.util.Iterator;


public class ResizingArrayStack<Item> implements Iterable<Item> {
    private Item[] a = (Item[]) new Object[1];  // stack items
    private int N = 0;  // number of items

    public boolean isEmpty() {
        return N == 0;
    }

    public int size() {
        return N;
    }

    private void resize(int max) {
        Item[] temp = (Item[]) new Object[max];

        for (int i = 0; i < N; i++)
            temp[i] = a[i];
        a = temp;
    }

    public void push(Item item) {
        if (N == a.length)
            resize(2*a.length);
        a[N++] = item;
    }

    public Item pop() {
        // Remove item from top of stack
        Item item = a[--N];
        a[N] = null;  // Avoid loitering

        if(N > 0 && N == a.length / 4)
            resize(a.length / 2);

        return item;
    }

    @Override
    public Iterator<Item> iterator() {
        return new ReverseArrayIterator();
    }

    private class ReverseArrayIterator implements Iterator<Item> {
        // Support LIFO iteration
        private int i = N;

        public boolean hasNext() {
            return i > 0;
        }

        public Item next() {
            return a[--i];
        }

        public void remove() {}
    }
}
