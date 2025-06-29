import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import time

# GPU'nun kullanılabilir olduğunu kontrol et
print("\nGPU Durumu:")
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPU KULLANILIYOR!")
    print("Kullanılan GPU:", gpus[0])
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("GPU bellek büyümesi etkinleştirildi")
    except RuntimeError as e:
        print(e)
else:
    print("GPU KULLANILAMIYOR! CPU kullanılıyor.")

# Örnek veri oluştur
print("\nVeri Hazırlanıyor...")
x = np.linspace(-10, 10, 1000)
y = np.sin(x) + np.random.normal(0, 0.1, 1000)

# Veriyi eğitim ve test setlerine ayır
train_size = int(0.8 * len(x))
x_train, x_test = x[:train_size], x[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Model oluştur
print("\nModel Oluşturuluyor...")
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Modeli derle
model.compile(optimizer='adam', loss='mse')

# Eğitim süresini ölç
print("\nEğitim Başlıyor...")
start_time = time.time()

# Modeli eğit
history = model.fit(x_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Eğitim süresini hesapla
end_time = time.time()
training_time = end_time - start_time
print(f"\nEğitim Süresi: {training_time:.2f} saniye")

# Modeli değerlendir
test_loss = model.evaluate(x_test, y_test)
print(f"Test Loss: {test_loss}")

# Tahminleri yap
print("\nTahminler Yapılıyor...")
y_pred = model.predict(x_test)

# Sonuçları görselleştir
print("\nGrafikler Oluşturuluyor...")
plt.figure(figsize=(10, 6))
plt.scatter(x_test, y_test, label='Gerçek Veri', alpha=0.5)
plt.plot(x_test, y_pred, 'r-', label='Tahmin', linewidth=2)
plt.title('Sinüs Fonksiyonu Tahmini')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('gpu_example_result.png')
plt.close()

# Eğitim geçmişini görselleştir
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Eğitim Kaybı')
plt.plot(history.history['val_loss'], label='Doğrulama Kaybı')
plt.title('Model Kaybı')
plt.xlabel('Epoch')
plt.ylabel('Kayıp')
plt.legend()
plt.savefig('gpu_example_history.png')
plt.close()

print("\nEğitim tamamlandı ve sonuçlar kaydedildi.")
print("Sonuçlar 'gpu_example_result.png' ve 'gpu_example_history.png' dosyalarında kaydedildi.") 