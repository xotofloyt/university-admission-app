import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    output = ''
    value_out_of_range = 0
    value_not_number = 0    
    
    #Get inputs
    features = [x for x in request.form.values()]
    
    #Test if inputs are numbers
    try:
        features[0] = float(features[0])
    except ValueError:
        output += 'You did not enter a number for GPA. \n'
        value_not_number = 1
    
    try:
        features[1] = int(features[1])
    except ValueError:
        output += 'You did not enter a number for GRE Score. \n'
        value_not_number = 1
    
    if value_not_number:
        output += ' Please make sure entered values are numbers.'
        return render_template('index.html', prediction_text=output)
    
    
    
    #test if inputs within range    
    if features[0] > 4.0 or features[0] < 0:
        output += 'GPA out of range.\n'
        value_out_of_range = 1
    
    if features[1] > 800 or features[1] < 0:
        output += 'GRE Score out of range.\n'
        value_out_of_range = 1
        
    if value_out_of_range:
        output += ' Please make sure values are in range.\n'
        return render_template('index.html', prediction_text=output)
    
    
    #Output final result
    else:
        prediction = model.predict([features])
        output = 'Admitted' if prediction else 'Not Admitted'
        return render_template('index.html', prediction_text='Student is {}'.format(output))
    

if __name__ == "__main__":
    app.run(debug=True)