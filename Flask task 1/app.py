from flask import Flask,request,render_template,url_for

app=Flask(__name__)

@app.route('/')
def index_Fun():
    return render_template('index.html')

@app.route('/upper',methods=['POST'])
def upper_case():
    st=request.form.get('a')
    Capital=st.upper()
    return render_template('upper.html',Capital=Capital)



if __name__=="__main__":
    app.run(debug=True)