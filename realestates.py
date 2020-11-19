"""Web application to yield real estates for a respective customer."""

from typing import Iterable
from xml.etree.ElementTree import Element, SubElement

from flask import Response

from mdb import Customer
from openimmodb import Immobilie
from wsgilib import Error, HTML, Application


APPLICATION = Application('realestates', debug=True)
TITLE = 'Ihre aktuellen Immobilien bei HOMEINFO'
TABLE_HEADERS = ('#', 'Objektnummer', 'Stand vom')


def get_table(immobilien: Iterable[Immobilie]) -> Element:
    """Returns an HTML table."""

    table = Element('table', attrib={'border': '1'})
    header_row = SubElement(table, 'tr')

    for header in TABLE_HEADERS:
        header_col = SubElement(header_row, 'th')
        header_col.text = header

    for index, immobilie in enumerate(immobilien, start=1):
        row = SubElement(table, 'tr')
        col_index = SubElement(row, 'td')
        col_index.text = str(index)
        col_objektnr_extern = SubElement(row, 'td')
        col_objektnr_extern.text = str(immobilie.objektnr_extern)
        col_stand_vom = SubElement(row, 'td')
        col_stand_vom.text = str(immobilie.stand_vom)

    return table


def get_html(customer: Customer, immobilien: Iterable[Immobilie]) -> Element:
    """Returns the HTML document."""

    html = Element('html')
    head = SubElement(html, 'head')
    SubElement(head, 'meta', attrib={'charset': 'UTF-8'})
    title = SubElement(head, 'title')
    title.text = TITLE
    body = SubElement(html, 'body')
    header = SubElement(body, 'h1')
    intro = SubElement(header, 'span')
    intro.text = 'Immobilien von '
    company = SubElement(header, 'em')
    company.text = customer.name
    outro = SubElement(header, 'span')
    outro.text = ' bei HOMEINFO'
    body.append(get_table(immobilien))
    return html


@APPLICATION.route('/<int:cid>', methods=['GET'])
def get(cid: int) -> Response:
    """Returns the customer's real estates."""

    try:
        customer = Customer[cid]
    except Customer.DoesNotExist:
        return Error('No such customer.')

    immobilien = Immobilie.select().where(Immobilie.customer == customer)
    return HTML(get_html(customer, immobilien))
