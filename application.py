from flask import Flask,render_template,request
import pickle

application=Flask(__name__)
app=application

#import ridge and scaler pickle files
ridgeregressor=pickle.load(open('ridge_regressor.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def regressionprediction():
    if request.method=='POST':
        temp=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        DC=float(request.form.get('DC'))
        ISI=float(request.form.get('ISI'))
        BUI=float(request.form.get('BUI'))
        Classes=(request.form.get('Classes'))
        Region=(request.form.get('Region'))
        newdata=[[temp,RH,Ws,Rain,FFMC,DMC,DC,ISI,BUI,Classes,Region]]
        newdata_scaled=scaler.transform(newdata)
        result=ridgeregressor.predict(newdata_scaled)
        return render_template('index.html',result=result)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")

