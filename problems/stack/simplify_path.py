# https://www.youtube.com/watch?v=AFVN1As_tqc

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

#  -------------------------------------

# parameters - path: string
# return - simplified_path: string

# /asdf///./as//.. -> /asdf/as/.. -> /asdf
# /. -> /
# /// -> /
# // -> /
# /../ -> /
# /... -> /...
# 

# 1 split("/")
# 2 loop through split_list and build result list based on the values in split_list
# 3  if . -> do nothing
# 4  if .. -> pop from our result list
# 5  if /// or // or ///+ -> "" -> do nothing
# 6  if 
# 7 return the joined list with / delimiter with a prefix /

# Time - O(n) -> n = len(split_list)
# Space - O(n) -> n = len(split_list)

class solution:
    def simplify_path(self, path: str) -> str:
        split_list = path.split("/")
        result_list = []

        for item in split_list:
            if item == ".":
                continue
            elif item == "..":
                if result_list:
                    result_list.pop()
            elif item == "":
                continue
            else:
                result_list.append(item)
        
        return "/" + "/".join(result_list)



# META Variant
# We're given:

# An absolute path representing the current working directory (abbreviated as cwd).

# This is already simplified: there are no special characters (e.g., "." or "..") in cwd.

# A relative path representing a change directory command (abbreviated as cd).

# This may contain special characters ("." means stay, ".." means go up one level), and may not be simplified (could contain redundant slashes).

# Return:
# The string representation of the absolute path you end up at after running cd from the given cwd.
# Your result should be in simplified form.

# parameters - cwd: str, cd: str
# return - simplified_path: str

# cwd -> /test
# cd -> //..
# res -> /

# cwd -> /test/sample
# cd -> /.
# res -> /test/sample

# cwd -> /test/sample
# cd -> /test
# res -> /test/sample/test

# cwd -> /
# cd -> /..
# res -> /

# cwd -> 
# cd -> 
# res ->

# prep cwd -> split("/")
# prep cd -> split("/")

# loop through cd
#   if . -> do nothing
#   if "" -> do nothing
#   if ".." -> pop cwd if cwd has values
#   else -> append value to cwd


# Time - O(n) -> n = len(split_cd)
# Space - O(k) -> k = the len of splt_cd or split_cwd depending on which is greater

class Solution:
    def simplify_path(self, cd: str, cwd: str) -> str:
        if not cd:
            cd = "/"
        if not cwd:
            cwd = "/"

        split_cd = cd.split("/")
        split_cwd = cwd.split("/")

        for item in split_cd:
            if item == "." or item == "":
                continue
            elif item == "..":
                if split_cwd:
                    split_cwd.pop()
            else:
                split_cwd.append(item)
        
        return "/" + "/".join(split_cwd)