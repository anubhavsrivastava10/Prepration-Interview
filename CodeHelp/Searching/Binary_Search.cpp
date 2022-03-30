#include<bits/stdc++.h>
using namespace std;

int binary_search(int arr[],int size, int key){
    int start = 0;
    int end = size-1;
    while(start<=end){
        // int mid = (start+end)/2;
        // Incase the array length is large and the mid goes beyound int range(2^31 -1) thus this code will not work then
        int mid = start + (end-start)/2;
        if(arr[mid]==key){
            return mid;
        }
        else if(arr[mid]>key){
            end = mid-1;
        }
        else{
            start = mid+1;
        }
    }
    return -1;
}

int main(){
    int arr1[6] = {2,5,7,9,11,18};
    int arr2[5] = {2,5,7,9,11};

    cout<< binary_search(arr1, 6, 18)<<endl;
    cout<< binary_search(arr2, 5, 11);
}