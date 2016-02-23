// Prevents the file from being included multiple time.
#ifndef _ex19_h
#define _ex19_h

#include "object.h"

// Create an anonymous struct and rename it to Monster.
typedef struct {
  Object proto;
  int hit_points;
} Monster;

int Monster_attack(void *self, int damage);
int Monster_init(void *self);

// I don't use the "typedef struct {..} <name>" syntax here because I need
// to declare pointers to the same type inside the type.
struct Room {
  Object proto;
  Monster *bad_guy;
  struct Room *north;
  struct Room *south;
  struct Room *east;
  struct Room *west;
};

typedef struct Room Room;

void *Room_move(void *self, Direction direction);
int Room_attack(void *self, int damage);
int Room_init(void *self);

struct Map {
  Object proto;
  Room *start;
  Room *location;
};

typedef struct Map Map;

void *Map_move(void *self, Direction direction);
int Map_attack(void *self, int damage);
int Map_init(void *self);

#endif
