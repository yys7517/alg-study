#include<bits/stdc++.h>
using namespace std;
int n,q;
itn size;
int a[64][64];
int dx[] ={-1,1,0,0};
int dy[] = {0,0,1,-1};

void rotate(int x, int y, int len){
    int temp[64][64]; 
    //x,y를 시작점으로 l^2크기만큼 회전
    for(int i = 0; i <len;i++){
        for(int j = 0; j<len; j++){
            temp[i][j] = a[x + len -j-1][y +i];
        }
    }

    //임시 배열을 원래 배열에 복사
    for(int i=0; i<len;i++){
        for(int j=0; j<len;j++){
            a[x+i][y+j] = temp[i][j];
        }
    }
}

void fireStorm(int l){
    int len = (1<<l);

    for(int i=0; i<size;i+=len){
        for(int j=0; j<size; j+=len){
            rotate(i,j,len);
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin >> n >> q;
    size = (1<<n);

    for(int i=0; i<size;i++){
        for(int j=0; j< size; j++){
            cin >> a[i][j];
        }
    }
    for(int i=0; i<q; i++){
        int l;
        cin >> l;
        fireStorm(l);
        
        }
    }
    return 0;
}