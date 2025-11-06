from flask import Flask, render_template, request

import os



# --- Monorepo Path Setup ---

# Define the absolute path to the project directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



# Set the template and static folder relative to the project directory

app = Flask(

    __name__,

    template_folder=os.path.join(BASE_DIR, 'templates'),

    static_folder=os.path.join(BASE_DIR, 'static')

)

# --- End Monorepo Path Setup ---



@app.route('/')

def index():

    # Initial page load - no calculation yet

    return render_template('index.html')



@app.route('/calculate', methods=['POST'])

def calculate():

    # Get values from the web form using the 'request.form' object

    amount = float(request.form['amount'])

    tip = int(request.form['tip'])

    split = int(request.form['split'])



    # --- Your Core Logic (NO CHANGES HERE) ---

    total_tip_amount = amount * tip / 100

    total_bill = amount + total_tip_amount

    bill_per_person = round(total_bill / split, 2)

    # --- End Core Logic ---

   

    # Format the result nicely for display

    result_text = f"Each person should pay: ${bill_per_person:.2f}"

   

    # Render the page again, passing the result to the HTML template

    return render_template('index.html', result=result_text)



if __name__ == '__main__':

    app.run(debug=True)