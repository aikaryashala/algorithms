# Algorithms Repository - Project Structure Documentation

## Overview

This is an **educational algorithms repository** designed for teaching programming fundamentals across multiple programming languages. It uses **CS50's check50 testing framework** to automatically validate student solutions.

## Purpose

- Provide programming exercises for beginners
- Support multiple programming languages (C, Python, Go, JavaScript, Rust)
- Automate testing and grading using check50
- Maintain consistent structure across all problems

## Repository Structure

Each problem/algorithm follows a consistent pattern:

```
<problem_name>/
├── ux.txt                          # Expected user interaction/output format
├── tests/                          # Test cases directory
│   ├── input1.txt                  # Test input 1
│   ├── expected_output1.txt        # Expected output 1
│   ├── input2.txt                  # Test input 2
│   ├── expected_output2.txt        # Expected output 2
│   ├── input3.txt                  # Test input 3
│   └── expected_output3.txt        # Expected output 3
├── c/                              # C implementation tests
│   ├── __init__.py                 # check50 test suite for C
│   └── .cs50.yml                   # CS50 configuration for C
├── py/                             # Python implementation tests
│   ├── __init__.py                 # check50 test suite for Python
│   └── .cs50.yml                   # CS50 configuration for Python
├── go/                             # Go implementation (future)
├── js/                             # JavaScript implementation (future)
└── rust/                           # Rust implementation (future)
```

## Current Problems

### Fully Implemented
1. **sum** - Add two numbers
2. **product** - Multiply three numbers
3. **natural_numbers_up_to_n** - Print first N natural numbers
4. **even_numbers_up_to_n** - Print even numbers up to N
5. **odd_numbers_up_to_n** - Print odd numbers up to N
6. **n_even_numbers** - Print first N even numbers
7. **n_odd_numbers** - Print first N odd numbers

### Incomplete
8. **multiplication_table** - Generate multiplication table
9. **table_book** - Table book related problem

## File Descriptions

### 1. ux.txt
Contains the expected user interaction format showing:
- The prompt displayed to the user
- Sample input
- Expected output format

**Example (from even_numbers_up_to_n/ux.txt):**
```
Up to which number you want to print even numbers? 5
The even numbers up to 5 are 0, 2, 4.
```

### 2. tests/ Directory
Contains input/output pairs for automated testing:
- **inputN.txt**: Contains the user input for test case N
- **expected_outputN.txt**: Contains the complete expected output including prompts

**Important**:
- Expected output files contain the FULL output including prompts
- Input and output are paired (input1.txt ↔ expected_output1.txt)
- Typically 3 test cases per problem

### 3. c/__init__.py
Python-based check50 test suite for C implementations.

**Structure:**
```python
import check50
import check50.c

EXECUTABLE = "./<problem_name>"

TEST_FILES = [
    "../tests/input1.txt", "../tests/expected_output1.txt",
    "../tests/input2.txt", "../tests/expected_output2.txt",
    "../tests/input3.txt", "../tests/expected_output3.txt"
]

@check50.check()
def exists_and_compiles():
    """<problem_name>.c exists"""
    check50.exists("<problem_name>.c")

    """<problem_name>.c compiles"""
    check50.c.compile("<problem_name>.c", lcs50=False)

    include_test_files()

@check50.check(exists_and_compiles)
def <problem_name>_test1():
    test_input_output("input1.txt", "expected_output1.txt")

# ... additional test functions ...

def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(EXECUTABLE).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

def include_test_files():
    for test_file in TEST_FILES:
        check50.include(test_file)
```

**Key Points:**
- Checks if the C source file exists
- Compiles without cs50 library (`lcs50=False`)
- Runs executable with test inputs
- Compares output exactly (no regex)

### 4. c/.cs50.yml
CS50 configuration file specifying which files students must submit.

**Structure:**
```yaml
check50:
  files: &check50_files
    - !exclude "*"
    - !require <problem_name>.c

submit50:
  files: *check50_files
```

### 5. py/__init__.py
Python-based check50 test suite for Python implementations.

**Structure:**
```python
import check50

EXECUTABLE = "python3 <problem_name>.py"

TEST_FILES = [
    "../tests/input1.txt", "../tests/expected_output1.txt",
    "../tests/input2.txt", "../tests/expected_output2.txt",
    "../tests/input3.txt", "../tests/expected_output3.txt"
]

@check50.check()
def exists_and_compiles():
    """<problem_name>.py exists"""
    check50.exists("<problem_name>.py")
    include_test_files()

@check50.check(exists_and_compiles)
def <problem_name>_test1():
    test_input_output("input1.txt", "expected_output1.txt")

# ... additional test functions ...

def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(EXECUTABLE).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

def include_test_files():
    for test_file in TEST_FILES:
        check50.include(test_file)
```

**Key Points:**
- Checks if Python source file exists
- No compilation step (interpreted language)
- Runs with `python3` interpreter
- Same test structure as C version

### 6. py/.cs50.yml
CS50 configuration file for Python submissions.

**Structure:**
```yaml
check50:
  files: &check50_files
    - !exclude "*"
    - !require <problem_name>.py

submit50:
  files: *check50_files
```

## How Students Use This System

