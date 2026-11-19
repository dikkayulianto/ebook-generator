import os
import json

GRADES_DATA = {
    1: {
        "fase": "Fase A",
        "title_soal": "Soal SAS PAI Kelas 1 SD Kurikulum Merdeka + Kunci Jawaban",
        "title_modul": "Modul Ajar PAI Kelas 1 SD Deep Learning (8 Halaman)",
        "title_buku": "Buku Siswa PAI Kelas 1 SD Kurikulum Merdeka Semester 1",
        "cover_soal": "/assets/soal_sas_cover_kelas1.jpg",
        "cover_modul": "/assets/cover_illustration.jpg",
        "cover_buku": "/assets/cover_penjualan_buku_kelas1.jpg",
        "bab_list": [
            ("Bab 1: Aku Cinta Al-Qur'an", "Hafalan Surah Al-Fatihah, pesan kasih sayang Allah Swt., dan pengenalan bentuk huruf hijaiah berharakat fathah, kasrah, dammah."),
            ("Bab 2: Mengenal Rukun Iman", "Memahami 6 Rukun Iman, meyakini Allah Swt. Maha Pencipta (al-Khaliq), dan bukti ciptaan-Nya di sekitar kita."),
            ("Bab 3: Membaca Basmalah dan Hamdalah", "Pembiasaan melafalkan kalimat thayyibah basmalah sebelum beraktivitas dan hamdalah setelah selesai."),
            ("Bab 4: Mengenal Rukun Islam", "Mengenal 5 Rukun Islam, makna syahadatain (syahadat tauhid & rasul), serta pentingnya shalat lima waktu."),
            ("Bab 5: Nabi dan Rasul Panutanku", "Mengenal keteladanan Nabi Adam a.s. sebagai manusia pertama dan Nabi Muhammad saw. sebagai penutup para nabi.")
        ],
        "sample_questions": [
            ("1. Surah pertama dalam kitab suci Al-Qur'an adalah surah ....", ["a. Al-Ikhlas", "b. Al-Fatihah", "c. An-Nas"], "b. Al-Fatihah (Ummul Qur'an)"),
            ("2. Sebelum makan atau mulai belajar, kita dianjurkan membaca ....", ["a. Basmalah", "b. Hamdalah", "c. Takbir"], "a. Basmalah (Bismillāhir-raḥmānir-raḥīm)"),
            ("3. Rukun Iman yang pertama adalah beriman kepada ....", ["a. Malaikat Allah", "b. Kitab Allah", "c. Allah Swt."], "c. Allah Swt. (Pondasi tauhid)"),
            ("4. Shalat wajib yang dikerjakan umat Islam dalam sehari semalam berjumlah .... waktu.", ["a. 3", "b. 5", "c. 7"], "b. 5 waktu (Subuh, Zuhur, Asar, Maghrib, Isya)"),
            ("5. (Uraian) Sebutkan 2 contoh ciptaan Allah Swt. yang ada di langit!", [], "Matahari, bulan, bintang, awan.")
        ],
        "modul_highlights": "Skenario 3 fase pembelajaran (Mindful, Meaningful, Joyful), LKPD mewarnai huruf hijaiah dan menjodohkan rukun iman, rubrik KKTP pengamatan adab.",
        "buku_highlights": "Ilustrasi kartun full-color ramah anak, teks huruf besar mudah dibaca siswa kelas 1, lembar aktivitas interaktif."
    },
    2: {
        "fase": "Fase A",
        "title_soal": "Soal SAS PAI Kelas 2 SD Kurikulum Merdeka + Kunci Jawaban",
        "title_modul": "Modul Ajar PAI Kelas 2 SD Deep Learning (8 Halaman)",
        "title_buku": "Buku Siswa PAI Kelas 2 SD Kurikulum Merdeka Semester 1",
        "cover_soal": "/assets/soal_sas_cover_kelas2.jpg",
        "cover_modul": "/assets/cover_illustration.jpg",
        "cover_buku": "/assets/cover_penjualan_buku_kelas2.jpg",
        "bab_list": [
            ("Bab 1: Huruf Hijaiyah Bersambung", "Membaca dan menuliskan huruf hijaiyah bersambung di awal, tengah, dan akhir kata dengan tanda baca sukun dan tasydid."),
            ("Bab 2: Mengenal Asmaul Husna", "Meneladani sifat Allah Swt.: Al-Hafiz (Maha Memelihara), Al-Wali (Maha Melindungi), Al-Alim (Maha Mengetahui), dan Al-Khabir (Maha Teliti)."),
            ("Bab 3: Senangnya Mengumandangkan Azan & Ikamah", "Memahami lafal azan, doa setelah azan, syarat muazin, dan perbedaan azan dengan ikamah."),
            ("Bab 4: Membiasakan Perilaku Terpuji", "Menumbuhkan sikap saling menyayangi, gemar menolong teman, berkata santun, dan menjaga kebersihan."),
            ("Bab 5: Kisah Keteladanan Nabi Nuh a.s.", "Ketabahan Nabi Nuh a.s. dalam berdakwah serta peristiwa pembuatan bahtera penyelamat kaum beriman.")
        ],
        "sample_questions": [
            ("1. Huruf hijaiyah yang tidak dapat disambung dengan huruf setelahnya adalah ....", ["a. Ba (ب)", "b. Alif (ا)", "c. Jim (ج)"], "b. Alif (ا)"),
            ("2. Asmaul Husna Al-Alim memiliki arti bahwa Allah Swt. Maha ....", ["a. Melihat", "b. Mengetahui", "c. Mendengar"], "b. Mengetahui segala sesuatu"),
            ("3. Panggilan yang dikumandangkan sebagai tanda bahwa waktu shalat wajib telah tiba adalah ....", ["a. Azan", "b. Ikamah", "c. Takbir"], "a. Azan"),
            ("4. Nabi Nuh a.s. diperintahkan oleh Allah Swt. untuk membuat .... besar sebelum banjir datang.", ["a. Rumah", "b. Bahtera/Kapal", "c. Tenda"], "b. Bahtera / Kapal besar"),
            ("5. (Uraian) Sebutkan 2 perilaku terpuji kepada teman di sekolah!", [], "Menolong teman yang terjatuh dan meminjamkan alat tulis.")
        ],
        "modul_highlights": "Pembelajaran bermakna Asmaul Husna, praktik lafal azan terpandu, LKPD menyambung huruf hijaiyah, asesmen rubrik unjuk kerja.",
        "buku_highlights": "Pedoman tajwid dasar bergambar, panduan praktik azan & ikamah bertahap, kisah bergambar Nabi Nuh a.s."
    },
    3: {
        "fase": "Fase B",
        "title_soal": "Soal SAS PAI Kelas 3 SD Kurikulum Merdeka + Kunci Jawaban",
        "title_modul": "Modul Ajar PAI Kelas 3 SD Deep Learning (8 Halaman)",
        "title_buku": "Buku Siswa PAI Kelas 3 SD Kurikulum Merdeka Semester 1",
        "cover_soal": "/assets/soal_sas_cover_kelas3.jpg",
        "cover_modul": "/assets/cover_illustration.jpg",
        "cover_buku": "/assets/cover_penjualan_buku_kelas3.jpg",
        "bab_list": [
            ("Bab 1: Surah Al-Humazah dan Al-Kautsar", "Hafalan, terjemah perkata, dan hukum bacaan tajwid serta larangan mencela dan anjuran bersyukur."),
            ("Bab 2: Sifat-Sifat Wajib Allah Swt.", "Memahami 20 Sifat Wajib Allah (Wujud, Qidam, Baqa', dll) beserta dalil aqli dan naqli."),
            ("Bab 3: Perilaku Mandiri dan Percaya Diri", "Menerapkan kemandirian dalam merapikan perlengkapan sekolah dan percaya diri saat tampil di kelas."),
            ("Bab 4: Berbakti Kepada Orang Tua dan Guru", "Adab menghormati orang tua (birrul walidain) dan memuliakan guru di sekolah."),
            ("Bab 5: Kelahiran & Masa Kanak-Kanak Nabi Muhammad saw.", "Peristiwa Tahun Gajah, masa susuan di Bani Sa'ad, pengasuhan kakek & paman, serta gelar Al-Amin.")
        ],
        "sample_questions": [
            ("1. Surah Al-Kautsar mengajarkan kepada kita agar selalu ....", ["a. Bersyukur dan mendirikan shalat", "b. Mengumpulkan harta", "c. Mencela orang lain"], "a. Bersyukur dan mendirikan shalat"),
            ("2. Sifat wajib bagi Allah Swt. 'Wujud' memiliki arti bahwa Allah Swt. itu ....", ["a. Terdahulu", "b. Ada", "c. Kekal"], "b. Ada (Pasti adanya)"),
            ("3. Sikap mengerjakan tugas sekolah sendiri tanpa selalu bergantung pada orang tua menunjukkan sifat ....", ["a. Mandiri", "b. Malas", "c. Sombong"], "a. Mandiri"),
            ("4. Nabi Muhammad saw. lahir pada tanggal 12 Rabiul Awwal tahun ....", ["a. Unta", "b. Gajah", "c. Kuda"], "b. Gajah (Penyerangan tentara Abrahah)"),
            ("5. (Uraian) Jelaskan mengapa Nabi Muhammad saw. sejak kecil dijuluki Al-Amin!", [], "Karena sejak kanak-kanak beliau selalu jujur, amanah, dan tidak pernah berbohong.")
        ],
        "modul_highlights": "Deep learning telaah surah pendek, LKPD tabel sifat wajib Allah, refleksi adab anak sholeh, rubrik KKTP holistik.",
        "buku_highlights": "Teks Arab berharakat rapi dengan arti kata, komik teladan berbakti orang tua, peta perjalanan masa kecil Nabi."
    },
    4: {
        "fase": "Fase B",
        "title_soal": "Soal SAS PAI Kelas 4 SD Kurikulum Merdeka + Kunci Jawaban",
        "title_modul": "Modul Ajar PAI Kelas 4 SD Deep Learning (8 Halaman)",
        "title_buku": "Buku Siswa PAI Kelas 4 SD Kurikulum Merdeka Semester 1",
        "cover_soal": "/assets/soal_sas_cover_kelas4.jpg",
        "cover_modul": "/assets/cover_illustration.jpg",
        "cover_buku": "/assets/cover_penjualan_buku_kelas4.jpg",
        "bab_list": [
            ("Bab 1: Surah Al-Hujurat Ayat 13", "Mengkaji pesan Al-Qur'an tentang keberagaman manusia diciptakan bersuku-suku untuk saling mengenal (ta'aruf)."),
            ("Bab 2: Asmaul Husna (Al-Malik, Al-Aziz, Al-Quddus, As-Salam, Al-Mu'min)", "Makna lima nama agung Allah Swt. dan implementasi menjaga kedamaian di lingkungan."),
            ("Bab 3: Indahnya Saling Menghargai dalam Keragaman", "Sikap toleransi, menghargai perbedaan pendapat, dan kerukunan antarteman sebaya."),
            ("Bab 4: Menyambut Usia Baligh", "Tanda-tanda baligh menurut fikih (mimpi basah, haid) dan biologi, serta kewajiban mandi wajib."),
            ("Bab 5: Kisah Hijrah Nabi Muhammad saw. ke Madinah", "Sebab-sebab hijrah, peristiwa di Gua Tsur, penyambutan kaum Ansar, dan pembangunan Masjid Nabawi.")
        ],
        "sample_questions": [
            ("1. Berdasarkan Q.S. Al-Hujurat ayat 13, manusia diciptakan bersuku-suku agar ....", ["a. Saling bertengkar", "b. Saling mengenal (lita'arafu)", "c. Saling membanggakan diri"], "b. Saling mengenal (lita'arafu)"),
            ("2. Asmaul Husna As-Salam mengandung makna bahwa Allah Swt. Maha ....", ["a. Merajai", "b. Memberi Keselamatan/Kedamaian", "c. Memelihara"], "b. Memberi Keselamatan / Kedamaian"),
            ("3. Salah satu tanda baligh bagi anak laki-laki menurut pandangan fikih adalah mengalami ....", ["a. Mimpi basah (ihtilam)", "b. Haid", "c. Suara serak"], "a. Mimpi basah (ihtilam)"),
            ("4. Sahabat mulia yang menemani Nabi Muhammad saw. bersembunyi di Gua Tsur saat hijrah adalah ....", ["a. Umar bin Khattab", "b. Abu Bakar As-Siddiq", "c. Ali bin Abi Thalib"], "b. Abu Bakar As-Siddiq r.a."),
            ("5. (Uraian) Sebutkan 2 tata cara bersuci (mandi wajib) setelah berhadas besar!", [], "Membaca niat dan meratakan air ke seluruh tubuh dari ujung rambut hingga ujung kaki.")
        ],
        "modul_highlights": "Pembelajaran kontekstual moderasi beragama, infografis tahapan baligh, analisis sebab hijrah Nabi, rubrik KKTP berbobot.",
        "buku_highlights": "Desain tata letak infografis modern, diagram perbedaan hadas kecil & besar, peta rute hijrah Makkah-Madinah."
    },
    5: {
        "fase": "Fase C",
        "title_soal": "Soal SAS PAI Kelas 5 SD Kurikulum Merdeka + Kunci Jawaban",
        "title_modul": "Modul Ajar PAI Kelas 5 SD Deep Learning (8 Halaman)",
        "title_buku": "Buku Siswa PAI Kelas 5 SD Kurikulum Merdeka Semester 1",
        "cover_soal": "/assets/soal_sas_cover_kelas5.jpg",
        "cover_modul": "/assets/cover_illustration.jpg",
        "cover_buku": "/assets/cover_penjualan_buku_kelas5.jpg",
        "bab_list": [
            ("Bab 1: Menyayangi Anak Yatim (Surah Al-Ma'un)", "Hukum bacaan mim sukun, kandungan surah Al-Ma'un, dan ancaman bagi orang yang mendustakan agama."),
            ("Bab 2: Asmaul Husna (Al-Qawiyyu, Al-Qayyum, Al-Muhyi, Al-Mumit, Al-Ba'is)", "Makna kekuatan, kemandirian Allah, serta keyakinan terhadap kehidupan setelah kematian."),
            ("Bab 3: Keragaman Sebagai Sunnatullah", "Menghormati perbedaan keyakinan dan suku bangsa sebagai wujud persaudaraan kemanusiaan (ukhuwwah insaniyyah)."),
            ("Bab 4: Zakat, Infak, Sedekah, dan Hadiah", "Perbedaan ketentuan zakat fitrah dan mal, mustahiq zakat (8 asnaf), serta keutamaan bersedekah."),
            ("Bab 5: Kisah Fathu Makkah dan Haji Wada'", "Pembebasan kota Makkah tanpa pertumpahan darah dan pesan toleransi pada khotbah terakhir Rasulullah saw.")
        ],
        "sample_questions": [
            ("1. Golongan pendusta agama menurut Q.S. Al-Ma'un adalah orang yang ....", ["a. Menghardik anak yatim dan enggan menolong", "b. Rajin membaca Al-Qur'an", "c. Gemar berpuasa"], "a. Menghardik anak yatim dan enggan menolong"),
            ("2. Allah Swt. Maha Mandiri dan tidak membutuhkan bantuan makhluk-Nya. Hal ini sesuai dengan Asmaul Husna ....", ["a. Al-Qawiyyu", "b. Al-Qayyum", "c. Al-Muhyi"], "b. Al-Qayyum (Maha Mandiri)"),
            ("3. Zakat yang wajib dikeluarkan oleh setiap jiwa muslim pada bulan Ramadhan disebut zakat ....", ["a. Mal", "b. Fitrah", "c. Tijarah"], "b. Fitrah (Membersihkan jiwa)"),
            ("4. Peristiwa Fathu Makkah terjadi pada tahun ke-.... Hijriyah.", ["a. 6 H", "b. 8 H", "c. 10 H"], "b. 8 Hijriyah"),
            ("5. (Uraian) Sebutkan 3 golongan yang berhak menerima zakat (mustahiq) menurut Al-Qur'an!", [], "Fakir, miskin, amil (atau mualaf, gharim, fisabilillah, ibnu sabil).")
        ],
        "modul_highlights": "Kajian kritis HOTS Surah Al-Ma'un, simulasi hitung zakat fitrah, studi kasus Fathu Makkah, rubrik KKTP analitis.",
        "buku_highlights": "Infografis 8 golongan mustahiq zakat, panduan tajwid hukum mim sukun, komik kepedulian sosial."
    },
    6: {
        "fase": "Fase C",
        "title_soal": "Soal SAS PAI Kelas 6 SD Kurikulum Merdeka + Kunci Jawaban",
        "title_modul": "Modul Ajar PAI Kelas 6 SD Deep Learning (8 Halaman)",
        "title_buku": "Buku Siswa PAI Kelas 6 SD Kurikulum Merdeka Semester 1",
        "cover_soal": "/assets/soal_sas_cover_kelas6.jpg",
        "cover_modul": "/assets/cover_illustration.jpg",
        "cover_buku": "/assets/cover_penjualan_buku_kelas6.jpg",
        "bab_list": [
            ("Bab 1: Mengkaji Surah Ad-Duha", "Hukum bacaan mad, asbabun nuzul surah Ad-Duha, optimisme hidup, dan larangan bersikap sewenang-wenang."),
            ("Bab 2: Asmaul Husna (Al-Ghaffar, Al-Afuw, Al-Wahid, As-Samad)", "Meneladani sifat pemaaf Allah Swt. dan bergantung hanya kepada Allah Yang Maha Esa."),
            ("Bab 3: Toleransi Beragama (Surah Al-Kafirun)", "Batasan toleransi dalam Islam: 'Untukmu agamamu, dan untukku agamaku' (Lakum dinukum waliyadin)."),
            ("Bab 4: Adab Bergaul & Menjauhi Ghibah", "Menghindari perilaku menggunjing (ghibah), memfitnah, dan menjaga etika berkomunikasi di media sosial."),
            ("Bab 5: Keteladanan Khulafaur Rasyidin", "Kepemimpinan Abu Bakar As-Siddiq, Umar bin Khattab, Utsman bin Affan, dan Ali bin Abi Thalib r.a.")
        ],
        "sample_questions": [
            ("1. Pesan utama dari Q.S. Ad-Duha kepada umat manusia yang sedang merasa sedih atau cemas adalah ....", ["a. Berputus asa", "b. Tetap optimis dan mengingat nikmat Allah", "c. Menyendiri"], "b. Tetap optimis dan mengingat nikmat Allah Swt."),
            ("2. Prinsip toleransi umat beragama yang tegas ditegaskan dalam Q.S. Al-Kafirun ayat terakhir adalah ....", ["a. Mengikuti ibadah agama lain", "b. Lakum dīnukum wa liya dīn", "c. Memusuhi pemeluk agama lain"], "b. Lakum dīnukum wa liya dīn"),
            ("3. Sikap membicarakan keburukan orang lain tanpa sepengetahuannya dalam ajaran Islam disebut ....", ["a. Ghibah", "b. Namimah", "c. Hasad"], "a. Ghibah (Menggunjing)"),
            ("4. Sahabat yang berinisiatif mengumpulkan dan membukukan mushaf Al-Qur'an adalah ....", ["a. Abu Bakar & Utsman bin Affan", "b. Muawiyah", "c. Khalid bin Walid"], "a. Abu Bakar As-Siddiq & Utsman bin Affan r.a."),
            ("5. (Uraian) Jelaskan salah satu sifat kepemimpinan Umar bin Khattab r.a. yang patut diteladani!", [], "Tegas membela kebenaran, adil, sederhana, dan sangat peduli terhadap rakyat kecil.")
        ],
        "modul_highlights": "Deep learning adab digital & pencegahan perundungan (bullying), analisis gaya kepemimpinan Khulafaur Rasyidin, rubrik KKTP integratif.",
        "buku_highlights": "Kajian tajwid hukum mad & waqaf, panduan etika digital muslim, biografi kepemimpinan 4 sahabat agung."
    }
}

