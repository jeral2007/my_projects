#!/usr/bin/env python
#coding:utf8
# http://habrahabr.ru/post/200190/#comment_6934460. pool problem
# There is a waterpool with size of N blocks, the form of pool described as height array of length N.
# For example arr = [3,1,1,2,3] describes pool of the following form:
#
# x   x
# x  xx
# xxxxx
# The question is what mass of water the pool can reserve? Water is going out from left and right edges.
def pool_str(arr_of_pool):
        """ returns string, that is ascii art picture of pool, the edge blocks denotes as x
            example:
            pool_str([3,1,1,2,3]) returns 
x
x  xx
xxxxx"""
     cur_level = max(arr_of_pool)
     res = ""
     while(cur_level>=min(arr_of_pool):
          res +="".join((cur_level<block_height) and "x" or " ") for block_height in arr_of_pool) + "\n" #ternary operator hack
     return res

print (pool_str([1]))
print (pool_str([2,1,2]))
print (pool_str([1,2]))
pool = [3,1,1,2,3]
print (pool_str(pool))
