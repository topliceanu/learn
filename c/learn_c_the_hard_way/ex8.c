#include <stdio.h>

int main(int argc, char *argv[]) {
  char full_name[] = {'Z', 'e', 'd', ' ', 'A', '.', ' ', 'S', 'h', 'a', 'w', '\0'};
  int areas[] = {10, 12, 13, 14, 20};
  char name[] = "Zed";

  areas[0] = 100;
  name[1] = 'E';
  name[2] = 'D';

  areas[1] = name[1];
  printf("Elements of areas are {%d, %d, %d, %d}.\n", areas[0], areas[1], areas[2], areas[3]);

  printf("The size of an int: %ld.\n", sizeof(int)); // == 4B
  printf("The size of an long: %ld.\n", sizeof(long)); // == 8B
  printf("The size of an float: %ld.\n", sizeof(float)); // == 4B
  printf("The size of an double: %ld.\n", sizeof(double)); // == 8B
  printf("The size of an long double: %ld.\n", sizeof(long double)); // == 16B
  printf("The size of areas: %ld.\n", sizeof(areas)); // == 20B
  printf("The first area is %d, the 2nd %d.\n", areas[0], areas[1]);
  printf("The size of a char: %ld.\n", sizeof(char)); // == 1B
  printf("The size of name: %ld.\n", sizeof(name)); // == 3B
  printf("Last char in name is: %c.\n", name[3]); // == \0 - all string literals end in \0 - null character.
  printf("The number of chars: %ld.\n", sizeof(name) / sizeof(char)); // == 4
  printf("The size of the full name: %ld.\n", sizeof(full_name)); // == 12B
  printf("The number of characters in the full name: %ld.\n", sizeof(full_name) / sizeof(char)); // == 12
  printf("name=%s and full_name=%s\n", name, full_name);

  return 0;
}
