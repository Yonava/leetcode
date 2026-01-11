class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        split on "/" and keep track of what is going on. if we see a ".." we can pop
        """
        p = path.split("/")
        
        final_path = []

        for c in p:
            if c == "." or c == "":
                continue
            elif c == "..":
                if final_path:
                    final_path.pop()
            else:
                final_path.append(c)

        return "/" + "/".join(final_path)