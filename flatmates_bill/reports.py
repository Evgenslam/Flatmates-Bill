import webbrowser
import os
from filestack import Client
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv()


class PDFReport:
    """
    Creates a pdf file that contains flatmates' names, bill amount and
    due payment for each flatmate
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Insert image
        pdf.image('files/house.png', w=40, h=40,
                  link='https://www.notion.so/ec69f57bf04d45eda7060d379ad67389?v=f43178eebb7e4eb0ae3799ae1ced0b89&p=0c9bc0a9ed81493c9c4d04d2e09678a2&pm=s')

        #Insert title
        pdf.set_font(family='Arial', style='B', size=24)
        pdf.cell(w=0, h=80, txt='Bill shares', border=1, align='C', ln=1)

        #insert period
        pdf.set_font(family='Arial', size=18)
        pdf.cell(w=100, h=40, txt='Period', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        #insert flatmates
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate1.pays(bill, flatmate2)), border=1, ln=1)
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate2.pays(bill, flatmate1)), border=1, ln=1)

        #change directory to files, generate and open pdf
        os.chdir('pdfreports')
        pdf.output(self.filename)
        webbrowser.open(self.filename)
        os.chdir('../')


class FileSharer:

    def __init__(self, filepath: str, api_key: str = os.getenv('FILESHARER_API_KEY')) -> str:
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

