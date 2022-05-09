//https://www.codingninjas.com/codestudio/problems/first-and-last-position-of-an-element-in-sorted-array_1082549?source=youtube&campaign=love_babbar_codestudio2&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio2&leftPanelTab=0

int firstOccur(vector<int>& arr, int n, int k){
    int s = 0;
    int e = n-1;
    int ans = -1;
    while(s<=e){
        int mid = s + (e-s)/2;
        if(arr[mid]==k){
            ans = mid;
            e = mid -1;
        }
        else if(arr[mid]>k){
            e = mid-1;
        }
        else if(arr[mid]<k){
            s = mid+1;
        }
    }
    return ans;
}
int lastOccur(vector<int>& arr, int n, int k){
    int s = 0;
    int e = n-1;
    int ans = -1;
    while(s<=e){
        int mid = s + (e-s)/2;
        if(arr[mid]==k){
            ans = mid;
            s= mid +1;
        }
        else if(arr[mid]>k){
            e = mid-1;
        }
        else if(arr[mid]<k){
            s = mid+1;
        }
    }
    return ans;
}
pair<int, int> firstAndLastPosition(vector<int>& arr, int n, int k)
{
    // Write your code here
    pair<int,int> ans;
    ans.first = firstOccur(arr, n, k);
    ans.second = lastOccur(arr, n, k);
    return ans;
}