class Solution {
    public int[] plusOne(int[] digits) {
        ArrayList <Integer> ar=new ArrayList<>();
        int carry=0;
        for(int i = digits.length-1 ; i >= 0 ; i--){
            if(i == digits.length-1){
                int val = digits[i]+1;
                ar.add( 0, val%10 );
                carry = val/10;
            }
            else{
                ar.add(0,(digits[i]+carry)%10);
                carry=(digits[i]+carry)/10;
            }
        }
        if(carry>0){
            ar.add(0,carry);
        }
        int[] ans=new int[ar.size()];
        for(int i=0;i<ar.size();i++){
            ans[i]=ar.get(i);
        }       
        return ans;
    }
}