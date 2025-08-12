# Example n=3
1)`TowerOfHanoi(3, A, B, C)`
- this calls `TowerOfHanoi(2,A,C,B)`
- this calls `TowerOfHanoi(1,A,B,C)`
- Now we have `n==1` so we meet base condition:
    - we print `we move disk 1 from A to B`. so we "moved it" by just printing. 
- now we go back one level and we returned to `TowerOfHanoi(2,A,C,B)`
- and we say we `move disk 2 from A to C`, which leads us again back one level of recursion of `TowerOfHanoi(3, A, B, C)`