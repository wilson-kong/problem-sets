import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public static void main(String[] args) {
        // String word1 = "abc";
        // String word2 = "pqr";
        // System.out.println(mergeAlternately(word1, word2));
        // word1 = "ab";
        // word2 = "pqrs";
        // System.out.println(mergeAlternately(word1, word2));
        // word1 = "abcd";
        // word2 = "pq";
        // System.out.println(mergeAlternately(word1, word2));
        // String str1 = "ABCABC";
        // String str2 = "ABC";
        // System.out.println(gcdOfStrings(str1, str2));
        // str1 = "ABABAB";
        // str2 = "ABAB";
        // System.out.println(gcdOfStrings(str1, str2));
        // str1 = "LEET";
        // str2 = "CODE";
        // System.out.println(gcdOfStrings(str1, str2));
        int[] candies = new int[]{2,3,5,1,3};
        int extraCandies = 3;
        System.out.println(kidsWithCandies(candies, extraCandies));
        candies = new int[]{4,2,1,1,2};
        extraCandies = 1;
        System.out.println(kidsWithCandies(candies, extraCandies));
        candies = new int[]{12,1,12};
        extraCandies = 10;
        System.out.println(kidsWithCandies(candies, extraCandies));
    }

    public static String mergeAlternately(String word1, String word2) {
        String output = "";
        int word2Len = word2.length();
        int index = 0;
        for (int i = 0; i < word1.length(); i++) {
            output += word1.charAt(i);
            if (i < word2Len) {
                output += word2.charAt(i);
            }
            index = i;
        }
        index += 1;
        System.out.println(index);
        if (index <= word2Len) {
            for (int i = index; i < word2.length(); i++) {
                output += word2.charAt(i);
            }
        }
        return output;
    }

    public static String gcdOfStrings(String str1, String str2) {
        if (str1.equals(str2)) {
            return str1;
        }
        if ((str1 + str2).equals(str2 + str1)){
            return str1.substring(0, gcd(str1.length(), str2.length()));
        }
        return "";
    }

    private static int gcd(int first, int second) {
        int result = Math.min(first, second);
        while (result > 0) {
            if (first % result == 0 && second % result == 0) {
                return result;
            }
            result -= 1;
        }
        return -1;
    }

    public static List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int greatest = Arrays.stream(candies).max().getAsInt(); 
        List<Boolean> output = new ArrayList<>();
        for (int kid : candies) {
            if (kid + extraCandies >= greatest) {
                output.add(true);
            } else {
                output.add(false);
            }
        }
        return output;
    }

}