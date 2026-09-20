# FORME Akıllı Satış Asistanı

FORME Akıllı Satış Asistanı, kişiselleştirilmiş giyim ve talep üzerine üretim alanında faaliyet gösteren FORME markası için geliştirilmiş yapay zekâ destekli bir web uygulamasıdır.

Proje, web sitesi ziyaretçilerinin ürünler, kişiselleştirme seçenekleri ve sipariş süreçleri hakkında bilgi almasını ve potansiyel müşteri bilgilerinin (lead) kaydedilmesini sağlar.

## Projenin Amacı

Bu projenin temel amacı, web sitesi ziyaretçilerine yapay zekâ destekli bir satış asistanı sunarken potansiyel müşterilerin iletişim ve talep bilgilerinin kayıt altına alınmasını sağlamaktır.

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Groq AI API
- HTML / CSS / JavaScript
- Wix Studio / Velo
- Render
- GitHub

## Mimari Yapı

Proje Separation of Concerns (Sorumlulukların Ayrılması) prensibine göre geliştirilmiştir.

- `run.py` → Uygulamayı başlatır.
- `config.py` → Ortam değişkenleri ve uygulama ayarlarını yönetir.
- `app/database.py` → SQLite veritabanı işlemlerini yönetir.
- `app/routes.py` → Web sayfaları ve API endpointlerini yönetir.
- `app/services/ai_service.py` → Yapay zekâ servisiyle iletişimi yönetir.
- `app/templates/index.html` → Akıllı satış asistanı arayüzüdür.
- `app/templates/dashboard.html` → Potansiyel müşteri yönetim panelidir.

## Temel Özellikler

- Yapay zekâ destekli müşteri soru-cevap sistemi
- Potansiyel müşteri bilgilerinin kaydedilmesi
- İsim, telefon ve müşteri talebi kaydı
- SQLite veritabanı
- Müşteri yönetim paneli
- REST API yapısı
- Wix Studio entegrasyonu
- Render üzerinde canlı backend

## API Endpointleri

- `GET /health` → Sistem durumunu kontrol eder.
- `POST /api/sohbet` → Yapay zekâ ile mesajlaşmayı sağlar.
- `POST /api/leads` → Yeni potansiyel müşteri kaydı oluşturur.
- `GET /api/leads` → Potansiyel müşteri kayıtlarını listeler.

## Canlı Uygulama

### Wix Web Sitesi
https://askinseval930.wixstudio.com/forme-ai

### Render Backend
https://forme-ai.onrender.com

### Sağlık Kontrolü
https://forme-ai.onrender.com/health

### Müşteri Yönetim Paneli
https://forme-ai.onrender.com/dashboard

## Güvenlik

API anahtarları ve hassas bilgiler `.env` dosyasında tutulmaktadır. `.env` dosyası `.gitignore` aracılığıyla GitHub deposunun dışında bırakılmıştır.

SQL sorgularında parametreli sorgular kullanılarak güvenli veri işlemleri uygulanmıştır.

## Proje Senaryosu

Ziyaretçi FORME web sitesindeki Akıllı Satış Asistanı üzerinden ürün ve kişiselleştirme seçenekleri hakkında soru sorabilir. Potansiyel müşteri adını, telefon numarasını ve talebini bıraktığında bilgiler Flask API üzerinden SQLite veritabanına kaydedilir.

İşletme sahibi, müşteri yönetim panelinden kaydedilen potansiyel müşterileri görüntüleyebilir.

## Proje

Python ile Ürün Geliştirme  
Proje Uzmanı Yetiştirme Programı
