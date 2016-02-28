#include <stdio.h>

int left_child(int parent);
int right_child(int parent);
//int inter_change(int *list, int pos1, int pos2);

//int min_heap_heapify(int *list[]) {}
//
//int min_heap_insert(int *list[], int value) {}
//
//int min_heap_extract_min(int *list[]) {}
//
//int min_heap_replace(int *list[], int value) {}
//
//int min_heap_merge(int *first[], int *second[], int *result) {}
//
//int min_heap_shift_up(int *list[], int pos) {
//  int list_size = sizeof(list) / sizeof(int);
//  int left_pos = left_child(pos);
//  int right_pos = right_child(pos);
//}

//int min_heap_shift_down(int *list[], int pos) {
//  int list_size = sizeof(*list) / sizeof(int);
//  int left_pos = left_child(pos);
//  int right_pos = right_child(pos);
//
//  if (left_pos < list_size && *list[pos] > *list[left_pos]) {
//    inter_change(list, pos, left_pos);
//    min_heap_shift_down(list, left_pos);
//  }
//}

int left_child(int parent) {
  return parent * 2 + 1;
}

int right_child(int parent) {
  return parent * 2 + 2;
}

int inter_change(int **list, int pos1, int pos2) {
  int list_size = sizeof(**list) / sizeof(int);
  if (pos1 < 0 || pos1 > list_size || pos2 < 0 || pos2 > list_size) {
    return 1;
  }

  int tmp = *list[pos1];
  *list[pos1] = *list[pos2];
  *list[pos2] = tmp;
  return 0;
}
