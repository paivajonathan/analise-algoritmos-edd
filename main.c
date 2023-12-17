#include <stdio.h>
#include <time.h>

#include "./data/data.h"
#include "./utils/utils.h"

#include "./sorting/merge_sort/merge_sort.h"
#include "./sorting/quick_sort/quick_sort.h"

#include "./sorting/insertion_sort/insertion_sort.h"
#include "./sorting/selection_sort/selection_sort.h"

int main(void) 
{ 
    clock_t start, end;
    double time_taken;

    int arr_size = MEDIUM_DATA_SIZE; 
  
    printf("Given array is \n"); 
    printArray(medium_reversed_data, arr_size); 
    
    start = clock();
    selectionSort(medium_reversed_data, arr_size);
    end = clock();

    time_taken = (double) (end - start) / CLOCKS_PER_SEC;

    printf("\nSorted array is \n"); 
    printArray(medium_reversed_data, arr_size);
    
    printf("Time taken in seconds: %f\n", time_taken);
    return 0; 
}
