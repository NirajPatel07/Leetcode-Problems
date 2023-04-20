class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        
        int reverse_x = 0;
        int origin = x;
        
        while (x != 0){
            reverse_x = (reverse_x * 10) + (x % 10);
            x = x / 10;
        }
        
        return reverse_x == origin;
    }
}