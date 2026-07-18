# YZTA Bootcamp 2026

## Takım İsmi

Grup 18

---

## Team Members

| Name            | Title         |
| --------------- | ------------- |
| Şevval Köseoğlu | Scrum Master  |
| Merve Altınsoy  | Product Owner |

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

# Sprint 1

## Backlog düzeni ve Story seçimleri

Backlog'umuz Sprint 1 kapsamında öncelikli olarak yapılması gereken story'lere göre düzenlenmiştir. İlk sprintte amaç, ürünün temel yapısını kurmak ve kullanıcıdan alınan mesaj metni üzerinden basit bir risk analizi yapabilen ilk prototipi geliştirmektir.

Sprint başına tahmin edilen puan sayısını geçmeyecek şekilde story seçimleri yapılmıştır. Story başına çıkan tahmin puanı, toplam sprint puanının yarısından az tutulmuştur.

Sprint 1 için seçilen story'ler aşağıdaki gibidir:

| No | Story                                                                                                                             | Tahmin Puanı | Öncelik |
| -- | --------------------------------------------------------------------------------------------------------------------------------- | -----------: | ------- |
| 1  | Kullanıcı olarak mesaj metni girmek istiyorum, böylece mesajın riskli olup olmadığını analiz edebilirim.                          |            3 | High    |
| 2  | Kullanıcı olarak mesajdaki şüpheli linkleri görmek istiyorum, böylece linke tıklamadan önce riskleri anlayabilirim.               |            5 | High    |
| 3  | Kullanıcı olarak mesaj için bir risk skoru görmek istiyorum, böylece mesajın ne kadar tehlikeli olabileceğini anlayabilirim.      |            5 | High    |
| 4  | Kullanıcı olarak mesajın neden riskli olduğunu madde madde görmek istiyorum, böylece sonucu daha kolay anlayabilirim.             |            5 | High    |
| 5  | Kullanıcı olarak güvenli aksiyon önerileri almak istiyorum, böylece şüpheli mesaj karşısında ne yapmam gerektiğini öğrenebilirim. |            2 | Medium  |

Story'ler yapılacak işlere, yani task'lere bölünmüştür. Sprint 1 kapsamında belirlenen temel task'ler; repository yapısının oluşturulması, README dosyasının hazırlanması, Streamlit arayüzünün kurulması, mesaj giriş alanının oluşturulması, link/telefon/IBAN tespiti için regex yapısının hazırlanması ve temel risk skoru hesaplama fonksiyonunun geliştirilmesidir.

---

## Daily Scrum

Sprint 1 sürecinde ekip içi iletişim ağırlıklı olarak mesajlaşma kanalı üzerinden yürütülmüştür.

Bu süreçte repository paylaşımı, Scrum Master ve Product Owner rollerinin belirlenmesi, ürün fikrinin netleştirilmesi, toplantı planlaması ve ekip bilgileri formu için gerekli bilgilerin toplanması gibi konular konuşulmuştur.

Daily Scrum / ekip iletişimi ekran görüntüleri aşağıda paylaşılmıştır:

![Daily Scrum 1](ProjectManagement/Sprint1Documents/scrum_1.png)

---

## Sprint board update

Sprint board üzerinde Sprint 1 için seçilen story'ler ve task'ler takip edilmiştir. Görevler To Do, In Progress ve Done durumlarına göre düzenlenmiştir.

Sprint board screenshotları:

![Backlog 1](ProjectManagement/Sprint1Documents/backlog_1.png)

---

## Ürün Durumu

Sprint 1 kapsamında ürünün tamamlanmış sürümü değil, ilk ürün prototipi ve arayüz taslağı hedeflenmiştir. Bu nedenle kullanıcıdan mesaj metni alan, temel risk sinyallerini kontrol etmeyi amaçlayan ve risk skorunu kullanıcıya gösterecek başlangıç ekranı hazırlanmıştır.

Sprint 1 ürün çıktısı kapsamında hedeflenen özellikler:

* Kullanıcıdan mesaj metni alma
* Link, telefon numarası ve IBAN formatı kontrolü
* Aciliyet ve ödeme talebi içeren ifadeleri analiz etme
* Temel risk skoru üretme
* Kullanıcıya şüpheli noktaları listeleme
* Güvenli aksiyon önerisi sunma

Ürün durumu ekran görüntüsü:

![Screenshot 1](ProjectManagement/Sprint1Documents/screenshot_1.png)

---

## Sprint Review

Sprint Review sırasında Sprint 1 kapsamında yapılan çalışmalar değerlendirilmiştir. Takım, ürün fikrini netleştirmiş ve ilk sprint için kapsamın temel risk analizi ile sınırlı tutulmasına karar vermiştir.

Alınan kararlar:

* Ürünün isminin Scam Message Detector olmasına karar verilmiştir.
* İlk sprintte kapsamın temel prototip ve risk analizi akışıyla sınırlı tutulmasına karar verilmiştir.
* Kullanıcıdan mesaj metni alınması, risk sinyallerinin tespit edilmesi ve risk skoru üretilmesi Sprint 1’in ana hedefi olarak belirlenmiştir.
* Gelişmiş yapay zekâ açıklamaları, analiz geçmişi ve dashboard özelliklerinin sonraki sprintlerde ele alınmasına karar verilmiştir.
* Verilerin kalıcı olarak saklanması için JSON veya SQLite kullanımının sonraki sprintte değerlendirilmesine karar verilmiştir.
* Çıkan ürünün ilk prototip akışında temel analiz mantığı için bir problem görülmemiştir.
* Ekstra eklenmesi gereken özellikler sonraki sprint için backlog'a aktarılmıştır.

