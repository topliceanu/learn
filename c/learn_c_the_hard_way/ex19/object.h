// the following CPP instructions prevent this file from being loaded twice.
#ifndef _object_h
#define _object_h

typedef enum {
  NORTH, SOUTH, EAST, WEST
} Direction;

// define an anonymous struct and name it Object.
typedef struct {
  char *description;
  int (*init)(void *self);
  void (*describe)(void *self);
  void (*destroy)(void *self);
  void *(*move)(void *self, Direction direction);
  int (*attack)(void *self, int damage);
} Object;

int Object_init(void *self);
void Object_destroy(void *self);
void Object_describe(void *self);
void *Object_move(void *self, Direction direction);
int Object_attack(void *self, int damage);
void *Object_new(size_t size, Object proto, char *description);

// Macro: Syntactic sugar, let you call the familiar NEW to create a new object
// from a prototype object.
// T##Proto means add "Proto" to the back of the name T.
#define NEW(T, N) Object_new(sizeof(T), T##Proto, N)

// Macro: Syntactic sugar, let's you write `obj->proto.blah` as
// simply as `obj->_(blah)`
#define _(N) proto.N

#endif
