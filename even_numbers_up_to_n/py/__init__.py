import check50

EXECUTABLE = "python3 even_numbers_up_to_n.py"

# Include files at module level (executed once)
TEST_FILES = [
    "../tests/input1.txt", "../tests/expected_output1.txt",
    "../tests/input2.txt", "../tests/expected_output2.txt",
    "../tests/input3.txt", "../tests/expected_output3.txt"
]

@check50.check()
def exists_and_compiles():
    """even_numbers_up_to_n.py exists"""
    check50.exists("even_numbers_up_to_n.py")
    include_test_files()

@check50.check(exists_and_compiles)
def even_numbers_up_to_n_5():
    test_input_output("input1.txt", "expected_output1.txt");

@check50.check(exists_and_compiles)
def even_numbers_up_to_n_10():
    test_input_output("input2.txt", "expected_output2.txt");

@check50.check(exists_and_compiles)
def even_numbers_up_to_n_1():
    test_input_output("input3.txt", "expected_output3.txt");


# Helper functions
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(EXECUTABLE).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

def include_test_files():
    for test_file in TEST_FILES:
        check50.include(test_file)