def generate_soal_page(grade):
    data = GRADES_DATA[grade]
    fase = data["fase"]
    title = f"Soal SAS PAI Kelas {grade} SD Kurikulum Merdeka + Kunci Jawaban"
    desc = f"Contoh soal SAS PAI Kelas {grade} SD Kurikulum Merdeka lengkap 25 butir soal, kunci jawaban, dan kisi-kisi CP 020. Unduh format Word dan PDF."
    canonical = f"https://bahanajarbuguru.my.id/soal-sas-pai-kelas-{grade}.html"
    
    bab_html = ""
    for title_b, desc_b in data["bab_list"]:
        bab_html += f"""
        <div class="p-3.5 rounded-xl bg-emerald-50/60 border border-emerald-100">
          <h3 class="font-bold text-emerald-950">{title_b}</h3>
          <p class="text-slate-600 mt-1">{desc_b}</p>
        </div>"""

    q_html = ""
    for i, (q_text, opts, ans) in enumerate(data["sample_questions"], 1):
        opts_html = "".join([f"<div>{opt}</div>" for opt in opts])
        q_html += f"""
        <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
          <p class="font-bold text-slate-900">{q_text}</p>
          {"<div class='pl-4 space-y-0.5 text-slate-700'>" + opts_html + "</div>" if opts else ""}
          <div class="pt-2 text-xs text-emerald-700 font-bold border-t border-slate-200/80">
            Kunci Jawaban: <strong>{ans}</strong>
          </div>
        </div>"""

    # Other grades links
    other_soal_links = "".join([
        f"""<a href="/soal-sas-pai-kelas-{g}.html" class="p-3 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 text-xs font-semibold flex items-center justify-between text-slate-800 hover:text-emerald-950">
          <span>Soal SAS PAI Kelas {g} SD</span> <span>&rarr;</span>
        </a>""" for g in range(1, 7) if g != grade
    ])

    html = f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  
  <link rel="canonical" href="{canonical}">
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{data['cover_soal']}">
  <meta property="og:url" content="{canonical}">

  <!-- Schema.org Product & FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Product",
        "name": "Naskah Soal SAS PAI Kelas {grade} SD Kurikulum Merdeka",
        "description": "Naskah soal SAS PAI Kelas {grade} SD 25 butir lengkap dengan kunci jawaban dan kisi-kisi penulisan soal CP No. 020. Format Word (.docx) dan PDF.",
        "image": "https://bahanajarbuguru.my.id{data['cover_soal']}",
        "brand": {{
          "@type": "Brand",
          "name": "Bahan Ajar Bu Guru"
        }},
        "offers": {{
          "@type": "Offer",
          "url": "https://lynk.id/bahanajarbuguru",
          "price": "15000",
          "priceCurrency": "IDR",
          "priceValidUntil": "2027-12-31",
          "availability": "https://schema.org/InStock"
        }}
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Apakah file soal SAS PAI Kelas {grade} bisa diedit?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Ya, 100% bisa diedit. File disediakan dalam format Microsoft Word (.docx) sehingga guru bebas mengganti KOP sekolah, nama guru, kelas, maupun butir soal."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Format file apa saja yang didapatkan?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Anda mendapatkan format Microsoft Word (.docx) siap sunting dan PDF siap cetak tanpa watermark."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Apakah instrumen soal sudah sesuai Kurikulum Merdeka?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Ya, seluruh butir soal dirumuskan berdasarkan Capaian Pembelajaran (CP) No. 020 Kemendikbudristek untuk jenjang SD {fase}."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Amiri:wght@400;700&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Outfit"', '"Plus Jakarta Sans"', 'sans-serif'],
            arabic: ['"Amiri"', 'serif'],
          }},
          colors: {{
            brand: {{
              50: '#f0fdf4',
              100: '#dcfce7',
              600: '#16a34a',
              700: '#15803d',
              900: '#14532d',
            }}
          }}
        }}
      }}
    }}
  </script>
