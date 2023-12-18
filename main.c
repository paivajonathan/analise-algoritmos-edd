#include <stdio.h>
#include <time.h>

#include "./data/data.h"
#include "./utils/utils.h"

#include "./sorting/merge_sort/merge_sort.h"
#include "./sorting/quick_sort/quick_sort.h"

#include "./sorting/insertion_sort/insertion_sort.h"
#include "./sorting/selection_sort/selection_sort.h"

#include "./sorting/heap_sort/heap_sort.h"
#include "./sorting/tim_sort/tim_sort.h"

int main(void) 
{ 
    clock_t start, end;
    double time_taken;
    int arr_size = LARGE_DATA_SIZE;
    
    start = clock();
    timSort(large_reversed_data, arr_size);
    end = clock();

    time_taken = (double) (end - start) / CLOCKS_PER_SEC;
    printf("Time taken in seconds: %f\n", time_taken);

    return 0; 
}
