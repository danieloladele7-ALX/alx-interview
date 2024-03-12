Curriculum <br>
**Short Specializations** <br>

# 0x01. Lockboxes

```Algorithm``` ```Python```

## General Requirement

* Allowed editors: `vi`, `vim`, `emacs`
* Files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* File first line exactly shebang `#!/usr/bin/python3`
* Mandatory `README.md` file
* Code is documented
* Code uses `PEP 8` style (version 1.7.x)
* Files executable

### Task:
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`