</head>
<body class="bg-[#faf7f2] text-slate-800 antialiased font-sans">

  <!-- TOP HEADER -->
  <header class="bg-white border-b border-[#e5ded4] sticky top-0 z-40 shadow-xs">
    <div class="max-w-4xl mx-auto px-4 py-3 flex items-center justify-between">
      <a href="/" class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-full bg-emerald-600 text-white font-black text-sm flex items-center justify-center shadow-xs">BG</div>
        <div>
          <span class="font-black text-slate-900 text-sm tracking-tight block">Bahan Ajar Bu Guru</span>
          <span class="text-[10px] text-slate-500 block -mt-0.5">PAI SD Kurikulum Merdeka</span>
        </div>
      </a>
      <div class="flex items-center gap-2">
        <a href="/" class="text-xs font-bold text-slate-600 hover:text-slate-900 px-3 py-1.5 rounded-full hover:bg-slate-100 transition-colors">&larr; Beranda</a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold shadow-xs transition-all">Toko Lynk.id &rarr;</a>
      </div>
    </div>
  </header>

  <!-- MAIN ARTICLE -->
  <main class="max-w-4xl mx-auto px-4 py-6 sm:py-8 space-y-8">
    
    <!-- BREADCRUMB -->
    <nav aria-label="Breadcrumb" class="text-xs font-medium text-slate-500 flex items-center gap-1.5">
      <a href="/" class="hover:text-emerald-700">Beranda</a>
      <span>&rsaquo;</span>
      <a href="/bank-soal-sas-pai-sd.html" class="hover:text-emerald-700">Bank Soal SAS PAI SD</a>
      <span>&rsaquo;</span>
      <span class="text-slate-800 font-bold">Soal SAS PAI Kelas {grade}</span>
    </nav>

    <!-- ARTICLE HERO -->
    <header class="space-y-3">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-950 font-bold text-xs">
        <span>Kurikulum Merdeka • CP No. 020 • {fase} (Kelas {grade} SD)</span>
      </div>
      <h1 class="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight leading-snug">
        Soal SAS PAI Kelas {grade} SD Kurikulum Merdeka (Kunci Jawaban + Kisi-kisi)
      </h1>
      <p class="text-sm sm:text-base text-slate-600 leading-relaxed font-normal">
        Halaman resmi unduhan dan referensi naskah ujian Sumatif Akhir Semester (SAS) 1 Pendidikan Agama Islam dan Budi Pekerti (PAI &amp; BP) Kelas {grade} SD. Berkas disusun lengkap mencakup naskah soal 25 butir, kunci jawaban terperinci, pedoman penskoran skala 100 poin, dan matriks kisi-kisi penulisan soal dalam format Microsoft Word (.docx) yang bebas diedit.
      </p>
    </header>

    <!-- SECTION 1: ISI NASKAH -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">
        Isi Naskah Soal SAS PAI Kelas {grade} SD
      </h2>
      <ul class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-medium">
        <li class="flex items-start gap-2 p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-emerald-600 font-bold">✓</span>
          <span><strong>15 Soal Pilihan Ganda:</strong> Butir soal standar asesmen sumatif dengan opsi a, b, c (atau a, b, c, d).</span>
        </li>
        <li class="flex items-start gap-2 p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-emerald-600 font-bold">✓</span>
          <span><strong>5 Soal Isian Singkat:</strong> Menguji pemahaman konsep kunci dan hafalan lafal dalil.</span>
        </li>
        <li class="flex items-start gap-2 p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-emerald-600 font-bold">✓</span>
          <span><strong>5 Soal Uraian HOTS:</strong> Soal penalaran bermakna terkait perilaku terpuji sehari-hari.</span>
        </li>
        <li class="flex items-start gap-2 p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-emerald-600 font-bold">✓</span>
          <span><strong>Kunci Jawaban &amp; Rubrik Penskoran:</strong> Pedoman penilaian transparan 100 poin.</span>
        </li>
        <li class="flex items-start gap-2 p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-emerald-600 font-bold">✓</span>
          <span><strong>Matriks Kisi-Kisi Penulisan Soal:</strong> Berdasarkan CP No. 020 Kemendikbudristek.</span>
        </li>
        <li class="flex items-start gap-2 p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-emerald-600 font-bold">✓</span>
          <span><strong>Format Word (.docx) &amp; PDF:</strong> Siap cetak langsung atau disesuaikan identitas sekolah.</span>
        </li>
      </ul>
    </section>

    <!-- SECTION 2: MATERI YANG DIUJIKAN -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">
        Materi yang Diujikan (Semester 1 Kelas {grade})
      </h2>
      <div class="space-y-3 text-xs sm:text-sm text-slate-700">
        {bab_html}
      </div>
    </section>

    <!-- SECTION 3: CONTOH SOAL GRATIS -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <div class="flex items-center justify-between border-b border-slate-100 pb-2">
        <h2 class="text-lg sm:text-xl font-black text-slate-900">
          Contoh Soal SAS PAI Kelas {grade} (Sampel Gratis)
        </h2>
        <span class="text-xs font-bold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">Sampel Asli</span>
      </div>
      <div class="space-y-4 text-xs sm:text-sm">
        {q_html}
      </div>
    </section>

    <!-- SECTION 4: PREVIEW GAMBAR -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">
        Cuplikan Naskah Ujian (Preview)
      </h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
        <div class="rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 shadow-xs flex flex-col items-center">
          <img src="{data['cover_soal']}" alt="Contoh halaman naskah soal SAS PAI Kelas {grade}" loading="lazy" class="w-full aspect-[3/4] object-cover">
          <p class="p-3 text-center text-xs font-semibold text-slate-600">Cover &amp; Lembar Penilaian Siswa</p>
        </div>
        <div class="rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 shadow-xs flex flex-col items-center justify-between p-6 text-center space-y-4">
          <div class="space-y-2">
            <span class="text-3xl">📄</span>
            <h3 class="font-black text-slate-900 text-sm">Pratinjau Lembar Interaktif</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Anda juga dapat mencoba sampel interaktif naskah soal dan kisi-kisi penulisan secara langsung melalui halaman simulasi kami.
            </p>
          </div>
          <a href="/preview_soal.html?kelas={grade}" class="px-4 py-2 rounded-full bg-slate-900 text-white font-bold text-xs hover:bg-slate-800 transition-colors">
            Buka Pratinjau Interaktif &rarr;
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 5: CTA LYNK.ID -->
    <section class="bg-gradient-to-br from-emerald-50 via-teal-50 to-amber-50 rounded-2xl p-6 sm:p-8 border border-emerald-200 space-y-4 text-center shadow-xs">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white text-emerald-800 font-extrabold text-xs shadow-2xs border border-emerald-100">
        <span>🎉 Diskon Khusus Pendidik PAI</span>
      </div>
      <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">
        Dapatkan Naskah Lengkap Soal SAS PAI Kelas {grade} (Word &amp; PDF)
      </h2>
      <p class="text-xs sm:text-sm text-slate-700 max-w-xl mx-auto leading-relaxed">
        Hemat waktu persiapan administrasi asesmen Anda. Berkas 25 butir soal, kunci jawaban, dan kisi-kisi penulisan soal dalam format Word (.docx) siap sunting langsung terkirim otomatis.
      </p>
      <div class="pt-2">
        <div class="inline-flex items-center gap-2 mb-3">
          <span class="text-xs text-slate-400 font-bold line-through">Rp 20.000</span>
          <span class="text-2xl font-black text-slate-950">Rp 15.000</span>
          <span class="text-[10px] bg-red-100 text-red-700 font-extrabold px-2 py-0.5 rounded-full">Hemat 25%</span>
        </div>
        <div>
          <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-black text-sm shadow-md transition-all hover:scale-105 active:scale-95">
            <span>Beli Naskah Lengkap di Lynk.id</span> <span>&rarr;</span>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 6: FAQ -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">Pertanyaan yang Sering Diajukan (FAQ)</h2>
      <div class="space-y-3 text-xs sm:text-sm">
        <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
          <h3 class="font-extrabold text-slate-900">Apakah naskah soal bisa diedit?</h3>
          <p class="text-slate-600">Ya, file disediakan dalam format Microsoft Word (.docx) sehingga Anda bebas mengganti nama sekolah, logo, dan identitas guru.</p>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
          <h3 class="font-extrabold text-slate-900">Apakah sesuai Kurikulum Merdeka?</h3>
          <p class="text-slate-600">Sangat sesuai. Disusun mengacu pada Capaian Pembelajaran (CP) No. 020 Kemendikbudristek untuk SD {fase}.</p>
        </div>
      </div>
    </section>

    <!-- SECTION 7: INTERNAL LINKS -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">
        Perangkat PAI Kelas Lainnya
      </h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-semibold">
        <a href="/modul-ajar-pai-kelas-{grade}.html" class="p-3.5 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
          <span>🚀 Modul Ajar PAI Kelas {grade} SD</span> <span>&rarr;</span>
        </a>
        <a href="/buku-siswa-pai-kelas-{grade}.html" class="p-3.5 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
          <span>📘 Buku Siswa PAI Kelas {grade} SD</span> <span>&rarr;</span>
        </a>
        <a href="/bank-soal-sas-pai-sd.html" class="p-3.5 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
          <span>📚 Kategori Bank Soal SAS PAI SD (Semua Kelas)</span> <span>&rarr;</span>
        </a>
        <a href="/" class="p-3.5 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
          <span>🏠 Kembali ke Halaman Utama</span> <span>&rarr;</span>
        </a>
      </div>
      <div class="pt-3 border-t border-slate-100">
        <p class="text-xs text-slate-500 font-bold mb-2">Soal SAS Jenjang Kelas Lain:</p>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
          {other_soal_links}
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="bg-white border-t border-[#ece6dc] py-6 px-4 text-xs text-slate-500 mt-12">
    <div class="max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
      <div><span class="font-bold text-slate-800">Bahan Ajar Bu Guru</span> &bull; Kurikulum Merdeka CP No. 020</div>
      <div class="flex items-center gap-4 font-semibold">
        <a href="/kebijakan-privasi.html">Kebijakan Privasi</a>
        <a href="/syarat-ketentuan.html">Syarat &amp; Ketentuan</a>
        <a href="/tentang-kami.html">Tentang Kami</a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="text-emerald-700 hover:underline">Toko Lynk.id &rarr;</a>
      </div>
    </div>
  </footer>

