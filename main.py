#  LRU Python script.
from lru_cache_class import LRUClass
from Timer import timer
from tabulate import tabulate
import re
import sys
from jinja2 import Template


@timer
def create_lru(capacity, query_type, keys, values):
    """
    Create cache and execute a given sequence of SET(key, value) and GET(key) operations.
    Generate report with intput output and sequence of execution
    :param capacity: Int
    :param query_type: List
    :param keys: List
    :param values: List
    :return: results of all the GET operations from the sequence As list.
    """
    # Define variables
    output = []  # output result
    # Check capacity and raise error when it is equal to zero no cache with 0 capacity
    if capacity == 0:
        insert_to_report('Cache Capacity could not be 0.')
        raise AttributeError('Cache Capacity could not be 0.')
    # Create Class object with input capacity
    lru_obj = LRUClass(capacity)
    # create_calls Function will generate the code of the sequence of SET and GET
    r = create_calls("lru_obj", lru_obj, query_type, keys, values)

    code = "\n".join(r)
    # Execute generated code
    exec(code)
    print(code)
    print(output)
    # preprae table data
    dispalyed_data = []
    for i in range(0, len(query_type)):
        data = []
        data.append(lru_obj.operations[i])
        data.append(lru_obj.cache_after[i])
        data.append(lru_obj.return_value[i])
        data.append(lru_obj.side_effect[i])
        dispalyed_data.append(data)
    print(
        tabulate(dispalyed_data, headers=['Operation', 'Cache After', 'Return Value', 'Side Effect'], tablefmt='grid'))
    with open('report.txt', 'w') as file:
        file.write(f"""Input:
        capacity = {capacity}
        query_type = {query_type}
        keys = {keys}
        values = {values}
        \n""")
        file.write(f"""output: 
        {output} \n""")
        file.write("Execution Process \n")
        file.write(tabulate(dispalyed_data, headers=['Operation', 'Cache After', 'Return Value', 'Side Effect'],
                            tablefmt='grid'))
    return output


def create_calls(str_obj, lru_obj, query_types, keys, values):
    """
    generate the code of the sequence of SET and GET to automate the task
    :param str_obj: Str class object used to create the SET and GET
    :param lru_obj: Class object
    :param query_types: List
    :param keys: List
    :param values: List
    :return: List with generated code
    """
    # Define variables
    query_code = []  # Used to save the generated code after looping over query_types
    try:
        for query in range(0, len(query_types)):
            # check the Query type
            if query_types[query].upper() == "SET".upper():
                # Save The operations to generate report
                lru_obj.operations.append("SET (" + str(keys[query]) + "," + str(values[query]) + ")")
                # Generate the SET code based on jinja template
                put_tmp = Template("{{ OBJ }}.put({{ KEY }},{{ VALUE }})")
                put_render_result = put_tmp.render(OBJ=str_obj, KEY=keys[query], VALUE=values[query])
                # Save the generated code line
                query_code.append(put_render_result)
            elif query_types[query].upper() == "GET".upper():
                # Save The operations to generate report
                lru_obj.operations.append("GET (" + str(keys[query]) + ")")
                # Generate the GET code based on jinja template
                get_tmp = Template("output.append(({{ OBJ }}.get({{ KEY }})))")
                get_render_result = get_tmp.render(OBJ=str_obj, KEY=keys[query])
                # Save the generated code line
                query_code.append(get_render_result)
            else:
                insert_to_report("There is no Query with this name please verify query_types List.")
                raise IOError("There is no Query with this name please verify query_types List.")
    except Exception as Except:
        raise Except
    return query_code


def insert_to_report(data):
    """
    insert data to report file
    :param data:
    :return:
    """
    with open('report.txt', 'w') as file:
        file.write(data)


def format_input(file_path):
    """
    # Get the input file path as argument if not use the input.txt it's possible to provide any
    # file path just be sure to make the variable and its input in the same line separated by a space
    :param file_path:
    :return: capacity, query_type, keys, values
    """
    try:
        """Add the input data from the file as string"""
        with open(file_path) as f:
            lines = f.readlines()
        """Extract the input data using regx , remove whitespace and convert it to the appropriate type"""
        input_regex = r'.*?\=(.*)\n'
        capacity = int(re.search(input_regex, lines[1]).group(1))
        query_type = [q.strip() for q in re.search(input_regex, lines[2]).group(1).strip().strip('][').split(',')]
        keys = [k.strip() for k in re.search(input_regex, lines[3]).group(1).strip().strip('][').split(',')]
        values = [v.strip() for v in re.search(input_regex, lines[4]).group(1).strip().strip('][').split(',')]
    except Exception as Ex:
        print(type(Ex).__name__)
        if type(Ex).__name__ == "FileNotFoundError":
            insert_to_report('File Path Not Found.')
            raise FileNotFoundError('File Path Not Found.')
        elif type(Ex).__name__ == "AttributeError":
            insert_to_report('Please verify the structure of the input data inserted to the file')
            raise AttributeError('Please verify the structure of the input data inserted to the file')
        else:
            insert_to_report("Error occurred during extraction data")
            raise "Error occurred during extraction data"
    return capacity, query_type, keys, values


if __name__ == '__main__':
    """
    Generate LRU based on input file 
    """
    try:
        input_file_path = sys.argv[1]
    except IndexError:
        input_file_path = "input_files/input.txt"
    # Start LRU Process
    print(input_file_path)
    capacity, query_type, keys, values = format_input(input_file_path)
    print(f"Output : "+str(create_lru(capacity, query_type, keys, values)))
