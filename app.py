from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        print(f"Nome: {nome}, Email: {email}")
        # Redireciona para seu link de pagamento
        return redirect("https://SEU-LINK-DE-PAGAMENTO.com")
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)