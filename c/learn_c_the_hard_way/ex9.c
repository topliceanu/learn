#include <stdio.h>

int main(int argc, char *argv[]) {
  int numbers[4] = {5};
  char name[4] = {'a'};
  //char *name = "a\0\0\0"; // SIGSEGV

  printf("numbers: %d %d %d %d\n", numbers[0], numbers[1], numbers[2], numbers[3]);
  printf("chars in name: %c %c %c %c\n", name[0], name[1], name[2], name[3]);
  printf("name is: %s\n", name);

  // set the numbers.
  numbers[0] = 1;
  numbers[1] = 2;
  numbers[2] = 3;
  numbers[3] = 4;

  // setup the name.
  name[0] = 'Z';
  name[1] = 'e';
  name[2] = 'd';

  // initialized.
  printf("initialized numbers: %d %d %d %d\n", numbers[0], numbers[1], numbers[2], numbers[3]);
  printf("initialized chars: %c %c %c %c\n", name[0], name[1], name[2], name[3]);
  printf("initialized name is: %s\n", name);

  // another way to use name.
  char *another = "Zed";
  printf("another name: %s\n", another);
  printf("another chars: %c %c %c %c\n", another[0], another[1], another[2], another[3]);

  // extra: assign chars into numbers.
  numbers[1] = 'Z';
  numbers[2] = 'e';
  numbers[3] = 'd';
  printf("assinging chars into numbers: %d %d %d %d\n", numbers[0], numbers[1], numbers[2], numbers[3]);

  // extra: assign numbers into string.
  name[0] = 1;
  name[1] = 2;
  name[2] = 3;
  printf("initialized chars: %c %c %c %c\n", name[0], name[1], name[2], name[3]);

  // extra: cast 4 chars into one int.
  name[0] = 1;
  name[1] = 1;
  name[2] = 1;
  name[3] = 1;
  int x = *(int *)numbers;
  printf("converting from string to int %d.\n", x);

  return 0;
}
