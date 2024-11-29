from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Data gaji pokok dan persen lembur
gaji_pokok = [5000000, 6500000, 9500000]
persen_lembur = [30, 32, 34, 36, 38]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hitung", methods=["POST"])
def hitung():
    data = request.json
    golongan = data.get("golongan")
    jam_lembur = int(data.get("jam_lembur", 0))

    if golongan == "A":
        index_gaji = 0
    elif golongan == "B":
        index_gaji = 1
    elif golongan == "C":
        index_gaji = 2
    else:
        return jsonify({"error": "Golongan tidak valid."}), 400

    gaji = gaji_pokok[index_gaji]

    if jam_lembur == 1:
        persen = persen_lembur[0]
    elif jam_lembur == 2:
        persen = persen_lembur[1]
    elif jam_lembur == 3:
        persen = persen_lembur[2]
    elif jam_lembur == 4:
        persen = persen_lembur[3]
    elif jam_lembur >= 5:
        persen = persen_lembur[4]
    else:
        persen = 0

    gaji_lembur = (persen / 100) * gaji
    total_penghasilan = gaji + gaji_lembur

    return jsonify({
        "gaji_pokok": f"Rp{gaji:,}",
        "gaji_lembur": f"Rp{gaji_lembur:,} ({persen}%)",
        "total_penghasilan": f"Rp{total_penghasilan:,}"
    })

if __name__ == "__main__":
    app.run(debug=True)
