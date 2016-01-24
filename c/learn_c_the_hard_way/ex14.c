#include <stdio.h>
#include <ctype.h>
#include <string.h>


int can_print_it(char ch);
void print_letters(int len, char arg[]);


void print_arguments(int argc, char *argv[]) {
  int i;
  int len;
  for (i = 1; i < argc; i ++) {
    len = strlen(argv[i]);
    print_letters(len, argv[i]);
  }
}

void print_letters(int len, char arg[]) {
  int i;
  char ch;
  for (i = 0; i < len; i++) {
    ch = arg[i];

    //if (isdigit(ch)) {
    if (isalpha(ch) || isblank(ch)) {
      printf("'%c' == %d ", ch, ch);
    }
  }
  printf("\n");
}

int main(int argc, char *argv[]) {
  print_arguments(argc, argv);
  return 0;
}
