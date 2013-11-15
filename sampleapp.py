import os
from flask import Flask, render_template
import amazonproduct
import lxml.etree

app = Flask(__name__)
api = amazonproduct.API()

@app.route('/')
def index():
    res = api.item_lookup(ItemId='9780131103627',
                          IdType='EAN',
                          ResponseGroup='ItemAttributes',
                          SearchIndex='All')
    res_xml = lxml.etree.tounicode(res, pretty_print=True)
    return render_template('index.html', response=res, response_xml=res_xml)

if __name__ == '__main__':
    app.run()
