class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort() 
        # this sorts the folder
        # the folders with the same starting will be clumped together and the start of each clump will be the parent folder
        l,r = 0, 1
        result = []
        result.append(folder[l])
        while r < len(folder):
            # we add a check to confirm that it contains a / after the comparison point.
            if len(folder[r]) < len(folder[l]) or folder[r][:len(folder[l])] != folder[l]:
                l = r
                r = l + 1
                result.append(folder[l])
                continue
            else:
                if len(folder[r]) != len(folder[l]) and folder[r][len(folder[l])] != "/":
                    # we know that it is longer than folder l
                    l = r
                    r = l + 1
                    result.append(folder[l])
                    continue
                r += 1
        return result            
    
# more efficient solution
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # Sort ensures parent folders come before subfolders
        result = [folder[0]]  # Always keep the first folder
        
        for f in folder[1:]:
            # Check if f starts with the last added parent + "/"
            if not f.startswith(result[-1] + "/"):
                result.append(f)
        
        return result
