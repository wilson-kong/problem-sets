import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class HackerRank {

    public static void main(String[] args) {
        
        // String s = "giraffe";
        // String charValue = "01111001111111111011111111";
        // int k = 2;
        
        // // should be 3
        // System.out.println(getSpecialSubstring(s, k, charValue));

        // s = "special";
        // charValue = "00000000000000000000000000";
        // k = 1;

        // // should be 1
        // System.out.println(getSpecialSubstring(s, k, charValue));

        // s = "stupid";
        // charValue = "00000000000000000000000000";
        // k = 1;

        // // should be 1
        // System.out.println(getSpecialSubstring(s, k, charValue));

        // s = "abcdef";
        // charValue = "00000011111111111111111111";
        // k = 2;

        // // should be 2
        // System.out.println(getSpecialSubstring(s, k, charValue));


        // s = "abcde";
        // charValue = "10101111111111111111111111";
        // k = 2;

        // // should be 5
        // System.out.println(getSpecialSubstring(s, k, charValue));

        // k = 1;

        // // should be 3
        // System.out.println(getSpecialSubstring(s, k, charValue));

        // s = "hwqrhxaklywjuxsihxecfbeagddaqekyadrhatsnuqyopqywpeywffxliaoahayhdsrdllqfdpvthupzyqxevwrfzffgggpjygplthtxyoqikhhlxgrudibcqhiypxjpgaczivyimoqywzjvgcslntndcxdtwmienlexiehuvyvtzgohjiswehbigecdsmhhxngisocnozgngwxphrnnzqvfuzkomswlhetbsyqixywfxvuemjtnzqtvqfkezirhmlkhlbpkznqwimcxwvkvofteldkknbtbmekzhakgpafamhzkfjitrbzcgjotkkwzqhaxjkdamkazuzlzltucuvgcgwvsgutwbutmezmrjpsdodebzafvvlybivwqpppqjieqjrhtgbywgdyfdfbbrzebuarksgcbrhraaavgduckzcpeiqhbpmemoxyggakxjdzjexphtursyjwizglrspfindrtdbspetykqqujmndmwcvyigrcywklzbgeeatltuvmmrxafbmddjdnsupqsbdrdlyjltuepsqbjqdqrsuwbzjvuanmbqggbgqmzmtpelsobygsqcqtczpwbckdvsjwyblaogpsrjithpnzrgtthirjkemhwxexzrxpxohoxsjhjzgafzwmjpxwtjdsjjriaozxcgobazkjarmfskuczravddnmngwnuvnyddbecmpffbkxlgbnabidfxrudpjzkwxnbatgmllrmvraeupgyxjfwczzriabhzqizmomxzflxyndtcjrbuyxwxyphyqoxixxwnlvpsjmrwpmbafcudaqcafjzxyyhxvgkidzbmnuleimenqysqqutxdswdqgaomnypobeevpiddpstpmmigffmzerrksfyhgpxhvbfmmipbdjspxaycikbmbsyvayeipcplfuxtfpuiynzxpxzxhcjlwjiyhngzrwmysjsxyohybhvtgwqoacbxljvvycwraiqsrisswzsai";
        // //  alpha = "abcdefghijklmnopqrstuvwxyz";
        // charValue = "11011110011100101101011011";
        // k = 182;

        // // should be 512
        // System.out.println(getSpecialSubstring(s, k, charValue));

        Set<Character> normalSet = new HashSet<Character>(); 

    }

    public static int getSpecialSubstring(String s, int k, String charValue) {
        Set<Character> normalSet = new HashSet<Character>(); 
        String alpha = "abcdefghijklmnopqrstuvwxyz";

        for (int i = 0; i < charValue.length(); i++) {
            if (charValue.charAt(i) == '0') {
                normalSet.add(alpha.charAt(i));
            }
        }

        // System.out.println(normalSet);

        // for (int i = 0; i < s.length(); i++) {
        //     int counter = k;
        //     int currentMax = 0;
        //     for (int j = 0; j < s.length(); j++) {
        //         if (counter > 0) {
        //             if (normalSet.contains(s.charAt(j))) {
        //                 currentMax += 1;
        //                 counter -= 1;
        //             } else {
        //                 currentMax += 1;
        //             }
        //         } else {
        //             if (currentMax > longest) {
        //                 longest = currentMax;
        //             }
        //             break;
        //         }

        //     }
        // }
        // return longest;
    
        // }
        // System.out.println(normalSet);
        List<Integer> nums = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (normalSet.contains(s.charAt(i))) {
                nums.add(0);
            } else {
                nums.add(1);
            }
        }
        // System.out.println(nums);
        int left = 0;
        int right = 0;
        for (int i = 0; i < s.length(); i++) {
            right = i;
            if (nums.get(right) == 0) {
                k -= 1;
            }
            if (k < 0) {
                if (nums.get(left) == 0) {
                    k += 1;
                }
                left += 1;
            }
            
        }
        
        return right - left + 1;
    }

}
