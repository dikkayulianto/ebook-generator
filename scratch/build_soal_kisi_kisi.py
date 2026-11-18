# -*- coding: utf-8 -*-
"""
Generator for authentic 5-page SAS Exam Papers + Official Kisi-Kisi CP 020/2026
Covering Kelas 1 to Kelas 6 SD (Pendidikan Agama Islam & Budi Pekerti)
"""
import json
import os

grades_data = [
    {
        "grade": 1,
        "fase": "Fase A",
        "title": "Naskah Soal SAS & Kisi-Kisi PAI Kelas 1 SD",
        "badge": "Fase A • Kelas 1 SD • Semester 1",
        "bab_list": [
            ("Bab 1: Aku Cinta Al-Qur'an", "Al-Qur'an Hadis", "Mengenal huruf hijaiyah berharakat fathah, kasrah, dhammah serta tempat keluarnya (makhraj).", "L1 (C1/C2)", "PG (1, 2), Isian (16), Uraian (21)"),
            ("Bab 2: Mengenal Rukun Iman", "Akidah Islamiyah", "Menyebutkan enam rukun iman dan meyakini keberadaan Allah Swt. sebagai Sang Pencipta semesta.", "L1 (C1/C2)", "PG (3, 4), Isian (17)"),
            ("Bab 3: Basmalah & Hamdalah", "Akhlak Terpuji", "Membiasakan membaca basmalah sebelum beraktivitas dan hamdalah setelah selesai sebagai wujud syukur.", "L2 (C3)", "PG (5, 6, 7), Isian (18), Uraian (22)"),
            ("Bab 4: Rukun Islam & Syahadat", "Fikih Ibadah", "Menyebutkan lima rukun Islam, melafalkan dua kalimat syahadat serta memahami artinya.", "L2 (C3)", "PG (8, 9, 10), Isian (19), Uraian (23)"),
            ("Bab 5: Nabi Adam a.s. & Bersuci", "Sejarah & Fikih", "Menceritakan keteladanan Nabi Adam a.s. serta mempraktikkan tata cara bersuci (wudhu & istinjak).", "L3 (C4 HOTS)", "PG (11-15), Isian (20), Uraian (24, 25)")
        ],
        "pg_items": [
            ("1", "Tanda baca dalam Al-Qur'an yang berada di atas huruf dan berbunyi vokal 'A' disebut ...", "A. Kasrah &nbsp;&nbsp;&nbsp; B. Fathah &nbsp;&nbsp;&nbsp; C. Dhammah", "B"),
            ("2", "Huruf hijaiyah yang dilafalkan dengan merapatkan kedua bibir secara sempurna adalah ...", "A. Ba (ب) &nbsp;&nbsp;&nbsp; B. Ta (ت) &nbsp;&nbsp;&nbsp; C. Tsa (ث)", "A"),
            ("3", "Rukun Iman yang pertama wajib kita yakini dalam hati adalah beriman kepada ...", "A. Malaikat &nbsp;&nbsp;&nbsp; B. Kitab Allah &nbsp;&nbsp;&nbsp; C. Allah Swt.", "C"),
            ("4", "Asmaul Husna 'Ar-Rahman' memiliki makna bahwa Allah Swt. Maha ...", "A. Pengasih &nbsp;&nbsp;&nbsp; B. Mengetahui &nbsp;&nbsp;&nbsp; C. Perkasa", "A"),
            ("5", "Sebelum kita memulai belajar dan makan, ucapan thayyibah yang sebaiknya kita lafalkan adalah ...", "A. Takbir &nbsp;&nbsp;&nbsp; B. Basmalah &nbsp;&nbsp;&nbsp; C. Tasbih", "B"),
            ("6", "Setelah selesai makan dan minum, kita mengucapkan hamdalah sebagai ungkapan rasa ...", "A. Syukur kepada Allah &nbsp;&nbsp;&nbsp; B. Takut &nbsp;&nbsp;&nbsp; C. Bangga diri", "A"),
            ("7", "Rukun Islam yang kedua adalah kewajiban mendirikan ...", "A. Salat lima waktu &nbsp;&nbsp;&nbsp; B. Zakat fitrah &nbsp;&nbsp;&nbsp; C. Puasa Ramadan", "A"),
            ("8", "Syahadat tauhid berisi persaksian bahwa tiada sesembahan yang berhak disembah selain ...", "A. Malaikat &nbsp;&nbsp;&nbsp; B. Allah Swt. &nbsp;&nbsp;&nbsp; C. Rasul", "B"),
            ("9", "Manusia pertama yang diciptakan oleh Allah Swt. dari tanah adalah Nabi ...", "A. Ibrahim a.s. &nbsp;&nbsp;&nbsp; B. Adam a.s. &nbsp;&nbsp;&nbsp; C. Nuh a.s.", "B"),
            ("10", "Sebelum melaksanakan ibadah salat, kita wajib menyucikan diri dari hadas kecil dengan ...", "A. Mandi &nbsp;&nbsp;&nbsp; B. Berwudhu &nbsp;&nbsp;&nbsp; C. Cuci tangan", "B"),
            ("11", "Jumlah rukun Islam yang wajib diamalkan setiap muslim ada ... perkara.", "A. Tiga &nbsp;&nbsp;&nbsp; B. Lima &nbsp;&nbsp;&nbsp; C. Enam", "B"),
            ("12", "Sikap terpuji Nabi Adam a.s. saat berbuat khilaf adalah segera ...", "A. Menyesal & bertobat &nbsp;&nbsp;&nbsp; B. Bersembunyi &nbsp;&nbsp;&nbsp; C. Membantah", "A"),
            ("13", "Anggota badan yang pertama kali dibasuh saat mempraktikkan wudhu setelah niat adalah ...", "A. Telinga &nbsp;&nbsp;&nbsp; B. Wajah / Muka &nbsp;&nbsp;&nbsp; C. Kaki", "B"),
            ("14", "Air yang sah dan suci digunakan untuk berwudhu adalah air ...", "A. Kopi manis &nbsp;&nbsp;&nbsp; B. Sumur / Keran bersih &nbsp;&nbsp;&nbsp; C. Sabun mandi", "B"),
            ("15", "Apabila teman di sekolah terjatuh dari sepeda, sikap kita yang sesuai akhlak Islam adalah ...", "A. Menertawakannya &nbsp;&nbsp;&nbsp; B. Menolong & menenangkan &nbsp;&nbsp;&nbsp; C. Meninggalkannya", "B")
        ],
        "isian_items": [
            ("16", "Harakat yang terletak di bawah huruf hijaiyah dan berbunyi vokal 'I' dinamakan ...", "Kasrah"),
            ("17", "Rukun Iman berjumlah ... perkara yang wajib diyakini setiap muslim.", "6 (Enam)"),
            ("18", "Lafal kalimat thayyibah basmalah berbunyi: ...", "Bismillahir-rahmanir-rahim"),
            ("19", "Kalimat syahadatain terdiri atas syahadat tauhid dan syahadat ...", "Rasul"),
            ("20", "Membersihkan kubul atau dubur setelah buang air kecil maupun besar disebut ...", "Istinjak")
        ],
        "uraian_items": [
            ("21", "Tuliskan 3 contoh huruf hijaiyah tunggal berharakat fathah yang telah kamu pelajari!", "Contoh: بَ (Ba), تَ (Ta), ثَ (Tsa)"),
            ("22", "Mengapa setiap kita hendak belajar, makan, atau bepergian dibiasakan membaca basmalah?", "Agar segala aktivitas bernilai ibadah, mendapat berkah, dan selalu dalam lindungan Allah Swt."),
            ("23", "Sebutkan urutan 3 anggota tubuh yang wajib dibasuh saat melaksanakan wudhu sesuai rukun!", "Membasuh wajah (disertai niat), membasuh kedua tangan sampai siku, dan membasuh kedua kaki sampai mata kaki."),
            ("24", "Bagaimana sikap kamu apabila melihat adikmu menangis karena mainannya rusak?", "Menghiburnya, membantu merapikan atau memperbaiki mainan tersebut, dan mengajaknya bermain bersama."),
            ("25", "Sebutkan teladan yang bisa kita ambil dari kisah Nabi Adam a.s. saat mengakui kesalahannya!", "Berani mengakui kesalahan dengan jujur, segera memohon ampun (istighfar) kepada Allah, dan berjanji tidak mengulanginya.")
        ]
    },
    {
        "grade": 2,
        "fase": "Fase A",
        "title": "Naskah Soal SAS & Kisi-Kisi PAI Kelas 2 SD",
        "badge": "Fase A • Kelas 2 SD • Semester 1",
        "bab_list": [
            ("Bab 1: Huruf Hijaiyah Bersambung", "Al-Qur'an Hadis", "Mengenali perubahan bentuk huruf hijaiyah bersambung di awal, tengah, dan akhir kata.", "L1 (C1/C2)", "PG (1, 2), Isian (16), Uraian (21)"),
            ("Bab 2: Surah An-Nas & Al-Falaq", "Al-Qur'an Hadis", "Membaca, menghafal, dan memahami pesan perlindungan diri dari kejahatan dalam surah Al-Mu'awwidzatain.", "L2 (C3)", "PG (3, 4, 5), Isian (17), Uraian (22)"),
            ("Bab 3: Asmaul Husna Al-Hafiz & Al-Wali", "Akidah Islamiyah", "Meneladani sifat Allah Swt. Yang Maha Menjaga dan Maha Melindungi dalam kehidupan sehari-hari.", "L2 (C3)", "PG (6, 7, 8), Isian (18)"),
            ("Bab 4: Hidup Bersih & Adab Berteman", "Akhlak Terpuji", "Menerapkan perilaku hidup bersih dan santun dalam interaksi pertemanan di sekolah dan rumah.", "L2 (C3)", "PG (9, 10, 11), Isian (19), Uraian (23)"),
            ("Bab 5: Salat Fardu, Azan & Nabi Nuh a.s.", "Fikih & Tarikh", "Menyebutkan nama-nama salat fardu, arti lafal azan, dan kesabaran dakwah Nabi Nuh a.s.", "L3 (C4 HOTS)", "PG (12-15), Isian (20), Uraian (24, 25)")
        ],
        "pg_items": [
            ("1", "Huruf hijaiyah yang tidak dapat disambung dengan huruf sesudahnya adalah ...", "A. Alif (ا) dan Dal (د) &nbsp;&nbsp;&nbsp; B. Ba (ب) dan Ta (ت) &nbsp;&nbsp;&nbsp; C. Sin (س) dan Mim (م)", "A"),
            ("2", "Perubahan bentuk huruf 'Jim' (ج) saat berada di awal kata yang tersambung adalah ...", "A. Bentuknya tetap utuh &nbsp;&nbsp;&nbsp; B. Ditulis kepalanya saja &nbsp;&nbsp;&nbsp; C. Hilang titiknya", "B"),
            ("3", "Surah An-Nas diturunkan untuk mengajarkan manusia memohon perlindungan hanya kepada ...", "A. Dukun &nbsp;&nbsp;&nbsp; B. Jin &nbsp;&nbsp;&nbsp; C. Allah Swt.", "C"),
            ("4", "Arti kata 'Al-Falaq' dalam Surah Al-Falaq adalah ...", "A. Waktu Subuh &nbsp;&nbsp;&nbsp; B. Manusia &nbsp;&nbsp;&nbsp; C. Bintang malam", "A"),
            ("5", "Lafal 'Qul a'uudzu birabbin-naas' merupakan ayat pertama dari Surah ...", "A. Al-Ikhlas &nbsp;&nbsp;&nbsp; B. An-Nas &nbsp;&nbsp;&nbsp; C. Al-Falaq", "B"),
            ("6", "Asmaul Husna 'Al-Hafiz' (الحَفِيظُ) bermakna bahwa Allah Swt. Maha ...", "A. Pemelihara / Maha Penjaga &nbsp;&nbsp;&nbsp; B. Pengampun &nbsp;&nbsp;&nbsp; C. Perkasa", "A"),
            ("7", "Meneladani sifat 'Al-Wali' (Maha Melindungi) dapat kita wujudkan dengan cara ...", "A. Menakut-nakuti teman &nbsp;&nbsp;&nbsp; B. Menjaga dan membela adik yang lemah &nbsp;&nbsp;&nbsp; C. Merusak tanaman", "B"),
            ("8", "Kebersihan merupakan sebagian dari ...", "A. Keberuntungan &nbsp;&nbsp;&nbsp; B. Iman &nbsp;&nbsp;&nbsp; C. Kekayaan", "B"),
            ("9", "Membuang sampah bekas jajanan ke tempat sampah di kelas mencerminkan adab ...", "A. Hidup bersih dan peduli lingkungan &nbsp;&nbsp;&nbsp; B. Berhemat uang &nbsp;&nbsp;&nbsp; C. Pamer ketertiban", "A"),
            ("10", "Salat fardu yang dikerjakan pada saat terbit fajar dengan jumlah dua rakaat adalah ...", "A. Subuh &nbsp;&nbsp;&nbsp; B. Magrib &nbsp;&nbsp;&nbsp; C. Isya", "A"),
            ("11", "Panggilan atau seruan resmi yang menandakan telah masuk waktu salat fardu dinamakan ...", "A. Ikamah &nbsp;&nbsp;&nbsp; B. Azan &nbsp;&nbsp;&nbsp; C. Tarhim", "B"),
            ("12", "Jumlah total rakaat salat fardu dalam sehari semalam bagi seorang muslim adalah ...", "A. 15 Rakaat &nbsp;&nbsp;&nbsp; B. 17 Rakaat &nbsp;&nbsp;&nbsp; C. 20 Rakaat", "B"),
            ("13", "Nabi Nuh a.s. diperintahkan oleh Allah Swt. untuk membuat kapal besar di atas bukit guna ...", "A. Berdagang ke pulau seberang &nbsp;&nbsp;&nbsp; B. Menyelamatkan kaum yang beriman dari banjir bandang &nbsp;&nbsp;&nbsp; C. Wisata bersama keluarga", "B"),
            ("14", "Anak Nabi Nuh a.s. yang membangkang dan menolak diajak naik ke perahu bernama ...", "A. Sam &nbsp;&nbsp;&nbsp; B. Kan'an &nbsp;&nbsp;&nbsp; C. Ham", "B"),
            ("15", "Ketika kita berjanji kepada teman untuk belajar bersama sore hari, maka sikap kita seharusnya ...", "A. Membatalkan sepihak &nbsp;&nbsp;&nbsp; B. Menepati janji tepat waktu &nbsp;&nbsp;&nbsp; C. Pura-pura lupa", "B")
        ],
        "isian_items": [
            ("16", "Huruf hijaiyah 'Mim' (م) apabila ditulis di akhir kata yang bersambung memiliki ekor yang mengarah ke ...", "Bawah"),
            ("17", "Surah Al-Falaq dan Surah An-Nas secara bersama-sama disebut sebagai surah Al-...", "Mu'awwidzatain (Dua surah perlindungan)"),
            ("18", "Nama baik Allah Swt. 'Al-Wali' artinya Allah Maha ...", "Melindungi / Menolong hamba-Nya"),
            ("19", "Panggilan salat yang dikumandangkan sebagai tanda salat fardu berjamaah segera dimulai dinamakan ...", "Ikamah"),
            ("20", "Nabi Nuh a.s. berdakwah mengajak kaumnya menyembah Allah selama kurang lebih ... tahun.", "950 Tahun")
        ],
        "uraian_items": [
            ("21", "Tuliskan 3 huruf hijaiyah yang bentuknya berubah ketika disambung di tengah kalimat!", "Contoh: Ba (ـبـ), Kaf (ـكـ), dan 'Ain (ـعـ)"),
            ("22", "Sebutkan pesan utama yang terkandung dalam Surah An-Nas mengenai perlindungan diri!", "Kita harus selalu memohon perlindungan hanya kepada Allah Swt. dari godaan bisikan setan, baik yang berasal dari golongan jin maupun manusia."),
            ("23", "Bagaimana caramu menerapkan teladan sifat Al-Hafiz (Maha Memelihara) di sekolah?", "Dengan memelihara fasilitas kelas, menjaga kebersihan meja kursi, serta menjaga lisan agar tidak menyakiti teman."),
            ("24", "Sebutkan nama-nama salat fardu lima waktu secara berurutan beserta jumlah rakaatnya!", "Subuh (2 rakaat), Zuhur (4 rakaat), Asar (4 rakaat), Magrib (3 rakaat), dan Isya (4 rakaat)."),
            ("25", "Pelajaran akhlak apakah yang dapat kita petik dari ketabahan dakwah Nabi Nuh a.s.?", "Sikap sabar, pantang menyerah dalam kebaikan, dan tetap taat kepada perintah Allah meskipun banyak rintangan.")
        ]
    },
    {
        "grade": 3,
        "fase": "Fase B",
        "title": "Naskah Soal SAS & Kisi-Kisi PAI Kelas 3 SD",
        "badge": "Fase B • Kelas 3 SD • Semester 1",
        "bab_list": [
            ("Bab 1: Surah Al-Humazah & Al-Kautsar", "Al-Qur'an Hadis", "Membaca tartil, mengartikan perkata, dan memahami larangan mencela serta perintah bersyukur atas nikmat.", "L1 (C1/C2)", "PG (1, 2, 3), Isian (16), Uraian (21)"),
            ("Bab 2: Asmaul Husna Al-Wahhab & Al-Kabir", "Akidah Islamiyah", "Menjelaskan makna Allah Maha Pemberi Karunia dan Maha Besar serta mengamalkannya dalam kehidupan sosial.", "L2 (C3)", "PG (4, 5, 6), Isian (17), Uraian (22)"),
            ("Bab 3: Berbakti kepada Orang Tua & Guru", "Akhlak Terpuji", "Menunjukkan sikap hormat, sopan santun, patuh, dan mendoakan kedua orang tua dan bapak/ibu guru.", "L2 (C3)", "PG (7, 8, 9), Isian (18), Uraian (23)"),
            ("Bab 4: Ketentuan Salat Rawatib", "Fikih Ibadah", "Membedakan salat sunah rawatib mu'akkad dan gairu mu'akkad serta waktu pelaksanaannya (qabliyah & ba'diyah).", "L2 (C3)", "PG (10, 11, 12), Isian (19), Uraian (24)"),
            ("Bab 5: Kisah Keteladanan Nabi Ibrahim a.s.", "Sejarah Peradaban", "Menganalisis pencarian kebenaran Nabi Ibrahim a.s., keteguhan iman, dan peristiwa kurban.", "L3 (C4 HOTS)", "PG (13-15), Isian (20), Uraian (25)")
        ],
        "pg_items": [
            ("1", "Kata 'Al-Humazah' memiliki arti golongan orang-orang yang gemar ...", "A. Berbohong &nbsp;&nbsp;&nbsp; B. Mengumpat dan mencela &nbsp;&nbsp;&nbsp; C. Menolong", "B"),
            ("2", "Dalam Surah Al-Kautsar, Allah Swt. memerintahkan orang beriman untuk mendirikan salat dan ...", "A. Membayar zakat &nbsp;&nbsp;&nbsp; B. Berkurban &nbsp;&nbsp;&nbsp; C. Berpuasa", "B"),
            ("3", "Hukum bacaan mim sukun bertemu huruf 'Ba' (ب) dinamakan ...", "A. Idgham Mimi &nbsp;&nbsp;&nbsp; B. Ikhfa Syafawi &nbsp;&nbsp;&nbsp; C. Izhar Halqi", "B"),
            ("4", "Allah Swt. melimpahkan rezeki dan kesehatan kepada setiap makhluk tanpa meminta imbalan, karena Allah memiliki Asmaul Husna ...", "A. Al-Wahhab (الوَهَّابُ) &nbsp;&nbsp;&nbsp; B. Al-Kabir &nbsp;&nbsp;&nbsp; C. Al-Qawiyyu", "A"),
            ("5", "Lafal 'Allahu Akbar' yang sering kita dengar dalam takbir salat berkaitan erat dengan Asmaul Husna ...", "A. Al-Kabir (الكَبِيرُ) &nbsp;&nbsp;&nbsp; B. As-Sami' &nbsp;&nbsp;&nbsp; C. Al-Basir", "A"),
            ("6", "Salah satu wujud meneladani Asmaul Husna Al-Wahhab di lingkungan kelas adalah ...", "A. Suka meminta barang teman &nbsp;&nbsp;&nbsp; B. Ikhlas berbagi alat tulis atau bekal kepada teman yang membutuhkan &nbsp;&nbsp;&nbsp; C. Menyimpan uang sendiri", "B"),
            ("7", "Cara berbakti kepada kedua orang tua yang telah membesarkan kita sejak kecil adalah ...", "A. Membantah nasihatnya &nbsp;&nbsp;&nbsp; B. Mendengarkan dan mematuhi perintah kebaikan mereka &nbsp;&nbsp;&nbsp; C. Mengabaikan panggilannya", "B"),
            ("8", "Ridha Allah Swt. tergantung kepada ridha kedua orang tua, dan murka Allah juga tergantung pada ...", "A. Teman sebaya &nbsp;&nbsp;&nbsp; B. Murka kedua orang tua &nbsp;&nbsp;&nbsp; C. Harta kekayaan", "B"),
            ("9", "Sikap terpuji seorang murid saat bapak atau ibu guru sedang menerangkan pelajaran di depan kelas adalah ...", "A. Bercanda dengan teman sebangku &nbsp;&nbsp;&nbsp; B. Menyimak dengan sungguh-sungguh dan tidak menyela &nbsp;&nbsp;&nbsp; C. Bermain gawai", "B"),
            ("10", "Salat sunah yang mengiringi salat fardu, baik dilakukan sebelum maupun sesudahnya, dinamakan salat ...", "A. Tarawih &nbsp;&nbsp;&nbsp; B. Rawatib &nbsp;&nbsp;&nbsp; C. Duha", "B"),
            ("11", "Salat sunah rawatib yang dikerjakan sebelum melaksanakan salat fardu disebut salat ...", "A. Qabliyah &nbsp;&nbsp;&nbsp; B. Ba'diyah &nbsp;&nbsp;&nbsp; C. Witir", "A"),
            ("12", "Waktu salat fardu yang TIDAK memiliki salat sunah rawatib ba'diyah adalah waktu salat ...", "A. Zuhur &nbsp;&nbsp;&nbsp; B. Magrib &nbsp;&nbsp;&nbsp; C. Subuh dan Asar", "C"),
            ("13", "Nabi Ibrahim a.s. dilahirkan di wilayah Babilonia pada masa kepemimpinan raja yang zalim bernama Raja ...", "A. Fir'aun &nbsp;&nbsp;&nbsp; B. Namrud &nbsp;&nbsp;&nbsp; C. Jalut", "B"),
            ("14", "Ketika Nabi Ibrahim a.s. dilemparkan ke dalam kobaran api yang membara, mukjizat yang terjadi adalah ...", "A. Apinya menjadi dingin dan menyelamatkannya &nbsp;&nbsp;&nbsp; B. Api langsung padam tersiram hujan &nbsp;&nbsp;&nbsp; C. Terbawa angin topan", "A"),
            ("15", "Putra Nabi Ibrahim a.s. yang dengan penuh keikhlasan bersedia disembelih demi menaati perintah wahyu Allah Swt. adalah Nabi ...", "A. Ishaq a.s. &nbsp;&nbsp;&nbsp; B. Ismail a.s. &nbsp;&nbsp;&nbsp; C. Ya'qub a.s.", "B")
        ],
        "isian_items": [
            ("16", "Surah Al-Kautsar merupakan surah terpendek dalam Al-Qur'an yang terdiri atas ... ayat.", "3 (Tiga)"),
            ("17", "Asmaul Husna 'Al-Kabir' mengandung arti bahwa Allah Swt. Maha ...", "Besar / Maha Agung"),
            ("18", "Doa memohon ampunan untuk kedua orang tua diawali dengan lafal: Rabbighfir lii wa liwaalidayya warhamhuma kamaa...", "Rabbayaanii shaghiiraa"),
            ("19", "Salat sunah rawatib yang sangat dianjurkan dan tidak pernah ditinggalkan Rasulullah dinamakan rawatib ...", "Mu'akkad"),
            ("20", "Ayah dari Nabi Ibrahim a.s. yang berprofesi sebagai pembuat dan penjual patung berhala bernama ...", "Azar")
        ],
        "uraian_items": [
            ("21", "Jelaskan pesan moral yang terkandung dalam Surah Al-Humazah bagi kehidupan sehari-hari anak sekolah!", "Surah Al-Humazah mengingatkan kita agar menjauhi sikap suka mengumpat, mencela kekurangan fisik teman, dan menyombongkan harta kekayaan karena perbuatan itu diancam siksa neraka."),
            ("22", "Sebutkan 2 contoh penerapan perilaku meneladani Asmaul Husna Al-Wahhab di lingkungan masyarakat!", "1) Memberikan santunan atau makanan kepada anak yatim dan kaum duafa; 2) Rela berbagi ilmu atau tenaga untuk membantu orang lain tanpa pamrih."),
            ("23", "Tuliskan 3 adab yang harus kita amalkan saat berbicara dengan bapak atau ibu guru!", "1) Berbicara dengan nada suara lemah lembut dan santun; 2) Mengucapkan salam terlebih dahulu; 3) Menatap dengan penuh hormat serta tidak memotong pembicaraan guru."),
            ("24", "Jelaskan perbedaan antara salat sunah rawatib qabliyah dan rawatib ba'diyah serta berikan contohnya!", "Salat rawatib qabliyah dilakukan SEBELUM salat fardu (contoh: 2 rakaat sebelum Zuhur), sedangkan rawatib ba'diyah dilakukan SETELAH salat fardu (contoh: 2 rakaat sesudah Magrib)."),
            ("25", "Bagaimanakah sikap kepatuhan Nabi Ismail a.s. saat ayahnya Nabi Ibrahim a.s. menyampaikan perintah kurban?", "Nabi Ismail a.s. menerimanya dengan ikhlas dan sabar tanpa ragu sedikit pun karena meyakini bahwa perintah tersebut merupakan wahyu suci dari Allah Swt.")
        ]
    },
    {
        "grade": 4,
        "fase": "Fase B",
        "title": "Naskah Soal SAS & Kisi-Kisi PAI Kelas 4 SD",
        "badge": "Fase B • Kelas 4 SD • Semester 1",
        "bab_list": [
            ("Bab 1: Surah Al-Hujurat Ayat 13", "Al-Qur'an Hadis", "Membaca dengan kaidah tajwid (mad thabi'i & gunnah), memahami pesan keberagaman suku dan bangsa.", "L1 (C1/C2)", "PG (1, 2, 3), Isian (16), Uraian (21)"),
            ("Bab 2: Asmaul Husna Al-Malik, Al-Aziz, Al-Quddus", "Akidah Islamiyah", "Menjelaskan makna Maharaja, Mahamulia, dan Mahasuci serta mengamalkan integritas dan kesucian hati.", "L2 (C3)", "PG (4, 5, 6), Isian (17), Uraian (22)"),
            ("Bab 3: Menyambut Usia Baligh", "Fikih Ibadah", "Mengidentifikasi tanda-tanda baligh menurut ilmu biologi dan fikih, serta kewajiban mandi wajib (hadas besar).", "L2 (C3)", "PG (7, 8, 9), Isian (18), Uraian (23)"),
            ("Bab 4: Salat Berjamaah & Salat Id", "Fikih Ibadah", "Menjelaskan syarat sah imam, makmum masbuq, keutamaan salat berjamaah 27 derajat, dan tata cara salat Id.", "L2 (C3)", "PG (10, 11, 12), Isian (19), Uraian (24)"),
            ("Bab 5: Kisah Hijrah Rasulullah ke Madinah", "Sejarah Peradaban", "Menganalisis sebab musabab hijrah, keteladanan Abu Bakar di Gua Tsur, dan pembangunan Masjid Quba.", "L3 (C4 HOTS)", "PG (13-15), Isian (20), Uraian (25)")
        ],
        "pg_items": [
            ("1", "Tujuan Allah Swt. menciptakan manusia bersuku-suku dan berbangsa-bangsa menurut Surah Al-Hujurat: 13 adalah agar ...", "A. Saling bersaing menguasai harta &nbsp;&nbsp;&nbsp; B. Saling mengenal dan menghargai (lita'arafu) &nbsp;&nbsp;&nbsp; C. Membanggakan garis keturunan", "B"),
            ("2", "Orang yang paling mulia di sisi Allah Swt. adalah orang yang paling ...", "A. Kaya hartanya &nbsp;&nbsp;&nbsp; B. Tinggi jabatannya &nbsp;&nbsp;&nbsp; C. Bertakwa kepada Allah", "C"),
            ("3", "Hukum bacaan nun sukun bertemu huruf 'Kaf' (ك) dalam kaidah tajwid dinamakan ...", "A. Ikhfa Hakiki &nbsp;&nbsp;&nbsp; B. Izhar Halqi &nbsp;&nbsp;&nbsp; C. Idgham Bighunnah", "A"),
            ("4", "Asmaul Husna 'Al-Malik' (المَلِكُ) mengandung pengertian bahwa Allah Swt. adalah ...", "A. Maharaja Pemilik Semesta &nbsp;&nbsp;&nbsp; B. Maha Pengampun &nbsp;&nbsp;&nbsp; C. Maha Kuat", "A"),
            ("5", "Sikap meneladani Asmaul Husna 'Al-Quddus' (Mahasuci) dalam kehidupan pelajar dapat diwujudkan dengan ...", "A. Menjaga hati dari rasa iri dengki &nbsp;&nbsp;&nbsp; B. Suka memamerkan kepintaran &nbsp;&nbsp;&nbsp; C. Menghindari kerja kelompok", "A"),
            ("6", "Asmaul Husna 'Al-Aziz' memberikan pelajaran bahwa kemuliaan sejati manusia berasal dari ...", "A. Ketaatan kepada syariat Allah &nbsp;&nbsp;&nbsp; B. Jumlah teman di media sosial &nbsp;&nbsp;&nbsp; C. Pakaian mewah", "A"),
            ("7", "Salah satu tanda usia baligh bagi seorang anak laki-laki menurut pandangan fikih Islam adalah ...", "A. Suara menjadi lebih lembut &nbsp;&nbsp;&nbsp; B. Mengalami mimpi basah (ihtilam) &nbsp;&nbsp;&nbsp; C. Bertambah tinggi badan", "B"),
            ("8", "Setelah seorang muslim memasuki usia baligh, seluruh perbuatan ibadah dan dosanya dicatat oleh malaikat, status ini disebut ...", "A. Mukallaf &nbsp;&nbsp;&nbsp; B. Mumayyiz &nbsp;&nbsp;&nbsp; C. Musafir", "A"),
            ("9", "Untuk menyucikan diri dari hadas besar seperti setelah selesai haid atau mimpi basah, maka wajib melakukan ...", "A. Cukup berwudhu biasa &nbsp;&nbsp;&nbsp; B. Mandi wajib (ghusl) &nbsp;&nbsp;&nbsp; C. Cuci tangan tiga kali", "B"),
            ("10", "Pahala mendirikan salat secara berjamaah dilipatgandakan oleh Allah Swt. sebanyak ... derajat dibandingkan salat sendirian.", "A. 10 &nbsp;&nbsp;&nbsp; B. 17 &nbsp;&nbsp;&nbsp; C. 27", "C"),
            ("11", "Makmum yang terlambat datang saat imam sudah memulai gerakan salat dinamakan makmum ...", "A. Muwafiq &nbsp;&nbsp;&nbsp; B. Masbuq &nbsp;&nbsp;&nbsp; C. Munfarid", "B"),
            ("12", "Salat hari raya Idulfitri dan Iduladha hukum pelaksanaannya adalah sunah ...", "A. Mu'akkad &nbsp;&nbsp;&nbsp; B. Gairu Mu'akkad &nbsp;&nbsp;&nbsp; C. Fardu Kifayah", "A"),
            ("13", "Sebab utama yang mendorong Nabi Muhammad saw. dan para sahabat melakukan hijrah ke Yatsrib (Madinah) adalah ...", "A. Keinginan berdagang rempah &nbsp;&nbsp;&nbsp; B. Tekanan dan boikot kejam kaum kafir Quraisy serta perintah Allah &nbsp;&nbsp;&nbsp; C. Udara Madinah lebih sejuk", "B"),
            ("14", "Sahabat setia yang menemani Rasulullah saw. bersembunyi di dalam Gua Tsur selama tiga hari adalah ...", "A. Ali bin Abi Thalib &nbsp;&nbsp;&nbsp; B. Abu Bakar As-Siddiq &nbsp;&nbsp;&nbsp; C. Umar bin Khattab", "B"),
            ("15", "Masjid pertama yang dibangun oleh Rasulullah saw. dalam rangkaian perjalanan hijrah menuju Madinah adalah Masjid ...", "A. Nabawi &nbsp;&nbsp;&nbsp; B. Quba &nbsp;&nbsp;&nbsp; C. Qiblatain", "B")
        ],
        "isian_items": [
            ("16", "Lafal 'Inna akramakum 'indallahi atqaakum' dalam surah Al-Hujurat ayat 13 menegaskan bahwa ukuran kemuliaan adalah ...", "Ketakwaan"),
            ("17", "Asmaul Husna 'Al-Aziz' (العَزِيزُ) memiliki makna bahwa Allah Swt. Maha ...", "Mulia / Perkasa tanpa tandingan"),
            ("18", "Tanda baligh yang dialami secara khusus oleh anak perempuan menurut ilmu medis dan fikih adalah datangnya ...", "Haid (Menstruasi)"),
            ("19", "Pada rakaat pertama salat Idulfitri, setelah membaca doa iftitah disunahkan melakukan takbir tambahan sebanyak ... kali.", "7 (Tujuh)"),
            ("20", "Pemuda pemberani yang rela tidur di ranjang Nabi Muhammad saw. untuk mengelabui kepungan algojo kafir Quraisy adalah sahabat ...", "Ali bin Abi Thalib r.a.")
        ],
        "uraian_items": [
            ("21", "Jelaskan pesan toleransi dan keberagaman yang diperintahkan Allah Swt. dalam Surah Al-Hujurat ayat 13!", "Allah Swt. menciptakan manusia dengan keragaman suku, ras, dan bangsa bukan untuk saling merendahkan atau bermusuhan, melainkan untuk saling mengenal (ta'aruf), bekerja sama, dan membangun persaudaraan."),
            ("22", "Bagaimanakah penerapan sifat Asmaul Husna Al-Malik dalam memimpin kelompok belajar di kelas?", "Menjadi pemimpin yang adil, tidak bersikap sewenang-wenang kepada teman, mendengarkan pendapat anggota, dan mengutamakan kepentingan bersama."),
            ("23", "Sebutkan 3 konsekuensi atau tanggung jawab syariat yang mulai dibebankan kepada seorang anak yang telah baligh (mukallaf)!", "1) Wajib menjalankan salat lima waktu; 2) Wajib menjalankan ibadah puasa Ramadan; 3) Bertanggung jawab penuh atas dosa dan pahala setiap perbuatannya."),
            ("24", "Jelaskan tata cara yang benar bagi seorang makmum masbuq apabila mendapati imam sedang melakukan rukuk!", "Makmum segera berniat, bertakbiratul ihram sambil berdiri tegak, lalu langsung membungkuk rukuk mengikuti imam. Jika sempat rukuk thuma'ninah bersama imam, ia dihitung telah mendapatkan satu rakaat itu."),
            ("25", "Analisis faktor yang menyebabkan kaum Yatsrib (kaum Anshar) menyambut gembira kedatangan Rasulullah saw. dan kaum Muhajirin!", "Kaum Anshar telah mendengar berita kenabian, merindukan juru damai atas konflik panjang antarsuku Aus dan Khazraj, serta memiliki ketulusan iman untuk membela agama Islam bersama Rasulullah.")
        ]
    },
    {
        "grade": 5,
        "fase": "Fase C",
        "title": "Naskah Soal SAS & Kisi-Kisi PAI Kelas 5 SD",
        "badge": "Fase C • Kelas 5 SD • Semester 1",
        "bab_list": [
            ("Bab 1: Surah Al-Ma'un & Nilai Kemanusiaan", "Al-Qur'an Hadis", "Membaca tartil, mengartikan lafal, memahami ciri pendusta agama (lalai salat, riya, enggan menolong anak yatim).", "L1 (C1/C2)", "PG (1, 2, 3), Isian (16), Uraian (21)"),
            ("Bab 2: Asmaul Husna Al-Qawiyyu & Al-Qayyum", "Akidah Islamiyah", "Menganalisis kemandirian dan kekuatan mutlak Allah Swt., serta meneladani sikap pantang bergantung kepada orang lain.", "L2 (C3)", "PG (4, 5, 6), Isian (17), Uraian (22)"),
            ("Bab 3: Adab Menghargai Perbedaan & Berteman", "Akhlak Terpuji", "Menunjukkan sikap tasamuh (toleransi), menjauhi perundungan (bullying), dan menjaga ukhuwah islamiyah.", "L2 (C3)", "PG (7, 8, 9), Isian (18), Uraian (23)"),
            ("Bab 4: Ibadah Zakat, Infak, dan Sedekah", "Fikih Ibadah", "Membedakan hukum zakat fitrah, zakat mal, 8 golongan asnaf mustahik, serta fungsi sosial pembersihan harta.", "L2 (C3)", "PG (10, 11, 12), Isian (19), Uraian (24)"),
            ("Bab 5: Peristiwa Bersejarah Fathu Makkah", "Sejarah Peradaban", "Menjelaskan sebab pelanggaran Perjanjian Hudaibiyah, penaklukan damai Kota Makkah, pembersihan berhala di Ka'bah.", "L3 (C4 HOTS)", "PG (13-15), Isian (20), Uraian (25)")
        ],
        "pg_items": [
            ("1", "Menurut Surah Al-Ma'un, salah satu ciri orang yang mendustakan agama adalah orang yang ...", "A. Memakan harta anak yatim dan menghardiknya &nbsp;&nbsp;&nbsp; B. Memberi sedekah secara sembunyi &nbsp;&nbsp;&nbsp; C. Menunaikan zakat tepat waktu", "A"),
            ("2", "Lafal 'Al-Laziina hum 'an shalaatihim saahuun' dalam Surah Al-Ma'un mengecam orang yang ...", "A. Suka berpuasa sunah &nbsp;&nbsp;&nbsp; B. Lalai dalam mengerjakan salatnya &nbsp;&nbsp;&nbsp; C. Membaca Al-Qur'an tiap malam", "B"),
            ("3", "Perilaku gemar memamerkan amal kebaikan kepada orang lain agar mendapat pujian disebut sifat ...", "A. Sum'ah &nbsp;&nbsp;&nbsp; B. Riya &nbsp;&nbsp;&nbsp; C. Nifak", "B"),
            ("4", "Asmaul Husna 'Al-Qawiyyu' (القَوِيُّ) memiliki makna bahwa Allah Swt. Maha ...", "A. Mengetahui hal gaib &nbsp;&nbsp;&nbsp; B. Memiliki Kekuatan yang Maha Perkasa &nbsp;&nbsp;&nbsp; C. Mengampuni dosa", "B"),
            ("5", "Allah Swt. mengatur seluruh alam semesta secara mandiri tanpa memerlukan bantuan siapapun, hal ini sesuai Asmaul Husna ...", "A. Al-Qayyum (القَيُّومُ) &nbsp;&nbsp;&nbsp; B. Al-Khabir &nbsp;&nbsp;&nbsp; C. Al-Batin", "A"),
            ("6", "Salah satu wujud meneladani sifat Al-Qayyum (Maha Mandiri) bagi seorang murid di rumah adalah ...", "A. Mempersiapkan perlengkapan sekolah sendiri tanpa bergantung pada orang tua &nbsp;&nbsp;&nbsp; B. Menyuruh adik mengerjakan PR kita &nbsp;&nbsp;&nbsp; C. Menunda merapikan kamar tidur", "A"),
            ("7", "Sikap saling menghormati dan menghargai keyakinan orang lain tanpa mengorbankan akidah Islam dinamakan ...", "A. Tawakal &nbsp;&nbsp;&nbsp; B. Tasamuh (Toleransi) &nbsp;&nbsp;&nbsp; C. Ta'awun", "B"),
            ("8", "Tindakan mengejek atau mengolok-olok kekurangan fisik teman (bullying) hukumnya haram karena melanggar persaudaraan ...", "A. Ukhuwah &nbsp;&nbsp;&nbsp; B. Muamalah &nbsp;&nbsp;&nbsp; C. Madaniyah", "A"),
            ("9", "Jika teman berbeda agama sedang beribadah di tempat ibadahnya, sikap kita yang benar adalah ...", "A. Mengganggu upacaranya &nbsp;&nbsp;&nbsp; B. Memberikan ketenangan dan tidak membuat keributan &nbsp;&nbsp;&nbsp; C. Ikut serta dalam ritualnya", "B"),
            ("10", "Zakat yang wajib dikeluarkan oleh setiap jiwa muslim menjelang hari raya Idulfitri dinamakan zakat ...", "A. Mal &nbsp;&nbsp;&nbsp; B. Fitrah &nbsp;&nbsp;&nbsp; C. Perniagaan", "B"),
            ("11", "Besaran zakat fitrah berupa makanan pokok (beras) yang wajib dikeluarkan per orang di Indonesia adalah ...", "A. 1,5 kg atau 2 liter &nbsp;&nbsp;&nbsp; B. 2,5 kg atau 3,5 liter &nbsp;&nbsp;&nbsp; C. 5 kg atau 6 liter", "B"),
            ("12", "Golongan mustahik yang berhak menerima zakat menurut Surah At-Taubah ayat 60 berjumlah ... golongan (asnaf).", "A. 6 &nbsp;&nbsp;&nbsp; B. 8 &nbsp;&nbsp;&nbsp; C. 10", "B"),
            ("13", "Sebab utama terjadinya peristiwa Fathu Makkah (Pembebasan Kota Makkah) pada tahun 8 Hijriah adalah ...", "A. Perang Badar &nbsp;&nbsp;&nbsp; B. Pengkhianatan kaum kafir Quraisy terhadap butir Perjanjian Hudaibiyah &nbsp;&nbsp;&nbsp; C. Kelaparan di Madinah", "B"),
            ("14", "Ketika menaklukkan Kota Makkah, Rasulullah saw. menunjukkan akhlak mulia dengan cara ...", "A. Membalas dendam seluruh pembesar Quraisy &nbsp;&nbsp;&nbsp; B. Memberikan amnesti (pengampunan umum) tanpa pertumpahan darah &nbsp;&nbsp;&nbsp; C. Menghancurkan rumah-rumah penduduk", "B"),
            ("15", "Tindakan pertama yang dilakukan Rasulullah saw. setibanya di Masjidil Haram saat Fathu Makkah adalah ...", "A. Membangun menara baru &nbsp;&nbsp;&nbsp; B. Thawaf dan menghancurkan 360 berhala di sekitar Ka'bah &nbsp;&nbsp;&nbsp; C. Mengumpulkan harta rampasan", "B")
        ],
        "isian_items": [
            ("16", "Lafal 'Wa yamna'uunal-maa'uun' dalam Surah Al-Ma'un mengecam orang yang enggan memberikan bantuan ...", "Barang berguna / bermanfaat"),
            ("17", "Asmaul Husna 'Al-Qawiyyu' menegaskan bahwa tidak ada satupun kekuatan di jagat raya yang mampu menandingi kekuatan ...", "Allah Swt."),
            ("18", "Prinsip toleransi beragama dalam Islam ditegaskan dalam Surah Al-Kafirun ayat terakhir: 'Lakum diinukum wa liya...", "Diin (Untukmu agamamu, dan untukkulah agamaku)"),
            ("19", "Orang yang bertugas mengumpulkan, mencatat, dan mendistribusikan zakat kepada yang berhak disebut ...", "Amil zakat"),
            ("20", "Peristiwa penaklukan Kota Makkah yang penuh kedamaian terjadi pada tanggal 20 bulan ... tahun ke-8 Hijriah.", "Ramadan")
        ],
        "uraian_items": [
            ("21", "Uraikan 3 perbuatan terpuji yang mencerminkan kepedulian sosial terhadap anak yatim dan fakir miskin sesuai isi Surah Al-Ma'un!", "1) Menyisihkan sebagian uang saku untuk membantu biaya sekolah anak yatim; 2) Bersikap ramah, mengasihi, dan tidak menghardik mereka; 3) Mengajak mereka makan bersama saat hari raya atau acara keluarga."),
            ("22", "Bagaimanakah keterkaitan antara meneladani Asmaul Husna Al-Qayyum dengan kemandirian belajar siswa kelas 5 SD?", "Siswa yang meneladani Al-Qayyum akan membiasakan diri mandiri: belajar tanpa disuruh, menyiapkan buku pelajaran sendiri, dan berusaha memecahkan masalah pelajaran dengan tekun sebelum meminta bantuan."),
            ("23", "Mengapa perbuatan perundungan (bullying) di sekolah sangat dilarang keras dalam ajaran agama Islam?", "Karena perundungan menyakiti hati dan fisik sesama manusia, merusak kehormatan ciptaan Allah Swt., memicu permusuhan, serta melanggar perintah ukhuwah dan keadilan sosial."),
            ("24", "Jelaskan perbedaan mendasar antara zakat, infak, dan sedekah dari segi hukum dan bentuk pengeluarannya!", "Zakat hukumnya wajib dengan ketentuan nisab, haul, dan kadar tertentu; infak hukumnya sunah/wajib berupa pengeluaran harta benda di jalan Allah tanpa batas waktu; sedangkan sedekah maknanya lebih luas (sunah) mencakup harta maupun non-materi seperti senyuman, tenaga, dan nasihat baik."),
            ("25", "Analisis faktor penyebab Rasulullah saw. memilih jalan damai (tanpa balas dendam) ketika menaklukkan Kota Makkah!", "Rasulullah saw. diutus sebagai rahmat bagi semesta alam (rahmatan lil 'alamin). Beliau ingin menunjukkan keluhuran budi pekerti Islam, meluluhkan hati penduduk Makkah agar masuk Islam secara sukarela, serta menjaga kesucian Kota Makkah dari pertumpahan darah.")
        ]
    },
    {
        "grade": 6,
        "fase": "Fase C",
        "title": "Naskah Soal SAS & Kisi-Kisi PAI Kelas 6 SD",
        "badge": "Fase C • Kelas 6 SD • Semester 1",
        "bab_list": [
            ("Bab 1: Surah Ad-Duha & Kasih Sayang Allah", "Al-Qur'an Hadis", "Membaca tartil, menghafal, menganalisis pesan optimisme, dan larangan bersikap sewenang-wenang terhadap dhuafa.", "L1 (C1/C2)", "PG (1, 2, 3), Isian (16), Uraian (21)"),
            ("Bab 2: Asmaul Husna Al-Ghaffar & Al-Wahid", "Akidah Islamiyah", "Menjelaskan luasnya ampunan Allah Swt. dan keesaan zat serta sifat-Nya dalam membentengi akidah dari syirik.", "L2 (C3)", "PG (4, 5, 6), Isian (17), Uraian (22)"),
            ("Bab 3: Moderasi Beragama & Toleransi Global", "Akhlak Terpuji", "Menerapkan sikap wasathiyah (moderat), menghargai kemajemukan budaya bangsa, dan menjunjung keadilan sosial.", "L2 (C3)", "PG (7, 8, 9), Isian (18), Uraian (23)"),
            ("Bab 4: Ketentuan Makanan & Minuman Halal Haram", "Fikih Ibadah", "Mengklasifikasikan jenis makanan halal/haram secara zat dan cara perolehannya, serta dampak konsumsi bagi kesehatan jasmani & rohani.", "L2 (C3)", "PG (10, 11, 12), Isian (19), Uraian (24)"),
            ("Bab 5: Masa Keemasan Khulafaur Rasyidin", "Sejarah Peradaban", "Menganalisis strategi Abu Bakar (kodifikasi Al-Qur'an), Umar bin Khattab (administrasi negara), Utsman bin Affan (Mushaf Utsmani), Ali bin Abi Thalib (stabilitas ilmu).", "L3 (C4 HOTS)", "PG (13-15), Isian (20), Uraian (25)")
        ],
        "pg_items": [
            ("1", "Surah Ad-Duha diturunkan oleh Allah Swt. untuk menghibur hati Rasulullah saw. dari tuduhan kaum musyrik bahwa Allah telah ...", "A. Mengangkat nabi lain &nbsp;&nbsp;&nbsp; B. Meninggalkan dan membenci beliau &nbsp;&nbsp;&nbsp; C. Menolak wahyu", "B"),
            ("2", "Lafal 'Fa ammal-yatiima falaa taqhar' dalam Surah Ad-Duha mengajarkan larangan ...", "A. Meminta-minta harta &nbsp;&nbsp;&nbsp; B. Bersikap sewenang-wenang terhadap anak yatim &nbsp;&nbsp;&nbsp; C. Berputus asa", "B"),
            ("3", "Ayat terakhir Surah Ad-Duha 'Wa ammaa bi ni'mati rabbika fa haddits' memerintahkan kita untuk ...", "A. Menyembunyikan nikmat &nbsp;&nbsp;&nbsp; B. Mensyukuri dan menyebut-nyebut nikmat Allah &nbsp;&nbsp;&nbsp; C. Menghitung uang", "B"),
            ("4", "Asmaul Husna 'Al-Ghaffar' (الغَفَّارُ) memiliki makna bahwa Allah Swt. Maha ...", "A. Pengampun dosa berulang kali bagi hamba-Nya yang bertobat &nbsp;&nbsp;&nbsp; B. Pemberi hukuman &nbsp;&nbsp;&nbsp; C. Pencipta", "A"),
            ("5", "Meyakini Asmaul Husna 'Al-Wahid' (الوَاحِدُ) berarti menolak segala bentuk perbuatan menyekutukan Allah, yang dinamakan perbuatan ...", "A. Riya &nbsp;&nbsp;&nbsp; B. Syirik &nbsp;&nbsp;&nbsp; C. Nifak", "B"),
            ("6", "Salah satu bentuk pengamalan meneladani sifat Al-Ghaffar dalam hubungan sosial adalah ...", "A. Menyimpan dendam kepada orang yang bersalah &nbsp;&nbsp;&nbsp; B. Menjadi pribadi yang pemaaf dan mudah melupakan kesalahan teman &nbsp;&nbsp;&nbsp; C. Membalas perbuatan buruk", "B"),
            ("7", "Sikap keberagamaan yang berada di jalan tengah, tidak ekstrem kanan maupun ekstrem kiri dinamakan sikap ...", "A. Radikal &nbsp;&nbsp;&nbsp; B. Wasathiyah (Moderat) &nbsp;&nbsp;&nbsp; C. Apatis", "B"),
            ("8", "Semboyan bangsa Indonesia yang sejalan dengan prinsip toleransi dan persatuan dalam Islam adalah ...", "A. Tut Wuri Handayani &nbsp;&nbsp;&nbsp; B. Bhinneka Tunggal Ika &nbsp;&nbsp;&nbsp; C. Ing Ngarso Sung Tulodo", "B"),
            ("9", "Jika tetangga kita yang non-muslim tertimpa bencana kebakaran rumah, sikap kita sesuai akhlak kemanusiaan adalah ...", "A. Mengabaikannya karena beda agama &nbsp;&nbsp;&nbsp; B. Bergotong royong memberikan bantuan sandang, pangan, dan tempat bernaung &nbsp;&nbsp;&nbsp; C. Menunggu pihak yayasan saja", "B"),
            ("10", "Makanan yang halal secara zatnya (halal li-dzaatihi) adalah makanan yang ...", "A. Hasil curian dari toko &nbsp;&nbsp;&nbsp; B. Bukan bangkai, darah mengalir, atau daging babi menurut syariat &nbsp;&nbsp;&nbsp; C. Harganya mahal", "B"),
            ("11", "Dua jenis bangkai binatang yang dihalalkan bagi umat Islam untuk dikonsumsi menurut hadis sahih adalah ...", "A. Ikan dan Belalang &nbsp;&nbsp;&nbsp; B. Ayam dan Bebek &nbsp;&nbsp;&nbsp; C. Kambing dan Sapi", "A"),
            ("12", "Binatang darat yang disembelih tanpa menyebut nama Allah Swt. hukum dagingnya berubah menjadi ...", "A. Halal &nbsp;&nbsp;&nbsp; B. Haram &nbsp;&nbsp;&nbsp; C. Makruh", "B"),
            ("13", "Khalifah pertama yang memprakarsai proyek pengumpulan mushaf Al-Qur'an atas usulan Umar bin Khattab adalah ...", "A. Abu Bakar As-Siddiq r.a. &nbsp;&nbsp;&nbsp; B. Utsman bin Affan r.a. &nbsp;&nbsp;&nbsp; C. Ali bin Abi Thalib r.a.", "A"),
            ("14", "Khalifah yang berjasa menyeragamkan bacaan dan penulisan Al-Qur'an menjadi satu mushaf induk (Mushaf Al-Imam) adalah ...", "A. Umar bin Khattab r.a. &nbsp;&nbsp;&nbsp; B. Utsman bin Affan r.a. &nbsp;&nbsp;&nbsp; C. Ali bin Abi Thalib r.a.", "B"),
            ("15", "Gelar 'Babul 'Ilmi' (Gerbangnya Ilmu Pengetahuan) diberikan oleh Rasulullah saw. kepada sahabat mulia ...", "A. Bilal bin Rabah &nbsp;&nbsp;&nbsp; B. Ali bin Abi Thalib r.a. &nbsp;&nbsp;&nbsp; C. Khalid bin Walid", "B")
        ],
        "isian_items": [
            ("16", "Lafal 'Wa la-saufa yu'thiika rabbuka fa tardhaa' dalam Surah Ad-Duha memberikan janji karunia dan ... dari Allah kepada Nabi.", "Keridhaan / Kebahagiaan abadi"),
            ("17", "Asmaul Husna 'Al-Wahid' bermakna bahwa Allah Swt. Maha ... dalam zat, sifat, maupun perbuatan-Nya.", "Tunggal / Esa"),
            ("18", "Sikap menghargai perbedaan budaya, pendapat, dan keyakinan dalam pergaulan masyarakat majemuk dinamakan ...", "Tasamuh (Toleransi)"),
            ("19", "Daging hewan ternak yang halal dimakan menjadi haram apabila disembelih diperuntukkan sebagai sesajen kepada ...", "Berhala / Selain Allah"),
            ("20", "Lembaga perbendaharaan negara Islam yang didirikan secara resmi pada masa kekhalifahan Umar bin Khattab bernama ...", "Baitul Mal")
        ],
        "uraian_items": [
            ("21", "Uraikan 3 nilai kepedulian terhadap kaum lemah yang diwajibkan dalam Surah Ad-Duha ayat 9-11!", "1) Tidak berlaku sewenang-wenang terhadap anak yatim; 2) Tidak menghardik atau mencela orang miskin yang meminta pertolongan; 3) Selalu mensyukuri dan membagikan kebaikan nikmat yang telah dianugerahkan Allah."),
            ("22", "Jelaskan bagaimana meneladani Asmaul Husna Al-Wahid dalam menjaga kemurnian tauhid di tengah kemajuan era digital!", "Dengan memegang teguh keyakinan bahwa Allah Swt. adalah satu-satunya tempat memohon dan bersandar, serta menjauhi segala ramalan zodiak, perdukunan digital, atau konten yang merusak akidah."),
            ("23", "Bagaimanakah sikap seorang muslim yang moderat (wasathiyah) dalam menyikapi keragaman budaya dan agama di Indonesia?", "Menghormati hak-hak pemeluk agama lain dalam beribadah, menjalin kerja sama sosial kemanusiaan, menjauhi sikap ekstrem atau fanatik buta, serta mengedepankan musyawarah demi menjaga keutuhan NKRI."),
            ("24", "Jelaskan perbedaan antara halal li-dzaatihi (halal zatnya) dan halal li-ghairihi (halal cara memperolehnya) dengan contoh konkret!", "Halal li-dzaatihi berarti zat bendanya memang suci menurut nas (contoh: beras, susu sapi, sayur); sedangkan halal li-ghairihi berarti cara memperolehnya harus sah dan diridhai (bukan hasil menipu, riba, atau korupsi)."),
            ("25", "Analisis kontribusi strategis Khalifah Abu Bakar As-Siddiq r.a. dan Umar bin Khattab r.a. dalam menjaga kelestarian Al-Qur'an pasca Perang Yamamah!", "Banyak penghafal Al-Qur'an yang gugur di Yamamah, sehingga Umar mengusulkan pengumpulan lembaran wahyu, lalu Abu Bakar menunjuk Zaid bin Tsabit memimpin kodifikasi mushaf resmi. Langkah ini menyelamatkan Al-Qur'an dari kepunahan dan menjadi dasar mushaf umat Islam hingga hari ini.")
        ]
    }
]

