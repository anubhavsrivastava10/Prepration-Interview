#include<iostream>
using namespace std;

// XOR property --
// a ^ a = 0 -- same element xor is always 0
// 0 ^ b = b -- any element xor with 0 is that number itself

// You can also do this question with hashmap and check the count of each unique element

int findDuplicate(int arr[], int size) 
{
    // Write your code here
	int ans = 0;
    for(int i=0; i<size; i++){
        ans = ans ^ arr[i];
    }
    for(int i=1;i<size;i++){
        ans = ans ^ i;
    }
    return ans;
}

int main(){
    int arr[5] = {1,2,2,4,3};
    cout<< findDuplicate(arr, 5);
}