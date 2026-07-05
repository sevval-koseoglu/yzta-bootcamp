# YZTA Bootcamp 2026

## Takım İsmi

Grup 18

---

## Team Members

| Name            | Title         |
| --------------- | ------------- |
| Şevval Köseoğlu | Scrum Master  |
| Merve Altınsoy  | Product Owner |
| Beyza Hız       | Developer     |

---

## Ürün İsmi

**Scam Message Detector**

---

## Ürün Fikri

Scam Message Detector, Türkçe SMS, e-posta ve mesaj içeriklerini analiz ederek dolandırıcılık riskini puanlayan, şüpheli öğeleri açıklayan ve kullanıcıya güvenli aksiyon önerileri sunan yapay zekâ destekli bir güvenlik farkındalık asistanıdır.

---

## Ürün Açıklaması

Scam Message Detector, kullanıcıların şüpheli gördüğü mesajları analiz ederek dolandırıcılık riski hakkında anlaşılır bir değerlendirme sunmayı amaçlar.

Kullanıcı sisteme SMS, e-posta veya mesaj uygulamalarından aldığı şüpheli bir metni girer. Sistem mesaj içerisindeki link, telefon numarası, IBAN, ödeme talebi, aciliyet ifadesi, kurum taklidi ve benzeri risk sinyallerini analiz eder. Analiz sonucunda kullanıcıya bir risk skoru, şüpheli bulunan noktalar ve güvenli aksiyon önerileri sunulur.

Bu ürünün amacı kesin hukuki, finansal veya teknik güvenlik kararı vermek değildir. Amaç, kullanıcıların dijital dolandırıcılık girişimlerine karşı daha bilinçli hareket etmesine yardımcı olmaktır.

---

## Problem

Günümüzde kullanıcılar; sahte kargo mesajları, banka taklidi yapan SMS’ler, sahte çekiliş duyuruları, burs dolandırıcılıkları ve kimlik avı bağlantılarıyla sıkça karşılaşmaktadır. Bu mesajlar çoğu zaman kullanıcıyı acele karar vermeye zorlar ve linke tıklama, ödeme yapma veya kişisel bilgi paylaşma gibi riskli davranışlara yönlendirir.

Özellikle dijital güvenlik farkındalığı düşük kullanıcılar için bu mesajların güvenilir olup olmadığını anlamak zor olabilir. Scam Message Detector, bu problemi Türkçe mesajlar özelinde analiz ederek kullanıcıya anlaşılır bir risk değerlendirmesi sunmayı hedefler.

---

## Hedef Kitle

* SMS, e-posta ve mesaj uygulamalarını aktif kullanan bireyler
* Dolandırıcılık mesajlarını ayırt etmekte zorlanan kullanıcılar
* Yaşlı bireyler ve dijital güvenlik farkındalığı düşük kullanıcılar
* Banka, kargo, e-devlet, burs veya çekiliş temalı sahte mesajlara karşı korunmak isteyen kişiler
* Temel düzeyde siber güvenlik farkındalığı kazanmak isteyen kullanıcılar

---

## Ürün Özellikleri

Sprint 1 kapsamında hedeflenen temel özellikler:

* Kullanıcıdan mesaj metni alma
* Mesaj içerisindeki şüpheli linkleri tespit etme
* Telefon numarası ve IBAN formatlarını tespit etme
* Aciliyet, ödeme talebi ve kurum taklidi gibi risk sinyallerini analiz etme
* Mesaja göre temel dolandırıcılık risk skoru üretme
* Şüpheli noktaları kullanıcıya madde madde açıklama
* Kullanıcıya güvenli aksiyon önerileri sunma
* Örnek mesajlar üzerinden test edilebilir analiz sistemi oluşturma

---

## Kullanılacak Teknolojiler

| Teknoloji                | Kullanım Amacı                                |
| ------------------------ | --------------------------------------------- |
| Python                   | Ana geliştirme dili                           |
| Streamlit                | Web arayüzü                                   |
| Regex                    | Link, telefon, IBAN ve anahtar kelime tespiti |
| JSON                     | Örnek mesajların saklanması                   |
| GitHub                   | Versiyon kontrolü ve proje dokümantasyonu     |
| GitHub Projects / Issues | Sprint ve backlog takibi                      |

---

## Product Backlog

| No | User Story                                                                                                                        | Öncelik | Durum |
| -- | --------------------------------------------------------------------------------------------------------------------------------- | ------- | ----- |
| 1  | Kullanıcı olarak mesaj metni girmek istiyorum, böylece mesajın riskli olup olmadığını analiz edebilirim.                          | High    | To Do |
| 2  | Kullanıcı olarak mesajdaki şüpheli linkleri görmek istiyorum, böylece linke tıklamadan önce riskleri anlayabilirim.               | High    | To Do |
| 3  | Kullanıcı olarak mesaj için bir risk skoru görmek istiyorum, böylece mesajın ne kadar tehlikeli olabileceğini anlayabilirim.      | High    | To Do |
| 4  | Kullanıcı olarak mesajın neden riskli olduğunu madde madde görmek istiyorum, böylece sonucu daha kolay anlayabilirim.             | High    | To Do |
| 5  | Kullanıcı olarak güvenli aksiyon önerileri almak istiyorum, böylece şüpheli mesaj karşısında ne yapmam gerektiğini öğrenebilirim. | Medium  | To Do |
| 6  | Takım olarak sprint sürecini GitHub üzerinde belgelemek istiyoruz, böylece proje gelişimi düzenli şekilde takip edilebilir.       | High    | To Do |

---

## Sprint 1

### Sprint Hedefi

