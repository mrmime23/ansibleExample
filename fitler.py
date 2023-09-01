#!/usr/bin/python

class Expanded_Filter_Module(object):
    def NewFilters(self):
        return {
            'new_filter': self.new_filter
        }

    def NewFilter(self, new_variable):
        new_newvariable = new_variable + ' WILD EXPANSION'
        return new_newvariable

class AnotherModule(object):
    def __init__(self):
        self.data = []

    def AddData(self, value):
        self.data.append(value)

    def ProcessData(self):
        processed_data = ""
        for item in self.data:
            processed_data += str(item) + " PROCESSED "
        return processed_data

if __name__ == "__main__":
    filter_instance = ExpandedFilterModule()
    filters = filter_instance.NewFilters()
    result = filters['new_filter']('Initial data')
    print(result)

    another_instance = AnotherModule()
    another_instance.AddData(10)
    another_instance.AddData(20)
    processed_result = another_instance.ProcessData()
    print(processed_result)