</body>
</html>
"""
    return html

def generate_modul_page(grade):
    data = GRADES_DATA[grade]
    fase = data["fase"]
    title = f"Modul Ajar PAI Kelas {grade} SD Kurikulum Merdeka (Deep Learning)"
    desc = f"Modul ajar Deep Learning PAI Kelas {grade} SD Kurikulum Merdeka 8 halaman lengkap dengan LKPD dan rubrik KKTP format Word dan PDF."
    canonical = f"https://bahanajarbuguru.my.id/modul-ajar-pai-kelas-{grade}.html"

    bab_html = "".join([f"""
    <div class="p-3.5 rounded-xl bg-amber-50/60 border border-amber-100">
      <h3 class="font-bold text-amber-950">{title_b}</h3>
      <p class="text-slate-600 mt-1">{desc_b}</p>
    </div>""" for title_b, desc_b in data["bab_list"]])

    other_modul_links = "".join([
        f"""<a href="/modul-ajar-pai-kelas-{g}.html" class="p-3 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 text-xs font-semibold flex items-center justify-between text-slate-800 hover:text-emerald-950">
          <span>Modul Ajar PAI Kelas {g} SD</span> <span>&rarr;</span>
        </a>""" for g in range(1, 7) if g != grade
    ])

    html = f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  
  <link rel="canonical" href="{canonical}">
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{data['cover_modul']}">
  <meta property="og:url" content="{canonical}">

  <!-- Schema.org Product & FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Product",
        "name": "Modul Ajar Deep Learning PAI & BP SD Kelas {grade}",
        "description": "Modul ajar lengkap 8 halaman standar supervisi: Siklus Mindful, Meaningful, Joyful Learning, LKPD diferensiasi, dan Rubrik KKTP CP No. 020.",
        "image": "https://bahanajarbuguru.my.id{data['cover_modul']}",
        "brand": {{
          "@type": "Brand",
          "name": "Bahan Ajar Bu Guru"
        }},
        "offers": {{
          "@type": "Offer",
          "url": "https://lynk.id/bahanajarbuguru",
          "price": "25000",
          "priceCurrency": "IDR",
          "priceValidUntil": "2027-12-31",
          "availability": "https://schema.org/InStock"
        }}
      }}
    ]
  }}
  </script>

  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="bg-[#faf7f2] text-slate-800 antialiased font-sans">

  <!-- HEADER -->
  <header class="bg-white border-b border-[#e5ded4] sticky top-0 z-40 shadow-xs">
    <div class="max-w-4xl mx-auto px-4 py-3 flex items-center justify-between">
      <a href="/" class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-full bg-emerald-600 text-white font-black text-sm flex items-center justify-center">BG</div>
        <div>
          <span class="font-black text-slate-900 text-sm tracking-tight block">Bahan Ajar Bu Guru</span>
          <span class="text-[10px] text-slate-500 block -mt-0.5">PAI SD Kurikulum Merdeka</span>
        </div>
      </a>
      <div class="flex items-center gap-2">
        <a href="/" class="text-xs font-bold text-slate-600 hover:text-slate-900 px-3 py-1.5 rounded-full hover:bg-slate-100">&larr; Beranda</a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold shadow-xs">Toko Lynk.id &rarr;</a>
      </div>
    </div>
  </header>

  <!-- CONTENT -->
  <main class="max-w-4xl mx-auto px-4 py-6 sm:py-8 space-y-8">
    <nav aria-label="Breadcrumb" class="text-xs font-medium text-slate-500 flex items-center gap-1.5">
      <a href="/" class="hover:text-emerald-700">Beranda</a>
      <span>&rsaquo;</span>
      <a href="/modul-ajar-pai-sd.html" class="hover:text-emerald-700">Modul Ajar PAI SD</a>
      <span>&rsaquo;</span>
      <span class="text-slate-800 font-bold">Modul Ajar PAI Kelas {grade}</span>
    </nav>

    <header class="space-y-3">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-100 text-amber-950 font-bold text-xs">
        <span>Deep Learning 8 Halaman • CP No. 020 • {fase} (Kelas {grade} SD)</span>
      </div>
      <h1 class="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight leading-snug">
        Modul Ajar PAI Kelas {grade} SD Kurikulum Merdeka (Deep Learning)
      </h1>
      <p class="text-sm sm:text-base text-slate-600 leading-relaxed font-normal">
        Naskah perangkat ajar Modul Ajar Pendidikan Agama Islam dan Budi Pekerti (PAI &amp; BP) Kelas {grade} SD format 8 halaman lengkap berbasis pendekatan <em>Deep Learning</em> (Mindful, Meaningful, Joyful Learning). Dilengkapi Lembar Kerja Peserta Didik (LKPD) diferensiasi dan rubrik Kriteria Ketercapaian Tujuan Pembelajaran (KKTP) dalam format Microsoft Word (.docx) siap sunting.
      </p>
    </header>

    <!-- SECTION: KOMPONEN MODUL -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">
        8 Halaman Struktur Lengkap Standar Supervisi
      </h2>
      <ul class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-medium">
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Hal 1:</strong> Identitas Umum, Capaian Pembelajaran (CP No. 020), dan Profil Pelajar Pancasila.</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Hal 2:</strong> Alur Tujuan Pembelajaran (ATP) dan Pemahaman Bermakna.</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Hal 3:</strong> Pertanyaan Pemantik &amp; Model Pembelajaran Berdiferensiasi.</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Hal 4:</strong> Skenario Pembelajaran Fase 1: Mindful Learning (Apersepsi &amp; Kesadaran).</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Hal 5:</strong> Skenario Pembelajaran Fase 2: Meaningful Learning (Eksplorasi Konsep).</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Hal 6:</strong> Skenario Pembelajaran Fase 3: Joyful Learning (Kolaborasi &amp; Permainan).</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Hal 7:</strong> Lembar Kerja Peserta Didik (LKPD) Berdiferensiasi.</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Hal 8:</strong> Rubrik Asesmen Diagnostik, Formatif, dan Sumatif KKTP.</li>
      </ul>
    </section>

    <!-- SECTION: MATERI -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">
        Cakupan Bab Semester 1 (Kelas {grade} SD)
      </h2>
      <div class="space-y-3 text-xs sm:text-sm">
        {bab_html}
      </div>
    </section>

    <!-- SECTION: CTA -->
    <section class="bg-gradient-to-br from-amber-50 via-rose-50 to-emerald-50 rounded-2xl p-6 sm:p-8 border border-amber-200 space-y-4 text-center shadow-xs">
      <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">
        Dapatkan Modul Ajar Lengkap Kelas {grade} (Word .docx)
      </h2>
      <p class="text-xs sm:text-sm text-slate-700 max-w-xl mx-auto leading-relaxed">
        Bebas ganti nama sekolah, logo madrasah, kepala sekolah, dan nama guru Anda langsung di Word tanpa proteksi.
      </p>
      <div class="pt-2">
        <p class="text-2xl font-black text-slate-950 mb-3">Rp 25.000</p>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-black text-sm shadow-md transition-all hover:scale-105">
          <span>Pesan Modul Ajar di Lynk.id</span> <span>&rarr;</span>
        </a>
      </div>
    </section>

    <!-- SECTION: LINKS -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">Perangkat PAI Terkait</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-semibold">
        <a href="/soal-sas-pai-kelas-{grade}.html" class="p-3.5 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 flex items-center justify-between text-slate-800">
          <span>📝 Naskah Soal SAS PAI Kelas {grade} SD</span> <span>&rarr;</span>
        </a>
        <a href="/buku-siswa-pai-kelas-{grade}.html" class="p-3.5 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 flex items-center justify-between text-slate-800">
          <span>📘 Buku Siswa PAI Kelas {grade} SD</span> <span>&rarr;</span>
        </a>
      </div>
      <div class="pt-3 border-t border-slate-100">
        <p class="text-xs text-slate-500 font-bold mb-2">Modul Ajar Jenjang Kelas Lain:</p>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
          {other_modul_links}
        </div>
      </div>
    </section>
  </main>

  <footer class="bg-white border-t border-[#ece6dc] py-6 px-4 text-xs text-slate-500 mt-12">
    <div class="max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
      <div><span class="font-bold text-slate-800">Bahan Ajar Bu Guru</span> &bull; Kurikulum Merdeka CP No. 020</div>
      <div class="flex items-center gap-4 font-semibold">
        <a href="/kebijakan-privasi.html">Kebijakan Privasi</a>
        <a href="/syarat-ketentuan.html">Syarat &amp; Ketentuan</a>
        <a href="/tentang-kami.html">Tentang Kami</a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="text-emerald-700 hover:underline">Toko Lynk.id &rarr;</a>
      </div>
    </div>
  </footer>
</body>
</html>
"""
    return html

