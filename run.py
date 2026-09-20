from app import create_app

# Flask uygulamasini uygulama fabrikasi uzerinden olustur.
app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)