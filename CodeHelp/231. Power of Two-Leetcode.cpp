class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n==0){
            return false;
        }
        while(n!=0){
            if(n%2!=0 && n!=1){
                return false;
            }
            n = n >> 1;
            // cout<<n<<"-";
        }
        return true;
    }
};