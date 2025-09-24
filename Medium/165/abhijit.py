class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
            compare the versioning of the string
        """
        v1 = version1.split(".")
        v2 = version2.split(".")

        i = 0

        while i < len(v1) or i < len(v2):
            v1_val, v2_val = 0,0
            if i < len(v1):
                v1_val = v1[i]
            if i < len(v2):
                v2_val = v2[i]
            
            if int(v2_val) > int(v1_val):
                return -1
            
            if int(v1_val) > int(v2_val):
                return 1
            
            i += 1
        
        return 0