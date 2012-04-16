#ifndef HASH_H
#define    HASH_H

#ifdef    __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stddef.h>
/** need to define the ENDIAN mode */
#define ENDIAN_BIG 1
//#define ENDIAN_LITTLE

/** 

 * to caculate the key's hash value
 * 
 * @param key the key to hash
 * @param length the length of key
 * @param initval initval, the default value is 0
 * 
 * @return return the hash value
 */
uint32_t hash(const void *key, size_t length, const uint32_t initval);

#ifdef    __cplusplus
}
#endif

#endif    /* HASH_H */

