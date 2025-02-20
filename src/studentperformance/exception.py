import sys #helps in tracking error details
from src.studentperformance.logger import logging


def error_message_detail(error,error_detail:sys):
    '''
    error_detail.exc_info() (which is sys.exc_info()) returns a tuple containing three values related to the last raised exception:
    (type, value, traceback)
    Where:
        type → The type of the exception (e.g., ZeroDivisionError, ValueError).
        value → The actual error message (e.g., "division by zero").
        traceback (exc_tb) → The traceback object, which contains information about where the error occurred (like file name, line number, etc.).
    We ignore type and value by assigning them to _(a throwaway variable).
    '''
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        return self.error_message