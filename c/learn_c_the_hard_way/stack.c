#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// A stack data structure implemented as a simple linked list.

struct Node {
  char *value;
  struct Node *next;
};

struct Stack {
  struct Node *head;
  int max_num_nodes;
  int num_nodes;
};

// Creates a new stack structure.
struct Stack *Stack_create(int max_num_nodes) {
  struct Stack *new_stack = malloc(sizeof(struct Stack));
  assert(new_stack != NULL);
  new_stack->max_num_nodes = max_num_nodes;
  new_stack->num_nodes = 0;
  new_stack->head = NULL;
  return new_stack;
}

// Adds a new string value to a stack.
void Stack_push(struct Stack *stack, char *value) {
  if (stack->num_nodes >= stack->max_num_nodes) {
    return; // Does not accept new values anymore.
  }

  struct Node *new_node = malloc(sizeof(struct Node));
  assert(new_node != NULL);

  new_node->value = value;
  new_node->next = stack->head;
  stack->head = new_node;
  stack->num_nodes += 1;
}

// Returns the value in the stack or NULL if the stack is empty.
char *Stack_pop(struct Stack *stack) {
  assert(stack != NULL); // throw Error.
  struct Node *head = stack->head;
  if (head == NULL) {
    return NULL;
  }
  char *value = head->value;
  stack->head = stack->head->next;
  stack->num_nodes -= 1;
  free(head);

  return value;
}

// Deletes the stack by removing all nodes and dealocating all memory.
void Stack_delete(struct Stack *stack) {
  while (Stack_pop(stack) != NULL) {}
  free(stack);
}

int main(int argc, char *argv[]) {
  struct Stack *stack1 = Stack_create(5);
  Stack_push(stack1, "First");
  Stack_push(stack1, "Second");
  Stack_push(stack1, "Third");

  printf("Stack pop: %s\n", Stack_pop(stack1));
  printf("Stack pop: %s\n", Stack_pop(stack1));
  printf("Stack pop: %s\n", Stack_pop(stack1));
  printf("Stack pop: %s\n", Stack_pop(stack1));

  Stack_delete(stack1);

  struct Stack *stack2 = Stack_create(3);
  Stack_push(stack2, "First");
  Stack_push(stack2, "Second");
  Stack_push(stack2, "Third");
  Stack_push(stack2, "Fourth");

  printf("Stack pop: %s\n", Stack_pop(stack2));
  printf("Stack pop: %s\n", Stack_pop(stack2));
  printf("Stack pop: %s\n", Stack_pop(stack2));
  printf("Stack pop: %s\n", Stack_pop(stack2));

  return 0;
}
