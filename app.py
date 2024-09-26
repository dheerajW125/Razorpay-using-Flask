from flask import Flask, render_template, request, redirect, jsonify
import razorpay


app = Flask(__name__)
razorpay_client = razorpay.Client(auth=("rzp_test_xxcVSfcWJgOsYT", "0cucu530NfgYo5nysBcyyOLC"))

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/create_order', methods=['POST'])
def create_order():
    try:
        payment_details = request.get_json()
        if 'amount' not in payment_details:
            return jsonify({"error": "Amount is required"}), 400
        
        order_data = {
            "amount": int(payment_details['amount']) * 100,  # Convert to paise
            "currency": "INR",
            "payment_capture": "1"
        }
        razorpay_order = razorpay_client.order.create(order_data)
        return jsonify(razorpay_order)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__== '__main__':
    app.run(debug=True, port=5002)