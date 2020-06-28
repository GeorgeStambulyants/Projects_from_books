package data_abstraction__1_2;


public class Accumulator {
    private double total;
    private int N;

    public void addDataValue(double val) {
        this.N++;
        this.total += val;
    }

    public double mean() {
        return this.total / this.N;
    }

    public String toString() {
        return "Mean (" + this.N + " values): "
                    + String.format("%7.5f", this.mean());
    }
}
