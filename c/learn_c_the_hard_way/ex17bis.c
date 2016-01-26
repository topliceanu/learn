// Same as ex17.c but with the conn instance being globally shared.

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define MAX_DATA 512
#define MAX_ROWS 100


// Data Structures.

struct Address {
  int id;
  int set;
  char name[MAX_DATA];
  char email[MAX_DATA];
};

struct Database {
  struct Address rows[MAX_ROWS];
};

struct Connection {
  FILE *file;
  struct Database *db;
};

// Functions.

struct Connection *conn;

void Database_close();

// Stops the current process with a message.
void die(const char *message) {
  if (errno) {
    perror(message);
  }
  else {
    printf("Error: %s\n", message);
  }
  if (conn != NULL) {
    Database_close();
  }
  exit(1);
}

// Prints a "row" in the database.
void Address_print(struct Address *addr) {
  printf("%d %s %s\n", addr->id, addr->name, addr->email);
}

// Loads the database file into memory.
void Database_load() {
  int rc = fread(conn->db, sizeof(struct Database), 1, conn->file);
  if (rc != 1) {
    die("Failed to load database.");
  }
}

// Creates a new Connection, opening a storage file and loading the database.
// Params:
//    mode - can only be 'c' which means write only.
struct Connection *Database_open(const char *filename, char mode) {
  conn = malloc(sizeof(struct Connection));
  if (conn == NULL) {
    die("Memory error");
  }

  conn->db = malloc(sizeof(struct Database));
  if (conn->db == NULL) {
    die("Memory error");
  }

  if (mode == 'c') {
    conn->file = fopen(filename, "w");
  }
  else {
    conn->file = fopen(filename, "r+");
    if (conn->file) {
      Database_load(conn);
    }
  }

  if (conn->file ==  NULL) {
    die("Failed to open the file");
  }

  return conn;
}

// Close a database by closing the underlying file and freeing the connection memory.
void Database_close() {
  if (conn) {
    if (conn->file) {
      fclose(conn->file);
    }
    if (conn->db) {
      free(conn->db);
    }
    free(conn);
  }
}

// Write the entire database to a file.
void Database_write() {
  rewind(conn->file);

  int rc = fwrite(conn->db, sizeof(struct Database), 1, conn->file);
  if (rc != 1) {
    die("Failed to write database.");
  }

  rc = fflush(conn->file);
  if (rc == -1) {
    die("Cannot flush database to file.");
  }
}

// Initialize the database by storing empty values for all available address slots.
void Database_create() {
  int i = 0;
  for (i = 0; i < MAX_ROWS; i++) {
    // Make a prototype to initialize it.
    struct Address addr = {.id = i, .set = 0};
    // then assign it.
    conn->db->rows[i] = addr;
  }
}

// Update the Address on a given row id.
void Database_set(int id, const char *name, const char *email) {
  struct Address *addr = &conn->db->rows[id];
  if (addr->set) {
    die("Already set, delete it first.");
  }

  addr->set = 1;
  // WARNING: this is a bug, because copying MAX_DATA bytes from name into addr->name
  // might not copy a null char as well and cause overflow.
  char *res = strncpy(addr->name, name, MAX_DATA);
  if (res == NULL) {
    die("Name copy failed.");
  }
  // Correctly overwrite the last character in the string.
  addr->name[MAX_DATA-1] = '\0';

  // WARNING: see above.
  res = strncpy(addr->email, email, MAX_DATA);
  if (res == NULL) {
    die("Email copy failed");
  }
  // Correctly overwrite the last character in the string.
  addr->email[MAX_DATA-1] = '\0';
}

// Prints the value of an address given by id.
void Database_get(int id) {
  struct Address *addr = &conn->db->rows[id];
  if (addr->set) {
    Address_print(addr);
  }
  else {
    die("ID is not set");
  }
}

void Database_find_by_name(const char *name) {
  int i;
  struct Address *addr;
  for (i = 0; i < MAX_ROWS; i ++) {
    addr = &conn->db->rows[i];
    if (addr->set && *addr->name == *name) {
      Address_print(addr);
      return;
    }
  }
}

// Clears a row corresponding to id in the database.
void Database_delete(int id) {
  struct Address addr = {.id = id, .set = 0};
  // Assigns one struct (addr) to another conn->db->rows[i]. C handles the copying.
  conn->db->rows[id] = addr;
}

void Database_list() {
  int i = 0;
  struct Database *db = conn->db;

  printf("Database size: %lu.\n", sizeof(*db));
  for (i = 0; i < MAX_ROWS; i ++) {
    struct Address *addr = &db->rows[i];

    if (addr->set) {
      Address_print(addr);
    }
  }
}

// Main.

int main(int argc, char *argv[]) {
  if (argc < 3) {
    die("Usage: ex17 <dbfile> <action> [action params]");
  }

  char *filename = argv[1];
  char action = argv[2][0];
  int id = 0;
  conn = Database_open(filename, action);

  if (argc > 3) {
    id = atoi(argv[3]);
  }

  if (id >= MAX_ROWS) {
    die("There's not that many records");
  }

  switch (action) {
    case 'c':
      Database_create();
      Database_write();
      break;
    case 'g':
      if (argc != 4) {
        die("Need and id to get");
      }
      Database_get(id);
      break;
    case 's':
      if (argc != 6) {
        die("Need an id, name and email to set");
      }
      Database_set(id, argv[4], argv[5]);
      Database_write();
      break;
    case 'd':
      if (argc != 4) {
        die("Need id to delete");
      }
      Database_delete(id);
      Database_write();
      break;
    case 'l':
      Database_list();
      break;
    case 'f':
      if (argc != 4) {
        die("Need a name to search for");
      }
      Database_find_by_name(argv[3]);
      break;
    default:
      die("Invalid action, only c=create, g=get, s=set, d=del, l=list, f=find supported");
  }

  return 0;
}
