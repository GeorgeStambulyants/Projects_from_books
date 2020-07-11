/*
    Exercise 1.2.6
    ---------------
    Write a program that checks whether two strings
    s and t a circular shifts of one another.
 */
package data_abstraction__1_2.exercises;


public class Exercise__1_2_6 {
    private static String shiftRight(String str) {
        StringBuilder shifted_str = new StringBuilder();

        for (int i = 1; i < str.length(); i++) {
            shifted_str.append(str.charAt(i));
        }
        shifted_str.append(str.charAt(0));

        return shifted_str.toString();
    }

    public static boolean areCircularShifts(String s, String t) {
        if (s.length() != t.length() || t.indexOf(s.charAt(0)) == -1)
            return false;

        for (int i = 0; i < s.length(); i++) {
            t = Exercise__1_2_6.shiftRight(t);
            if (t.equals(s))
                return true;
        }

        return false;
    }
}
