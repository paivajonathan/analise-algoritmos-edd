#include <stdio.h>
#include <time.h>
#include "./sorting/merge_sort/merge_sort.h"
#include "./data/data.h"
#include "./utils/utils.h"
 
// Driver code 
int main(void) 
{ 
    clock_t start, end;
    double time_taken;

    int arr_size = LARGE_DATA_SIZE; 
  
    printf("Given array is \n"); 
    printArray(large_ordered_data, arr_size); 
    
    start = clock();
    mergeSort(large_ordered_data, 0, arr_size - 1); 
    end = clock();

    time_taken = (double) (end - start) / CLOCKS_PER_SEC;

    printf("\nSorted array is \n"); 
    printArray(large_ordered_data, arr_size);
    
    printf("Time taken in seconds: %f\n", time_taken);
    return 0; 
}
