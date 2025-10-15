from flask import Flask, render_template, request

app = Flask(__name__)

# List of ASPECTS regions
ASPECTS_REGIONS = [
    "Caudate",
    "Lentiform nucleus",
    "Internal capsule",
    "Insular cortex",
    "M1 (anterior MCA cortex)",
    "M2 (MCA cortex lateral to insular cortex)",
    "M3 (posterior MCA cortex)",
    "M4 (anterior MCA territory lateral to M1)",
    "M5 (lateral MCA territory lateral to M2)",
    "M6 (posterior MCA territory lateral to M3)"
]

@app.route("/", methods=["GET", "POST"])
def index():
    score = 10
    selected_regions = []
    if request.method == "POST":
        selected_regions = request.form.getlist("regions")
        score -= len(selected_regions)
    return render_template("index.html", regions=ASPECTS_REGIONS, score=score, selected=selected_regions)

if __name__ == "__main__":
    app.run(debug=True)
