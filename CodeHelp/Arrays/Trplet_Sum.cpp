vector<vector<int>> findTriplets(vector<int>arr, int n, int K) {
   vector<vector<int>>ans;
   int left, right;
   sort(arr.begin(),arr.end());
   for(int i=0; i<n; i++)
   {
      left = i+1;
      right = n-1;
      while(left<right)
      {
          if(arr[i]+arr[left]+arr[right] == K)
          {
              ans.push_back({arr[i],arr[left],arr[right]});

                //remove duplicate left and right element for same ith element
                
              		int x = arr[left];
              		int y = arr[right];
      		
              		while(left< right && arr[left] == x )
              		{
                  		left++;
              		}
              		while(left<right && arr[right] == y )
              		{
                  		right--;
              		}
          }
          else if(arr[i]+arr[left]+arr[right] < K)
          {
              left++;
          }
          else
              right--;
      }
      
      // Start i from next element
      while(arr[i] == arr[i+1] && i<n-1)
      {
          i++;
      }
   }
   return ans;
}