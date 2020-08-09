class RunTestCases:

    def __init__(self, **kwargs):
        if 'case_type' not in kwargs or 'cases_list' not in kwargs:
            raise Exception('Args - case_type and cases_list are mandatory')
        self.responses = []
        self.case_list = []
        self.case_type = kwargs['case_type']
        self.split_cases(kwargs['cases_list'])

    def split_cases(self, cases_list):
        curr_case = []
        for cases in cases_list.splitlines():
            curr_string = cases.strip()
            if curr_string:
                curr_list = curr_string.split(',')
                if curr_list:
                    self.case_list.append(map(int,curr_list))

    def run_cases(self, calling_method):
        try:
            if self.case_type == 'single_list_int':
                for indi_case in self.case_list:
                    result = calling_method(indi_case)
                    self.responses.append(result)
            else:
                raise Exception('Unknown case type')
            return self.fetch_final_result()
        except Exception as e:
            print('Exception happened while running the cases. Reason - {}'.format(str(e)))

    def fetch_final_result(self):
        return all(self.responses)