def make_page_header(title, badge):
    return f"""<div class="page-header"><span>PENILAIAN SUMATIF AKHIR SEMESTER (SAS)</span><span>{badge.upper()}</span></div>"""

def make_page_footer(grade, page_num):
    return f"""<div class="page-footer"><span>Naskah Ujian SAS PAI Kelas {grade} SD • Dokumen Terintegrasi Kisi-Kisi</span><span>Halaman {page_num} dari 5</span></div>"""

def generate_page_1(d):
    g = d["grade"]
    pg1 = d["pg_items"][:7]
    items_html = ""
    for no, q, opt, ans in pg1:
        items_html += f"""
    <div style="margin-bottom: 6px;">
      <strong>{no}.</strong> {q}<br>
      <div style="padding-left: 14px; margin-top: 2px; color: #334155;">{opt}</div>
    </div>"""

    return f"""<div class="page">
{make_page_header(d['title'], d['badge'])}

<!-- KOP RESMI LEMBAGA PENYELENGGARA (TEMPLATE KOSONG SIAP EDIT) -->
<div style="border-bottom: 2px solid #0f172a; padding-bottom: 6px; margin-bottom: 8px; text-align: center;">
  <div style="font-size: 8pt; font-weight: 700; text-transform: uppercase; color: #475569;">PEMERINTAH KABUPATEN / KOTA ........................................................ &bull; DINAS PENDIDIKAN</div>
  <div style="font-size: 10pt; font-weight: 800; text-transform: uppercase; color: #1e293b; margin-top: 2px;">SD / MI ............................................................................................................</div>
  <h2 style="font-family: 'Fredoka', sans-serif; font-size: 13pt; font-weight: 900; color: #047857; margin-top: 2px;">SUMATIF AKHIR SEMESTER (SAS) GANJIL — TAHUN AJARAN 2026/2027</h2>
  <div style="font-size: 8pt; font-weight: 600; color: #64748b;">Mata Pelajaran: PAI & Budi Pekerti • Kurikulum Merdeka (BSKAP No. 020/2026) • Alokasi Waktu: 90 Menit</div>
</div>

<!-- IDENTITAS PESERTA & KOTAK NILAI -->
<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 8px; margin-bottom: 8px;">
  <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 6px 10px; font-size: 8pt;">
    <table style="width: 100%; border-collapse: collapse;">
      <tr><td style="width: 35%; font-weight: 700;">Nama Lengkap</td><td>: .................................................</td></tr>
      <tr><td style="font-weight: 700;">Nomor Peserta</td><td>: ........................ / Kelas: {g} SD</td></tr>
      <tr><td style="font-weight: 700;">Hari / Tanggal</td><td>: .................................................</td></tr>
    </table>
  </div>
  <div style="background: #f0fdf4; border: 1px solid #86efac; border-radius: 6px; padding: 6px 10px; text-align: center;">
    <span style="font-size: 7.5pt; font-weight: 700; text-transform: uppercase; color: #166534; display: block;">Nilai / Paraf Guru</span>
    <div style="font-size: 16pt; font-weight: 900; color: #047857; height: 26px; line-height: 26px;">...... / ......</div>
  </div>
</div>

<div style="background: #fffbeb; border-left: 3px solid #f59e0b; padding: 4px 8px; font-size: 7.5pt; color: #78350f; margin-bottom: 8px;">
  <strong>PETUNJUK UMUM:</strong> 1. Berdoalah sebelum mengerjakan soal. 2. Tuliskan nama dan nomor peserta dengan teliti. 3. Dahulukan soal yang kamu anggap mudah. 4. Periksa kembali seluruh jawaban sebelum diserahkan.
</div>

<!-- BAGIAN A: SOAL PILIHAN GANDA (1-7) -->
<div style="margin-bottom: 4px;">
  <div style="background: #0f172a; color: white; padding: 3px 8px; border-radius: 4px; font-size: 8pt; font-weight: 800; display: inline-block; margin-bottom: 6px;">
    BAGIAN A: PILIHAN GANDA (Berilah tanda silang (X) pada huruf A, B, atau C!)
  </div>
  <div style="font-size: 8.5pt; line-height: 1.42; color: #1e293b;">
{items_html}
  </div>
</div>

{make_page_footer(g, 1)}
</div>"""

