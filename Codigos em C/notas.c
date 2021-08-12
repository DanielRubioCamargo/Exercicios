#include <stdio.h>

int main()
{
    int qtdAlunos;
    printf("Insira a quantidades de alunos na sala : ");
    scanf("%d",&qtdAlunos);
    float notas[qtdAlunos],mediaDaSala,acmNotas;
    acmNotas = 0.0;
    for(int i = 0; i < qtdAlunos; i++){
        printf("Olá aluno de número %d!\nInsira sua nota : ",i+1);
        scanf("%f",&notas[i]);
        printf("-------------------------------------------\n");
        acmNotas+=notas[i];
    }
    mediaDaSala = acmNotas/qtdAlunos;
    printf("Media da sala : %.1f\n\n",mediaDaSala);
    printf("Quer saber a nota mais alta da turma e de quem foi? (1 = sim/0 = não) : ");
    int resp;
    scanf("%d",&resp);
    if(resp == 1){
        float maior = 0;
        int melhor = 0;
        for(int i = 0; i < qtdAlunos; i++){
            if(notas[i] > maior){
                maior = notas[i];
                melhor = i+1;
            }
        }
        printf("A maior nota encontrada foi %.1f!\nAlunos que atingiram essa nota : \n",maior);
        for(int i = 0; i < qtdAlunos; i++){
            if(notas[i] == maior){
                printf("-> Aluno número %d, Parabens!\n",i+1);
            }
        }
    }else{
        printf("Adeus!");
    }
    return 0;
}