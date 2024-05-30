import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

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
        // int[] candies = new int[]{2,3,5,1,3};
        // int extraCandies = 3;
        // System.out.println(kidsWithCandies(candies, extraCandies));
        // candies = new int[]{4,2,1,1,2};
        // extraCandies = 1;
        // System.out.println(kidsWithCandies(candies, extraCandies));
        // candies = new int[]{12,1,12};
        // extraCandies = 10;
        // System.out.println(kidsWithCandies(candies, extraCandies));
        // int[] flowerbed = new int[]{1,0,0,0,1};
        // int n = 1;
        // System.out.println(canPlaceFlowers(flowerbed, n));
        // flowerbed = new int[]{1,0,0,0,1};
        // n = 1;
        // System.out.println(canPlaceFlowers(flowerbed, n));
        // LinkedList linkedList = new LinkedList();
        // linkedList.insertAtStart("H");
        // linkedList.insertAtStart("e");
        // linkedList.insertAtStart("l");
        // System.out.println(linkedList.allData());
        // linkedList.insertAtStart("l");
        // linkedList.insertAtStart("o");
        // linkedList.insertAtStart("!");
        // System.out.println(linkedList.allData());

        String s = "the sky is blue"; 
        System.out.println(reverseWords(s));
        // "blue is sky the"
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

    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        int previous = 0;
        int totalEmpty = 1;
        int flowerbedLen = flowerbed.length;

        // Add an extra element at the end of flowerbed to simplify boundary checking
        int[] updatedFlowerbed = new int[flowerbedLen + 1];
        System.arraycopy(flowerbed, 0, updatedFlowerbed, 0, flowerbedLen);

        if (updatedFlowerbed[flowerbedLen - 1] == 0) {
            totalEmpty += flowerbedLen;
            n -= totalEmpty;
            return n <= 0;
        }

        for (int index = 0; index < flowerbedLen; index++) {
            previous = updatedFlowerbed[index];
            if (previous == 1) {
                n -= totalEmpty;
                totalEmpty = 0;
                continue;
            }
            totalEmpty++;
        }

        n -= totalEmpty;

        return n <= 0;
    
        
    }

    public static int[] asteroidCollision(int[] asteroids) {
        
        Stack<Integer> stack = new Stack<>();

        for (int asteroid: asteroids) {
            while (stack.empty() == false && asteroid < 0 && stack.peek() > 0) {
                int diff = asteroid + stack.peek();
                if (diff < 0) {
                    stack.pop();
                } else if (diff > 0) {
                    asteroid = 0;
                } else {
                    asteroid = 0;
                    stack.pop();
                }
            }
            if (asteroid != 0) {
                stack.push(asteroid);
            }
        }

        int[] output = new int[stack.size()];
        for (int i = 0; i < stack.size(); i++) {
            output[i] = stack.get(i);
        }
        return output;
    }

    public static String reverseWords(String s) {
        LinkedList output = new LinkedList();
        int start_index = -1;
        s = " " + s + " ";
        for (int index = 0; index < s.length(); index++) {
            if (s.charAt(index) != ' ') {
                if (start_index == -1) {
                    start_index = index;
                    System.out.print("start index: ");
                    System.out.println(start_index);
                }
            } else {
                if (start_index != -1) {
                    output.insertAtStart(s.substring(start_index, index));
                    start_index = -1;
                }
            }
        }
        return output.allData();
    }

}


class LinkedListNode {

    public String data;
    public LinkedListNode next;

    public LinkedListNode(String data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    public LinkedListNode head;
    
    public LinkedList() {
        this.head = null;
    }

    public void insertAtStart(String data) {
        LinkedListNode newNode = new LinkedListNode(data);
        if (this.head == null) {
            this.head = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
    }

    public String allData() {
        LinkedListNode currentNode = this.head;
        String output = "";

        while (currentNode != null) {
            output += currentNode.data + " ";
            currentNode = currentNode.next;
        }
        return output.substring(0, output.length() - 1);
    }
}