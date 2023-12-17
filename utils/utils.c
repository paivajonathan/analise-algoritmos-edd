#include <stdio.h>

// UTILITY FUNCTIONS 
// Function to print an array 
void printArray(int array[], int size)
{ 
    for (int i = 0; i < size; i++) 
        printf("%d ", array[i]); 
    printf("\n"); 
}

// function to swap the the position of two elements
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
