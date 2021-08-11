#include <stdio.h>

int main()
{
    int vet[8];
    for(int i = 0; i < 8; i++){
        vet[i] = 0;
    }
    printf("Digite 8 números quaisquer : \n");
    for(int i = 0; i < 8; i++){
        scanf("%d",&vet[i]);
        if(i != 0){
            for(int j = 0; j < 7; j++){
                for(int k = j+1; k < 8; k++){
                    if(vet[k] != 0){
                        if(vet[j] > vet[k]){
                            int aux = vet[j];
                            vet[j] = vet[k];
                            vet[k] = aux;
                        }
                    }else{
                        break;
                    }
                }
            }
        }
    }
    printf("\n\nOs mesmos números, porém ordenados : ");
    for(int i = 0; i < 8; i++){
        printf("%d ",vet[i]);
    }
    return 0;
}