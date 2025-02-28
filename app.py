from flask import Flask,render_template,request
import joblib

filename = 'classifier_model.sav'
classifier = joblib.load(filename)
cv = joblib.load("countvector.sav")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        return render_template('result.html', prediction = my_prediction)
    
if __name__ == '__main__':
    app.run(debug=True)
