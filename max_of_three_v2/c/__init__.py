import check50
import check50.c

EXECUTABLE = "./max_of_three_v2"

TEST_FILES = [
    "../tests/input1.txt", "../tests/expected_output1.txt",
    "../tests/input2.txt", "../tests/expected_output2.txt",
    "../tests/input3.txt", "../tests/expected_output3.txt",
    "../tests/input4.txt", "../tests/expected_output4.txt",
    "../tests/input5.txt", "../tests/expected_output5.txt",
    "../tests/input6.txt", "../tests/expected_output6.txt"
]

@check50.check()
def exists_and_compiles():
    """max_of_three_v2.c exists"""
    check50.exists("max_of_three_v2.c")

    """max_of_three_v2.c compiles"""
    check50.c.compile("max_of_three_v2.c", lcs50=False)

    include_test_files()

@check50.check(exists_and_compiles)
def max_of_three_v2_5_55_555():
    test_input_output("input1.txt", "expected_output1.txt")

@check50.check(exists_and_compiles)
def max_of_three_v2_100_50_25():
    test_input_output("input2.txt", "expected_output2.txt")

@check50.check(exists_and_compiles)
def max_of_three_v2_10_200_50():
    test_input_output("input3.txt", "expected_output3.txt")

@check50.check(exists_and_compiles)
def max_of_three_v2_55_5_555():
    test_input_output("input4.txt", "expected_output4.txt")

@check50.check(exists_and_compiles)
def max_of_three_v2_100_25_50():
    test_input_output("input5.txt", "expected_output5.txt")

@check50.check(exists_and_compiles)
def max_of_three_v2_50_200_10():
    test_input_output("input6.txt", "expected_output6.txt")

def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(EXECUTABLE).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

def include_test_files():
    for test_file in TEST_FILES:
        check50.include(test_file)
