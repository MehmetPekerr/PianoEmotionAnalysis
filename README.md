# Müzik Duygu ve Tonalite Analizi

Bu proje, MIDI formatındaki müzik dosyalarını analiz ederek tonaliteyi ve yansıttığı duyguları tespit eden yapay zeka destekli bir web uygulamasıdır.

## Özellikler

- MIDI dosyalarının yüklenmesi ve analizi
- Tonalite tespiti (Major/Minor)
- Duygu analizi ve tahmini
- Görselleştirme ve raporlama
- Kullanıcı dostu web arayüzü

## Kurulum

1. Gerekli Python sürümünü yükleyin (Python 3.8 veya üzeri)

2. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/muzik-duygu-analizi.git
cd muzik-duygu-analizi
```

3. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows için
source .venv/bin/activate  # Linux/Mac için
```

4. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

1. Web uygulamasını başlatın:
```bash
python app.py
```

2. Tarayıcınızda `http://localhost:5000` adresine gidin

3. MIDI dosyası yükleyin ve analiz sonuçlarını görüntüleyin

## Proje Yapısı

```
muzik-duygu-analizi/
├── app.py                    # Web uygulaması
├── music_emotion_analyzer.py # Ana analiz kodu
├── requirements.txt          # Bağımlılıklar
├── emotion_model.h5         # Duygu analizi modeli
├── tonality_model.h5        # Tonalite analizi modeli
├── templates/               # Web arayüzü
│   └── index.html
├── train/                   # Eğitim verileri
├── test/                    # Test verileri
├── val/                     # Doğrulama verileri
└── uploads/                 # Yüklenen dosyalar
```

## Teknolojiler

- Python
- TensorFlow/Keras
- Flask
- pretty_midi
- music21
- matplotlib
- numpy
- pandas

## Analiz Süreci

1. **Nota Analizi**
   - MIDI dosyasından notaların çıkarılması
   - Nota kullanım oranlarının hesaplanması

2. **Tonalite Analizi**
   - Major/Minor tespiti
   - Tonal merkezin belirlenmesi

3. **Duygu Analizi**
   - Duygu tahminleri
   - Benzerlik oranlarının hesaplanması

## Görselleştirme

- Duygu Modeli Sonuçları
- Tonalite Modeli Sonuçları
- Tahmin Edilen Duygular
- Tonalite Dağılımı

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

- Proje Sahibi: [İsim Soyisim]
- E-posta: [E-posta Adresi]
- GitHub: [GitHub Profili]

## Teşekkürler

- [Katkıda Bulunanlar]
- [Kullanılan Kütüphaneler]
- [Referanslar] 