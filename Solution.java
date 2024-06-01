import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
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

        // String s = "the sky is blue"; 
        // System.out.println(reverseWords(s));
        // "blue is sky the"

        // Trie trie = new Trie();
        // System.out.println(trie.search("Hello"));
        // System.out.println(trie.search("Hel"));
        // System.out.println(trie.search("Hell"));
        // trie.insert("Hello");
        // trie.insert("Hell");
        // System.out.println(trie.search("Hello"));
        // System.out.println(trie.search("Hel"));
        // System.out.println(trie.search("Hell"));

        // Set<Character> normalSet = new HashSet<Character>(); 
        // normalSet.add('1');
        // normalSet.add('1');
        // normalSet.add('1');
        // normalSet.add('1');
        // System.out.println(normalSet);

        // List<Integer> arr = new ArrayList<>();
        // // [3, 2, 3, 3, 1, 3]
        // arr.add(3);
        // arr.add(2);
        // arr.add(3);
        // arr.add(3);
        // arr.add(1);
        // arr.add(3);
        // int k = 3;

        // //  should be 4
        // System.out.println(findMinimumLengthSubarray(arr, k));

        // arr = new ArrayList<>();
        // // [1, 2, 2, 1, 2]
        // arr.add(1);
        // arr.add(2);
        // arr.add(2);
        // arr.add(1);
        // arr.add(2);

        // k = 4;
        // //  should be -1
        // System.out.println(findMinimumLengthSubarray(arr, k));

        List<Integer> x = new ArrayList<>();
        List<Integer> y = new ArrayList<>();
        x.add(543243);
        x.add(5000);

        y.add(0);
        y.add(322);

        System.out.println(closestSquaredDistance(x, y));
    }

    public static long closestSquaredDistance(List<Integer> x, List<Integer> y) {
        long clostest = Long.MAX_VALUE;
        for (int i = 0; i < x.size() - 1; i++) {
            long distance;
            System.out.println(x.get(i));
            System.out.println(x.get(i + 1));
            System.out.println(y.get(i));
            System.out.println(y.get(i + 1));
            distance = ((x.get(i) - x.get(i + 1)) * (x.get(i) - x.get(i + 1))) + ((y.get(i) - y.get(i + 1)) * (y.get(i) - y.get(i + 1)));
            if (distance < clostest) {
                clostest = distance;
            }
        }
        return clostest;
    
    }

    public static int findMinimumLengthSubarray(List<Integer> arr, int k) {
        int minSize = arr.size();
        Set<Integer> uniqueSet = new HashSet<Integer>(); 
        boolean flag = false;

        for (int i = 0; i < k; i++) {
            uniqueSet.add(arr.get(i));
        }
        if (uniqueSet.size() == k) {
            return k;
        }
        
    
        for (int left = 0; left < arr.size() - k ; left++) {
            uniqueSet = new HashSet<Integer>(); 
            for (int right = left + k; right < arr.size(); right++){
                if (uniqueSet.size() == 0) {
                    List<Integer> smallerList = arr.subList(left, right);
                    uniqueSet.addAll(smallerList);
                } else {
                    uniqueSet.add(arr.get(right));
                }
                
                int diff = right - left;
                if (uniqueSet.size() == k && diff < minSize) {
                    minSize = diff;
                    flag = true;
                }
            }


        }
        if (flag) {
            return minSize;
        } else {
            return -1;
        }
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

/**
 * This class is a trie implementation.
 */
class Trie {
    private HashMap<Character, HashMap> origin;
    
    /**
     * 
     */
    public Trie() {
        this.origin = new HashMap<>();
    }
    
    /**
     * Inserts a word into the trie
     * 
     * @param word the word to be inserted into the trie
     */
    public void insert(String word) {
        HashMap<Character, HashMap> node = this.origin;
        
        for (int i = 0; i < word.length(); i++) {
            char letter = word.charAt(i);
            if (node.containsKey(letter)) {
                node = node.get(letter);
            } else {
                HashMap<Character, HashMap> newNode = new HashMap<>();
                node.put(letter, newNode);
                node = node.get(word.charAt(i)); 
            }
        }
        node.put('\0', new HashMap<Character, HashMap>(0)); 
    }
    
    /**
     * Search to see if a word exist in the Trie.
     * 
     * @param word that is searched.
     * @return True if the word exist in the trie, false otherwise.
     */
    public boolean search(String word) {
        HashMap<Character, HashMap> node = this.origin;

        for (int i = 0; i < word.length(); i++) {
            char letter = word.charAt(i);
            if (node.containsKey(letter)) {
                node = node.get(letter);
            } else {
                return false;
            }
        }
        if (node.containsKey('\0')) {
            return true;
        }
        return false;
    }
    
    /**
     * Search the trie to see if any word starts with the given prefix exists
     * in the trie
     * 
     * @param prefix to search.
     * @return Returns true if there is a previously inserted string word that
     *  has the prefix prefix, and false otherwise.
     */
    public boolean startsWith(String prefix) {
        HashMap<Character, HashMap> node = this.origin;

        for (int i = 0; i < prefix.length(); i++) {
            char letter = prefix.charAt(i);
            if (node.containsKey(letter)) {
                node = node.get(letter);
            } else {
                return false;
            }
        }
        return true;
    }
}