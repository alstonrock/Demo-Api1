from flask import Flask,jsonify

app = Flask(__name__)

country=[{'name':"China",
         'Rank(Area wise)':"4",
         'President':"Xi Jinping",
          'Population':"139.27 crores",
          'Capital':"Beijing"},
          {'name':"India",
          'President':"Ram Nath Kovind",
          'Population':"121 crores",
          'Capital':"Delhi",
          'Rank(Area wise)':"7"},
          {'name':"Russia",
          'Rank(Area wise)':"1",
          'President':"Vladimir Putin",
          'Population':"14.45 crores",
          'Capital':"Moscow"},
          {'name':"USA",
          'Rank(Area wise)':"3",
          'President':"Donald Trump",
          'Population':"32.28 crores",
          'Capital':"Washington D.C."},
          {'name':"CANADA",
          'President':"Justin Trudeau (PM)",
          'Population':"3.76 crores",
          'Capital':"Ottawa",
          'Rank (Area wise)':"2"},
          {'name':"United Kingdom",
          'President':"Queen Elizabeth II",
          'Population':"5.6 crores",
          'Capital':"London",
          'Rank(Area wise)':"80"
          }
          ]

@app.route('/')
def index():
    return "Welcome to the Con-Info Section:" 

@app.route("/country",methods=['GET'])
def get():
    return jsonify({'Countries': country})


if __name__ == "__main__":
    app.run(debug=True,port='8083')
