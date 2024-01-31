import json

from transaction import Transaction

SELECT_COUNT = 5

# json_link = "../sourses/operations.json"
# json_link = "../sourses/test_1.json"
json_link = "../sourses/test_2.json"





def main():
    with open(json_link, "r", encoding="utf-8") as file:
        data_ = json.load(file)
        selected_trs_list = select_trs(data_)
        print_trs_list_items(selected_trs_list)



def get_data_full(data_):
    return [value for value in data_ if value != {}]


def get_sorted_trns_by_date(data_full):
    return sorted(data_full, key=lambda d: d['date'], reverse=True)


def select_trs(data_):
    data_full = get_data_full(data_)
    sorted_trns_by_date = get_sorted_trns_by_date(data_full)

    selected_list = sorted_trns_by_date[:SELECT_COUNT]

    selected_trs_list = []
    for list_item in selected_list:
        selected_trs_list.append(Transaction(list_item))

    print(selected_trs_list)
    return selected_trs_list

def print_trs_list_items(selected_trs_list):
    for selected_trs_list_item in selected_trs_list:
        print(selected_trs_list_item)

def summ(a,b):
    return a+b




if __name__ == '__main__':
    main()
