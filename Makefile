all:
	gcc -Wall ./sorting/merge_sort/merge_sort.c ./data/data.c ./utils/utils.c main.c -o ./bin/main

clean:
	rm -f ./bin/main