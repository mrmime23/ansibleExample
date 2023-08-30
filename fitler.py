#!/usr/bin/python
class filter_module(object):
    def filters(self):
        return {
            'a_filter': self.a_filter
        }

    def a_filter(self, a_variable):
        a_newvariable = a_variable + ' CRAZY NEW FILTER'
        return a_newvariable