Sprint Review katılımcıları:

* Şevval Köseoğlu
* Merve Altınsoy
* Beyza Hız

---

## Sprint Retrospective

Sprint Retrospective sırasında takımın Sprint 1 sürecindeki çalışma düzeni değerlendirilmiş ve sonraki sprint için iyileştirme alanları belirlenmiştir.

Alınan kararlar:

* Takım içindeki görev dağılımıyla ilgili düzenleme yapılması kararı alınmıştır.
* Tahmin puanları gözden geçirilmeli ve sprint planlama toplantılarında gerekli geri bildirimlerin developer tarafından verildiğine emin olunmalıdır.
* Daily Scrum ekran görüntülerinin daha düzenli şekilde saklanmasına karar verilmiştir.
* Sprint board güncellemelerinin daha sık yapılması gerektiği belirlenmiştir.
* Test mesajları için ayrılan eforun artırılmasına karar verilmiştir.
* Risk skoru hesaplama sisteminin sonraki sprintte daha detaylı hale getirilmesi planlanmıştır.

---

# Sprint 2

## Backlog düzeni ve Story seçimleri

Backlog'umuz Sprint 2 kapsamında, Sprint 1 sonunda elde edilen çalışan prototipin geliştirilmesine yönelik öncelikli story'lere göre düzenlenmiştir. İkinci sprintte amaç; mevcut risk analizi sistemini daha detaylı hale getirmek, farklı mesaj örnekleriyle test etmek ve mesajın bağlamını değerlendirebilen yapay zekâ destekli analiz özelliğini ürüne eklemektir.

Ekip üyelerinin Sprint 2 sürecinde yeterli katılım sağlayamaması üzerine durum bootcamp yetkilisine bildirilmiştir. Alınan yönlendirme doğrultusunda sprint kapsamı bireysel olarak tamamlanabilecek şekilde düzenlenmiş ve proje Şevval Köseoğlu tarafından sürdürülmüştür.

Sprint başına tahmin edilen puan sayısını geçmeyecek şekilde story seçimleri yapılmıştır. Story başına çıkan tahmin puanı, toplam sprint puanının yarısından az tutulmuştur. Sprint 2 kapsamında toplam 18 puanlık iş tamamlanması hedeflenmiştir.

Sprint 2 için seçilen story'ler aşağıdaki gibidir:

| No | Story | Tahmin Puanı | Öncelik |
| -- | ----- | -----------: | ------- |
| 6 | Kullanıcı olarak daha detaylı bir risk analizi görmek istiyorum, böylece mesajdaki farklı dolandırıcılık sinyallerini anlayabilirim. | 5 | High |
| 7 | Kullanıcı olarak mesajın bağlamını değerlendiren yapay zekâ destekli bir yorum görmek istiyorum, böylece yalnızca anahtar kelimelere dayanmayan bir sonuç alabilirim. | 8 | High |
| 8 | Kullanıcı olarak sistemin farklı güvenli ve şüpheli mesajlarla test edilmesini istiyorum, böylece analiz sonuçlarının güvenilirliğini değerlendirebilirim. | 3 | High |
| 9 | Kullanıcı olarak analiz sonucunu daha anlaşılır bir arayüzde görmek istiyorum, böylece risk seviyesini ve şüpheli noktaları kolayca inceleyebilirim. | 2 | Medium |

Story'ler yapılacak işlere, yani task'lere bölünmüştür. Sprint 2 kapsamında belirlenen temel task'ler; yeni dolandırıcılık sinyallerinin eklenmesi, risk skoru ağırlıklarının yeniden düzenlenmesi, kişisel bilgi talebi ile ödül ve hesap kapatma tehdidi içeren ifadelerin tespit edilmesi, yapay zekâ destekli bağlamsal mesaj analizinin eklenmesi, yapay zekâ servisine erişilemediğinde kural tabanlı sistemin çalışmaya devam etmesinin sağlanması, güvenli ve şüpheli test mesajlarının hazırlanması ve Streamlit sonuç ekranının geliştirilmesidir.

---

## Daily Scrum

Sprint 2 başlangıcında backlog'un değerlendirilmesi, görev dağılımının yapılması ve geliştirme sürecinin planlanması amacıyla ekip üyeleriyle iletişim kurulmaya çalışılmıştır.

Daily Scrum / ekip iletişimi ekran görüntüleri aşağıda paylaşılmıştır:

![Daily Scrum 2](ProjectManagement/Sprint1Documents/scrum_2.png)

---

## Sprint board update

Sprint board üzerinde Sprint 2 için seçilen story'ler ve bu story'lere bağlı task'ler takip edilmektedir. Görevler To Do, In Progress ve Done durumlarına göre düzenlenmiştir.

Sprint board screenshotları:

![Backlog 2](ProjectManagement/Sprint2Documents/backlog_2.png)
