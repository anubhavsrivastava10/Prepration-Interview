#include<iostream>
using namespace std;

// XOR property --
// a ^ a = 0 -- same element xor is always 0
// 0 ^ b = b -- any element xor with 0 is that number itself

// You can also do this question with hashmap and check the count of each unique element

int unique(int arr[], int size){
    int ans = 0;
    for(int i=0; i<size; i++){
        ans = ans^arr[i];
    }
    return ans;
}

int main(){
    int arr[5] = {1,2,2,1,3};
    cout<< unique(arr, 5);
}