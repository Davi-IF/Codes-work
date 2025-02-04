#include<stdio.h>
#include<string.h>

int main(){

    char A[100], B[100];    
    int i, j=0;

    printf("digite caracteres do vetor A:");
    fgets(A, sizeof(A), stdin);

    for(i=0; i<strlen(A); i++){
        if(A[i]!=' '){
            B[j]=A[i];
            j++;
        }
    }

    B[j] = '\0';
    printf("vetor resultante: %s \n", B);

    return 0;
}