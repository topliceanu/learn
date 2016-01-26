#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// A stack data structure.
struct StackNode {
  char *value;
  struct StackNode *next;
};

// Creates a single node
struct StackNode *StackNode_create(char *value) {
  struct StackNode *new_node = malloc(sizeof(struct StackNode));
  assert(new_node != NULL);

  new_node->value = value;
  return new_node;
}

// Push a new value into the stack's head.
void StackNode_push(struct StackNode **head, char *value) {
  assert(head != NULL);

  struct StackNode *new_node = StackNode_create(value);
  new_node->next = *head;
  head = &new_node;
}

// Pop the value from the head of the stack, then rewire the new head.
char *StackNode_pop(struct StackNode **head) {
  assert(head != NULL);
  char *value = (*head)->value;
  *head = (*head)->next;
  return value;
}

int main(int argc, char *argv[]) {
  struct StackNode *head = StackNode_create("First");
  StackNode_push(&head, "Second");
  StackNode_push(&head, "Third");

  printf("Stack pop: %s\n", StackNode_pop(&head));
  printf("Stack pop: %s\n", StackNode_pop(&head));
  printf("Stack pop: %s\n", StackNode_pop(&head));
  printf("Stack pop: %s\n", StackNode_pop(&head));

  return 0;
}
