class Solution(object):
    def singleNumber(nums):

        single=0
        for num in nums:
            single ^=num
        return single
    mylist = [4,1,2,1,2]
    print (singleNumber(mylist))