def generate_buku_page(grade):
    data = GRADES_DATA[grade]
    fase = data["fase"]
    title = f"Buku Siswa PAI Kelas {grade} SD Kurikulum Merdeka Semester 1"
    desc = f"Naskah Buku Siswa PAI & BP SD Kelas {grade} Kurikulum Merdeka Semester 1 edisi bergambar format Word (.docx) dan PDF siap pakai."
    canonical = f"https://bahanajarbuguru.my.id/buku-siswa-pai-kelas-{grade}.html"

    bab_html = "".join([f"""
    <div class="p-3.5 rounded-xl bg-sky-50/60 border border-sky-100">
      <h3 class="font-bold text-sky-950">{title_b}</h3>
      <p class="text-slate-600 mt-1">{desc_b}</p>
    </div>""" for title_b, desc_b in data["bab_list"]])

    other_buku_links = "".join([
        f"""<a href="/buku-siswa-pai-kelas-{g}.html" class="p-3 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 text-xs font-semibold flex items-center justify-between text-slate-800 hover:text-emerald-950">
          <span>Buku Siswa PAI Kelas {g} SD</span> <span>&rarr;</span>
        </a>""" for g in range(1, 7) if g != grade
    ])

    html = f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  
  <link rel="canonical" href="{canonical}">
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{data['cover_buku']}">
  <meta property="og:url" content="{canonical}">

  <!-- Schema.org Product -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Product",
        "name": "Buku Siswa PAI & BP SD Kelas {grade} Semester 1",
        "description": "Naskah materi buku siswa 1 semester penuh format Word dan PDF A4 acuan CP No. 020.",
        "image": "https://bahanajarbuguru.my.id{data['cover_buku']}",
        "brand": {{
          "@type": "Brand",
          "name": "Bahan Ajar Bu Guru"
        }},
        "offers": {{
          "@type": "Offer",
          "url": "https://lynk.id/bahanajarbuguru",
          "price": "35000",
          "priceCurrency": "IDR",
          "priceValidUntil": "2027-12-31",
          "availability": "https://schema.org/InStock"
        }}
      }}
    ]
  }}
  </script>

  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="bg-[#faf7f2] text-slate-800 antialiased font-sans">

  <!-- HEADER -->
  <header class="bg-white border-b border-[#e5ded4] sticky top-0 z-40 shadow-xs">
    <div class="max-w-4xl mx-auto px-4 py-3 flex items-center justify-between">
      <a href="/" class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-full bg-emerald-600 text-white font-black text-sm flex items-center justify-center">BG</div>
        <div>
          <span class="font-black text-slate-900 text-sm tracking-tight block">Bahan Ajar Bu Guru</span>
          <span class="text-[10px] text-slate-500 block -mt-0.5">PAI SD Kurikulum Merdeka</span>
        </div>
      </a>
      <div class="flex items-center gap-2">
        <a href="/" class="text-xs font-bold text-slate-600 hover:text-slate-900 px-3 py-1.5 rounded-full hover:bg-slate-100">&larr; Beranda</a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold shadow-xs">Toko Lynk.id &rarr;</a>
      </div>
    </div>
  </header>

  <!-- CONTENT -->
  <main class="max-w-4xl mx-auto px-4 py-6 sm:py-8 space-y-8">
    <nav aria-label="Breadcrumb" class="text-xs font-medium text-slate-500 flex items-center gap-1.5">
      <a href="/" class="hover:text-emerald-700">Beranda</a>
      <span>&rsaquo;</span>
      <a href="/buku-siswa-pai-sd.html" class="hover:text-emerald-700">Buku Siswa PAI SD</a>
      <span>&rsaquo;</span>
      <span class="text-slate-800 font-bold">Buku Siswa PAI Kelas {grade}</span>
    </nav>

    <header class="space-y-3">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-100 text-sky-950 font-bold text-xs">
        <span>Semester 1 Penuh • CP No. 020 • {fase} (Kelas {grade} SD)</span>
      </div>
      <h1 class="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight leading-snug">
        Buku Siswa PAI Kelas {grade} SD Kurikulum Merdeka Semester 1
      </h1>
      <p class="text-sm sm:text-base text-slate-600 leading-relaxed font-normal">
        Naskah buku materi ajar siswa Pendidikan Agama Islam dan Budi Pekerti (PAI &amp; BP) Kelas {grade} SD untuk 1 semester penuh. Didesain dengan visual ramah anak, tata letak standar penerbit A4, dan acuan Capaian Pembelajaran (CP) No. 020 Kemendikbudristek dalam format Microsoft Word (.docx) dan PDF siap cetak.
      </p>
    </header>

    <!-- SECTION: DETAIL BUKU -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">
        Keunggulan Buku Siswa PAI Kelas {grade}
      </h2>
      <ul class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-medium">
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Full Color &amp; Ramah Anak:</strong> Dilengkapi ilustrasi edukatif Islami yang memotivasi semangat belajar peserta didik.</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>15 Halaman A4 Standar:</strong> Materi ringkas, padat, dan tidak membebani siswa.</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>Format Word (.docx):</strong> Sekolah dan guru bebas mencantumkan identitas dan nama madrasah.</li>
        <li class="p-3 rounded-xl bg-slate-50 border border-slate-100"><strong>PDF Siap Cetak:</strong> Resolusi cetak tajam tanpa watermark untuk penggandaan di sekolah.</li>
      </ul>
    </section>

    <!-- SECTION: DAFTAR BAB -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">
        Daftar Bab Pembelajaran Semester 1
      </h2>
      <div class="space-y-3 text-xs sm:text-sm">
        {bab_html}
      </div>
    </section>

    <!-- SECTION: CTA -->
    <section class="bg-gradient-to-br from-sky-50 via-teal-50 to-emerald-50 rounded-2xl p-6 sm:p-8 border border-sky-200 space-y-4 text-center shadow-xs">
      <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">
        Dapatkan Buku Siswa Lengkap Kelas {grade} (Word &amp; PDF)
      </h2>
      <p class="text-xs sm:text-sm text-slate-700 max-w-xl mx-auto leading-relaxed">
        Paket lengkap 1 semester naskah buku siswa siap cetak dan bebas disunting.
      </p>
      <div class="pt-2">
        <p class="text-2xl font-black text-slate-950 mb-3">Rp 35.000</p>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-black text-sm shadow-md transition-all hover:scale-105">
          <span>Beli Buku Lengkap di Lynk.id</span> <span>&rarr;</span>
        </a>
      </div>
    </section>

    <!-- SECTION: LINKS -->
    <section class="bg-white rounded-2xl p-6 border border-[#e5ded4] space-y-4 shadow-xs">
      <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-2">Perangkat PAI Terkait</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-semibold">
        <a href="/soal-sas-pai-kelas-{grade}.html" class="p-3.5 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 flex items-center justify-between text-slate-800">
          <span>📝 Naskah Soal SAS PAI Kelas {grade} SD</span> <span>&rarr;</span>
        </a>
        <a href="/modul-ajar-pai-kelas-{grade}.html" class="p-3.5 rounded-xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 flex items-center justify-between text-slate-800">
          <span>🚀 Modul Ajar PAI Kelas {grade} SD</span> <span>&rarr;</span>
        </a>
      </div>
      <div class="pt-3 border-t border-slate-100">
        <p class="text-xs text-slate-500 font-bold mb-2">Buku Siswa Jenjang Kelas Lain:</p>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
          {other_buku_links}
        </div>
      </div>
    </section>
  </main>

  <footer class="bg-white border-t border-[#ece6dc] py-6 px-4 text-xs text-slate-500 mt-12">
    <div class="max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
      <div><span class="font-bold text-slate-800">Bahan Ajar Bu Guru</span> &bull; Kurikulum Merdeka CP No. 020</div>
      <div class="flex items-center gap-4 font-semibold">
        <a href="/kebijakan-privasi.html">Kebijakan Privasi</a>
        <a href="/syarat-ketentuan.html">Syarat &amp; Ketentuan</a>
        <a href="/tentang-kami.html">Tentang Kami</a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="text-emerald-700 hover:underline">Toko Lynk.id &rarr;</a>
      </div>
    </div>
  </footer>
