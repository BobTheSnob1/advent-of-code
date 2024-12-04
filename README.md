# advent-of-code

Richard's solutions for advent of code 2024.
see <https://adventofcode.com/2024>

## run.sh

This script automates the setup and execution of Advent of Code challenges.
It supports three main operations: running scripts for a specific day, pushing changes to GitHub, and running all scripts.

### Usage:
`./run.sh <day_number>`: Creates the directory and files for the specified day if they do not exist, and executes any Python scripts found in the directory.
`./run.sh push`: Commits all changes with a message containing the current day number and pushes to GitHub.
`./run.sh all`: Executes all Python scripts in all day directories, using corresponding input files.

### Arguments:
`<day_number>`: The day number for which to create the directory and files, or to execute the scripts.
`push`: Commits and pushes all changes to GitHub with a commit message containing the current day number.
`all`: Executes all Python scripts in all day directories, using corresponding input files.

### Examples:
`./run.sh 1` - Sets up or runs the scripts for day 1.
`./run.sh push` - Commits and pushes all changes to GitHub.
`./run.sh all` - Runs all scripts for all days.
