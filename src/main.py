import json

from src.utils import print_trs_list_items, select_trs


def main():
    with open("../sourses/operations.json", "r", encoding="utf-8") as file:
        data_ = json.load(file)
        selected_trs_list = select_trs(data_)
        print_trs_list_items(selected_trs_list)


if __name__ == '__main__':
    main()
