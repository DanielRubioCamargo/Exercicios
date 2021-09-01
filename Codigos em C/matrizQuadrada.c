#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int mat[n][n];
    mat[0][0] = 1;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(i == 0 && j == 0){
                continue;
            }
            if(i == 0){
                if(j != 0){
                    mat[i][j]  = mat[i][j-1] * 2;
                }
            }else{
                mat[i][j] = mat[i-1][j] * 2;
            }
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            printf("%d ",mat[i][j]);
        }
        printf("\n");
    }
    return 0;
}