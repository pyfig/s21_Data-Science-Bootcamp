def data_types():
    int_var = 42
    str_var = "Hello, World!"
    float_var = 3.14
    bool_var = True
    list_var = [1, 2, 3]
    dict_var = {"key": "value"}
    tuple_var = (1, 2, 3)
    set_var = {1, 2, 3}
    print([type(int_var), type(str_var), type(float_var), type(bool_var), 
           type(list_var), type(dict_var), type(tuple_var), type(set_var)])

if __name__ == '__main__':
    data_types()
