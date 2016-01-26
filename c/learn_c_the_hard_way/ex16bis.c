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
struct Person Person_create(char *name, int age, int height, int weight) {
  // malloc will not throw an error if it can't allocate memory!
  struct Person who = {
    .name = strdup(name),
    .age = age,
    .height = height,
    .weight = weight
  };
  return who;
}

// Prints a struct Person.
void Person_print(struct Person who) {
  printf("Name %s\n", who.name);
  printf("\tAge: %d\n", who.age);
  printf("\tHeight: %d\n", who.height);
  printf("\tWeight: %d\n", who.weight);
}

int main(int argc, char *argv[]) {
  struct Person joe = Person_create("Joe Nash", 32, 64, 140);
  struct Person frank = Person_create("Frank Blank", 20, 72, 180);

  Person_print(joe);
  Person_print(frank);

  joe.age += 20;
  joe.height -= 2;
  joe.weight += 40;
  Person_print(joe);

  frank.age += 20;
  frank.weight += 20;
  Person_print(frank);

  return 0;
}
