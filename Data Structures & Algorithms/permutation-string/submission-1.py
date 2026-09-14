class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = defaultdict(int)
        curr = defaultdict(int)
        correctletters = 0
        
        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            target[s1[i]] += 1
        for i in range(len(s1)):
            if s2[i] in target:
                if curr[s2[i]] == target[s2[i]]:
                    correctletters -= 1
                curr[s2[i]] += 1
                if curr[s2[i]] == target[s2[i]]:
                    correctletters += 1
        
        if correctletters == len(target):
            return True

        for i in range(len(s1), len(s2)):
            # remove leftmost letter
            if s2[i-len(s1)] in target:
                if curr[s2[i-len(s1)]] == target[s2[i-len(s1)]]:
                    correctletters -= 1
                curr[s2[i-len(s1)]] -= 1
                if curr[s2[i-len(s1)]] == target[s2[i-len(s1)]]:
                    correctletters += 1
            # add next letter
            if s2[i] in target:
                if curr[s2[i]] == target[s2[i]]:
                    correctletters -= 1
                curr[s2[i]] += 1
                if curr[s2[i]] == target[s2[i]]:
                    correctletters += 1
            if correctletters == len(target):
                return True
        return False
# TAKEAWAYS
# because target is a default dict, be careful how you access it because it may spawn in a default value. so check if the letter you are working with is in the target dict.

# APPROACH
        # fill freqs for target word first

        # fill freqs for initial curr word. 
        # for each addition if letter = freqs in target, correct letters += 1

        # loop through rest of the string.
        # remove tail letter and add new letter to curr. 
        # for each addition decrement or increment correct letters accordingly.

        # end of each iteration: if correct letters = s1 length, return True