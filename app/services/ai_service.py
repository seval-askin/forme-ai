import requests
from flask import current_app


class AIServiceError(Exception):
    """Yapay zeka servisiyle ilgili hatalari temsil eder."""

    pass


class AIService:
    """FORME Akilli Satis Asistani icin yapay zeka servisi."""

    def _sistem_mesaji(self):
        """Yapay zekanin davranis kurallarini config dosyasindan alir."""
        return current_app.config["BUSINESS_CONTEXT"]

    def yanit_uret(self, mesaj, gecmis=None):
        """
        Kullanicinin mesajini Groq API'ye gonderir
        ve yapay zeka cevabini dondurur.
        """

        api_key = current_app.config.get("GROQ_API_KEY", "")

        # API anahtari yoksa uygulama cokmek yerine demo cevabi verir.
        if not api_key:
            return (
                "Demo modu aktif. FORME Akilli Satis Asistani calisiyor, "
                "ancak gercek yapay zeka cevabi icin Groq API anahtari gereklidir."
            )

        if gecmis is None:
            gecmis = []

        mesajlar = [
            {
                "role": "system",
                "content": self._sistem_mesaji(),
            }
        ]

        # Onceki konusmalari mesaja ekler.
        mesajlar.extend(gecmis)

        # Kullanicinin yeni mesajini ekler.
        mesajlar.append(
            {
                "role": "user",
                "content": mesaj,
            }
        )

        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        veri = {
            "model": "openai/gpt-oss-20b",
            "messages": mesajlar,
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=veri,
                timeout=30,
            )

            response.raise_for_status()

            sonuc = response.json()

            return sonuc["choices"][0]["message"]["content"]

        except requests.RequestException as hata:
            raise AIServiceError(
                "Yapay zeka servisine su anda ulasilamiyor."
            ) from hata

        except (KeyError, IndexError, TypeError, ValueError) as hata:
            raise AIServiceError(
                "Yapay zeka servisinden beklenmeyen bir cevap alindi."
            ) from hata


# Uygulamanin diger bolumlerinde kullanilacak tek servis nesnesi.
ai_service = AIService()