import check50
import check50.c

EXECUTABLE = "./multiples_of_7"

TEST_FILES = [
    "../tests/input1.txt", "../tests/expected_output1.txt",
    "../tests/input2.txt", "../tests/expected_output2.txt",
    "../tests/input3.txt", "../tests/expected_output3.txt"
]

@check50.check()
def exists_and_compiles():
    """multiples_of_7.c exists"""
    check50.exists("multiples_of_7.c")

    """multiples_of_7.c compiles"""
    check50.c.compile("multiples_of_7.c", lcs50=False)

    include_test_files()

@check50.check(exists_and_compiles)
def multiples_of_7_test1():
    test_input_output("input1.txt", "expected_output1.txt")

@check50.check(exists_and_compiles)
def multiples_of_7_test2():
    test_input_output("input2.txt", "expected_output2.txt")

@check50.check(exists_and_compiles)
def multiples_of_7_test3():
    test_input_output("input3.txt", "expected_output3.txt")

def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(EXECUTABLE).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

def include_test_files():
    for test_file in TEST_FILES:
        check50.include(test_file)
