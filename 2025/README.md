# Advent of Code 2025

## Goals

Goals for this year's Advent of Code:
- Want to practice Git
- Want to Learn and Practice RPGLE Built-in Functions
- Want to Practice Clean Code Principles
- Want to help family in Python - so may do a few in Python as well


## Learnings

### Generic

Thinking a bit more about O(n^2) vs O(n) complexities

Regarding recursive functions - consider caching results if there's a possibility that it gets called again. Sped up day 7 a ton (an hour without results to running in 0.2 seconds). Caching unneccessarily will just be an additional cost though.

### Git

`git reflog`

`git reflog --date=relative`

`git log --oneline --graph`

`git branch <branchname> <commit>` - branch off from a specific commit - useful to check `git log --oneline` for the commit #

reflog interactions:
`git branch <branchname> <commit>` will copy the commits, and it places them as if the branch existed at that time. deleting the branch will then remove them from reflog completely. what does remain is the switch (i did not do a commit on the branch, but theoretically that remains existing as well). Note the commit # remains the same - quite interesting.

```
>>> git reflog

47dd8a7 HEAD@{1}: checkout: moving from main to test
...
47dd8a7 HEAD@{12}: commit: Day 2 Part 1 in Python
```

I had Day 4 on work pc, and day 5 & 6 on main pc. To move over history, I did:
```
cd <repo to apply changes>
git remote add <source_name> <repo_to_copy_from>
git fetch <source_name>
git cherry-pick <commit_hash_from_source_repo>
```


### RPGLE
- %Div to divide and get the integer portion
- Reading an IFS file line by line with SQL is way way easier than the read-open-close stuff
```rpgle
  exec sql
    DECLARE c1 CURSOR FOR
    SELECT line FROM table(qsys2.ifs_read_utf8(path_name => :filePath));
```
- remember `sorta array`



### Python

- rich.print is quite costly - when running for a ton of records, printing each, it takes a significant time. Removing the print brings back to a second of runtime, as opposed to 30s+
- `list.match(value, start=, end=)` and `list.index(value, start=, end=)` is the same thing, only `.index()` raises exception if value not found
- `list(str)` will explode str value into a list, each digit it's own element
- `import bisect` -> `bisect.bisect_left(sorted_list, value)` and `bisect_right` finds the position that a value would be inserted into a sorted list, ie `bisect.bisect_left([2,4,6], 5)` would return `2`.
- `str.replace(value, replace_with)`
- `zip(lists)` -> `list(zip(*list_containing_lists)`