#include<iostream>
using namespace std;

void change(int *a,int *b){
    int ch = *a;
    *a = *b;
    *b = ch;
}

void alternate(int arr[],int n){
    int start = 0;
    while(start < n-1){
        change(&arr[start], &arr[start+1]);
        start += 2;
    }
}

void print(int arr[], int n){
    for(int i=0; i < n; i++){
        cout << arr[i] << "-";
    }
}

int main(){
    cout << "Enter the size of an array";
    int n;
    cin >> n;
    int arr[n];
    cout << "Enter the values of an array";
    for(int i=0; i < n; i++){
        cin >> arr[i];
    }
    alternate(arr, n);
    print(arr, n);
}