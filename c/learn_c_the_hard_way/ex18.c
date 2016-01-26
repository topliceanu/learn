#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>


void die(const char *message) {
  if (errno) {
    perror(message);
  }
  else {
    printf("Error: %s\n", message);
  }
  exit(1);
}

// Create a new type, in this case a function pointer.
typedef int (*compare_cb)(int a, int b);

typedef int *(*sort_method)(int *numbers, int count, compare_cb cmp);

// Three implementations of the compare_cb function pointer type.
int sorted_order(int a, int b) {
  return a - b;
}

int reverse_order(int a, int b) {
  return b - a;
}

int strange_order(int a, int b) {
  if (a == 0 || b == 0) {
    return 0;
  }
  else {
    return a % b;
  }
}

int sorted_chars(char a, char b) {
  return a - b;
}

// numbers is a pointer to an array of ints.
int *bubble_sort(int *numbers, int count, compare_cb cmp) {
  int temp = 0;
  int i = 0;
  int j = 0;

  int *target = malloc(count * sizeof(int)); // array where to dump sorted data.
  if (!target) {
    die("Memory error.");
  }

  // copy the initial numbers into the target array.
  memcpy(target, numbers, count * sizeof(int));

  for (i = 0; i < count; i ++) {
    for (j = 0; j < count-1; j ++) {
      if (cmp(target[j], target[j+1]) > 0) {
        temp = target[j+1];
        target[j+1] = target[j];
        target[j] = temp;
      }
    }
  }
  return target;
}

int *selection_sort(int *numbers, int count, compare_cb cmp) {
  int i = 0;
  int j = 0;
  int min_pos = 0;
  int temp = 0;

  // Copy input array numbers into target.
  int *target = malloc(count * sizeof(int));
  if (target == NULL) {
    die("Memory error.");
  }
  memcpy(target, numbers, (count * sizeof(int)));

  for (i = 0; i < count-1; i ++) {
    min_pos = i;
    for (j = i; j < count; j ++) {
      if (cmp(numbers[j], numbers[min_pos]) > 0) {
        min_pos = j;
      }
    }
    if (min_pos != i) {
      temp = numbers[i];
      numbers[i] = numbers[min_pos];
      numbers[min_pos] = temp;
    }
  }

  return target;
}

void test_sorting(int *numbers, int count, sort_method sort, compare_cb cmp) {
  int i = 0;

  int *sorted = sort(numbers, count, cmp);
  if (!sorted) {
    die("Failed to sort as requested.");
  }

  for(i = 0; i < count; i ++) {
    printf("%d ", sorted[i]);
  }
  printf("\n");

  free(sorted);

  //extra: Print the ASM code of the cmp function in use.
  //unsigned char *data = (unsigned char *)cmp;
  //for (i = 0; i < 25; i ++) {
  //  printf("%02x:", data[i]);
  //}
}

int main(int argc, char *argv[]) {
  if (argc < 2) {
    die("Usage: ex18 4 3 1 5 7");
  }

  int count = argc - 1;
  int i = 0;
  char **inputs = argv + 1;

  int *numbers = malloc(count * sizeof(int));
  if (!numbers) {
    die("Memory error.");
  }

  for (i = 0; i < count; i ++) {
    numbers[i] = atoi(inputs[i]);
  }

  test_sorting(numbers, count, bubble_sort, sorted_order);
  test_sorting(numbers, count, bubble_sort, reverse_order);
  test_sorting(numbers, count, bubble_sort, strange_order);

  test_sorting(numbers, count, selection_sort, sorted_order);
  test_sorting(numbers, count, selection_sort, reverse_order);
  test_sorting(numbers, count, selection_sort, strange_order);

  free(numbers);

  return 0;
}
