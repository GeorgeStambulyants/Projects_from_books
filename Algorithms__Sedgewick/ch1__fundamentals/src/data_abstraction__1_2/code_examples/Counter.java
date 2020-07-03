package data_abstraction__1_2.code_examples;

import edu.princeton.cs.algs4.StdOut;


public class Counter {
    private final String name;
    private int count;

    public Counter(String id) {
        this.name = id;
    }

    public void increment() {
        this.count++;
    }

    public int tally(){
        return this.count;
    }

    public String toString() {
        return this.count + " " + this.name;
    }

    public static void main(String[] args) {
        Counter heads = new Counter("heads");
        Counter tails = new Counter("tails");

        heads.increment();
        heads.increment();
        heads.increment();
        tails.increment();

        StdOut.println(heads + " " + tails);
        StdOut.println(heads.tally() + tails.tally());
    }
}
