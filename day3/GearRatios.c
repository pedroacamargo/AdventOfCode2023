#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int initMatrix(char ** matrix, FILE * fptr) {
    char line[150];
    int i = 0;

    while (fgets(line, sizeof(line), fptr)) {
        char * a = calloc(strlen(line), sizeof(char));
        strcpy(a, line);
        matrix[i] = a;
        i++;
    }
    
    return i;
}

void printMatrix(char ** matrix, int lines) {
    for (int i = 0; i < lines; i++) {
        printf("%s", matrix[i]);
    }
}

int getNumber(char ** matrix, int i, int j) {
    char number[10]= "";
    int exit = 0;

    for (int k = i - 1; k <= i + 1 && !exit; k++) {
        for (int l = j - 1; l <= j + 1 && !exit; l++) {
            // printf("k: %d, l: %d\n", k, l);
            

            if (k >= 0 && l >= 0 && k < strlen(matrix[0]) - 1 && l < strlen(matrix[0]) - 1) {
                if (matrix[k][l] <= '9' && matrix[k][l] >= '0') {
                    // get first number
                    while (matrix[k][l] <= '9' && matrix[k][l] >= '0') {
                        if (l == 0 || matrix[k][l - 1] == ' ' || matrix[k][l - 1] == '.' || matrix[k][l - 1] == 'x') break;
                        l--;
                    }

                    while (matrix[k][l] <= '9' && matrix[k][l] >= '0') {
                        if (matrix[k][l] == ' ') break;
                        number[strlen(number)] = matrix[k][l];
                        matrix[k][l] = ' ';
                        l++;
                    }


                    exit = 1;

                }
            }

        }        
    }

    // printf("number: %s\n", number);
    int finalNumber = atoi(number);


    return finalNumber;
}

int colorAdjacent(char ** matrix, int y, int x) {
    int finalNumber = 0;
    for (int i = y - 1; i <= y + 1; i++) {
        for (int j = x - 1; j <= x + 1; j++) {
            if (i >= 0 && j >= 0 && i < strlen(matrix[0]) - 1 && j < strlen(matrix[0]) - 1) {
                if (matrix[i][j] < '0' || matrix[i][j] > '9'){
                    if (matrix[i][j] == '.' || matrix[i][j] == ' ') {
                        matrix[i][j] = ' ';
                        // getchar();
                        // printMatrix(matrix, 10);
                    } else if (matrix[i][j] < 'a' || matrix[i][j] > 'z' || matrix[i][j] < 'A' || matrix[i][j] > 'Z' || matrix[i][j] == 'x') {

                        matrix[i][j] = 'x';

                        // printMatrix(matrix, 10);
                        // printf("i: %d, j: %d\n", i, j);
                        // getchar();

                        finalNumber = getNumber(matrix, i, j);
                        // printf("number: %d\n", finalNumber);
                    } 
                }
            }
        }
    }
    return finalNumber;
}

void manipulateMatrix(char ** matrix, int lines) {
    int cols = strlen(matrix[0]);
    int rows = lines;
    int sum = 0;

    printMatrix(matrix, rows);
    getchar();
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {

            if (matrix[i][j] <= '9' && matrix[i][j] >= '0') {
                sum += colorAdjacent(matrix, i, j);
            }

        }
    }

    printf("sum: %d\n", sum);
    getchar();
}

int main() {
    FILE *fptr;
    fptr = fopen("input.txt", "r");

    if (fptr == NULL) {
        printf("Error opening file");
        exit(1);
    }

    char ** matrix;

    int lines = initMatrix(matrix, fptr);
    // printMatrix(matrix, lines);
    manipulateMatrix(matrix, lines);



    fclose(fptr);

    return 1;
}