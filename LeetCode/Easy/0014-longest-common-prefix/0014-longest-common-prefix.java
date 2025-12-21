import java.util.*;
class Solution {
    public String longestCommonPrefix(String[] strs) {
        for(int i = 0; i < strs[0].length(); i++)
        {
            for(int j = 0; j < strs.length; j++)
            {
                if(strs[j].length() <= i || strs[0].charAt(i) != strs[j].charAt(i))
                {
                    return strs[0].substring(0,i); 
                }
            }
        }
        return "";
    }
}