import check50
import check50.c

EXECUTABLE = "./sum_of_even_up_to_n"

TEST_FILES = [
    "../tests/input1.txt", "../tests/expected_output1.txt",
    "../tests/input2.txt", "../tests/expected_output2.txt",
    "../tests/input3.txt", "../tests/expected_output3.txt"
]

@check50.check()
def exists_and_compiles():
    """sum_of_even_up_to_n.c exists"""
    check50.exists("sum_of_even_up_to_n.c")

    """sum_of_even_up_to_n.c compiles"""
    check50.c.compile("sum_of_even_up_to_n.c", lcs50=False)

    include_test_files()

@check50.check(exists_and_compiles)
def sum_of_even_up_to_n_test1():
    test_input_output("input1.txt", "expected_output1.txt")

@check50.check(exists_and_compiles)
def sum_of_even_up_to_n_test2():
    test_input_output("input2.txt", "expected_output2.txt")

@check50.check(exists_and_compiles)
def sum_of_even_up_to_n_test3():
    test_input_output("input3.txt", "expected_output3.txt")

def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(EXECUTABLE).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

def include_test_files():
    for test_file in TEST_FILES:
        check50.include(test_file)
