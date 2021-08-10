#include <stdio.h>

int main()
{
    int n1,n2;
    printf("Informe a resolução da matriz ([X][Y]) : ");
    scanf("%d%d",&n1,&n2);
    int mat[n1][n2], qtdPar, qtdImpar, nMat;
    qtdPar = 0;
    qtdImpar = 0;
    nMat = n1*n2;
    printf("Digite os %d numeros : \n",nMat);
    for(int i = 0; i < n1; i++){
        for(int j = 0; j < n2; j++){
            scanf("%d",&mat[i][j]);
            if(mat[i][j]%2==0){
                qtdPar++;
            }else{
                qtdImpar++;
            }
        }
    }
    if(qtdPar > qtdImpar){
        printf("Há mais numeros pares do que ímpares!");
    }else if(qtdImpar > qtdPar){
        printf("Há mais numeros ímpares do que pares!");
    }else{
        printf("Há um balanceamento na matriz entre numeros pares e ímpares!");
    }
    return 0;
}