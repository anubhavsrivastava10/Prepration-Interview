// https://www.codingninjas.com/codestudio/problems/sort-0-1-2_631055?source=youtube&campaign=LoveBabbar_Codestudiovideo1&utm_source=youtube&utm_medium=affiliate&utm_campaign=LoveBabbar_Codestudiovideo1
void sort012(int *arr, int n)
{
   //   Write your code here
    int i = 0;
    int j = 0;
    int k = n-1;
    while(j<=k){
        if(arr[j]==0){
            swap(arr[i],arr[j]);
            i++;
            j++;
        }
        else if(arr[j]==1){
            j++;
        }
        else if(arr[j]==2){
            swap(arr[j],arr[k]);
            k--;
        }
    }
}