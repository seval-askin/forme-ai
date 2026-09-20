from flask import Flask, jsonify
from flask_cors import CORS

from config import config_by_name
from app.database import init_db
from app.routes import api_bp, pages_bp


def create_app(config_name="development"):
    """Flask uygulamasini olusturur ve gerekli bilesenleri baglar."""

    app = Flask(__name__)

    # Secilen ortam ayarlarini yukle.
    app.config.from_object(config_by_name[config_name])

    # Wix gibi farkli bir kaynaktan gelecek isteklere izin ver.
    CORS(app, origins=app.config["CORS_ORIGINS"])

    # Veritabanini hazirla.
    init_db(app)

    # Sayfa ve API route'larini uygulamaya bagla.
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    # Sunucunun calisip calismadigini kontrol etmek icin kullanilir.
    @app.route("/health")
    def health():
        return jsonify(
            {
                "basari": True,
                "durum": "calisiyor",
                "uygulama": "FORME Akilli Satis Asistani",
            }
        )

    return app