def generate_page_2(d):
    g = d["grade"]
    pg2 = d["pg_items"][7:15]
    pg_html = ""
    for no, q, opt, ans in pg2:
        pg_html += f"""
    <div style="margin-bottom: 6px;">
      <strong>{no}.</strong> {q}<br>
      <div style="padding-left: 14px; margin-top: 2px; color: #334155;">{opt}</div>
    </div>"""

    isian_html = ""
    for no, q, ans in d["isian_items"]:
        isian_html += f"""
    <div style="margin-bottom: 6px;">
      <strong>{no}.</strong> {q}<br>
      <div style="padding-left: 14px; color: #64748b; font-style: italic; font-size: 8pt;">Jawaban: .................................................................................................................</div>
    </div>"""

    return f"""<div class="page">
{make_page_header(d['title'], d['badge'])}

<!-- LANJUTAN BAGIAN A -->
<div style="margin-bottom: 8px;">
  <div style="background: #334155; color: white; padding: 3px 8px; border-radius: 4px; font-size: 8pt; font-weight: 800; display: inline-block; margin-bottom: 6px;">
    LANJUTAN BAGIAN A: PILIHAN GANDA (Nomor 8 – 15)
  </div>
  <div style="font-size: 8.5pt; line-height: 1.42; color: #1e293b;">
{pg_html}
  </div>
</div>

<!-- BAGIAN B: ISIAN SINGKAT -->
<div style="margin-top: 6px;">
  <div style="background: #047857; color: white; padding: 3px 8px; border-radius: 4px; font-size: 8pt; font-weight: 800; display: inline-block; margin-bottom: 6px;">
    BAGIAN B: ISIAN SINGKAT (Isilah titik-titik di bawah ini dengan jawaban tepat!)
  </div>
  <div style="font-size: 8.5pt; line-height: 1.45; color: #1e293b;">
{isian_html}
  </div>
</div>

{make_page_footer(g, 2)}
</div>"""

