#include<iostream>
using namespace std;

int main(){
    int arr[10];
    // Fill each element of an array with a default value
    std::fill_n(arr, 10, -1);
    for(int i=0;i<10;i++){
        cout<<arr[i]<<"-";
    }
}