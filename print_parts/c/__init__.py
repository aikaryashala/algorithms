import check50
import check50.c

EXECUTABLE = "./print_parts"

TEST_FILES = [
    "../tests/input1.txt", "../tests/expected_output1.txt",
    "../tests/input2.txt", "../tests/expected_output2.txt",
    "../tests/input3.txt", "../tests/expected_output3.txt",
    "../tests/input4.txt", "../tests/expected_output4.txt"
]

@check50.check()
def exists_and_compiles():
    """print_parts.c exists"""
    check50.exists("print_parts.c")

    """print_parts.c compiles"""
    check50.c.compile("print_parts.c", lcs50=False)

    include_test_files()

@check50.check(exists_and_compiles)
def print_parts_57_lanka_pavan_kumar():
    test_input_output("input1.txt", "expected_output1.txt")

@check50.check(exists_and_compiles)
def print_parts_1_arjun_sharma():
    test_input_output("input2.txt", "expected_output2.txt")

@check50.check(exists_and_compiles)
def print_parts_100_ravi_kumar_reddy():
    test_input_output("input3.txt", "expected_output3.txt")

@check50.check(exists_and_compiles)
def print_parts_42_sita_rama_krishna_murthy():
    test_input_output("input4.txt", "expected_output4.txt")

def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(EXECUTABLE).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

def include_test_files():
    for test_file in TEST_FILES:
        check50.include(test_file)
