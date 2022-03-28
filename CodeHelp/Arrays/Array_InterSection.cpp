//https://www.codingninjas.com/codestudio/problems/intersection-of-2-arrays_1082149?source=youtube&campaign=love_babbar_codestudio1&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio1&leftPanelTab=0

vector<int> findArrayIntersection(vector<int> &arr1, int n, vector<int> &arr2, int m)
{
	// Write your code here.
    int l = 0;
    int k = 0;
    vector<int> ans;
    while(l<n && k<m){
        if(arr1[l]==arr2[k]){
            ans.push_back(arr1[l]);
            l = l+1;
            k = k+1;
        }
        else if(arr1[l]>arr2[k]){
            k = k+1;
        }
        else if(arr1[l]<arr2[k]){
            l = l+1;
        }
    }
    return ans;
}