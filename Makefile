all:
	gcc -Wall ./sorting/merge_sort/merge_sort.c ./sorting/quick_sort/quick_sort.c ./data/data.c ./utils/utils.c main.c -o ./bin/main

clean:
	rm -f ./bin/main