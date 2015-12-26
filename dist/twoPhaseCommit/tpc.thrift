service TPC {
  bool queryToCommit(1: string tid, 2: string tbody),
  bool commit(1: string tid),
  bool rollback(1: string tid)
}
