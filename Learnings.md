# Things I've learned so far

## Generic

## Git

`git reflog`

`git reflog --date=relative

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

## RPGLE
- %Div to divide and get the integer portion
- Reading an IFS file line by line with SQL is way way easier than the read-open-close stuff
```rpgle
  exec sql
    DECLARE c1 CURSOR FOR
    SELECT line FROM table(qsys2.ifs_read_utf8(path_name => :filePath));
```
- remember sorta
- 



## Python

- rich.print is quite costly - when running for a ton of records, printing each, it takes a significant time. Removing the print brings back to a second of runtime, as opposed to 30s+
- `list.match(value, start=, end=)` and `list.index(value, start=, end=)` is the same thing, only `.index()` raises exception if value not found
- `list(str)` will explode str value into a list, each digit it's own element