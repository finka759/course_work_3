from src.transaction import Transaction


def select_trs(data_):
    data_full = get_data_full(data_)
    sorted_trns_by_date = get_sorted_trns_by_date(data_full)

    selected_list = sorted_trns_by_date[:5]

    selected_trs_list = []
    for list_item in selected_list:
        selected_trs_list.append(Transaction(list_item))
    return selected_trs_list

def print_trs_list_items(selected_trs_list):
    for selected_trs_list_item in selected_trs_list:
        print(selected_trs_list_item.get_output_str())


def get_data_full(data_):
    return [value for value in data_ if value != {}]


def get_sorted_trns_by_date(data_full):
    return sorted(data_full, key=lambda d: d['date'], reverse=True)