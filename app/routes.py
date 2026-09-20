from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import AIServiceError, ai_service


# Web sayfalari icin Blueprint.
pages_bp = Blueprint("pages", __name__)

# API islemleri icin Blueprint.
# /api on eki uygulama kurulurken __init__.py dosyasinda eklenecek.
api_bp = Blueprint("api", __name__)


@pages_bp.route("/")
def ana_sayfa():
    """Musteriye gosterilecek ana sayfayi acar."""
    return render_template("index.html")


@pages_bp.route("/dashboard")
def dashboard():
    """Isletme sahibinin lead listesini gorecegi paneli acar."""
    return render_template("dashboard.html")


@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    """Kullanicinin mesajini yapay zeka servisine gonderir."""

    veri = request.get_json(silent=True) or {}

    mesaj = veri.get("mesaj", "").strip()
    gecmis = veri.get("gecmis", [])

    if not mesaj:
        return jsonify(
            {
                "basari": False,
                "hata": "Mesaj alani bos birakilamaz.",
            }
        ), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)

        return jsonify(
            {
                "basari": True,
                "cevap": cevap,
            }
        )

    except AIServiceError as hata:
        return jsonify(
            {
                "basari": False,
                "hata": str(hata),
            }
        ), 503


@api_bp.route("/leads", methods=["POST"])
def yeni_lead():
    """Yeni musteri iletisim bilgisini veritabanina kaydeder."""

    veri = request.get_json(silent=True) or {}

    isim = veri.get("isim", "").strip()
    telefon = veri.get("telefon", "").strip()
    mesaj = veri.get("mesaj", "").strip() or None

    if not isim or not telefon:
        return jsonify(
            {
                "basari": False,
                "hata": "Isim ve telefon alanlari zorunludur.",
            }
        ), 400

    try:
        lead_id = lead_ekle(isim, telefon, mesaj)

        return jsonify(
            {
                "basari": True,
                "mesaj": "Iletisim bilginiz basariyla kaydedildi.",
                "id": lead_id,
            }
        ), 201

    except Exception:
        return jsonify(
            {
                "basari": False,
                "hata": "Musteri bilgisi kaydedilirken bir hata olustu.",
            }
        ), 500


@api_bp.route("/leads", methods=["GET"])
def leadleri_listele():
    """Kayitli musteri adaylarini JSON olarak dondurur."""

    try:
        leadler = tum_leadler()

        return jsonify(
            {
                "basari": True,
                "leadler": leadler,
            }
        )

    except Exception:
        return jsonify(
            {
                "basari": False,
                "hata": "Musteri kayitlari alinirken bir hata olustu.",
            }
        ), 500