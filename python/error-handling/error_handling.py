def handle_error_by_throwing_exception():
    raise Exception('this is an exception')


def handle_error_by_returning_none(input_data):
    try:
        input_data
    except:
        pass


def handle_error_by_returning_tuple(input_data):
    pass


def filelike_objects_are_closed_on_exception(filelike_object):
    pass
