#include<stdio.h>
int main(){
int arr[]={16,17,4,3,5,2};   // array declaration
int n = sizeof(arr)/sizeof(arr[0]); // this line finds the total no of elements in array
int leaders[n]; // this is another array ..that will store the leader elements
int count=0;// this keeps track of how many leaders found
int max = arr[n-1]; // last element always a leader
leaders[count++]=max; // i.e leaders[0]=2,count=1

for(int i= n-2;i>=0;i--) // this loop runs from right to left
{ if(arr[i]>max){
    max = arr[i];
    leaders[count++]=max;
} }
 
printf("Leaders are: ");
for(int i =count-1;i>=0;i--) // this prints leaders in reverse order
{
printf("%d",leaders[i]);
}
return 0;
}