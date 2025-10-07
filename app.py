import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
@app.route('/',methods=['Get','Post'])
def home():
     return render_template('home.html')
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    msg=''
    output=""
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = int(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])
        test_data=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        print("test_data",test_data)
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score

        data = pd.read_csv("heart.csv")
        data.head()

        data.info()

        X= data.drop('target', axis=1)
        Y= data['target']

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        model = RandomForestClassifier(n_estimators=100, random_state=42)

        model.fit(X_train, Y_train)

        Predictions = model.predict([test_data])
        print(Predictions)
        
        if(Predictions[0]==0):
                print("No Heart Disease")
                output="No Heart Disease" 
                return render_template('No_Disease.HTML', msg=msg, output= output, Title="No Disease Prediction")

        else:
                print("Heart Disease")
                output="Heart Disease"
                return render_template('Treatment.HTML', msg=msg, output= output, Title="Heart Disease Prediction")
    return render_template('Heart_Disease_Prediction.html', msg=msg, output= output, Title="Heart Disease Prediction")
@app.route('/signup', methods=['GET', 'POST'])
def SignUp():
    msg = ''
    if request.method =='POST':
        username=request.form['username']
        password=request.form['password']
        confirm_password=request.form['confirm_password']
        print("Username",username)
        print("password",password)
        print("confirm_password",username)
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ashwathy21!",
            database="Heart_Disease"
            )
        mycursor = mydb.cursor()
        sql="Insert Into signup(username, password) Values (%s, %s)"
        val=(username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)
        msg="Record successfully inserted"
        return render_template('login.html', msg=msg)

    return render_template('Signup.html', msg=msg)
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method =='POST': # when uclick the btn
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        import mysql.connector
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ashwathy21!",
            database="Heart_Disease"
        )
        cursor = mydb.cursor()
        count = cursor.execute(''' select count(*) from Signup where username=%s and password=%s''', (username, password))
        print((''' select count(*) from Heart_Disease where  username=%s and password=%s''', (username, password)))
        count = cursor.fetchone()[0]
        print(count)
        cursor.close()
        if count>0:

            msg = 'Login Success'
            return render_template('Dashboard.HTML', msg=msg)
        else:
            msg = 'Login failed'
            return render_template('Login.HTML', msg=msg)
        print(msg)
    return render_template('Login.HTML', msg=msg)
@app.route('/upload', methods=['GET', 'POST'])
def Upload():
   
    msg = ''
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        f.save(secure_filename(f.filename))
        return redirect("/datasetview") 
    return render_template('Upload.html', msg=msg)
@app.route('/datasetview', methods=['GET', 'POST'])
def datasetview():
    msg = ''
    df = pd.read_csv('heart.csv')
    data = (df.head(20))
    df.shape
    df.info()
    df.columns
    data.to_html(header="true", table_id="table")
    return render_template('data_set_view.html', column_names=data.columns.values, row_data=list(data.values.tolist()),zip=zip)
@app.route('/Lupusprediction', methods=['GET', 'POST'])
def Lupusprediction():
    msg=''
    output=""
    if request.method == 'POST':
        age = int(request.form['Age'])
        gender = int(request.form['Gender'])
        Sickness_time_duration = int(request.form['Sickness_time_duration'])
        Esbach = int(request.form['Esbach'])
        MBL_Level = int(request.form['MBL_Level'])
        ESR = int(request.form['ESR'])
        C3 = int(request.form['C3'])
        C4 = int(request.form['C4'])
        CRP = int(request.form['CRP'])
        ANA = int(request.form['ANA'])
        ANTIdsDNA = int(request.form['ANTIdsDNA'])
        SLE_DAI = int(request.form['SLE_DAI'])
        test_data=[age,gender, Sickness_time_duration ,Esbach,MBL_Level,ESR,C3,C4,CRP,ANA,ANTIdsDNA,SLE_DAI]
        print("test_data",test_data)
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.metrics import accuracy_score
        data = pd.read_csv("static/data_lupus.csv")
        data.head()

        data.info()
        Y= data['Lupus']
        X= data.drop('Lupus', axis=1)
        

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        model = DecisionTreeClassifier(criterion='entropy', random_state=1)
        model.fit(X_train, Y_train)

        Predictions = model.predict([test_data])
        print(Predictions)
        if(Predictions[0]==0):
                print("No Lupus Disease")
                output="No Lupus Disease"
                return render_template('No_Disease.HTML', msg=msg, output= output, Title="No Disease Prediction")
        else:
                print("Lupus Disease")
                output="Lupus Disease"
                return render_template('Lupus_Treatment.HTML', msg=msg, output= output, Title="Lupus Disease Prediction")

    return render_template('Lupus_Prediction.html', msg=msg, output= output, Title="Lupus Disease Prediction")
@app.route('/Dashboard', methods=['GET', 'POST'])
def Dashboard():
    return render_template('Dashboard.html', Title="Lupus Disease Prediction")
  
if __name__ == '__main__':
    app.run(port=5000,debug=True)
