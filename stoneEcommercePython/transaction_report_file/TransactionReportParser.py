from datetime import datetime
from uuid import UUID


class TransactionReportParser(object):
    def parser(self, data):
        report = {'creditcard_transaction_collection': [], 'online_debit_transaction_collection': [],
                  'boleto_transaction_collection': []}
        switch = {'01': self.__parser_header,
                  '20': self.__parser_creditcard_transaction,
                  '40': self.__parser_online_debit_transaction,
                  '30': self.__parser_boleto_transaction,
                  '99': self.__parser_trailer}
        lines = data.replace('\r', '').split('\n')
        for line in lines:
            items_to_parse = line.split(',')
            if items_to_parse[0]:
                switch[items_to_parse[0]](items_to_parse, report)
        return report

    @staticmethod
    def __parser_header(row, report):
        print row
        if len(row) != 4:
            raise ValueError('The expected parameter count for Header parser is 4.', len(row))
        header = {'transaction_processed_date': datetime.strptime(row[1], '%Y%m%d'),
                  'report_file_create_date': datetime.strptime(row[2], '%Y%m%d %H:%M:%S'), 'version': row[3]}
        report['header'] = header

    @staticmethod
    def __parser_creditcard_transaction(row, report):
        if len(row) != 27:
            raise ValueError('The expected parameter count for CreditCardTransaction parser is 27', len(row))
        transaction = {'order_key': UUID(row[1]), 'order_reference': row[2], 'merchant_key': UUID(row[3]),
                       'merchant_name': row[4], 'transaction_key': UUID(row[5]), 'transaction_key_to_acquirer': row[6],
                       'transaction_reference': row[7], 'creditcard_brand': row[8], 'creditcard_number': row[9],
                       'installment_count': int(row[10]) if len(row[10].strip()) > 0 else 0, 'acquirer_name': row[11],
                       'status': row[12], 'amount_in_cents': long(row[13]) if len(row[13].strip()) > 0 else long(0),
                       'iata_amount_in_cents': long(row[14]) if len(row[14].strip()) > 0 else long(0),
                       'authorization_code': row[15], 'transaction_identifier': row[16],
                       'unique_sequential_number': row[17],
                       'authorized_amount_in_cents': long(row[18]) if len(row[18].strip()) > 0 else long(0),
                       'captured_amount_in_cents': long(row[19]) if len(row[19].strip()) > 0 else long(0),
                       'voided_amount_in_cents': long(row[20]) if len(row[20].strip()) > 0 else long(0),
                       'refunded_amount_in_cents': long(row[21]) if len(row[21].strip()) > 0 else long(0),
                       'acquirer_authorization_return_code': row[22],
                       'authorized_date': datetime.strptime(row[23], "%Y-%m-%dT%H:%M:%S") if len(
                           row[23].strip()) > 0 else None,
                       'captured_date': datetime.strptime(row[24], "%Y-%m-%dT%H:%M:%S") if len(
                           row[24].strip()) > 0 else None,
                       'voided_date': datetime.strptime(row[25], "%Y-%m-%dT%H:%M:%S") if len(
                           row[25].strip()) > 0 else None,
                       'last_probe_date': datetime.strptime(row[26], "%Y-%m-%dT%H:%M:%S") if len(
                           row[26].strip()) > 0 else None}
        report['creditcard_transaction_collection'].append(transaction)

    @staticmethod
    def __parser_boleto_transaction(row, report):
        if len(row) != 18:
            raise ValueError('The expected parameter count for BoletoTransaction  parser is 18', len(row))
        transaction = {'order_key': UUID(row[1]), 'order_reference': row[2], 'merchant_key': UUID(row[3]),
                       'merchant_name': row[4], 'transaction_key': UUID(row[5]),
                       'transaction_reference': row[6],
                       'status': row[7], 'nosso_numero': row[8], 'bank_number': row[9], 'agency': row[10],
                       'account': row[11], 'barcode': row[12],
                       'expiration_date': datetime.strptime(row[13], "%m/%d/%Y %I:%M:%S %p"),
                       'amount_in_cents': long(row[14]) if len(row[14].strip()) > 0 else long(0),
                       'amount_paid_in_cents': long(row[15]) if len(row[15].strip()) > 0 else long(0),
                       'payment_date': datetime.strptime(row[16], "%m/%d/%Y %I:%M:%S %p") if len(
                           row[16].strip()) > 0 else None,
                       'credit_date': datetime.strptime(row[17], "%m/%d/%Y %I:%M:%S %p") if len(
                           row[17].strip()) > 0 else None}
        report['boleto_transaction_collection'].append(transaction)

    @staticmethod
    def __parser_online_debit_transaction(row, report):
        if len(row) != 16:
            raise ValueError('The expected parameter count for OnlineDebitTransaction parser is 16', len(row))
        transaction = {'order_key': UUID(row[1]), 'order_reference': row[2], 'merchant_key': UUID(row[3]),
                       'merchant_name': row[4], 'transaction_key': UUID(row[5]),
                       'transaction_reference': row[6], 'bank': row[7],
                       'status': row[8],
                       'amount_in_cents': long(row[9]) if len(row[9].strip()) > 0 else long(0),
                       'amount_paid_in_cents': long(row[10]) if len(row[10].strip()) > 0 else long(0),
                       'payment_date': datetime.strptime(row[11], "%m/%d/%Y %I:%M:%S %p") if len(
                           row[11].strip()) > 0 else None,
                       'bank_return_code': row[12], 'bank_payment_date': row[13], 'signature': row[14],
                       'transaction_key_to_bank': row[15]}
        report['online_debit_transaction_collection'].append(transaction)

    @staticmethod
    def __parser_trailer(row, report):
        if len(row) != 5:
            raise ValueError("The expected parameter count for Trailer parser is 5", len(row))
        trailer = {'order_data_count': long(row[1]), 'creditcard_transaction_data_count': long(row[2]),
                   'boleto_transaction_data_count': long(row[3]), 'online_debit_transaction_data_count': long(row[4])}
        report['trailer'] = trailer
