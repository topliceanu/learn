// Debug Macros for C. http://c.learncodethehardway.org/book/ex20.html
#ifndef __dbg_h__
#define __dbg_h__

#include <stdio.h>
#include <errno.h>
#include <string.h>

// If you defined NDEBUG, then all debug() macros are replaced with empty
// string, otherwise they are replaced with prinf statements.
#ifdef NDEBUG
#define debug(M, ...)
#else
// debug() is a printf toghether with __FILE__, __LINE__ and __FUNCTION__
#define debug(M, ...) fprintf(stderr, "DEBUG %s:%d in %s(): " M "\n", __FILE__, __LINE__, __FUNCTION__, ##__VA_ARGS__)
#endif

// Produce a safe, readable version of errno.
#define clean_errno() (errno == 0 ? "None" : strerror(errno))

// Logging functions for various severity errors. They work like printf but with __FILE__ and __LINE__
#define log_err(M, ...) fprintf(stderr, "[ERROR] (%s:%d in %s(): errno: %s) " M "\n", __FILE__, __LINE__, __FUNCTION__, clean_errno(), ##__VA_ARGS__)

#define log_warn(M, ...) fprintf(stderr, "[WARN] (%s:%d in %s(): errno: %s) " M "\n", __FILE__, __LINE__, __FUNCTION__, clean_errno(), ##__VA_ARGS__)

#define log_info(M, ...) fprintf(stderr, "[INFO] (%s:%d in %s()) " M "\n", __FILE__, __LINE__, __FUNCTION__, ##__VA_ARGS__)

// Checks if condition A is true. If not, it logs the error, and jumps to the error label!? of the function for cleanup.
#define check(A, M, ...) if(!(A)) { log_err(M, ##__VA_ARGS__); errno=0; goto error; }

// Place this in every part of the code that shouldn't run (and only runs because of an error). It jumps to the error label in the function.
#define sentinel(M, ...)  { log_err(M, ##__VA_ARGS__); errno=0; goto error; }

// Checks that a pointer if valid!
#define check_mem(A) check((A), "Out of memory.")

// Same as `check` but without the error logging.
#define check_debug(A, M, ...) if(!(A)) { debug(M, ##__VA_ARGS__); errno=0; goto error; }

#endif
