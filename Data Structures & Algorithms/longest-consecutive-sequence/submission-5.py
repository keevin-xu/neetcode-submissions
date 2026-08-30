class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mydict = dict()
        ret = 0
        for i in nums:
            if i in mydict:
                continue;
            mydict[i] = [i, i]
            if (i - 1) in mydict and (i + 1) in mydict:
                mydict[i - 1][1] = mydict[i + 1][1]
                # set mydict[i + 1] to be pointing to same list object
                mydict[mydict[i + 1][1]] = mydict[i - 1]
                mydict[i] = mydict[i - 1]
            elif (i - 1) in mydict:
                mydict[i - 1][1] = i
                mydict[i] = mydict[i - 1]
            elif (i + 1) in mydict:
                mydict[i + 1][0] = i
                mydict[i] = mydict[i + 1]
            if (mydict[i][1] - mydict[i][0] + 1) > ret:
                ret = (mydict[i][1] - mydict[i][0] + 1)
        return ret
# keep a dict between nums[i] elements and the values are pointers to a list
# list's bounds are [left bound, right bound]
# you only need to update the mydict key's of the boundaries of the sequence
# keep a var of running max lenght. everytime hashmap updated, you check if max has been exceeded.