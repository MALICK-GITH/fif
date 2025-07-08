from flask import Flask, render_template
from utils.fetch_api import get_paris_raw
from ai.preprocessor import transformer_donnees
from ai.predictor import predict

app = Flask(__name__)

@app.route("/")
def index():
    paris_recommandes = []

    for pari in get_paris_raw():
        vecteur = transformer_donnees(pari)
        resultat = predict(vecteur)
        if resultat["fiabilité"] >= 65:
            paris_recommandes.append({
                "match": pari["match"],
                "cote": pari["cote"],
                "type": pari["type"],
                "groupe": pari["groupe"],
                "fiabilité": f"{resultat['fiabilité']}%",
                "recommandé": "✅" if resultat["prediction"] == 1 else "❌"
            })

    return render_template("index.html", paris=paris_recommandes)

if __name__ == "__main__":
    app.run(debug=True)
