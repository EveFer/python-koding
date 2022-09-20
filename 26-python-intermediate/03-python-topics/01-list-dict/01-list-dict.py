def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {
        'name': 'Fernanda',
        'lastName': 'Palacios'
    }

    super_list = [
        {
            'name': 'Fernanda',
            'lastName': 'Palacios'
        },
        {
            'name': 'Jose',
            'lastName': 'Lopez'
        },
        {
            'name': 'Guadalupe',
            'lastName': 'Palacios'
        },
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.45]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    print("--------")

    for item in super_list:
        print(item)

# entry point
if __name__ == '__main__':
    run()