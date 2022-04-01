#https://www.codingninjas.com/codestudio/problems/sum-of-infinite-array_873335

vector<int> sumInRanges(vector<int> &arr, int n, vector<vector<long long>> &queries, int q) {
    // Write your code here
    long long  mo = 1000000007;
    vector <int> ans(q);
    vector <long long> presum(n+1);
    presum[0] = 0;
    for(long long i = 0; i < n; i++){
        presum[i+1] = (presum[i] + arr[i]) % mo;
    }
    long long temp;
    for(int i = 0; i < q; i++){
        long long l=queries[i][0];
        long long r=queries[i][1];
        l--;
        temp = (presum[r % n] - presum[l % n] + ((presum[n] * ((r/n - l/n) % mo)))) % mo ;
        ans[i] = temp;
    }
    return ans;
}