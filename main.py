from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat, reports
from datetime import datetime


app = Flask(__name__)


class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)
    
    def post(self):
        bill_form = BillForm(request.form)
        amount, period, name1, days_in_house1, name2, days_in_house2 = [x.data for x in bill_form][:-1]
        bill = flat.Bill(amount, period)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        flatmate2 = flat.Flatmate(name2, days_in_house2)

        report = reports.PDFReport(filename=f'Bill for {period} for {name1} and {name2} at {datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pdf')
        report.generate(flatmate1, flatmate2, bill)
        return render_template('bill_form_page.html', 
                               result=True,
                               bill_form=bill_form,
                               name1=name1,
                               name2=name2,
                               amount1 = flatmate1.pays(bill, flatmate2),   
                               amount2 = flatmate2.pays(bill, flatmate1))


class BillForm(Form):
    amount = StringField('Bill amount: ', default='70000')
    period = StringField('Period: ', default='October 2023')

    name1 = StringField('Name: ', default='John')
    days_in_the_house1 = StringField('Days in the house: ', default=20)

    name2 = StringField('Name: ', default='Georg')
    days_in_the_house2 = StringField('Days in the house: ', default=30)

    button = SubmitField('SUBMIT')

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/result', view_func=ResultPage.as_view('result_page'))

app.run(debug=True)