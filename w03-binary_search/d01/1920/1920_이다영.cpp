#include <stdio.h>

int compare(void *a, void *b){
    int x=*(int*)a;
    int y=*(int*)b;
    
    if(x<y) return -1;
    if(x>y) return 1;
    return 0;
}

int binarySearch(int arr[],int n, int target){
    int left=0,right=n-1;
    while(left<=right){
        int mid=(left+right)/2;
        if(arr[mid]==target) return 1;
        else if(arr[mid]<target) left=mid+1;
       else right=mid-1;}
    return 0;
}

int main(){
    int N;
    scanf("%d",&N);
    
    int A[100000];
    for(int i=0;i<N;i++){
        scanf("%d",&A[i]);
    }
    
    qsort(A,N,sizeof(int),compare);
    
    int M;
   scanf("%d",&M);
    
    for(int i=0;i<M;i++){
        int x;
        scanf("%d",&x);
        printf("%d\n",binarySearch(A,N,x));
    }
    return 0;
}










