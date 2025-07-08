def transformer_donnees(pari):
    return [
        float(pari["cote"]),
        int(pari["type"]),
        int(pari["groupe"]),
        float(pari.get("param", 0))
    ]