1. Student navigates to the appropriate directory (e.g., `sum/c/` or `sum/py/`)
2. Student creates their solution file (e.g., `sum.c` or `sum.py`)
3. Student runs `check50` to test their solution
4. check50 framework:
   - Verifies the file exists
   - Compiles (for C) or validates (for Python)
   - Runs the program with test inputs
   - Compares actual output against expected output
   - Reports which tests pass/fail

## Adding a New Problem

Follow these 3 stages:

### Stage 1: Create tests/ folder

1. Create `<problem_name>/tests/` directory
2. Create 3 test cases (can be more):
   - `input1.txt`, `input2.txt`, `input3.txt`
   - `expected_output1.txt`, `expected_output2.txt`, `expected_output3.txt`
3. Ensure expected output includes prompts and full interaction

**Test Case Guidelines:**
- Test 1: Example from ux.txt
- Test 2: Different input value
- Test 3: Edge case (e.g., 1, 0, or boundary value)

### Stage 2: Create c/ folder

1. Create `<problem_name>/c/` directory
2. Create `__init__.py` with check50 test suite:
   - Set `EXECUTABLE = "./<problem_name>"`
   - List all test files in `TEST_FILES`
   - Add exists and compiles check
   - Add test functions for each test case
   - Include helper functions
3. Create `.cs50.yml`:
   - Require `<problem_name>.c`
   - Exclude all other files

### Stage 3: Create py/ folder

1. Create `<problem_name>/py/` directory
2. Create `__init__.py` with check50 test suite:
   - Set `EXECUTABLE = "python3 <problem_name>.py"`
   - List all test files in `TEST_FILES`
   - Add exists check (no compile check needed)
   - Add test functions for each test case
   - Include helper functions
3. Create `.cs50.yml`:
   - Require `<problem_name>.py`
   - Exclude all other files

## Example: Creating "even_numbers_up_to_n"

### ux.txt
```
Up to which number you want to print even numbers? 5
The even numbers up to 5 are 0, 2, 4.
```

### Test Cases

**input1.txt:**
```
5
```

**expected_output1.txt:**
```
Up to which number you want to print even numbers? The even numbers up to 5 are 0, 2, 4.
```

**input2.txt:**
```
10
```

**expected_output2.txt:**
```
Up to which number you want to print even numbers? The even numbers up to 10 are 0, 2, 4, 6, 8, 10.
```

**input3.txt:**
```
1
```

**expected_output3.txt:**
```
Up to which number you want to print even numbers? The even numbers up to 1 are 0.
```

### Directory Structure Created
```
even_numbers_up_to_n/
├── ux.txt
├── tests/
│   ├── input1.txt
│   ├── expected_output1.txt
│   ├── input2.txt
│   ├── expected_output2.txt
│   ├── input3.txt
│   └── expected_output3.txt
├── c/
│   ├── __init__.py
│   └── .cs50.yml
└── py/
    ├── __init__.py
    └── .cs50.yml
```

## Naming Conventions

1. **Problem directories**: Use underscores, lowercase (e.g., `natural_numbers_up_to_n`)
2. **Solution files**: Match problem name with appropriate extension:
   - C: `<problem_name>.c`
   - Python: `<problem_name>.py`
3. **Executables** (C only): Match problem name (e.g., `./sum`)
4. **Test files**: Use sequential numbering:
   - `input1.txt`, `input2.txt`, `input3.txt`
   - `expected_output1.txt`, `expected_output2.txt`, `expected_output3.txt`

## Common Patterns

### Input/Output Format
- All expected output files include the full user interaction
- Prompts and outputs are on the same line (no newline between prompt and input echo)
- Format: `Prompt text? The result is X.`

### Test File References
- Always use relative paths: `../tests/input1.txt`
- Check50 includes test files at module level
- Test files are included once and reused across test functions

### Check50 Configuration
- Use `!exclude "*"` to exclude all files by default
- Use `!require` to specify required submission file
- Anchor files with `&check50_files` and reference with `*check50_files`

## Future Enhancements

1. **Additional Languages**: Implement Go, JavaScript, and Rust versions
2. **More Problems**: Add new algorithmic challenges
3. **Complexity Levels**: Organize problems by difficulty
4. **Documentation**: Create student-facing README files for each problem

## Tools and Technologies

- **check50**: CS50's automated testing framework
- **Python**: For writing test suites
- **YAML**: For CS50 configuration
- **Git**: Version control

## Best Practices

1. **Consistency**: Always follow the established directory structure
2. **Test Coverage**: Ensure edge cases are tested
3. **Clear Prompts**: Make ux.txt examples clear and unambiguous
4. **Exact Matching**: Expected outputs must match exactly (including whitespace)
5. **No Dependencies**: Compile C without cs50 library (`lcs50=False`)

## Troubleshooting

### Common Issues

1. **Test fails due to whitespace**: Ensure expected output matches exactly
2. **File not found**: Check relative paths in test file references
3. **Compilation errors**: Verify student code compiles without cs50 library
4. **Wrong executable name**: Ensure EXECUTABLE matches problem name

## Maintenance Notes

- Test files should be reviewed when updating problem specifications
- Keep ux.txt synchronized with expected outputs
- Verify all test cases pass before committing new problems
- Document any deviations from standard structure

---

**Last Updated**: November 2025
**Maintainer**: Aikaryashala
**Framework**: CS50 check50
