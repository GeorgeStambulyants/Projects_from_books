/*
    Exercise 1.1.20
    ---------------
    Write a recursive static method that computes
    the value of ln(N!)
 */
package basic_programming_model__1_1.exercises;


public class Exercise__1_1_20 {
    public static double ln_of_factorial(int N) {
        // N >= 0
        if (N == 1 || N == 0) {
            return 0;
        }
        return Math.log(N) + ln_of_factorial(N - 1);
    }
}
