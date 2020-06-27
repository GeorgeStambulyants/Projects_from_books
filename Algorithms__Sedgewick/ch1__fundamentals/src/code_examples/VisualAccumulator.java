package code_examples;

import edu.princeton.cs.algs4.StdDraw;


public class VisualAccumulator {
    private double total;
    private int N;

    public VisualAccumulator(int trials, double max) {
        StdDraw.setXscale(0, trials);
        StdDraw.setYscale(0, max);
        StdDraw.setPenRadius(.005);
    }

    public void addDataValue(double val) {
        this.N++;
        this.total += val;
        StdDraw.setPenColor(StdDraw.DARK_GRAY);
        StdDraw.point(N, val);
        StdDraw.setPenColor(StdDraw.RED);
        StdDraw.point(N, total / N);
    }

    public double mean() {
        return this.total / this.N;
    }

    public String toString() {
        return "Mean (" + this.N + " values): "
                + String.format("%7.5f", this.mean());
    }
}