def generate_page_3(d):
    g = d["grade"]
    uraian_html = ""
    for no, q, ans in d["uraian_items"]:
        uraian_html += f"""
    <div style="margin-bottom: 6px;">
      <strong>{no}.</strong> {q}<br>
      <div style="padding-left: 14px; color: #64748b; font-style: italic; font-size: 8pt; margin-top: 2px;">
        Jawab: ....................................................................................................................................................
      </div>
    </div>"""

    # Kunci Jawaban Table
    pg_keys = ", ".join([f"<strong>{no}</strong>:{ans}" for no, q, opt, ans in d["pg_items"]])
    isian_keys = "; ".join([f"<strong>{no}</strong>: {ans}" for no, q, ans in d["isian_items"]])

    return f"""<div class="page">
{make_page_header(d['title'], d['badge'])}

<!-- BAGIAN C: URAIAN HOTS -->
<div style="margin-bottom: 8px;">
  <div style="background: #b45309; color: white; padding: 3px 8px; border-radius: 4px; font-size: 8pt; font-weight: 800; display: inline-block; margin-bottom: 6px;">
    BAGIAN C: URAIAN PENALARAN &amp; HOTS (Jawablah pertanyaan berikut secara jelas!)
  </div>
  <div style="font-size: 8.5pt; line-height: 1.45; color: #1e293b;">
{uraian_html}
  </div>
</div>

<!-- KUNCI JAWABAN LENGKAP RESMI -->
<div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 8px 10px; margin-top: 6px;">
  <div style="font-size: 8.5pt; font-weight: 800; color: #0f172a; margin-bottom: 4px; display: flex; align-items: center; justify-content: space-between;">
    <span>🔑 KUNCI JAWABAN RESMI 25 BUTIR SOAL</span>
    <span style="font-size: 7.5pt; color: #047857; font-weight: 700;">KURIKULUM MERDEKA</span>
  </div>
  <div style="font-size: 7.8pt; line-height: 1.5; color: #1e293b;">
    <div style="margin-bottom: 3px; background: #ffffff; padding: 4px 6px; border-radius: 4px; border: 1px solid #e2e8f0;">
      <span style="font-weight: 700; color: #0f172a;">Kunci PG (1-15):</span> {pg_keys}
    </div>
    <div style="margin-bottom: 3px; background: #ffffff; padding: 4px 6px; border-radius: 4px; border: 1px solid #e2e8f0;">
      <span style="font-weight: 700; color: #047857;">Kunci Isian (16-20):</span> {isian_keys}
    </div>
  </div>
</div>

<!-- RUBRIK & PEDOMAN PENSKORAN -->
<div style="margin-top: 6px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 6px 8px;">
  <div style="font-size: 8pt; font-weight: 800; color: #334155; margin-bottom: 4px;">📊 PEDOMAN PENSKORAN &amp; BOBOT NILAI (SKOR MAKSIMAL = 100)</div>
  <table style="width: 100%; font-size: 7.5pt; border-collapse: collapse; text-align: center;">
    <tr style="background: #f1f5f9; font-weight: 700;">
      <th style="padding: 3px 6px; border: 1px solid #cbd5e1;">Bentuk Soal</th>
      <th style="padding: 3px 6px; border: 1px solid #cbd5e1;">Jumlah Butir</th>
      <th style="padding: 3px 6px; border: 1px solid #cbd5e1;">Bobot per Butir</th>
      <th style="padding: 3px 6px; border: 1px solid #cbd5e1;">Skor Maksimal</th>
      <th style="padding: 3px 6px; border: 1px solid #cbd5e1;">Kontribusi Nilai</th>
    </tr>
    <tr>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1; font-weight: 600; text-align: left;">Pilihan Ganda (PG)</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">15 Butir</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">1 Poin</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">15 Poin</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">40% (x 2.67)</td>
    </tr>
    <tr>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1; font-weight: 600; text-align: left;">Isian Singkat</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">5 Butir</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">2 Poin</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">10 Poin</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">30% (x 3.00)</td>
    </tr>
    <tr>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1; font-weight: 600; text-align: left;">Uraian Penalaran (HOTS)</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">5 Butir</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">3 Poin</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">15 Poin</td>
      <td style="padding: 3px 6px; border: 1px solid #cbd5e1;">30% (x 2.00)</td>
    </tr>
    <tr style="font-weight: 800; background: #ecfdf5; color: #047857;">
      <td colspan="3" style="padding: 4px 6px; border: 1px solid #cbd5e1; text-align: right;">TOTAL NILAI AKHIR:</td>
      <td style="padding: 4px 6px; border: 1px solid #cbd5e1;">40 Poin</td>
      <td style="padding: 4px 6px; border: 1px solid #cbd5e1;">100 POIN SEMPURNA</td>
    </tr>
  </table>
</div>

{make_page_footer(g, 3)}
</div>"""

