all:
	gcc -Wall ./sorting/merge_sort/merge_sort.c ./sorting/quick_sort/quick_sort.c ./sorting/insertion_sort/insertion_sort.c ./sorting/selection_sort/selection_sort.c ./sorting/heap_sort/heap_sort.c ./data/data.c ./utils/utils.c main.c -o ./bin/main

clean:
	rm -f ./bin/main