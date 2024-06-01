/**
 * https://neetcode.io/roadmap
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class neet150 {

    public static void main(String[] args) {
        // int[] nums = {1, 2, 3, 3};
        // System.out.println(hasDuplicate(nums));
        // int[] nums1 = {1, 2, 3, 4};
        // System.out.println(hasDuplicate(nums1));

        String s = "racecar";
        String t = "carrace";
        System.out.println(isAnagram(s, t));
        s = "jar";
        t = "jam";
        System.out.println(isAnagram(s, t));
        s = "a";
        t = "ab";
        System.out.println(isAnagram(s, t));
    }
    
    public static boolean hasDuplicate(int[] nums) {
        Set<Integer> numsSet = new HashSet<Integer>(); 
        for (int i = 0; i < nums.length; i++) {
            numsSet.add(nums[i]);
        }
        return numsSet.size() != nums.length;
    }

    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        List<Character> s_letters = new ArrayList<Character>();
        for (char c : s.toCharArray()) {
            s_letters.add(c);
        }
        for (char charT : t.toCharArray()) {
            
            if (s_letters.contains(charT)) {
                s_letters.remove((Character) charT);
            }
        }
        return s_letters.size() == 0;
    }
}