def generate_page_4(d):
    g = d["grade"]
    babs = d["bab_list"][:3] # Bab 1 - 3
    rows_html = ""
    for idx, (bab, elemen, ind, cog, bentuk) in enumerate(babs, start=1):
        bg = "#f8fafc" if idx % 2 == 0 else "#ffffff"
        cog_badge = ""
        if "L1" in cog:
            cog_badge = f'<span style="background: #dbeafe; color: #1e40af; font-weight: 700; padding: 2px 4px; border-radius: 4px; font-size: 7.2pt;">{cog}</span>'
        elif "L2" in cog:
            cog_badge = f'<span style="background: #fef3c7; color: #92400e; font-weight: 700; padding: 2px 4px; border-radius: 4px; font-size: 7.2pt;">{cog}</span>'
        else:
            cog_badge = f'<span style="background: #fee2e2; color: #991b1b; font-weight: 700; padding: 2px 4px; border-radius: 4px; font-size: 7.2pt;">{cog}</span>'

        rows_html += f"""
      <tr style="border-bottom: 1px solid #e2e8f0; background: {bg};">
        <td style="padding: 6px; text-align: center; font-weight: 700;">{idx}</td>
        <td style="padding: 6px; font-weight: 700; color: #0f172a;">{elemen}<div style="font-size: 7.2pt; color: #64748b; font-weight: 500;">{bab}</div></td>
        <td style="padding: 6px; line-height: 1.35; color: #334155;">{ind}</td>
        <td style="padding: 6px; text-align: center;">{cog_badge}</td>
        <td style="padding: 6px; font-weight: 600; color: #047857; text-align: center;">{bentuk}</td>
      </tr>"""

    return f"""<div class="page">
<div class="page-header"><span>MATRIKS KISI-KISI RESMI PENULISAN SOAL SAS</span><span>KURIKULUM MERDEKA CP NO. 020/2026</span></div>

<div style="border-bottom: 2px solid #047857; padding-bottom: 6px; margin-bottom: 10px; display: flex; align-items: center; justify-content: space-between;">
  <div>
    <h2 style="font-family: 'Fredoka', sans-serif; font-size: 13pt; font-weight: 900; color: #047857; margin: 0;">📋 KISI-KISI PENULISAN SOAL SAS SEMESTER I — KELAS {g} SD</h2>
    <div style="font-size: 8pt; color: #475569; margin-top: 2px;">Capaian Pembelajaran (CP) No. 020 Tahun 2026 • Bagian I (Bab 1 s.d. Bab 3)</div>
  </div>
  <div style="background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 6px; padding: 4px 8px; text-align: right; font-size: 7.5pt; color: #065f46;">
    <strong>Jenjang:</strong> SD/MI • <strong>Alokasi:</strong> 90 Menit<br>
    <strong>Bentuk:</strong> 15 PG, 5 Isian, 5 Uraian
  </div>
</div>

<div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 8px; overflow: hidden; margin-bottom: 10px;">
  <table style="width: 100%; font-size: 7.8pt; border-collapse: collapse; text-align: left;">
    <thead style="background: #0f172a; color: #ffffff;">
      <tr>
        <th style="padding: 6px; width: 5%; text-align: center;">No.</th>
        <th style="padding: 6px; width: 22%;">Elemen &amp; Materi Pokok</th>
        <th style="padding: 6px; width: 43%;">Indikator Soal Ketercapaian Pembelajaran</th>
        <th style="padding: 6px; width: 14%; text-align: center;">Level Kognitif</th>
        <th style="padding: 6px; width: 16%; text-align: center;">Bentuk &amp; No. Soal</th>
      </tr>
    </thead>
    <tbody>
{rows_html}
    </tbody>
  </table>
</div>

<div style="background: #eff6ff; border-left: 3px solid #3b82f6; padding: 6px 10px; border-radius: 4px; font-size: 7.8pt; color: #1e3a8a; line-height: 1.4;">
  <strong>💡 Petunjuk Guru Penguji:</strong> Indikator soal disusun berjenjang mulai dari ingatan/pemahaman (L1) hingga penalaran kritis / analisis kasus (L3 HOTS). Seluruh butir nomor soal yang tertera pada kisi-kisi ini memiliki korespondensi 1-to-1 dengan naskah ujian pada Halaman 1 sampai 3.
</div>

{make_page_footer(g, 4)}
</div>"""

