#include <stdio.h>

int main(int argc, char *argv[]) {
  int i = 0;

  if (argc == 1) {
    printf("Not enough arguments. At least one is required!\n");
  }
  else if (argc > 1 && argc < 4) {
    printf("Here are the arguments:\n");

    for (i = 1; i < argc; i++) {
      printf("(%d: %s), ", i, argv[i]);
    }
    printf("\n");
  }
  else {
    printf("You have too many arguments\n");
  }

  return 0;
}
