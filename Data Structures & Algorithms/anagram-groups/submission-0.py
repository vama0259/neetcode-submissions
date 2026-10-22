class Solution:
    def map_ana(self, word):
        b = {}
        for a in range(len(word)):
            c = word[a]
            if c in b.keys():
                b[c] += 1
            else:
                b[c] = 1
        return b

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b = {}
        for a in strs:
            # 1 & 2. Get the dict, sort its items, and turn it into a tuple to use as a key
            word_dict = self.map_ana(a)
            key = tuple(sorted(word_dict.items())) 
            
            if key in b:
                # 3. Just append, don't reassign
                b[key].append(a) 
            else:
                b[key] = [a]
        
        # 4. Wrap values in a list
        return list(b.values())