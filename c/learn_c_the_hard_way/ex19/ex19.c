#include <assert.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "ex19.h"


int Monster_attack(void *self, int damage) {
  assert(self != NULL);
  // Cast the pointer self to type (Monster *).
  Monster *monster = self;
  // printf("You attach %s!\n", monster->proto.description());
  printf("You attack %s!\n", monster->_(description));

  monster->hit_points -= damage;

  if (monster->hit_points > 0) {
    printf("It is still alive.\n");
    return 0;
  }
  else {
    printf("It is dead!\n");
    return 1;
  }
}

int Monster_init(void *self) {
  assert(self != NULL);
  Monster *monster = self;
  monster->hit_points = 10;
  return 1;
}

Object MonsterProto = {
  .init = Monster_init,
  .attack = Monster_attack
};

void *Room_move(void *self, Direction direction) {
  assert(self != NULL);
  Room *room = self;
  Room *next = NULL;

  if (direction == NORTH && room->north) {
    printf("You go north, into:\n");
    next = room->north;
  }
  else if (direction == SOUTH && room->south) {
    printf("You go south, into:\n");
    next = room->south;
  }
  else if (direction == WEST && room->west) {
    printf("You go west, into:\n");
    next = room->west;
  }
  else {
    printf("You can't go that direction.");
    next = NULL;
  }

  if (next) {
    // next->proto.describe(next);
    next->_(describe)(next);
  }
  return next;
}

int Room_attack(void *self, int damage) {
  assert(self != NULL);
  // Cast self variable into type (Room *).
  Room *room = self;
  Monster *monster = room->bad_guy;

  if (monster) {
    // monster->proto.attack(monster, damage);
    monster->_(attack)(monster, damage);
    return 1;
  }
  else {
    printf("You flail in the air at nothing. Idiot!\n");
    return 0;
  }
}

Object RoomProto = {
  .move = Room_move,
  .attack = Room_attack
};

void *Map_move(void *self, Direction direction) {
  assert(self != NULL);
  Map *map = self;
  Room *location = map->location;
  Room *next = NULL;

  // next = location->proto.move(location, direction);
  next = location->_(move)(location, direction);

  if (next) {
    map->location = next;
  }
  return next;
}

int Map_attack(void *self, int damage) {
  assert(self != NULL);
  Map *map = self;
  Room *location = map->location;

  // return location->proto.attack(location, damage);
  return location->_(attack)(location, damage);
}

int Map_init(void *self) {
  assert(self != NULL);
  Map *map = self;

  // Create the amp.
  // Room *hall = Object_new(sizeof(Room), RoomProto, "The great Hall");
  Room *hall = NEW(Room, "The great Hall");
  // Room *throne = Object_new(sizeof(Room), RoomProto, "The throne room");
  Room *throne = NEW(Room, "The throne room");
  // Room *arena = Object_new(sizeof(Room), RoomProto, "The throne room");
  Room *arena = NEW(Room, "The arena, with the minotaur");
  // Room *kitchen = Object_new(sizeof(Room), RoomProto, "The throne room");
  Room *kitchen = NEW(Room, "Kitchen, you have a knife now");

  // Puth the bad guy in the arena.
  // arena->bad_guy = Object_new(sizeof(Monster), MonsterProto, "The evil minotaur");
  arena->bad_guy = NEW(Monster, "The evil minotaur");

  // Setup the map rooms.
  hall->north = throne;
  throne->west = arena;
  throne->east = kitchen;
  throne->south = hall;
  arena->east = throne;
  kitchen->west = throne;

  // Start the map and the character off in the hall.
  map->start = hall;
  map->location = hall;

  return 1;
}

Object MapProto = {
  .init = Map_init,
  .move = Map_move,
  .attack = Map_attack
};

int process_input (Map *game) {
  assert(game != NULL);
  printf("\n> ");

  // Each the ENTER typed after the command character above.
  char ch = getchar();
  assert(ch != EOF);
  getchar();

  int damage = rand() % 4;

  switch (ch) {
    case -1:
      printf("Givin up? You suck.\n");
      return 0;
      break;
    case 'h':
      printf("l - prints which directions are available\n");
      printf("n - move to the north room\n");
      printf("s - move to the south room\n");
      printf("e - move to the east room\n");
      printf("w - move to the west room\n");
      printf("a - attack whoeven is in the current root\n");
      break;
    case 'n':
      // game->proto.move(game, NORTH);
      game->_(move)(game, NORTH);
      break;
    case 's':
      // game->proto.move(game, SOUTH);
      game->_(move)(game, SOUTH);
      break;
    case 'e':
      // game->proto.move(game, EAST);
      game->_(move)(game, EAST);
      break;
    case 'w':
      // game->proto.move(game, WEST);
      game->_(move)(game, WEST);
      break;
    case 'a':
      // game->proto.attack(game, damage);
      game->_(attack)(game, damage);
      break;
    case 'l':
      printf("You can go:\n");
      if (game->location->north) {
        printf("NORTH\n");
      }
      if (game->location->south) {
        printf("SOUTH\n");
      }
      if (game->location->east) {
        printf("EAST\n");
      }
      if (game->location->west) {
        printf("WEST\n");
      }
      break;
    default:
      printf("What?: %d\n", ch);
  }
  return 1;
}

int main(int argc, char *argv[]) {
  srand(time(NULL));

  // Map *game = Object_new(sizeof(Map), MapProto, "The Hall of the Minotaur");
  Map *game = NEW(Map, "The Hall of the Minotaur.");

  printf("You enter the ");
  // game->location->proto.describe(game->location);
  game->location->_(describe)(game->location);

  while(process_input(game)) {
  }

  return 0;
}
