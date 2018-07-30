"""Web application to yield real estates for a respective customer."""

from mdb import Customer
from openimmodb import Immobilie
from wsgilib import Error, HTML, Application


APPLICATION = Application('realestates', debug=True)
TITLE = 'Ihre aktuellen Immobilien bei HOMEINFO'
HEAD = '<head>\n  <title>{}</title>\n</head>'.format(TITLE)
TEMPLATE = '<!DOCTYPE HTML>\n{}\n{{}}'.format(HEAD)
COLUMN = '    <td>\n      {}\n    </td>'
ROW = '  <tr>\n{}\n  </tr>'
TABLE = '<table border="1">\n{}\n</table>'
TABLE_HEADER = '    <th>\n      {}\n    </th>'
TABLE_HEADERS = ('Objektnummer', 'Stand vom')
COMPANY = '<em>{}</em>'
HEADER = '<h1>Immobilien von {} bei HOMEINFO</h1>'.format(COMPANY)


def table_header():
    """Returns the table header."""

    return ROW.format('\n'.join(
        TABLE_HEADER.format(header) for header in TABLE_HEADERS))


@APPLICATION.route('/<int:cid>', methods=['GET'])
def get(cid):
    """Returns the customer's real estates."""

    try:
        customer = Customer.get(Customer.id == cid)
    except Customer.DoesNotExist:
        raise Error('No such customer.')

    header = HEADER.format(customer)
    rows = [table_header()]

    for immobilie in Immobilie.select().where(Immobilie.customer == customer):
        columns = (
            COLUMN.format(immobilie.objektnr_extern),
            COLUMN.format(immobilie.stand_vom))
        rows.append(ROW.format('\n'.join(columns)))

    table = TABLE.format('\n'.join(rows))
    return HTML(TEMPLATE.format('{}\n{}'.format(header, table)))
