# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:

# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:

# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.





# Parameter - absolutepath: str
# return - simplifiedpath: str

# /test/folder/one

# Q - /test/folder///one -> test/folder/one
# Q - /test/folder/../one -> test/one
# Q - /test/..../one -> /test/..../one
# Q - 

# 1. if . -> remove it -> /test/./one -> /test/one
# 2. if .. -> move up -> /test/../one -> /one
# 3. if //+ -> replace with / -> /test///one -> /test/one.    with split, this becomes check ""

# split("/")
# stack

# /test/folder/../one
# run split
# splitlist = ["test", "folder", "..", "one"]
# stack = []

# loop through this
# stack = ["test", "one"]
# join(stack) -> /test/one

# /test/folder/../one/./two////three -> /test/one/two/three
# run split
# splitlist = ["test", "folder", "..", "one", ".", "two", "", "", "", "three"]
# stack = ["test", "one", "two", "three"]


# Time - O(n) -> n = len(splitlist)
# Space - O(n) -> n = len(splitlist)


# 1. def class
# 2  def method
# 3. declare variables
# 4. run split into splitlist
# 5. loop through splitlist
# 6.     if "." or ".."
# 7.     elif ".." pop stack
# 8.     else append to stack
# 9.  return the stack joined   


# 
class Solution:
    def simplify_path(self, path: str) -> str:
        stack = []
        splitlist = path.split("/")

        for item in splitlist:
            if item == "." or item == "":
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        
        return "/" + "/".join(stack)