#include <stdio.h>

int main(int argc, char *argv[]) {
  int ages[] = {23, 43, 12, 89, 2};
  char *names[] = {"Alan", "Frank", "Mary", "John", "Lisa"};

  // correctly determine the size of an array!
  int count = sizeof(ages) / sizeof(int);
  int i = 0;

  // List names and ages by indexing.
  i = 0;
  while (i < count) {
    printf("%s is %d years old.\n", names[i], ages[i]);
    i += 1;
  }
  printf("----\n");

  // Setup the pointers to the start of the arrays and iterate.
  int *cur_age = ages;
  char **cur_name = names;

  i = 0;
  while (i < count) {
    printf("%s is %d years old.\n", *(cur_name + i), *(cur_age + i));
    i += 1;
  }
  printf("----\n");

  // Pointers are like arrays.
  i = 0;
  while (i < count) {
    printf("%s is %d years old\n", cur_name[i], cur_age[i]);
    i += 1;
  }
  printf("----\n");

  // Pointer in a stupid complex way.
  cur_age = ages;
  cur_name = names;
  while (cur_age - ages < count) {
    printf("%s is %d years old\n", *cur_name, *cur_age);
    cur_age += 1;
    cur_name += 1;
  }
  printf("----\n");

  // extra: print out arguments as pointers.
  char **arguments = argv;
  for (i = 0; i < argc; i++) {
    printf("argument %d is %s.\n", i, *(arguments + i));
  }
  printf("----\n");

  // extra: print the addresses of the pointers.
  for (i = 0; i < count; i++) {
    printf("%d: name address %p and age address %p.\n",
            i, (cur_name + i), (cur_age + i));
  }

  return 0;
}
