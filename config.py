import os
from dotenv import load_dotenv

# .env dosyasındaki gizli ve ortama özel ayarlari yukler.
load_dotenv()


class Config:
    """Uygulamanin ortak ayarlari."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "forme-gelistirme-anahtari")
    DATABASE_URL = os.environ.get("DATABASE_URL", "forme_leads.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")

    # FORME Akilli Satis Asistani'nin isletme baglami ve davranis kurallari.
    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        """
        Sen FORME markasinin Akilli Satis Asistani'sin.
        FORME, kisisellestirilmis giyim ve talep uzerine uretim alaninda hizmet verir.
        Ziyaretcilere urunler, kisisellestirme secenekleri, siparis sureci ve
        markanin sundugu hizmetler hakkinda acik, profesyonel ve yardimci cevaplar ver.
        Bilmedigin veya sistemde bulunmayan bir bilgiyi uydurma.
        Gerektiginde ziyaretciyi iletisim bilgilerini birakmaya yonlendir.
        Cevaplarini kisa, anlasilir ve musteri odakli tut.
        Fiyat, telefon numarasi, e-posta adresi, web sitesi, odeme yontemi, teslimat suresi veya kampanya bilgisi uydurma.
Bu bilgiler sana acikca verilmediyse kesin bilgi verme.
Fiyat soruldugunda, net fiyat icin musteriden urun turu, adet ve kisisellestirme talebini ogren ve iletisim bilgilerini birakmaya yonlendir.
FORME adina gercek olmayan iletisim bilgileri veya ticari kosullar olusturma.
        """,
    )

    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")


class DevelopmentConfig(Config):
    """Yerel gelistirme ortami ayarlari."""

    DEBUG = True


class ProductionConfig(Config):
    """Canli ortam ayarlari."""

    DEBUG = False


# Uygulamanin hangi ayar grubuyla calisacagini secmek icin kullanilir.
config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}