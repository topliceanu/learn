#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

#include "object.h"

void Object_destroy(void *self) {
  Object *obj = self;
  if (obj) {
    if (obj->description) {
      free(obj->description);
    }
    free(obj);
  }
}

void Object_describe(void *self) {
  Object *obj = self;
  printf("%s.\n", obj->description);
}

// An interface of the initialization function.
// Should return >0 if the initialization is successfull, 0 if it failed.
int Object_init(void *self) {
  return 1;
}

void *Object_move(void *self, Direction direction) {
  printf("You can't go that direction.\n");
  return NULL;
}

int Object_attack(void *self, int damage) {
  printf("You can't attack that.\n");
  return 0;
}

void *Object_new(size_t size, Object proto, char *description) {
  if (!proto.init) {
    proto.init = Object_init;
  }
  if (!proto.describe) {
    proto.describe = Object_describe;
  }
  if (!proto.destroy) {
    proto.destroy = Object_destroy;
  }
  if (!proto.attack) {
    proto.attack = Object_attack;
  }
  if (!proto.move) {
    proto.move = Object_move;
  }

  // Create a pointer to a memory location with the size of the prototype.
  // Then store a pointer index of the prototype int he pointer.
  Object *el = calloc(1, size);
  *el = proto;

  // Copy over the description.
  el->description = strdup(description);

  // Initialize it with whatever init we were given.
  if (!el->init(el)) {
    el->destroy(el);
    return NULL;
  }
  else {
    return el;
  }
}
