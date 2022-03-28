from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/test',methods = ['POST', 'GET'])
def test():
  parametri = ["IQ", "Augums", "Kajas izmers"]
  param2 = ["https://norway.news24viral.com/wp-content/uploads/2021/12/1638397356_423_Alle-Guinness-verdensrekorder-satt-av-Justin-Bieber.jpg","https://presizely.finansavisen.no/980x%2Cdsu%2Car%3A16%3A9%2Csh%3A1.2%3A1.2%3A1.2%2Cq65%2Cprog/https://smooth-storage.aptoma.no/users/hegnar/images/8738763.jpg?t[quality]=100&t[resize][width]=500&t[resize][height]=500&accessToken=f9b85d56553202900c3eb5bec1f4e6827f9f515c87d3e2105c6ba7425e2e99a3","https://g.acdn.no/obscura/API/dynamic/r1/nadp/tr_2000_2000_s_f/0000/2014/08/13/8474273/1/original/Justin_Bieber_arrested_for_DUI__Miami_Beach__Florida___23_Jan_20.jpg?chk=21C977"]
  return render_template("test.html",parametri=parametri,images=images)

    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")
