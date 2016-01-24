#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Struct definition. Creates a new type called `struct Person`.
struct Person {
  char *name;
  int age;
  int height;
  int weight;
};

// Functions creates a new Person struct instance.
struct Person *Person_create(char *name, int age, int height, int weight) {
  // malloc will not throw an error if it can't allocate memory!
  struct Person *who = malloc(sizeof(struct Person));
  assert(who != NULL);

  who->name = strdup(name); // function of string.h
  who->age = age;
  who->height = height;
  who->weight = weight;

  return who;
}

struct Person Person_create_stack(char *name, int age, int height, int weight) {
  struct Person who;
  who.name = strdup(name);
  who.age = age;
  who.height = height;
  who.weight = weight;

  return who;
}

// Cleanup the memory of a struct Person instance.
void Person_destory(struct Person *who) {
  assert(who != NULL);

  free(who->name); // must free the name which is a pointer to a String.
  free(who); // free the structure itself.
}

// Prints a struct Person.
void Person_print(struct Person *who) {
  printf("Name %s\n", who->name);
  printf("\tAge: %d\n", who->age);
  printf("\tHeight: %d\n", who->height);
  printf("\tWeight: %d\n", who->weight);
}

int main(int argc, char *argv[]) {
  struct Person *joe = Person_create("Joe Nash", 32, 64, 140);
  struct Person *frank = Person_create("Frank Blank", 20, 72, 180);

  printf("Jeo is at memory location %p:\n", joe);
  Person_print(joe);

  printf("Frank is at memory location %p:\n", frank);
  Person_print(frank);

  joe->age += 20;
  joe->height -= 2;
  joe->weight += 40;
  Person_print(joe);

  frank->age += 20;
  frank->weight += 20;
  Person_print(frank);

  Person_destory(joe);
  Person_destory(frank);

  return 0;
}
