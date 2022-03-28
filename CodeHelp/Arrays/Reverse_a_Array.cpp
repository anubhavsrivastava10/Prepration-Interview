#include<iostream>
using namespace std;

void change(int *a,int *b){
    int ch = *a;
    *a = *b;
    *b = ch;
}

void reverse(int arr[],int n){
    int start = 0;
    int end = n-1;
    while(start<=end){
        change(&arr[start],&arr[end]);
        start++;
        end--;
    }
}

void print(int arr[], int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<"-";
    }
}

int main(){
    cout << "Enter the size of an array";
    int n;
    cin >> n;
    int arr[n];
    cout << "Enter the values of an array";
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    reverse(arr,n);
    print(arr,n);
}