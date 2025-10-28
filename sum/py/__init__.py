import check50

EXECUTABLE = "python3 sum.py"

# Include files at module level (executed once)
TEST_FILES = [
    "../tests/sum_2_3_input.txt", "../tests/sum_2_3_output.txt",
    "../tests/sum_20_22_input.txt", "../tests/sum_20_22_output.txt",
    "../tests/sum_10_20_input.txt", "../tests/sum_10_20_output.txt"
]

@check50.check()
def exists_and_compiles():
    """sum.py exists"""
    check50.exists("sum.py")
    include_test_files()

@check50.check(exists_and_compiles)
def sum_2_3():
    test_input_output("sum_2_3_input.txt", "sum_2_3_output.txt");

@check50.check(exists_and_compiles)
def sum_20_22():
    test_input_output("sum_20_22_input.txt", "sum_20_22_output.txt");

@check50.check(exists_and_compiles)
def sum_10_20():
    test_input_output("sum_10_20_input.txt", "sum_10_20_output.txt");


# Helper functions
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(EXECUTABLE).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

def include_test_files():
    for test_file in TEST_FILES:
        check50.include(test_file)


    