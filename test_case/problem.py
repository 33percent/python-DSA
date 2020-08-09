from index import RunTestCases

def sample_call(array_of_vals):
    for indi in array_of_vals:
        if indi % 2 == 0:
            return True
    return False

if __name__ == "__main__":
    list_of_usecases = """
    1,2,3
    1,1,1,5,6,2
    1,9,7,5,4
    """
    sample_test = RunTestCases(cases_list = list_of_usecases, case_type = 'single_list_int')
    print(sample_test.run_cases(sample_call))