</body>
</html>
"""
    return html

def generate_category_hub(cat_type):
    if cat_type == "soal":
        title = "Kumpulan Bank Soal SAS PAI SD Kelas 1–6 Kurikulum Merdeka"
        desc = "Download naskah bank soal Sumatif Akhir Semester (SAS) PAI & BP SD Kelas 1-6 Kurikulum Merdeka lengkap kunci jawaban dan kisi-kisi CP No. 020."
        canonical = "https://bahanajarbuguru.my.id/bank-soal-sas-pai-sd.html"
        filename = "public/bank-soal-sas-pai-sd.html"
        icon = "📝"
        heading = "Katalog Bank Soal SAS PAI SD (Kelas 1–6)"
        cards = "".join([
            f"""<div class="p-5 rounded-2xl bg-white border border-[#e5ded4] shadow-xs flex flex-col justify-between">
              <div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-900">Kelas {g} SD</span>
                <h3 class="font-black text-slate-900 text-lg mt-2">Soal SAS PAI Kelas {g} SD</h3>
                <p class="text-xs text-slate-600 mt-1">25 Butir Soal (15 PG, 5 Isian, 5 Uraian HOTS), kunci jawaban, dan kisi-kisi CP No. 020.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between">
                <span class="text-sm font-black text-slate-900">Rp 15.000</span>
                <a href="/soal-sas-pai-kelas-{g}.html" class="px-4 py-2 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold transition-colors">Lihat Rincian &rarr;</a>
              </div>
            </div>""" for g in range(1, 7)
        ])
    elif cat_type == "modul":
        title = "Modul Ajar Deep Learning PAI SD Kelas 1–6 Kurikulum Merdeka"
        desc = "Download Modul Ajar Deep Learning PAI & BP SD Kelas 1-6 format 8 halaman lengkap LKPD dan rubrik KKTP CP No. 020 format Word (.docx) dan PDF."
        canonical = "https://bahanajarbuguru.my.id/modul-ajar-pai-sd.html"
        filename = "public/modul-ajar-pai-sd.html"
        icon = "🚀"
        heading = "Katalog Modul Ajar Deep Learning PAI SD (Kelas 1–6)"
        cards = "".join([
            f"""<div class="p-5 rounded-2xl bg-white border border-[#e5ded4] shadow-xs flex flex-col justify-between">
              <div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-100 text-amber-900">Kelas {g} SD</span>
                <h3 class="font-black text-slate-900 text-lg mt-2">Modul Ajar PAI Kelas {g} SD</h3>
                <p class="text-xs text-slate-600 mt-1">Format Deep Learning 8 halaman standar supervisi: Mindful, Meaningful, Joyful Learning &amp; LKPD.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between">
                <span class="text-sm font-black text-slate-900">Rp 25.000</span>
                <a href="/modul-ajar-pai-kelas-{g}.html" class="px-4 py-2 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold transition-colors">Lihat Rincian &rarr;</a>
              </div>
            </div>""" for g in range(1, 7)
        ])
    else: # buku
        title = "Buku Siswa PAI & BP SD Kelas 1–6 Kurikulum Merdeka Semester 1"
        desc = "Download naskah Buku Siswa PAI & BP SD Kelas 1-6 Kurikulum Merdeka Semester 1 edisi bergambar format Word (.docx) dan PDF siap pakai."
        canonical = "https://bahanajarbuguru.my.id/buku-siswa-pai-sd.html"
        filename = "public/buku-siswa-pai-sd.html"
        icon = "📘"
        heading = "Katalog Buku Siswa PAI & BP SD (Kelas 1–6)"
        cards = "".join([
            f"""<div class="p-5 rounded-2xl bg-white border border-[#e5ded4] shadow-xs flex flex-col justify-between">
              <div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-sky-100 text-sky-900">Kelas {g} SD</span>
                <h3 class="font-black text-slate-900 text-lg mt-2">Buku Siswa PAI Kelas {g} SD</h3>
                <p class="text-xs text-slate-600 mt-1">Buku materi 1 semester penuh, full-color ramah anak, tata letak standar penerbit A4.</p>
              </div>
              <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between">
                <span class="text-sm font-black text-slate-900">Rp 35.000</span>
                <a href="/buku-siswa-pai-kelas-{g}.html" class="px-4 py-2 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold transition-colors">Lihat Rincian &rarr;</a>
              </div>
            </div>""" for g in range(1, 7)
        ])

    html = f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="canonical" href="{canonical}">
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">

  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="bg-[#faf7f2] text-slate-800 antialiased font-sans">
  <header class="bg-white border-b border-[#e5ded4] sticky top-0 z-40 shadow-xs">
    <div class="max-w-4xl mx-auto px-4 py-3 flex items-center justify-between">
      <a href="/" class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-full bg-emerald-600 text-white font-black text-sm flex items-center justify-center">BG</div>
        <div>
          <span class="font-black text-slate-900 text-sm tracking-tight block">Bahan Ajar Bu Guru</span>
          <span class="text-[10px] text-slate-500 block -mt-0.5">PAI SD Kurikulum Merdeka</span>
        </div>
      </a>
      <div class="flex items-center gap-2">
        <a href="/" class="text-xs font-bold text-slate-600 hover:text-slate-900 px-3 py-1.5 rounded-full hover:bg-slate-100">&larr; Beranda</a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold shadow-xs">Toko Lynk.id &rarr;</a>
      </div>
    </div>
  </header>

  <main class="max-w-4xl mx-auto px-4 py-6 sm:py-8 space-y-8">
    <nav aria-label="Breadcrumb" class="text-xs font-medium text-slate-500 flex items-center gap-1.5">
      <a href="/" class="hover:text-emerald-700">Beranda</a>
      <span>&rsaquo;</span>
      <span class="text-slate-800 font-bold">{heading}</span>
    </nav>

    <header class="space-y-3">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-950 font-bold text-xs">
        <span>{icon} Kurikulum Merdeka • CP No. 020 Kemendikbudristek</span>
      </div>
      <h1 class="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight leading-snug">
        {heading}
      </h1>
      <p class="text-sm sm:text-base text-slate-600 leading-relaxed font-normal">
        Daftar lengkap perangkat pembelajaran Pendidikan Agama Islam dan Budi Pekerti (PAI &amp; BP) untuk Sekolah Dasar jenjang Fase A (Kelas 1–2), Fase B (Kelas 3–4), dan Fase C (Kelas 5–6). Semua berkas dapat disunting bebas di Microsoft Word (.docx) dan siap cetak di PDF.
      </p>
    </header>

    <section class="grid grid-cols-1 md:grid-cols-2 gap-4">
      {cards}
    </section>

    <!-- INTERNAL LINK TO OTHER HUBS -->
    <section class="p-6 rounded-2xl bg-white border border-[#e5ded4] space-y-3">
      <h3 class="font-black text-slate-900 text-base">Kategori Perangkat Pembelajaran Lainnya</h3>
      <div class="flex flex-wrap gap-2 text-xs font-bold">
        <a href="/bank-soal-sas-pai-sd.html" class="px-4 py-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800">📝 Bank Soal SAS PAI SD</a>
        <a href="/modul-ajar-pai-sd.html" class="px-4 py-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800">🚀 Modul Ajar Deep Learning</a>
        <a href="/buku-siswa-pai-sd.html" class="px-4 py-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800">📘 Buku Siswa 1 Semester</a>
        <a href="/game-petualangan-islami.html" class="px-4 py-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800">🎮 Game Petualangan Islami</a>
      </div>
    </section>
  </main>

  <footer class="bg-white border-t border-[#ece6dc] py-6 px-4 text-xs text-slate-500 mt-12">
    <div class="max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
      <div><span class="font-bold text-slate-800">Bahan Ajar Bu Guru</span> &bull; Kurikulum Merdeka CP No. 020</div>
      <div class="flex items-center gap-4 font-semibold">
        <a href="/kebijakan-privasi.html">Kebijakan Privasi</a>
        <a href="/syarat-ketentuan.html">Syarat &amp; Ketentuan</a>
        <a href="/tentang-kami.html">Tentang Kami</a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="text-emerald-700 hover:underline">Toko Lynk.id &rarr;</a>
      </div>
    </div>
  </footer>
</body>
</html>
"""
    return filename, html