def generate_page_5(d):
    g = d["grade"]
    babs = d["bab_list"][3:] # Bab 4 - 5
    rows_html = ""
    for idx, (bab, elemen, ind, cog, bentuk) in enumerate(babs, start=4):
        bg = "#f8fafc" if idx % 2 == 0 else "#ffffff"
        cog_badge = ""
        if "L1" in cog:
            cog_badge = f'<span style="background: #dbeafe; color: #1e40af; font-weight: 700; padding: 2px 4px; border-radius: 4px; font-size: 7.2pt;">{cog}</span>'
        elif "L2" in cog:
            cog_badge = f'<span style="background: #fef3c7; color: #92400e; font-weight: 700; padding: 2px 4px; border-radius: 4px; font-size: 7.2pt;">{cog}</span>'
        else:
            cog_badge = f'<span style="background: #fee2e2; color: #991b1b; font-weight: 700; padding: 2px 4px; border-radius: 4px; font-size: 7.2pt;">{cog}</span>'

        rows_html += f"""
      <tr style="border-bottom: 1px solid #e2e8f0; background: {bg};">
        <td style="padding: 6px; text-align: center; font-weight: 700;">{idx}</td>
        <td style="padding: 6px; font-weight: 700; color: #0f172a;">{elemen}<div style="font-size: 7.2pt; color: #64748b; font-weight: 500;">{bab}</div></td>
        <td style="padding: 6px; line-height: 1.35; color: #334155;">{ind}</td>
        <td style="padding: 6px; text-align: center;">{cog_badge}</td>
        <td style="padding: 6px; font-weight: 600; color: #047857; text-align: center;">{bentuk}</td>
      </tr>"""

    return f"""<div class="page">
<div class="page-header"><span>MATRIKS KISI-KISI RESMI PENULISAN SOAL SAS</span><span>KURIKULUM MERDEKA CP NO. 020/2026</span></div>

<div style="border-bottom: 2px solid #047857; padding-bottom: 6px; margin-bottom: 10px;">
  <h2 style="font-family: 'Fredoka', sans-serif; font-size: 13pt; font-weight: 900; color: #047857; margin: 0;">📋 KISI-KISI SOAL SAS SEMESTER I — KELAS {g} SD (BAGIAN II)</h2>
  <div style="font-size: 8pt; color: #475569; margin-top: 2px;">Capaian Pembelajaran (CP) No. 020 Tahun 2026 • Lanjutan Bab 4 &amp; 5 serta Rekapitulasi Sebaran Butir</div>
</div>

<div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 8px; overflow: hidden; margin-bottom: 10px;">
  <table style="width: 100%; font-size: 7.8pt; border-collapse: collapse; text-align: left;">
    <thead style="background: #0f172a; color: #ffffff;">
      <tr>
        <th style="padding: 6px; width: 5%; text-align: center;">No.</th>
        <th style="padding: 6px; width: 22%;">Elemen &amp; Materi Pokok</th>
        <th style="padding: 6px; width: 43%;">Indikator Soal Ketercapaian Pembelajaran</th>
        <th style="padding: 6px; width: 14%; text-align: center;">Level Kognitif</th>
        <th style="padding: 6px; width: 16%; text-align: center;">Bentuk &amp; No. Soal</th>
      </tr>
    </thead>
    <tbody>
{rows_html}
    </tbody>
  </table>
</div>

<!-- REKAPITULASI PROPORSI TINGKAT KOGNITIF -->
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 6px 10px; margin-bottom: 10px;">
  <div style="font-size: 8pt; font-weight: 800; color: #1e293b; margin-bottom: 4px;">📈 REKAPITULASI SEBARAN LEVEL KOGNITIF SOAL SAS (25 BUTIR)</div>
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; text-align: center; font-size: 7.8pt;">
    <div style="background: #ffffff; border: 1px solid #dbeafe; padding: 5px; border-radius: 4px;">
      <div style="font-weight: 700; color: #1e40af;">Level 1 (Pengetahuan/C1-C2)</div>
      <div style="font-size: 11pt; font-weight: 900; color: #1d4ed8; margin-top: 2px;">30% (7-8 Butir)</div>
      <div style="color: #64748b; font-size: 7pt;">Menyebutkan, mengenali, mengidentifikasi</div>
    </div>
    <div style="background: #ffffff; border: 1px solid #fef3c7; padding: 5px; border-radius: 4px;">
      <div style="font-weight: 700; color: #92400e;">Level 2 (Aplikasi/C3)</div>
      <div style="font-size: 11pt; font-weight: 900; color: #b45309; margin-top: 2px;">50% (12-13 Butir)</div>
      <div style="color: #64748b; font-size: 7pt;">Menerapkan, meneladani, menghitung</div>
    </div>
    <div style="background: #ffffff; border: 1px solid #fee2e2; padding: 5px; border-radius: 4px;">
      <div style="font-weight: 700; color: #991b1b;">Level 3 (Penalaran/C4 HOTS)</div>
      <div style="font-size: 11pt; font-weight: 900; color: #dc2626; margin-top: 2px;">20% (5 Butir Uraian)</div>
      <div style="color: #64748b; font-size: 7pt;">Menganalisis studi kasus, memecahkan masalah</div>
    </div>
  </div>
</div>

<!-- TANDA TANGAN PENGESAHAN GURU PENGAMPU & KEPALA SEKOLAH (BLANK TEMPLATE) -->
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-size: 8pt; margin-top: 14px; color: #1e293b;">
  <div style="text-align: center;">
    <div>Mengetahui,</div>
    <div style="font-weight: 700;">Kepala Sekolah .................................................</div>
    <div style="height: 48px;"></div>
    <div style="font-weight: 800; text-decoration: underline;">( ............................................................ )</div>
    <div style="font-size: 7.5pt; color: #64748b; margin-top: 2px;">NIP. ............................................................</div>
  </div>
  <div style="text-align: center;">
    <div>......................., ...... ........................ 2026</div>
    <div style="font-weight: 700;">Guru Pengampu PAI &amp; BP</div>
    <div style="height: 48px;"></div>
    <div style="font-weight: 800; text-decoration: underline;">( ............................................................ )</div>
    <div style="font-size: 7.5pt; color: #64748b; margin-top: 2px;">NIP. ............................................................</div>
  </div>
</div>

{make_page_footer(g, 5)}
</div>"""

def main():
    output_dict = {}
    for d in grades_data:
        g = d["grade"]
        page1 = generate_page_1(d)
        page2 = generate_page_2(d)
        page3 = generate_page_3(d)
        page4 = generate_page_4(d)
        page5 = generate_page_5(d)

        output_dict[str(g)] = {
            "grade": g,
            "title": d["title"],
            "badge": d["badge"],
            "totalPages": 5,
            "sampleCount": 5,
            "pages": [page1, page2, page3, page4, page5]
        }

    output_path = "public/data/soal_samples.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_dict, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {len(output_dict)} grades with 5 pages each in {output_path}")

if __name__ == "__main__":
    main()
