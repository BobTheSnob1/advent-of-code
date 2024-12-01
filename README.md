# advent-of-code

Richard's solutions for advent of code 2024.
see https://adventofcode.com/2024

## run.sh

`run.sh` runs python solutions for the problems or creates the skeleton if no dir is present. 
usage:
`bash run.sh [day]`: runs solutions as `python3 *.py < *.in > *.out` in the day's dir. if dir doesn't exist creates `day*/{1, 2}.{py, in, out}`.
example:
```
bash run.sh 1
```