def main():
    print("Generating all dedicated product and category pages...")
    
    # 1. Generate Soal Pages
    for g in range(1, 7):
        html = generate_soal_page(g)
        p = f"public/soal-sas-pai-kelas-{g}.html"
        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: {p}")

    # 2. Generate Modul Pages
    for g in range(1, 7):
        html = generate_modul_page(g)
        p = f"public/modul-ajar-pai-kelas-{g}.html"
        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: {p}")

    # 3. Generate Buku Pages
    for g in range(1, 7):
        html = generate_buku_page(g)
        p = f"public/buku-siswa-pai-kelas-{g}.html"
        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: {p}")

    # 4. Generate Category Hub Pages
    for cat in ["soal", "modul", "buku"]:
        filename, html = generate_category_hub(cat)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created Hub: {filename}")

    # 5. Update portal_content.json to point to clean URLs
    content_file = "public/data/portal_content.json"
    with open(content_file, "r", encoding="utf-8") as f:
        content = json.load(f)

    content["bukuSection"]["topSampleUrl"] = "/buku-siswa-pai-sd.html"
    content["modulSection"]["topSampleUrl"] = "/modul-ajar-pai-sd.html"
    content["soalSection"]["topSampleUrl"] = "/bank-soal-sas-pai-sd.html"

    for item in content.get("bukuItems", []):
        g = item.get("grade", 1)
        item["sampleUrl"] = f"/buku-siswa-pai-kelas-{g}.html"

    for item in content.get("modulItems", []):
        g = item.get("grade", 1)
        item["sampleUrl"] = f"/modul-ajar-pai-kelas-{g}.html"

    for item in content.get("soalItems", []):
        g = item.get("grade", 1)
        item["sampleUrl"] = f"/soal-sas-pai-kelas-{g}.html"

    with open(content_file, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    print("Updated public/data/portal_content.json with clean URLs!")

    # 6. Generate Complete sitemap.xml
    all_urls = [
        ("https://bahanajarbuguru.my.id/", "1.0", "daily"),
        ("https://bahanajarbuguru.my.id/bank-soal-sas-pai-sd.html", "0.9", "weekly"),
        ("https://bahanajarbuguru.my.id/modul-ajar-pai-sd.html", "0.9", "weekly"),
        ("https://bahanajarbuguru.my.id/buku-siswa-pai-sd.html", "0.9", "weekly"),
        ("https://bahanajarbuguru.my.id/game-petualangan-islami.html", "0.8", "monthly"),
        ("https://bahanajarbuguru.my.id/lembar_penilaian_harian_kelas3_bab5.html", "0.8", "monthly"),
        ("https://bahanajarbuguru.my.id/tentang-kami.html", "0.5", "monthly"),
        ("https://bahanajarbuguru.my.id/kebijakan-privasi.html", "0.4", "monthly"),
        ("https://bahanajarbuguru.my.id/syarat-ketentuan.html", "0.4", "monthly"),
    ]

    for g in range(1, 7):
        all_urls.append((f"https://bahanajarbuguru.my.id/soal-sas-pai-kelas-{g}.html", "0.9", "weekly"))
        all_urls.append((f"https://bahanajarbuguru.my.id/modul-ajar-pai-kelas-{g}.html", "0.9", "weekly"))
        all_urls.append((f"https://bahanajarbuguru.my.id/buku-siswa-pai-kelas-{g}.html", "0.9", "weekly"))

    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in all_urls:
        sitemap_xml.append('  <url>')
        sitemap_xml.append(f'    <loc>{loc}</loc>')
        sitemap_xml.append('    <lastmod>2026-11-19</lastmod>')
        sitemap_xml.append(f'    <changefreq>{freq}</changefreq>')
        sitemap_xml.append(f'    <priority>{priority}</priority>')
        sitemap_xml.append('  </url>')
    sitemap_xml.append('</urlset>')

    with open("public/sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_xml))
    print("Updated public/sitemap.xml with all 27 indexed clean URLs!")

if __name__ == "__main__":
    main()
