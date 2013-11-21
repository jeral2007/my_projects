#!/usr/bin/env python
# http://habrahabr.ru/post/200190/#comment_6934460. pool problem
# There is a waterpool with size of N blocks, the form of pool described as height array of length N.
# For example arr = [3,1,1,2,3] describes pool of the following form:
#
# x   x
# x  xx
# xxxxx
# The question is what mass of water the pool can hold? Water is going out from left and right edges.
def pool_str(arr_of_pool):
    """ returns string, that is ascii art picture of pool, the edge blocks denotes as x
            example:
            pool_str([3,1,1,2,3]) returns 
            x
            x  xx
            xxxxx"""
    cur_level = max(arr_of_pool)
    res = ""
    while(cur_level>=min(arr_of_pool)):
        res +="".join((cur_level<=block_height) and "x" or " " for block_height in arr_of_pool) + "\n" #ternary operator hack
        cur_level-=1
    return res

def water_front(ap):
    wf = [max(ap)]*len(ap)
    owf = wf[:]
    for iter in xrange((max(ap)-min(ap))*len(ap)):
        wf[0],wf[-1]=ap[0],ap[-1] #boundary condition water is leaking from edges
        owf = wf[:]
        for i in xrange(1,len(wf)-1):
            if ((wf[i]>owf[i-1] and wf[i]>ap[i]) or (wf[i]>owf[i+1] and wf[i]>ap[i])):
                wf[i]-=1
    res = ""
    cur_level=max(wf)
    while(cur_level>=min(ap)):
        tmp = ""
        for i in xrange(len(ap)):
            if cur_level<= ap[i]:
               s = "x"
            elif cur_level<=wf[i]:
               s = "-"
            else:
               s = " "
            tmp+=s
        res +=tmp+"\n"
        cur_level-=1
    return res

def water_mass(arr_of_pool):
    """returns maximum amount of water that given pool can hold"""

    #initialization section
    ind_l = 0 #index of left border of current left pit in the pool
    ind_r = len(arr_of_pool)-1 #index of right border of current right pit in the pool
    w_l = 0 #width of current left pit
    w_r = 0 #width of current right pit
    water_tot = 0 #total amount of water 
    water_lev_l = arr_of_pool[ind_l]
    water_lev_r = arr_of_pool[ind_r] # water level in current left and rights pits
    l_volume = 0
    cl = 0 # arbitrary values, this variables will be reassigned in main loop
    cr = 0 # 
    r_volume = 0 # overall volume of filled blocks in current pits

    #main loop
    while(ind_l+w_l<=ind_r-w_r-1):
            w_l+=1 
            w_r+=1 # go to the next left and right pits blocks
            cl = ind_l + w_l
            cr = ind_r - w_r
            if (arr_of_pool[cl]>water_lev_l): # if we meet right wall of the left current pit
                water_tot+=water_lev_l*(w_l+1)-l_volume #add to the total water amount amount in the current left pit
                ind_l=cl #and start to consider next pit
                w_l= 0 
                water_lev_l = arr_of_pool[ind_l]
                l_volume = 0
           # for the right pit we do the same
            if (arr_of_pool[cr]>water_lev_r): 
                water_tot+=water_lev_r*(w_r+1)-r_volume
                ind_r=cr 
                w_r= 0 
                water_lev_r = arr_of_pool[ind_r]
                r_volume = 0
            l_volume+=arr_of_pool[cl] #volumes of blocks
            r_volume+=arr_of_pool[cr]
            
    if (cl==cr): 
        water_tot+=arr_of_pool[cl] #overlap account
    water_tot+=min(water_lev_r,water_lev_l)*(w_l+w_r-1)-l_volume-r_volume
    return max(water_tot,0)
#test
arrs = [[1],[2,1,2],[2,1,1,2],
        [2,1,1,2,1],
        [2,1,1,2,1][::-1],
        [2,1],
        [1,2],
        [3,1,1,2,4]]
for arr in arrs:
        print "="*10
        print ("pool:")
        print (water_front(arr))
        print ("watermass:{}".format(water_mass(arr)))
