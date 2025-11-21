import check50

EXECUTABLE = "python3 max_of_2.py"

TEST_FILES = [
    "../tests/input1.txt", "../tests/expected_output1.txt",
    "../tests/input2.txt", "../tests/expected_output2.txt"
]

@check50.check()
def exists_and_compiles():
    """max_of_2.py exists"""
    check50.exists("max_of_2.py")
    include_test_files()

@check50.check(exists_and_compiles)
def max_of_2_test1():
    test_input_output("input1.txt", "expected_output1.txt")

@check50.check(exists_and_compiles)
def max_of_2_test2():
    test_input_output("input2.txt", "expected_output2.txt")

def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(EXECUTABLE).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

def include_test_files():
    for test_file in TEST_FILES:
        check50.include(test_file)
