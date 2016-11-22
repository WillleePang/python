#!/usr/bin/env python
# -*- coding:utf-8 -*-


# The main HTML for the whole page.
PAGE_HTML = """
<p>Welcome, {name}!</p>
<p>Products:</p>
<ul>
{products}
</ul>
"""
# The HTML for each product displayed.
PRODUCT_HTML = "<li>{prodname}: {price}</li>\n"


def make_page(username, products):
    product_html = ""
    for prodname, price in products:
        product_html += PRODUCT_HTML.format(
            prodname=prodname, price=price)
    html = PAGE_HTML.format(name=username, products=product_html)
    return html


def render_function(context, do_dots):
    c_user_name = context['user_name']
    c_product_list = context['product_list']
    c_format_price = context['format_price']

    result = []
    append_result = result.append
    extend_result = result.extend
    to_str = str

    extend_result(['<p>Welcome, ', to_str(c_user_name), '!</p>\n<p>Products:</p>\n<ul>\n'])
    for c_product in c_product_list:
        extend_result([
            '\n <li>',
            to_str(do_dots(c_product, 'name')),
            ':\n ',
            to_str(c_format_price(do_dots(c_product, 'price'))),
            '</li>\n'
        ])
    append_result('\n</ul>\n')


if __name__ == '__main__':
    print make_page("pangweili", [{'book1', 100}, {'book2', 100}, {'book3', 100}, {'book4', 100}])
