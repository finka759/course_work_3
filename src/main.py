import json

from src.utils import get_data_full, get_sorted_trns_by_date, print_trs_list_items
from transaction import Transaction



def main():
    with open("../sourses/operations.json", "r", encoding="utf-8") as file:
        data_ = json.load(file)
        selected_trs_list = select_trs(data_)
        print_trs_list_items(selected_trs_list)






def select_trs(data_):
    data_full = get_data_full(data_)
    sorted_trns_by_date = get_sorted_trns_by_date(data_full)

    selected_list = sorted_trns_by_date[:5]

    selected_trs_list = []
    for list_item in selected_list:
        selected_trs_list.append(Transaction(list_item))

    print(selected_trs_list)
    return selected_trs_list








if __name__ == '__main__':
    main()
