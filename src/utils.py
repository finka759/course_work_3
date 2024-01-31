def summ(a,b):
    return a+b

def print_trs_list_items(selected_trs_list):
    for selected_trs_list_item in selected_trs_list:
        print(selected_trs_list_item)

def get_data_full(data_):
    return [value for value in data_ if value != {}]


def get_sorted_trns_by_date(data_full):
    return sorted(data_full, key=lambda d: d['date'], reverse=True)