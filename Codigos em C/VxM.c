#include <stdio.h>

int main(){
    int mat[4][4], vH[4],vV[4];
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            scanf("%d",&mat[i][j]);
            if(j == 0){
                vH[i] = mat[i][j];
            }
            if(i == 0){
                vV[j] = mat[i][j];
            }
        }
    }
    printf("\n");
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            printf("%d ", mat[i][j]);
            if(mat[i][j] > vH[i]){
                vH[i] = mat[i][j];
            }
            if(mat[j][i] > vV[i]){
                vV[i] = mat[j][i];
            }
        }
        printf("\n");
    }
    printf("\n");
    for(int i = 0; i < 4; i++){
        printf("%d ",vH[i]);
    }
    printf("\n\n");
    for(int i = 0; i < 4; i++){
        printf("%d\n",vV[i]);
    }
    return 0;
}