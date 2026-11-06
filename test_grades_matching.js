function getSmartChapterImage(title, content, index, usedImages = new Set()) {
  const t = (title || '').toLowerCase();
  const c = (content || '').toLowerCase();

  // Helper to pick candidate if not already used in this book
  function pick(candidates) {
    for (const img of candidates) {
      if (!usedImages.has(img)) {
        usedImages.add(img);
        return img;
      }
    }
    const chosen = candidates[0];
    usedImages.add(chosen);
    return chosen;
  }

  // === PRIORITY 1: MATCH BY SPECIFIC CHAPTER TITLE (Highest Accuracy) ===

  // 1. Sifat Wajib, Mustahil, dan Jaiz bagi Allah Swt. (Faith in Allah & His Attributes)
  if (t.match(/sifat\s+wajib|sifat\s+mustahil|sifat\s+jaiz|wujud|qidam|baqa|sifat-sifat\s+kesempurnaan/)) {
    return pick(['/assets/rukun_iman.jpg', '/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }

  // 2. Akhlak Terhadap Allah Swt. / Husnuzan / Doa & Tawakal / Sabar & Syukur
  if (t.match(/akhlak\s+terhadap\s+allah|ḥ?husnuzan|berbaik\s+sangka|berdoa|doa|tawakal|ikhtiar|syukur|sabar/)) {
    return pick(['/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }

  // 3. Puasa (Shaum / Siyam) Wajib & Sunah / Ramadan
  if (t.match(/puasa|shaum|siyam|ramadan|ramadhan|iftar|sahur/)) {
    return pick(['/assets/rukun_islam.jpg', '/assets/sedekah_berbagi.jpg', '/assets/boy_praying.jpg']);
  }

  // 4. Tasbih / Menyucikan Allah / Zikir / Subhanallah
  if (t.match(/tasbih|subhanallah|menyucikan\s+allah|zikir|memuji\s+allah/)) {
    return pick(['/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }

  // 5. Rukun Islam / Syahadat / Syahadatain / Dua Kalimat Syahadat
  if (t.match(/rukun\s+islam|syahadat|syahadatain|kalimat\s+syahadat/)) {
    return pick(['/assets/rukun_islam.jpg', '/assets/boy_praying.jpg']);
  }

  // 6. Rukun Iman / 6 Rukun Iman / Meyakini Rukun Iman / Hari Akhir / Qada Qadar
  if (t.match(/rukun\s+iman|enam\s+rukun\s+iman|iman\s+kepada|meyakini\s+rukun\s+iman|hari\s*akhir|kiamat|takdir|qada|qadar/)) {
    return pick(['/assets/rukun_iman.jpg', '/assets/boy_praying.jpg']);
  }
  
  // 7. Shalat / Salat / Azan / Ikamah / Sujud / Salat Rawatib, Duha, Tahajud / Salat Berjamaah / Fardu
  if (t.match(/salat|sholat|solat|sujud|ruku|azan|adzan|ikamah|iqamah|rawatib|duha|dhuha|tahajud|berjamaah|fardu|saf|waktu\s+salat/)) {
    return pick(['/assets/boy_praying.jpg', '/assets/sholat_berjamaah.jpg']);
  }

  // 8. Asmaul Husna (Al-Gaffar, Al-Wahhab, Al-Fattah, Al-Latif, Al-Halim, Asy-Syakur, Al-Hakim, Al-Wadud, dll)
  if (t.match(/asmaul|husna|nama.*allah|ar-rahman|ar-rahim|al-hafiz|al-wali|al-alim|al-khabir|al-wahhab|al-fattah|al-latif|al-halim|asy-syakur|al-hakim|al-wadud|al-kabir|al-malik|al-quddus|as-salam|al-mu'min|al-qawiyyu|al-qayyum|al-muhyi|al-ghaffar|al-afuw/)) {
    return pick(['/assets/asmaul_husna.jpg', '/assets/boy_praying.jpg']);
  }

  // 9. Huruf Hijaiyah / Tajwid / Mim Sukun / Mad Thabi'i / Makhraj
  if (t.match(/hijaiyah|harakat|huruf|makhraj|makhārijul|bersambung|tanwin|fathah|kasrah|dhammah|mad\s*ṭ?t?ab|mim\s+sukun|idgam|ikhfa|izhar/)) {
    return pick(['/assets/hijaiyah_bersambung.jpg', '/assets/quran_rehal.jpg']);
  }

  // 10. Surah Al-Qur'an / Juz Amma / Membaca Al-Qur'an (An-Nas, Al-Falaq, Al-Kautsar, Al-'Asr, An-Nasr, At-Tin, Al-Ma'un, dll)
  if (t.match(/surah|q\.?s\.?|al-kau[sṡ]ar|an-na[sṣ]r|al-'?a[sṣ]r|al-falaq|an-nas|al-fatihah|al-ikhlas|at-tin|al-ma'?un|al-hujurat|al-a'?la|ad-duha|juz\s*'amma|qur'?an|tadarus|tartil|tilawah/)) {
    return pick(['/assets/cover_kelas3.jpg', '/assets/quran_rehal.jpg']);
  }

  // 11. Wudhu / Thaharah / Bersuci / PHBS / Pola Hidup Bersih & Sehat
  if (t.match(/wudhu|wudu|thaharah|bersuci|istinja|mandi|najis|cuci|bersih|phbs|sehat/)) {
    return pick(['/assets/wudu_girl.jpg', '/assets/menjaga_alam.jpg']);
  }

  // 12. Zakat / Sedekah / Infaq / Berbagi / Tolong Menolong
  if (t.match(/zakat|sedekah|infaq|infak|berbagi|dermawan|kedermawanan|tolong|peduli/)) {
    return pick(['/assets/sedekah_berbagi.jpg', '/assets/cover_kelas4.jpg']);
  }

  // 13. Akhlak Terhadap Sesama / Adab / Sopan Santun / Hormat Orang Tua & Guru & Keluarga
  if (t.match(/keluarga|orang\s*tua|ibu|ayah|guru|adab|sopan|hormat|santun|birrul|ukhuwah|tetangga/)) {
    return pick(['/assets/adab_orangtua.jpg', '/assets/cover_kelas4.jpg']);
  }

  // 14. Kisah Kerasulan / Dakwah Nabi Periode Makkah / Gua Hira / Wahyu Pertama
  if (t.match(/kerasulan|dakwah.*makkah|gua\s+hira|al-alaq|periode\s+makkah|fathu\s+makkah|hijrah\s+nabi/)) {
    return pick(['/assets/quran_rehal.jpg', '/assets/cover_kelas5.jpg', '/assets/jannah_garden.jpg']);
  }

  // 15. Kisah Nabi / Rasul / Sahabat / Keteladanan / Adam / Nuh / Ibrahim / Surga
  if (t.match(/nabi|rasul|kisah|mukjizat|adam|nuh|ibrahim|surga|jannah/)) {
    return pick(['/assets/jannah_garden.jpg', '/assets/cover_kelas5.jpg']);
  }

  // 16. Menjaga Alam / Lingkungan / Ciptaan Allah
  if (t.match(/alam|lingkungan|pohon|tanaman|bumi|ciptaan|hewan|flora|fauna/)) {
    return pick(['/assets/menjaga_alam.jpg', '/assets/cover_kelas5.jpg']);
  }

  // === PRIORITY 2: MATCH BY CONTENT (Strict Multi-word Phrases) ===
  if (c.match(/puasa\s+ramadan|puasa\s+sunah|menahan\s+lapar|berbuka\s+puasa|shaum/)) {
    return pick(['/assets/rukun_islam.jpg', '/assets/sedekah_berbagi.jpg']);
  }
  if (c.match(/berdoa\s+kepada\s+allah|bertawakal|ikhtiar\s+dan\s+doa|memohon\s+pertolongan/)) {
    return pick(['/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/kalimat\s+tasbih|ucapan\s+subhanallah|membaca\s+tasbih|berzikir/)) {
    return pick(['/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/lima\s+rukun\s+islam|dua\s+kalimat\s+syahadat|syahadatain/)) {
    return pick(['/assets/rukun_islam.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/sifat\s+wajib\s+allah|sifat\s+mustahil|wujud|qidam|baqa/)) {
    return pick(['/assets/rukun_iman.jpg', '/assets/tasbih_zikir.jpg']);
  }
  if (c.match(/enam\s+rukun\s+iman|iman\s+kepada\s+allah|iman\s+kepada\s+malaikat/)) {
    return pick(['/assets/rukun_iman.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/melaksanakan\s+salat|shalat\s+berjamaah|bacaan\s+ruku|bacaan\s+sujud|salat\s+fardu|salat\s+sunah/)) {
    return pick(['/assets/boy_praying.jpg', '/assets/sholat_berjamaah.jpg']);
  }
  if (c.match(/asmaul\s*husna|ar-rahman|ar-rahim|al-quddus|as-salam|al-malik|al-mu'min/)) {
    return pick(['/assets/asmaul_husna.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/huruf\s+hijaiyah|harakat|tanda\s+baca\s+arab|makharijul|mad\s+tabii|mim\s+sukun/)) {
    return pick(['/assets/hijaiyah_bersambung.jpg', '/assets/quran_rehal.jpg']);
  }
  if (c.match(/surah\s+al-kau|surah\s+al-'as|surah\s+an-nas|surah\s+al-falaq|al-qur'?an\s+adalah|membaca\s+surah/)) {
    return pick(['/assets/cover_kelas3.jpg', '/assets/quran_rehal.jpg']);
  }
  if (c.match(/tata\s+cara\s+wudhu|berwudhu|rukun\s+wudhu|hidup\s+bersih|kebersihan/)) {
    return pick(['/assets/wudu_girl.jpg', '/assets/menjaga_alam.jpg']);
  }
  if (c.match(/mengeluarkan\s+zakat|bersedekah|infak|memberi\s+bantuan/)) {
    return pick(['/assets/sedekah_berbagi.jpg', '/assets/cover_kelas4.jpg']);
  }
  if (c.match(/berbakti\s+kepada\s+orang\s*tua|menghormati\s+guru|sopan\s+santun|akhlak\s+keluarga/)) {
    return pick(['/assets/adab_orangtua.jpg', '/assets/cover_kelas4.jpg']);
  }
  if (c.match(/menjaga\s+kelestarian|merawat\s+lingkungan|ciptaan\s+allah\s+di\s+bumi/)) {
    return pick(['/assets/menjaga_alam.jpg', '/assets/cover_kelas5.jpg']);
  }
  if (c.match(/kisah\s+nabi|keteladanan\s+rasul|nabi\s+adam|mukjizat|wahyu\s+pertama/)) {
    return pick(['/assets/jannah_garden.jpg', '/assets/cover_kelas5.jpg']);
  }

  // === PRIORITY 3: ROTATING DIVERSE FALLBACKS ===
  const diverseLibrary = [
    '/assets/tasbih_zikir.jpg',
    '/assets/rukun_islam.jpg',
    '/assets/rukun_iman.jpg',
    '/assets/cover_kelas3.jpg',
    '/assets/asmaul_husna.jpg',
    '/assets/boy_praying.jpg',
    '/assets/quran_rehal.jpg',
    '/assets/wudu_girl.jpg',
    '/assets/sedekah_berbagi.jpg',
    '/assets/adab_orangtua.jpg',
    '/assets/menjaga_alam.jpg',
    '/assets/jannah_garden.jpg'
  ];
  return pick(diverseLibrary);
}

// Test titles for Kelas 3, 4, 5
const titlesKelas3 = [
  "Membaca, menulis, dan membedakan huruf hijaiyah bersambung (Mad Ṭabī‘ī)",
  "Mengenal, Menghafal, dan Memahami Q.S. Al-Kauṡar",
  "Sifat Wajib, Mustahil, dan Jaiz bagi Allah Swt.",
  "Akhlak Terhadap Allah Swt.: Berbaik Sangka (Ḥusnuzan)",
  "Azan, Ikamah, dan Kisah Kelahiran Nabi Muhammad saw."
];

const titlesKelas4 = [
  "Huruf Hijaiyah Bersambung dan Q.S. an-Naṣr",
  "Asmaulhusna (Al-Gaffār, Al-Wahhāb, Al-Fattāḥ, Al-Laṭīf)",
  "Akhlak Terhadap Keluarga",
  "Salat Sunah Rawatib, Duha, dan Tahajud",
  "Kisah Kerasulan dan Dakwah Nabi Muhammad saw. Periode Makkah"
];

const titlesKelas5 = [
  "Membaca Huruf Hijaiyah Bersambung dan Hukum Bacaan Mim Sukun",
  "Mengkaji Pesan Bermakna Surah Al-'Aṣr",
  "Mengenal Asmaulhusna: Al-Ḥalīm, Asy-Syakūr, Al-Ḥakīm, dan Al-Wadūd",
  "Akhlak Terpuji: Berdoa dan Bertawakal kepada Allah Swt.",
  "Ketentuan Puasa Wajib dan Puasa Sunah dalam Islam"
];

console.log("=== KELAS 3 ===");
let used3 = new Set(["/assets/cover_penjualan_buku_kelas3.jpg"]);
titlesKelas3.forEach((t, i) => {
  console.log(`Bab ${i+1}: ${t}`);
  console.log(` -> Match: ${getSmartChapterImage(t, '', i, used3)}`);
});

console.log("\n=== KELAS 4 ===");
let used4 = new Set(["/assets/cover_penjualan_buku_kelas4.jpg"]);
titlesKelas4.forEach((t, i) => {
  console.log(`Bab ${i+1}: ${t}`);
  console.log(` -> Match: ${getSmartChapterImage(t, '', i, used4)}`);
});

console.log("\n=== KELAS 5 ===");
let used5 = new Set(["/assets/cover_penjualan_buku_kelas5.jpg"]);
titlesKelas5.forEach((t, i) => {
  console.log(`Bab ${i+1}: ${t}`);
  console.log(` -> Match: ${getSmartChapterImage(t, '', i, used5)}`);
});
const titlesKelas1 = [
  "Mengenal Huruf Hijaiah Berharakat",
  "Mengenal Rukun Iman",
  "Membaca Kalimat Tayibah (Basmalah & Hamdalah)",
  "Mengenal Rukun Islam dan Syahadatain",
  "Kisah Keteladanan Nabi Adam a.s."
];

const titlesKelas2 = [
  "Membaca dan Membedakan Huruf Hijaiyah Bersambung",
  "Menghafal Surah An-Nās dan Al-Falaq",
  "Mengenal Asmaulhusna: Ar-Raḥmān, Ar-Raḥīm, As-Salām, dan Al-Mu'min",
  "Akhlak Terhadap Diri Sendiri: Pola Hidup Bersih dan Sehat",
  "Menerapkan Salat Fardu dan Kisah Keteladanan Nabi Nūh a.s."
];

console.log("=== KELAS 1 ===");
let used1 = new Set(["/assets/cover_penjualan_buku_kelas1.jpg"]);
titlesKelas1.forEach((t, i) => {
  console.log(`Bab ${i+1}: ${t}`);
  console.log(` -> Match: ${getSmartChapterImage(t, '', i, used1)}`);
});

console.log("\n=== KELAS 2 ===");
let used2 = new Set(["/assets/cover_penjualan_buku_kelas2.jpg"]);
titlesKelas2.forEach((t, i) => {
  console.log(`Bab ${i+1}: ${t}`);
  console.log(` -> Match: ${getSmartChapterImage(t, '', i, used2)}`);
});
const titlesKelas6 = [
  "Membaca, Menulis, dan Membedakan Huruf Hijaiyah Bersambung Serta Bacaan Gunnah",
  "Menjelaskan Surah Pendek Al-Insyirāḥ",
  "Memahami Asmaulhusna: Al-Waliyy, Al-Ḥamīd, Al-‘Adl, dan Aṣ-Ṣabūr",
  "Akhlak Terhadap Tetangga dan Nonmuslim Serta Zakat, Infak, dan Sedekah",
  "Kisah Teladan Kepemimpinan Khulafaurasyidin: Abu Bakar aṣ-Ṣiddīq dan Umar bin Khattab"
];

console.log("=== KELAS 6 ===");
let used6 = new Set(["/assets/cover_penjualan_buku_kelas6.jpg"]);
titlesKelas6.forEach((t, i) => {
  console.log(`Bab ${i+1}: ${t}`);
  console.log(` -> Match: ${getSmartChapterImage(t, '', i, used6)}`);
});
