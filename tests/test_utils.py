from src.utils import select_trs, print_trs_list_items


def test_select_trs():
    test_data1 = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                   'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                   'description': 'Перевод организации', 'to': 'Счет 64686473678894779589'},
                  {
                  },
                  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                   'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
                   'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                   'to': 'Счет 35383033474447895560'}]
    test_data2 = [{
                  },
                  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                   'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
                   'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                   'to': 'Счет 35383033474447895560'},
                    {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                   'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                   'description': 'Перевод организации','to': 'Счет 64686473678894779589'}
                  ]
    assert select_trs(test_data1)[0].date == select_trs(test_data2)[0].date
    assert print_trs_list_items(select_trs(test_data1)) == print_trs_list_items(select_trs(test_data2))