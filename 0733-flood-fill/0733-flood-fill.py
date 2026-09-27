from copy import deepcopy
class Solution:
    def dfs(self, i, j, new_color, initial_color, vis, r, c):
        # ye case ki agar bondary k bahar chala jaye to
        if i < 0 or i == r or j < 0 or j == c:
            return
        # ye case ki agar jo color h usi ko fill krna h initial_me wohi n ho to
        if vis[i][j] != initial_color:
            return
        # ye case ki pehle se wohi color ho chuka ho to
        if vis[i][j] == new_color:
            return
        # yaani upar ka sab fail to new_color 
        vis[i][j] = new_color
        # four directions me jane k liye
        self.dfs(i+1, j, new_color, initial_color, vis, r, c)
        self.dfs(i-1, j, new_color, initial_color, vis, r, c)
        self.dfs(i, j+1, new_color, initial_color, vis, r, c)
        self.dfs(i, j-1, new_color, initial_color, vis, r, c)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # dfs k zariye krte hai
        # ye base case hai ki agar color whi hai to change hi nhi hoga
        if image[sr][sc] == color:
            return image
        vis = deepcopy(image)
        r = len(vis)
        c = len(vis[0])
        initial_color = vis[sr][sc] # ye is liye kyun ki isi ko check krna h n jha pe milega
        self.dfs(sr, sc, color, initial_color, vis, r, c)
        return vis

        