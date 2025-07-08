import joblib

model = joblib.load("ai/model.pkl")

def predict(features):
    prediction = model.predict([features])[0]
    proba = model.predict_proba([features])[0]
    return {
        "prediction": int(prediction),
        "fiabilité": round(max(proba) * 100, 2)
    }
