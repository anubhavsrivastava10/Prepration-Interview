#include<bits/stdc++.h>
using namespace std;

bool linear_search(int arr[], int n,int target){
    for(int i=0;i<n;i++){
        if(arr[i]==target){
            return true;
        }
    }
    return false;
}

int main(){
    int arr[] = {10,20,30,40,50,60};
    int target = 5;
    // int target = 50;
    int arrSize = sizeof(arr)/sizeof(arr[0]);
    cout<< linear_search(arr, arrSize, target);
}