Sprint 1’in hedefi, Scam Message Detector projesinin temel repository yapısını kurmak, ürün fikrini belgelemek ve kullanıcıdan alınan mesaj metni üzerinden basit risk analizi yapabilen ilk prototipi geliştirmektir.

---

### Sprint 1 Kapsamı

Bu sprintte ürünün temel altyapısı ve ilk çalışan prototipi hedeflenmiştir.

Planlanan işler:

* GitHub repository kurulumu
* README dosyasının hazırlanması
* Takım rollerinin belgelenmesi
* Ürün fikri, hedef kitle ve backlog bilgilerinin eklenmesi
* Streamlit arayüzünün oluşturulması
* Kullanıcıdan mesaj metni alma ekranının hazırlanması
* Link, telefon numarası, IBAN ve anahtar kelime tespiti için ilk analiz fonksiyonlarının yazılması
* Basit risk skoru hesaplama yapısının oluşturulması
* Örnek test mesajlarının hazırlanması

---

## Sprint 1 Backlog

| Görev                                                 | Sorumlu                      | Durum |
| ----------------------------------------------------- | ---------------------------- | ----- |
| Repository yapısını oluşturma                         | Developer Team               | To Do |
| README.md dosyasının ilk sürümünü hazırlama           | Developer Team               | To Do |
| Takım üyeleri ve rollerini belgeleme                  | Scrum Master                 | To Do |
| Ürün fikri ve hedef kitleyi belgeleme                 | Product Owner                | To Do |
| Product backlog hazırlama                             | Product Owner / Scrum Master | To Do |
| Streamlit arayüzünü oluşturma                         | Developer Team               | To Do |
| Mesaj giriş alanını geliştirme                        | Developer Team               | To Do |
| Link, telefon ve IBAN tespiti için regex yapısı kurma | Developer Team               | To Do |
| Risk skoru hesaplama fonksiyonunu geliştirme          | Developer Team               | To Do |
| Örnek test mesajları hazırlama                        | Developer Team               | To Do |

---

## Risk Analizinde Kullanılacak İlk Sinyaller

| Risk Sinyali     | Açıklama                                                               |
| ---------------- | ---------------------------------------------------------------------- |
| Link bulunması   | Mesaj içerisinde URL olup olmadığı kontrol edilir.                     |
| Aciliyet ifadesi | "Hemen", "24 saat içinde", "son gün", "acil" gibi ifadeler aranır.     |
| Ödeme talebi     | Para, ödeme, kart bilgisi veya IBAN isteyen ifadeler analiz edilir.    |
| Kurum taklidi    | Banka, kargo, e-devlet, burs veya çekiliş gibi temalar kontrol edilir. |
| Telefon numarası | Mesaj içerisinde telefon numarası bulunup bulunmadığı tespit edilir.   |
| IBAN             | Mesaj içerisinde IBAN formatına benzeyen ifadeler aranır.              |

---

## Proje Dosya Yapısı

```text
scam-message-detector/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── app/
│   ├── main.py
│   ├── analyzer.py
│   └── scoring.py
│
├── data/
│   └── sample_messages.json
│
└── docs/
    └── sprint_1.md
```

---

## Kurulum

Projeyi klonlayın:

```bash
git clone <repository-url>
cd scam-message-detector
```

Sanal ortam oluşturun:

```bash
python -m venv venv
```

Sanal ortamı aktif edin:

```bash
# macOS / Linux
source venv/bin/activate
```

```bash
# Windows
venv\Scripts\activate
```

Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

Uygulamayı çalıştırın:

```bash
streamlit run app/main.py
```

---

## Örnek Kullanım Senaryosu

Kullanıcı aşağıdaki gibi bir mesaj girer:

```text
Sayın müşterimiz, kargonuz teslimat merkezinde beklemektedir. Teslimatın iptal olmaması için 24 saat içinde ödeme yapınız: http://example-link.com
```

Sistem aşağıdaki bilgileri üretir:

```text
Risk Skoru: 85/100

Şüpheli Noktalar:
- Mesajda ödeme talebi bulunuyor.
- Mesajda kullanıcıyı hızlı hareket etmeye zorlayan aciliyet ifadesi var.
- Mesajda dış bağlantı bulunuyor.
- Mesaj kargo firması taklidi yapıyor olabilir.

Öneri:
Linke tıklamayın. Kargo durumunu yalnızca ilgili firmanın resmi web sitesi veya mobil uygulaması üzerinden kontrol edin.
```

---

## Sprint 1 Definition of Done

Sprint 1’in tamamlanmış sayılması için:

* Repository oluşturulmuş olmalı
* README dosyası hazırlanmış olmalı
* Takım üyeleri ve rolleri belgelenmiş olmalı
* Ürün fikri, hedef kitle ve product backlog eklenmiş olmalı
* Kullanıcıdan mesaj alabilen basit arayüz çalışmalı
* Temel risk sinyallerini kontrol eden analiz fonksiyonu yazılmış olmalı
* Risk skoru üreten ilk yapı çalışmalı
* En az 5 örnek mesaj ile test yapılmalı
* Yapılan işler GitHub commit geçmişiyle belgelenmiş olmalı

---

## Not

Scam Message Detector, kullanıcıları şüpheli mesajlara karşı bilinçlendirmeyi amaçlayan bir yardımcı araçtır. Sistem tarafından verilen sonuçlar kesin güvenlik, hukuk veya finans tavsiyesi olarak değerlendirilmemelidir. Şüpheli durumlarda kullanıcıların ilgili kurumun resmi kanallarını kullanarak doğrulama yapması önerilir.
