# CRM Optimization

Bu proje, müşteri temsilcilerine en uygun müşteri atamalarını yapmak ve belirlenen bütçeye göre en iyi pazarlama kampanyalarını seçmek için Dinamik Programlama (DP) ve Kombinasyon yöntemlerini kullanır.

## Özellikler

- **Müşteri Temsilcisi Atama**:
  - Temsilcilerin her müşteriyle çalışma maliyetine göre en düşük toplam maliyetle atama yapar.
  - Dinamik Programlama kullanarak optimal çözümü belirler.

- **Pazarlama Kampanyası Seçimi**:
  - Bütçe dahilinde en yüksek Getiri (ROI) sağlayan kampanyaları seçer.
  - Tüm kombinasyonları değerlendirerek en iyi seçeneği belirler.

## Kullanılan Teknolojiler
- Python
- NumPy
- itertools

## Kurulum ve Kullanım

1. **Projeyi klonlayın**:
   ```sh
   git clone https://github.com/KULLANICI_ADIN/CRM_Optimization.git
   cd CRM_Optimization
   ```

2. **Gerekli bağımlılıkları yükleyin**:
   ```sh
   pip install numpy
   ```

3. **Python scriptini çalıştırın**:
   ```sh
   python main.py
   ```

## Örnek Girdi & Çıktı

### **Girdi:**
- **Müşteri temsilcisi atama matrisi:**
  ```python
  cost_matrix = [
      [9, 2, 7, 8],
      [6, 4, 3, 7],
      [5, 8, 1, 8],
      [7, 6, 9, 4]
  ]
  representatives = ["Ahmet", "Mehmet", "Ayşe", "Fatma"]
  ```
- **Pazarlama kampanyaları:**
  ```python
  campaigns = [
      {"id": 1, "cost": 50, "roi": 60},
      {"id": 2, "cost": 30, "roi": 40},
      {"id": 3, "cost": 20, "roi": 50},
      {"id": 4, "cost": 40, "roi": 80},
      {"id": 5, "cost": 10, "roi": 30}
  ]
  budget = 70
  ```

### **Çıktı:**
```sh
Toplam Kazanç: 120
Yönlendirme:
Müşteri 1 -> Temsilci 3 (Ayşe)
Müşteri 2 -> Temsilci 2 (Mehmet)
Müşteri 3 -> Temsilci 1 (Ahmet)
Müşteri 4 -> Temsilci 4 (Fatma)

Pazarlama Kampanyası Seçimi:
Maksimum ROI: 120
Seçilen Kampanyalar: [3, 4]
```


