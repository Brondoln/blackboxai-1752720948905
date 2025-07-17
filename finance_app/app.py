# app.py
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Reemplazar con una clave segura en producción

# In-memory storage for transactions (for demonstration purposes)
transactions = []

@app.route('/')
def index():
    """
    Dashboard displaying a summary of finances.
    """
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = total_income - total_expense
    return render_template('index.html', balance=balance, income=total_income, expense=total_expense)

@app.route('/finances', methods=['GET', 'POST'])
def finances():
    """
    Page to add income/expense transactions and display history.
    """
    if request.method == 'POST':
        try:
            type_ = request.form.get('type')
            description = request.form.get('description', '')
            amount = float(request.form.get('amount'))
            # Append the new transaction
            transactions.append({"type": type_, "description": description, "amount": amount})
            flash("Transacción agregada exitosamente", "success")
        except Exception as e:
            flash("Error: " + str(e), "danger")
        return redirect(url_for('finances'))
    
    return render_template('finances.html', transactions=transactions)

@app.route('/chat')
def chat():
    """
    Chat interface with embedded intelligent agent webchat.
    """
    return render_template('chat.html')

# Custom Error Handlers

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)
