import levelup from 'levelup';
import leveldown from 'leveldown';

class Storage {
  constructor (dbPath) {
    this.db = levelup(leveldown(dbPath));
  }
  readUserById (id) {
    return this.db.get(id);
  }
  putUser (id, user) {
    return this.db.put(id, user);
  }
}
