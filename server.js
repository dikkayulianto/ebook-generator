const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const multer = require('multer');
const pdfParse = require('pdf-parse');
const mammoth = require('mammoth');

const app = express();
const PORT = process.env.PORT || 3000;

// Setup Multer for document uploads
const upload = multer({
  dest: path.join(__dirname, 'uploads'),
  limits: { fileSize: 25 * 1024 * 1024 } // 25 MB
});

app.use(cors());
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true, limit: '50mb' }));
app.use(express.static(path.join(__dirname, 'public')));
app.use('/assets', express.static(path.join(__dirname, 'assets')));

// Ensure directories exist
const exportsDir = path.join(__dirname, 'exports');
const uploadsDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(exportsDir)) fs.mkdirSync(exportsDir, { recursive: true });
if (!fs.existsSync(uploadsDir)) fs.mkdirSync(uploadsDir, { recursive: true });

// Extract text from uploaded document
async function extractTextFromDoc(filePath, originalName) {
  const ext = path.extname(originalName).toLowerCase();
  try {
    if (ext === '.pdf') {
      const dataBuffer = fs.readFileSync(filePath);
      const data = await pdfParse(dataBuffer);
      return data.text || '';
    } else if (ext === '.docx') {
      const result = await mammoth.extractRawText({ path: filePath });
      return result.value || '';
    } else {
      // .txt, .md, .csv, etc.
      return fs.readFileSync(filePath, 'utf8');
    }
  } catch (err) {
    console.error('Error extracting text from document:', err);
    return '';
  }
}

// Endpoint: Upload & Extract Document
app.post('/api/upload-doc', upload.single('docFile'), async (req, res) => {
  try {
    if (!req.file) return res.status(400).json({ error: 'Tidak ada file yang diunggah' });
    const text = await extractTextFromDoc(req.file.path, req.file.originalname);
    
    // Clean up temp file
    try { fs.unlinkSync(req.file.path); } catch (e) {}

    res.json({
      success: true,
      fileName: req.file.originalname,
      fileSize: req.file.size,
      textSnippet: text.substring(0, 300) + '...',
      extractedText: text
    });
  } catch (err) {
    res.status(500).json({ error: 'Gagal memproses dokumen: ' + err.message });
  }
});

// Enhanced System prompt strictly following uploaded document reference OR standard CP No. 020 Tahun 2026
function getSystemPrompt(subject, grade, semester, curriculum, referenceText) {
  let prompt = `Anda adalah penulis buku teks sekolah dasar (SD) terkemuka dan konsultan kurikulum nasional di Indonesia.
Tugas Anda adalah menyusun BUKU SISWA / MODUL AJAR RESMI LENGKAP, MENDALAM, dan SIAP CETAK untuk:
- Mata Pelajaran: ${subject}
- Tingkat: Kelas ${grade} SD
- Periode: Semester ${semester}
- Acuan Kurikulum: ${curriculum}

=======================================================
ATURAN UTAMA SUMBER MATERI & JUDUL BAB (SANGAT KETAT):
=======================================================`;

  if (referenceText && referenceText.trim().length > 0) {
    prompt += `
1. REFERENSI DOKUMEN PENGGUNA TERDETEKSI:
   Pengguna telah mengunggah dokumen materi/silabus berikut ini:
   """
   ${referenceText.substring(0, 30000)}
   """
   ATURAN MUTLAK DOKUMEN:
   - WAJIB MENGIKUTI SEMUA JUDUL BAB, URUTAN BAB, DAN POKOK BAHASAN DARI DOKUMEN DI ATAS!
   - JANGAN mengganti judul bab dengan topik lain di luar dokumen!
   - Kembangkan isi materi setiap bab dari poin-poin dokumen tersebut menjadi penjelasan komprehensif, kaya contoh ramah anak SD, dan mendalam!`;
  } else {
    prompt += `
1. TIDAK ADA DOKUMEN UNGGAHAN (STANDAR SISTEM RESMI):
   Karena tidak ada dokumen unggahan, Anda WAJIB MENGIKUTI Capaian Pembelajaran (CP) No. 020 Tahun 2026 (Kurikulum Merdeka SD) secara akurat sesuai Kelas ${grade} Semester ${semester}:
   - Jika Kelas 1 SD: Fase A (Mengenal Huruf Hijaiah berharakat, Rukun Iman dasar, Kalimat Tayibah Basmalah/Hamdalah, Asmaulhusna Ar-Rahman/Ar-Rahim, Rukun Islam & Syahadatain, Bersuci & Wudhu, Kisah Nabi Adam a.s.).
   - Jika Kelas 2 SD: Fase A (Huruf Hijaiah bersambung, Surah An-Nas & Al-Falaq, Asmaulhusna Al-Hafiz/Al-Wali/Al-Alim/Al-Khabir, Pola Hidup Bersih & Sehat/PHBS, Salat Fardu Lima Waktu, Kisah Nabi Nuh a.s.).
   - Jika Kelas 3 SD: Fase B (Surah Al-Kautsar & Al-Ikhlas, Asmaulhusna Al-Wahhab/Al-Kabir/Al-Malik, Berbakti kepada orang tua dan guru, Salat Berjamaah, Kisah Nabi Ibrahim a.s.).
   - Jika Kelas 4 SD: Fase B (Surah Al-Hujurat:13 keragaman, Asmaulhusna Al-Quddus/As-Salam/Al-Mu'min, Tanda-tanda Baligh, Salat Jumat & Dhuha, Kisah Hijrah Nabi Muhammad saw.).
   - Jika Kelas 5 SD: Fase C (Surah At-Tin & Al-Ma'un, Asmaulhusna Al-Qawiyyu/Al-Qayyum/Al-Muhyi, Zakat & Sedekah, Menghargai Keragaman Budaya & Agama, Kisah Fathu Makkah).
   - Jika Kelas 6 SD: Fase C (Surah Al-A'la & Ad-Duha, Asmaulhusna Al-Ghaffar/Al-Afuw, Iman Hari Akhir & Takdir, Jual Beli Halal & Muamalah Sederhana, Keteladanan Khulafaur Rasyidin).`;
  }

  prompt += `

=======================================================
PANDUAN KONTEN & STRUKTUR PEDAGOGIS (LENGKAP & HOTS):
=======================================================
1. PENJELASAN MENDALAM: Setiap bab terdiri dari Sub-Bab A dan Sub-Bab B. Uraikan minimal 2-3 paragraf panjang berbobot per sub-bab dengan bahasa santun, ceria, dan mudah dipahami siswa SD.
2. FITUR PENDUKUNG TIAP BAB:
   - "Kamus Cilik": 2-3 kosakata baru beserta maknanya.
   - "Kisah Teladan & Mutiara Hikmah": Cerita inspiratif menyentuh hati 1-2 paragraf.
   - "Aktivitas Ceria Siswa": Praktik seru / tepuk anak pintar / bernyanyi.
   - "Tantangan Berpikir Kritis (Soal HOTS)": 1 soal analisis studi kasus nyata kehidupan anak di sekolah/rumah yang melatih nalar kritis dan pemecahan masalah moral.
   - "Ayo Berlatih (Pemahaman Konsep)": 3 soal latihan formatif singkat.
3. ASESMEN SUMATIF AKHIR SEMESTER:
   - Buat minimal 20 Soal Pilihan Ganda (a, b, c) yang mencakup seluruh bab.
   - Lengkapi dengan Kunci Jawaban Lengkap (1-20).
4. RUBRIK PENILAIAN GURU (ASESMEN OTENTIK):
   - Sertakan kriteria penilaian resmi mencakup Aspek Sikap, Pengetahuan, dan Keterampilan.

Format output WAJIB berupa JSON murni (valid JSON) tanpa awalan/akhiran markdown seperti \`\`\`json.
Struktur JSON yang HARUS dikembalikan:
{
  "title": "${subject}",
  "grade": "${grade}",
  "semester": "${semester}",
  "curriculum": "${curriculum}",
  "tagline": "Slogan motivasi ceria anak SD",
  "chapters": [
    {
      "number": 1,
      "title": "Judul Bab 1",
      "objective": "Tujuan pembelajaran terperinci ramah anak",
      "subChapters": [
        { 
          "title": "A. Judul Sub-Bab A", 
          "content": "Penjelasan materi mendalam dan komprehensif minimal 2-3 paragraf panjang, dilengkapi contoh nyata kehidupan anak." 
        },
        { 
          "title": "B. Judul Sub-Bab B", 
          "content": "Penjelasan materi lanjutan yang mendalam, langkah-langkah praktis, dan pembiasaan akhlak budi pekerti." 
        }
      ],
      "vocabulary": [
        { "term": "Istilah 1", "meaning": "Arti kata sederhana untuk anak SD" },
        { "term": "Istilah 2", "meaning": "Arti kata sederhana untuk anak SD" }
      ],
      "inspirationalStory": "Kisah teladan inspiratif bermakna yang relevan dengan bab ini.",
      "funActivity": "Aktivitas seru interaktif (Lagu Belajar / Tepuk Ceria / Praktik Mandiri)",
      "hotsQuestion": "Studi kasus situasi nyata: Contohnya ketika melihat teman yang terjatuh atau menemukan uang di kelas, apa yang harus dilakukan dan jelaskan alasannya?",
      "exercises": [
        "Soal pemahaman konsep 1",
        "Soal pemahaman konsep 2",
        "Soal refleksi karakter 3"
      ]
    }
  ],
  "finalAssessment": [
    {
      "question": "Pertanyaan nomor 1",
      "options": ["a. Opsi 1", "b. Opsi 2", "c. Opsi 3"],
      "answer": "a"
    }
  ]
}
Catatan: Pastikan bab berjumlah 5 bab dan finalAssessment berjumlah 20 soal pilihan ganda!`;

  return prompt;
}

// Sleep helper for retries
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// Helper: Call Gemini API with Auto-Retry & Dynamic Model Discovery
async function callGemini(prompt, apiKey, requestedModel) {
  // 1. Fetch live models list from Google
  let activeModels = [];
  try {
    const listRes = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${apiKey}`);
    if (listRes.ok) {
      const listData = await listRes.json();
      activeModels = (listData.models || [])
        .filter(m => m.supportedGenerationMethods && m.supportedGenerationMethods.includes('generateContent'))
        .map(m => m.name.replace('models/', ''));
      console.log('Google AI Studio active models for your key:', activeModels);
    }
  } catch (err) {
    console.warn('Could not query model list:', err.message);
  }

  // Filter out any models known to be deprecated
  activeModels = activeModels.filter(m => !m.includes('2.5') && !m.includes('1.5') && !m.includes('2.0'));

  // Priority queue
  const candidateModels = [
    requestedModel,
    'gemini-3.8-flash',
    'gemini-3.8-pro',
    ...activeModels
  ].filter((v, i, a) => v && a.indexOf(v) === i); // unique

  let lastError = null;

  for (const model of candidateModels) {
    console.log(`Mencoba memanggil Gemini model: ${model}...`);
    
    // Try up to 3 times if 503 (temporary high demand spike)
    for (let attempt = 1; attempt <= 3; attempt++) {
      try {
        const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
        const response = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }],
            generationConfig: {
              responseMimeType: "application/json",
              temperature: 0.7
            }
          })
        });

        if (response.status === 503) {
          console.warn(`Model ${model} terkena lonjakan trafik (503). Mencoba ulang (percobaan ${attempt}/3) dalam 2 detik...`);
          if (attempt < 3) {
            await sleep(2000);
            continue;
          }
        }

        if (!response.ok) {
          const errText = await response.text();
          console.warn(`Model ${model} gagal (${response.status}):`, errText);
          lastError = new Error(`Model ${model} Error (${response.status}): ${errText}`);
          break; // break retry loop, try next model
        }

        const data = await response.json();
        const rawText = data.candidates?.[0]?.content?.parts?.[0]?.text;
        if (!rawText) throw new Error('Respon kosong dari Gemini');
        
        console.log(`✅ SUKSES menggunakan model: ${model}`);
        return JSON.parse(rawText.replace(/^```json\s*/i, '').replace(/```\s*$/i, '').trim());
      } catch (e) {
        lastError = e;
        if (e.message && e.message.includes('503') && attempt < 3) {
          await sleep(2000);
          continue;
        }
        break;
      }
    }
  }

  throw lastError || new Error('Gagal menghubungi Gemini API setelah mencoba beberapa model.');
}

// Helper: Call OpenAI/Hermes/Local LLM API
async function callOpenAICompatible(prompt, endpoint, apiKey, model) {
  const targetUrl = endpoint.endsWith('/chat/completions') ? endpoint : `${endpoint.replace(/\/+$/, '')}/chat/completions`;
  const selectedModel = model || 'qwen2.5:1.5b';
  console.log(`Mencoba memanggil Local LLM di: ${targetUrl} dengan model: ${selectedModel}...`);

  const response = await fetch(targetUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey || 'not-needed'}`
    },
    body: JSON.stringify({
      model: selectedModel,
      messages: [
        { role: 'system', content: 'You are an educational book creator for Indonesian elementary school. Output strictly valid JSON without explanation.' },
        { role: 'user', content: prompt }
      ],
      temperature: 0.7
    })
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`Hermes/LLM Error (${response.status}): ${errText}`);
  }

  const data = await response.json();
  const rawText = data.choices?.[0]?.message?.content;
  if (!rawText) throw new Error('Respon kosong dari model Hermes/LLM');

  let cleanJson = rawText.trim();
  const jsonMatch = cleanJson.match(/\{[\s\S]*\}/);
  if (jsonMatch) cleanJson = jsonMatch[0];

  console.log('✅ SUKSES memproses respons dari Local LLM!');
  return JSON.parse(cleanJson);
}

// Grade Theming: Specific colors, badges, and cover artwork per grade
// Grade Theming: Specific colors, badges, and cover artwork per grade and semester
function getGradeTheme(grade, semester = 1) {
  const g = parseInt(grade) || 1;
  const sem = parseInt(semester) === 2 ? 2 : 1;
  const themes = {
    1: {
      fase: "FASE A",
      gradient: "linear-gradient(180deg, #ecfdf5 0%, #d1fae5 45%, #fef3c7 100%)",
      border: "#059669",
      accent: "#b45309",
      titleColor: "#064e3b",
      badgeBg: "#059669",
      coverImg: sem === 2 ? "/assets/cover_penjualan_buku_kelas1_sem2.jpg" : "/assets/cover_penjualan_buku_kelas1.jpg",
      coverTag: sem === 2 ? "Semester 2: Penguatan Ibadah & Keteladanan" : "Mengenal Dasar Keislaman & Budi Pekerti"
    },
    2: {
      fase: "FASE A",
      gradient: "linear-gradient(180deg, #f0f9ff 0%, #e0f2fe 45%, #fef3c7 100%)",
      border: "#0284c7",
      accent: "#0369a1",
      titleColor: "#0c4a6e",
      badgeBg: "#0284c7",
      coverImg: sem === 2 ? "/assets/cover_penjualan_buku_kelas2_sem2.jpg" : "/assets/cover_penjualan_buku_kelas2.jpg",
      coverTag: sem === 2 ? "Semester 2: Penguatan Akhlak & Kisah Teladan" : "Belajar Huruf Bersambung & Ketaatan Ibadah"
    },
    3: {
      fase: "FASE B",
      gradient: "linear-gradient(180deg, #faf5ff 0%, #ede9fe 45%, #fef3c7 100%)",
      border: "#7c3aed",
      accent: "#6d28d9",
      titleColor: "#4c1d95",
      badgeBg: "#7c3aed",
      coverImg: sem === 2 ? "/assets/cover_penjualan_buku_kelas3_sem2.jpg" : "/assets/cover_penjualan_buku_kelas3.jpg",
      coverTag: sem === 2 ? "Semester 2: Penguatan Keimanan & Shalat Berjamaah" : "Mendalami Shalat, Zikir, & Sifat Terpuji"
    },
    4: {
      fase: "FASE B",
      gradient: "linear-gradient(180deg, #fff7ed 0%, #ffedd5 45%, #fef3c7 100%)",
      border: "#ea580c",
      accent: "#c2410c",
      titleColor: "#7c2d12",
      badgeBg: "#ea580c",
      coverImg: sem === 2 ? "/assets/cover_penjualan_buku_kelas4_sem2.jpg" : "/assets/cover_penjualan_buku_kelas4.jpg",
      coverTag: sem === 2 ? "Semester 2: Keragaman & Kisah Hijrah Nabi" : "Memahami Tanda Baligh & Akhlak Mulia"
    },
    5: {
      fase: "FASE C",
      gradient: "linear-gradient(180deg, #f0fdf4 0%, #dcfce7 45%, #fef3c7 100%)",
      border: "#16a34a",
      accent: "#15803d",
      titleColor: "#14532d",
      badgeBg: "#16a34a",
      coverImg: sem === 2 ? "/assets/cover_penjualan_buku_kelas5_sem2.jpg" : "/assets/cover_penjualan_buku_kelas5.jpg",
      coverTag: sem === 2 ? "Semester 2: Ibadah Haji, Kurban, & Kebersamaan" : "Menerapkan Toleransi, Zakat, & Ukhuwah"
    },
    6: {
      fase: "FASE C",
      gradient: "linear-gradient(180deg, #fdf2f8 0%, #fce7f3 45%, #fef3c7 100%)",
      border: "#db2777",
      accent: "#be185d",
      titleColor: "#831843",
      badgeBg: "#db2777",
      coverImg: sem === 2 ? "/assets/cover_penjualan_buku_kelas6_sem2.jpg" : "/assets/cover_penjualan_buku_kelas6.jpg",
      coverTag: sem === 2 ? "Semester 2: Muamalah Halal & Keteladanan Sahabat" : "Memantapkan Iman Hari Akhir & Kepemimpinan"
    }
  };
  return themes[g] || themes[1];
}

// Smart Local Image Matcher: Matches exact chapter title to best 3D artwork with strict priority & no duplicates
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

  // 1. Surah Al-Qur'an Pilihan (MUST BE CHECKED FIRST before general 'syukur'/'salat')
  if (t.match(/surah|q\.?s\.?|al-kau[sṡ]ar|an-na[sṣ]r|al-'?a[sṣ]r|al-falaq|an-nas|al-fatihah|al-ikhlas|at-tin|al-ma'?un|al-hujurat|al-a'?la|ad-duha/)) {
    return pick(['/assets/cover_kelas3.jpg', '/assets/quran_rehal.jpg']);
  }

  // 2. Huruf Hijaiyah / Tajwid / Mim Sukun / Mad Thabi'i / Makhraj
  if (t.match(/hijaiyah|harakat|huruf|makhraj|makhārijul|bersambung|tanwin|fathah|kasrah|dhammah|mad\s*ṭ?t?ab|mim\s+sukun|idgam|ikhfa|izhar/)) {
    return pick(['/assets/hijaiyah_bersambung.jpg', '/assets/quran_rehal.jpg']);
  }

  // 2b. General Al-Qur'an / Juz 'Amma / Tadarus
  if (t.match(/juz\s*'amma|qur'?an|tadarus|tartil|tilawah/)) {
    return pick(['/assets/cover_kelas3.jpg', '/assets/quran_rehal.jpg']);
  }

  // 3. Sifat Wajib, Mustahil, dan Jaiz bagi Allah Swt. (Faith in Allah & His 20 Attributes)
  if (t.match(/sifat\s+wajib|sifat\s+mustahil|sifat\s+jaiz|wujud|qidam|baqa|sifat-sifat\s+kesempurnaan/)) {
    return pick(['/assets/sifat_allah.jpg', '/assets/asmaul_husna.jpg', '/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }

  // 4. Asmaul Husna (Al-Gaffar, Al-Wahhab, Al-Fattah, Al-Latif, Al-Halim, Asy-Syakur, Al-Hakim, Al-Wadud, dll)
  if (t.match(/asmaul|husna|nama-nama\s+allah|ar-rahman|ar-rahim|al-hafiz|al-wali|al-alim|al-khabir|al-wahhab|al-fattah|al-latif|al-halim|asy-syakur|al-hakim|al-wadud|al-kabir|al-malik|al-quddus|as-salam|al-mu'min|al-qawiyyu|al-qayyum|al-muhyi|al-ghaffar|al-afuw/)) {
    return pick(['/assets/asmaul_husna.jpg', '/assets/sifat_allah.jpg', '/assets/boy_praying.jpg']);
  }

  // 5. Azan dan Ikamah (Muazin Cilik / Panggilan Salat)
  if (t.match(/azan|adzan|ikamah|iqamah|muazin|muadzin|menyeru\s+salat/)) {
    return pick(['/assets/azan_ikamah.jpg', '/assets/sholat_berjamaah.jpg', '/assets/boy_praying.jpg']);
  }

  // 6. Shalat / Salat / Sujud / Rukuk / Rawatib / Duha / Tahajud / Berjamaah / Fardu
  if (t.match(/salat|sholat|solat|sujud|\bruku'?k?\b|rawatib|duha|dhuha|tahajud|berjamaah|fardu|\bsaf\b|waktu\s+salat/)) {
    return pick(['/assets/boy_praying.jpg', '/assets/sholat_berjamaah.jpg']);
  }

  // 7. Puasa (Shaum / Siyam) Wajib & Sunah / Ramadan
  if (t.match(/puasa|shaum|siyam|ramadan|ramadhan|iftar|sahur/)) {
    return pick(['/assets/rukun_islam.jpg', '/assets/sedekah_berbagi.jpg', '/assets/boy_praying.jpg']);
  }

  // 8. Rukun Islam / Syahadat / Syahadatain / Dua Kalimat Syahadat
  if (t.match(/rukun\s+islam|syahadat|syahadatain|kalimat\s+syahadat/)) {
    return pick(['/assets/rukun_islam.jpg', '/assets/boy_praying.jpg']);
  }

  // 9. Rukun Iman / 6 Rukun Iman / Meyakini Rukun Iman / Hari Akhir / Qada Qadar
  if (t.match(/rukun\s+iman|enam\s+rukun\s+iman|iman\s+kepada|meyakini\s+rukun\s+iman|hari\s*akhir|kiamat|takdir|qada|qadar/)) {
    return pick(['/assets/rukun_iman.jpg', '/assets/boy_praying.jpg']);
  }

  // 10. Akhlak Terhadap Allah Swt. / Husnuzan / Doa & Tawakal / Sabar & Syukur / Berbaik Sangka
  if (t.match(/akhlak\s+terhadap\s+allah|ḥ?husnuzan|berbaik\s+sangka|berdoa|doa|tawakal|ikhtiar|syukur|sabar/)) {
    return pick(['/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }

  // 11. Tasbih / Menyucikan Allah / Zikir / Subhanallah
  if (t.match(/tasbih|subhanallah|menyucikan\s+allah|zikir|memuji\s+allah/)) {
    return pick(['/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }

  // 12. Wudhu / Thaharah / Bersuci / PHBS / Pola Hidup Bersih & Sehat
  if (t.match(/wudhu|wudu|thaharah|bersuci|istinja|mandi|najis|cuci|bersih|phbs|sehat/)) {
    return pick(['/assets/wudu_girl.jpg', '/assets/menjaga_alam.jpg']);
  }

  // 13. Zakat / Sedekah / Infaq / Berbagi / Tolong Menolong
  if (t.match(/zakat|sedekah|infaq|infak|berbagi|dermawan|kedermawanan|tolong|peduli/)) {
    return pick(['/assets/sedekah_berbagi.jpg', '/assets/cover_kelas4.jpg']);
  }

  // 14. Akhlak Terhadap Sesama / Adab / Sopan Santun / Hormat Orang Tua & Guru & Keluarga
  if (t.match(/keluarga|orang\s*tua|ibu|ayah|guru|adab|sopan|hormat|santun|birrul|ukhuwah|tetangga/)) {
    return pick(['/assets/adab_orangtua.jpg', '/assets/cover_kelas4.jpg']);
  }

  // 15. Kisah Kerasulan / Dakwah Nabi Periode Makkah / Gua Hira / Wahyu Pertama
  if (t.match(/kerasulan|dakwah.*makkah|gua\s+hira|al-alaq|periode\s+makkah|fathu\s+makkah|hijrah\s+nabi/)) {
    return pick(['/assets/quran_rehal.jpg', '/assets/cover_kelas5.jpg', '/assets/jannah_garden.jpg']);
  }

  // 16. Kisah Keteladanan Sahabat Nabi / Khulafaurasyidin (Abu Bakar, Umar, Utsman, Ali) / Kodifikasi Al-Qur'an
  if (t.match(/khulafaurasyidin|khulafa|abu\s+bakar|umar\s+bin\s+khattab|utsman|ali\s+bin\s+abi\s+thalib|sahabat\s+nabi|kepemimpinan/)) {
    return pick(['/assets/quran_rehal.jpg', '/assets/boy_praying.jpg', '/assets/tasbih_zikir.jpg']);
  }

  // 17. Kisah Kelahiran Nabi Muhammad / Maulid / Kisah Nabi / Rasul / Adam / Nuh / Ibrahim
  if (t.match(/kelahiran\s+nabi|maulid|nabi\s+muhammad|kisah.*nabi|rasul|mukjizat|adam|nuh|ibrahim|surga|jannah/)) {
    return pick(['/assets/jannah_garden.jpg', '/assets/cover_kelas5.jpg', '/assets/quran_rehal.jpg']);
  }

  // 18. Menjaga Alam / Lingkungan / Ciptaan Allah
  if (t.match(/alam|lingkungan|pohon|tanaman|bumi|ciptaan|hewan|flora|fauna/)) {
    return pick(['/assets/menjaga_alam.jpg', '/assets/cover_kelas5.jpg']);
  }

  // === PRIORITY 2: MATCH BY CONTENT (Strict Multi-word Phrases) ===
  if (c.match(/surah\s+al-kau|surah\s+al-'as|surah\s+an-nas|surah\s+al-falaq|al-qur'?an\s+adalah|membaca\s+surah/)) {
    return pick(['/assets/cover_kelas3.jpg', '/assets/quran_rehal.jpg']);
  }
  if (c.match(/sifat\s+wajib\s+allah|sifat\s+mustahil|wujud|qidam|baqa/)) {
    return pick(['/assets/sifat_allah.jpg', '/assets/asmaul_husna.jpg', '/assets/tasbih_zikir.jpg']);
  }
  if (c.match(/azan\s+dan\s+ikamah|panggilan\s+salat|muazin/)) {
    return pick(['/assets/azan_ikamah.jpg', '/assets/sholat_berjamaah.jpg']);
  }
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
  if (c.match(/khulafaurasyidin|abu\s+bakar|umar\s+bin\s+khattab|kodifikasi\s+al-qur'?an/)) {
    return pick(['/assets/quran_rehal.jpg', '/assets/boy_praying.jpg']);
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

// Template Builder: Convert JSON into Printable A4 HTML with Balanced Two-Spread Layout
async function renderBookHtml(bookData, apiKey) {
  const gradeTheme = getGradeTheme(bookData.grade, bookData.semester);

  const colors = [
    { badge: '#10b981', gradient: 'linear-gradient(135deg, #059669, #10b981)', border: '#34d399' },
    { badge: '#0284c7', gradient: 'linear-gradient(135deg, #0284c7, #38bdf8)', border: '#38bdf8' },
    { badge: '#7c3aed', gradient: 'linear-gradient(135deg, #7c3aed, #a855f7)', border: '#c084fc' },
    { badge: '#ea580c', gradient: 'linear-gradient(135deg, #ea580c, #fb923c)', border: '#fb923c' },
    { badge: '#e11d48', gradient: 'linear-gradient(135deg, #e11d48, #fb7185)', border: '#fb7185' }
  ];

  let chaptersHtml = '';
  const usedImages = new Set([gradeTheme.coverImg]);
  bookData.chapters.forEach((chap, idx) => {
    const theme = colors[idx % colors.length];

    // Smart Local Illustration matched strictly to topic, avoiding duplicates
    let fullChapterText = (chap.subChapters || []).map(s => s.content).join(' ');
    const chapImgUrl = getSmartChapterImage(chap.title, fullChapterText, idx, usedImages);

    const subA = (chap.subChapters && chap.subChapters[0]) ? chap.subChapters[0] : { title: 'A. Materi Utama', content: '' };
    const subB = (chap.subChapters && chap.subChapters[1]) ? chap.subChapters[1] : null;

    // Vocabulary / Kamus Cilik
    let vocabHtml = '';
    if (chap.vocabulary && chap.vocabulary.length > 0) {
      vocabHtml = `
        <div style="background: #f0fdfa; border: 1.5px solid #5eead4; border-radius: 10px; padding: 8px 12px; margin: 8px 0; font-size: 9.5pt;">
          <strong style="color: #0f766e;">📖 Kamus Cilik (Kosakata Baru):</strong>
          <div style="margin-top: 4px; display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
            ${chap.vocabulary.map(v => `<div><b style="color: #0d9488;">• ${v.term}:</b> ${v.meaning}</div>`).join('')}
          </div>
        </div>
      `;
    }

    // Inspirational Story
    let storyHtml = '';
    if (chap.inspirationalStory) {
      storyHtml = `
        <div style="background: #fffbeb; border-left: 4px solid #f59e0b; border-radius: 8px; padding: 8px 12px; margin: 8px 0; font-size: 9.5pt;">
          <strong style="color: #b45309;">🌟 Kisah Teladan & Mutiara Hikmah:</strong>
          <p style="margin-top: 4px; color: #78350f; font-style: italic; line-height: 1.5;">"${chap.inspirationalStory}"</p>
        </div>
      `;
    }

    let exercisesHtml = chap.exercises ? chap.exercises.map((ex, i) => `
      <div class="soal-item"><strong>${i + 1}.</strong> ${ex}</div>
    `).join('') : '';

    // Beautiful Balanced Page Spread for each Bab (Exactly 2 Pages per Bab, No Overflow)
    chaptersHtml += `
      <!-- ==================== BAB ${chap.number} (BAGIAN 1) ==================== -->
      <div class="page">
        <div class="page-header">
          <span>BAB ${chap.number}: ${chap.title}</span>
          <span>${bookData.curriculum} — KELAS ${bookData.grade} SD</span>
        </div>

        <div class="bab-header-flex">
          <div>
            <div class="bab-badge" style="background: ${theme.gradient};">BAB ${chap.number}</div>
            <h2 class="bab-title">${chap.title}</h2>
          </div>
        </div>

        <div class="box-tujuan">
          🎯 <strong>Tujuan Pembelajaran:</strong> ${chap.objective}
        </div>

        <!-- Hero Illustration Banner (Full Width, Centered, Clean with Optional Manual Switcher) -->
        <div class="chapter-hero-card" style="position: relative;">
          <img id="chap-img-${chap.number}" src="${chapImgUrl}" class="chapter-hero-img" alt="Ilustrasi ${chap.title}" onerror="this.src='/assets/cover_illustration.jpg'">
          <div class="chapter-caption">
            🎨 <strong>Ayo Mengamati:</strong> Amatilah gambar di atas yang berkaitan erat dengan tema pembelajaran <em>${chap.title}</em>.
          </div>
          <!-- Quick Image Switcher (Hidden during Print) -->
          <div class="no-print" style="position: absolute; top: 8px; right: 8px; background: rgba(15,23,42,0.8); backdrop-filter: blur(4px); border-radius: 8px; padding: 4px 8px; display: flex; align-items: center; gap: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
            <span style="color: #f8fafc; font-size: 8pt; font-weight: 700;">🖼️ Ganti Gambar:</span>
            <select onchange="document.getElementById('chap-img-${chap.number}').src = this.value" style="font-size: 8.5pt; padding: 2px 6px; border-radius: 4px; background: #ffffff; border: 1px solid #cbd5e1; cursor: pointer; font-weight: 600; color: #0f172a;">
              <option value="${chapImgUrl}">✨ Rekomendasi AI Sesuai Bab</option>
              <option value="/assets/cover_kelas2.jpg">Belajar Huruf Hijaiyah Berharakat</option>
              <option value="/assets/rukun_iman.jpg">Mengenal 6 Rukun Iman</option>
              <option value="/assets/tasbih_zikir.jpg">Menyucikan Allah Swt. (Tasbih & Zikir)</option>
              <option value="/assets/rukun_islam.jpg">Rukun Islam & Dua Kalimat Syahadat</option>
              <option value="/assets/jannah_garden.jpg">Kisah Keteladanan Nabi Adam a.s. / Surga</option>
              <option value="/assets/asmaul_husna.jpg">Asmaul Husna (99 Nama Allah)</option>
              <option value="/assets/sholat_berjamaah.jpg">Shalat Fardhu Berjamaah di Masjid</option>
              <option value="/assets/quran_rehal.jpg">Mushaf Al-Qur'an & Surah Pendek</option>
              <option value="/assets/wudu_girl.jpg">Wudhu & Hidup Bersih Sehat</option>
              <option value="/assets/sedekah_berbagi.jpg">Zakat, Infak, & Sedekah</option>
              <option value="/assets/adab_orangtua.jpg">Adab Orang Tua & Guru</option>
              <option value="/assets/menjaga_alam.jpg">Menjaga Kelestarian Alam</option>
              <option value="/assets/boy_praying.jpg">Doa Khusyuk & Ketakwaan</option>
              <option value="/assets/cover_kelas3.jpg">Juz Amma & Doa di Musholla</option>
              <option value="/assets/cover_kelas4.jpg">Akhlak Mulia & Tolong Menolong</option>
              <option value="/assets/cover_kelas5.jpg">Observasi Alam & Toleransi</option>
            </select>
          </div>
        </div>

        <!-- Sub-Bab A (Full Width, Balanced Typography) -->
        <div class="box-materi">
          <h3>${subA.title}</h3>
          <div class="materi-text">
            ${subA.content.replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>')}
          </div>
        </div>

        <div class="page-footer">
          <span>${bookData.title} Kelas ${bookData.grade}</span>
          <span>Halaman ${(idx * 2) + 3}</span>
        </div>
      </div>

      <!-- ==================== BAB ${chap.number} (BAGIAN 2: PENDALAMAN & LATIHAN) ==================== -->
      <div class="page">
        <div class="page-header">
          <span>BAB ${chap.number}: Pendalaman & Aktivitas</span>
          <span>${bookData.title}</span>
        </div>

        ${subB ? `
        <!-- Sub-Bab B -->
        <div class="box-materi">
          <h3>${subB.title}</h3>
          <div class="materi-text">
            ${subB.content.replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>')}
          </div>
        </div>
        ` : ''}

        ${vocabHtml}
        ${storyHtml}

        ${chap.funActivity ? `
        <div class="box-fun">
          🎉 <strong>Aktivitas Ceria Siswa:</strong><br>${chap.funActivity}
        </div>` : ''}

        ${chap.hotsQuestion ? `
        <div style="background: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 8px; padding: 7px 12px; margin: 6px 0; font-size: 9.5pt;">
          <strong style="color: #15803d;">🧠 Tantangan Nalar Kritis (Soal HOTS):</strong>
          <p style="margin-top: 3px; color: #166534; line-height: 1.45;">${chap.hotsQuestion}</p>
        </div>` : ''}

        <div class="box-latihan">
          <h4>✏️ Ayo Berlatih & Refleksi Karakter (Bab ${chap.number})</h4>
          ${exercisesHtml}
        </div>

        <div class="page-footer">
          <span>${bookData.title} Kelas ${bookData.grade}</span>
          <span>Halaman ${(idx * 2) + 4}</span>
        </div>
      </div>
    `;
  });

  // TOC
  let tocRows = bookData.chapters.map((chap, idx) => {
    const theme = colors[idx % colors.length];
    return `
      <div class="toc-card">
        <div class="toc-badge" style="background: ${theme.badge};">BAB ${chap.number}</div>
        <div style="flex-grow: 1;">
          <strong style="font-size: 11pt; color: #0f172a;">${chap.title}</strong><br>
          <small style="color: #64748b;">${chap.objective}</small>
        </div>
        <span style="font-weight: 800; color: #64748b; font-size: 10pt; min-width: 45px; text-align: right;">Hal. ${(idx * 2) + 3}</span>
      </div>
    `;
  }).join('');

  // Final Assessment (split cleanly across 2 pages for 20+ questions)
  const assessmentList = bookData.finalAssessment || [];
  const part1 = assessmentList.slice(0, 10);
  const part2 = assessmentList.slice(10);

  function renderQuestionList(list, startIndex) {
    return list.map((q, i) => `
      <div class="soal-item" style="margin-bottom: 8px;">
        <strong>${startIndex + i + 1}.</strong> ${q.question}<br>
        <div style="margin-left: 15px; color: #334155; margin-top: 2px;">${q.options.join(' &nbsp;|&nbsp; ')}</div>
      </div>
    `).join('');
  }

  let assessmentPagesHtml = '';
  if (assessmentList.length > 10) {
    assessmentPagesHtml += `
      <div class="page">
        <div class="page-header"><span>Asesmen Sumatif (Bagian 1)</span><span>${bookData.title}</span></div>
        <div class="bab-badge" style="background: #ca8a04;">EVALUASI</div>
        <h2 class="bab-title">Soal Asesmen Sumatif Akhir Semester (Bagian 1)</h2>
        <p style="margin-bottom: 10px; font-weight: 600; font-size: 10.5pt;">Berilah tanda silang (X) pada huruf a, b, atau c di depan jawaban yang paling benar!</p>
        <div style="margin-top: 10px; font-size: 10.5pt;">${renderQuestionList(part1, 0)}</div>
        <div class="page-footer"><span>${bookData.title} Kelas ${bookData.grade}</span><span>Halaman Evaluasi 1</span></div>
      </div>

      <div class="page">
        <div class="page-header"><span>Asesmen Sumatif (Bagian 2)</span><span>${bookData.title}</span></div>
        <div class="bab-badge" style="background: #ca8a04;">EVALUASI</div>
        <h2 class="bab-title">Soal Asesmen Sumatif Akhir Semester (Bagian 2)</h2>
        <div style="margin-top: 10px; font-size: 10.5pt;">${renderQuestionList(part2, 10)}</div>
        <div style="background: #f1f5f9; padding: 12px 14px; border-radius: 8px; margin-top: 15px; font-size: 10pt; border-left: 4px solid #10b981;">
          <strong style="color: #065f46;">🔑 Kunci Jawaban Lengkap (Soal 1 s.d. ${assessmentList.length}):</strong><br>
          <div style="margin-top: 6px; line-height: 1.8;">
            ${assessmentList.map((q, i) => `<b>${i + 1}.</b> ${q.answer}`).join(' &nbsp;|&nbsp; ')}
          </div>
        </div>
        <div class="page-footer"><span>${bookData.title} Kelas ${bookData.grade}</span><span>Halaman Evaluasi 2</span></div>
      </div>

      <!-- ==================== LEMBAR RUBRIK & ASESMEN GURU ==================== -->
      <div class="page" style="justify-content: flex-start;">
        <div class="page-header"><span>Rubrik Penilaian & Asesmen Guru</span><span>${bookData.title}</span></div>
        <div class="bab-badge" style="background: #0284c7;">RUBRIK PENILAIAN</div>
        <h2 class="bab-title" style="margin-bottom: 4px;">📋 Lembar Rubrik Asesmen Otentik Guru</h2>
        <p style="font-size: 9pt; color: #475569; margin-bottom: 6px;">Instrumen Penilaian Ketercapaian Pembelajaran Sesuai ${bookData.curriculum}</p>

        <!-- Identitas Siswa -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 8px; padding: 6px 10px; font-size: 8.5pt; margin-bottom: 6px;">
          <div><strong>Nama Siswa:</strong> ....................................................</div>
          <div><strong>Kelas / Semester:</strong> Kelas ${bookData.grade} / Semester ${bookData.semester}</div>
          <div><strong>Nomor Induk / NISN:</strong> .....................................</div>
          <div><strong>Tanggal Penilaian:</strong> .....................................</div>
        </div>

        <!-- Tabel 1: Rubrik Penilaian Sikap (Profil Pelajar Pancasila & Karakter Islami) -->
        <table style="width: 100%; border-collapse: collapse; font-size: 8pt; margin-bottom: 6px;">
          <thead>
            <tr style="background: #e0f2fe; color: #0369a1;">
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 5%;">No</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 35%; text-align: left;">Aspek Sikap & Karakter (Afektif)</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 15%;">4 (Sangat Baik)</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 15%;">3 (Baik)</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 15%;">2 (Cukup)</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 15%;">1 (Perlu Bimbingan)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">1</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px;">Ketaatan Beribadah & Berdoa Khusyuk</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Selalu taat & mandiri</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Sering taat</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Kadang diingatkan</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Perlu pengawasan</td>
            </tr>
            <tr>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">2</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px;">Kejujuran & Sikap Nalar Kritis (HOTS)</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Sangat jujur & kritis</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Jujur konsisten</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Cukup jujur</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Perlu pembinaan</td>
            </tr>
            <tr>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">3</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px;">Adab Sopan Santun kepada Guru & Orang Tua</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Sangat santun & hormat</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Santun</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Cukup santun</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Perlu bimbingan adab</td>
            </tr>
          </tbody>
        </table>

        <!-- Tabel 2: Rubrik Keterampilan & Pengetahuan -->
        <table style="width: 100%; border-collapse: collapse; font-size: 8pt; margin-bottom: 6px;">
          <thead>
            <tr style="background: #fef3c7; color: #92400e;">
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 5%;">No</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 35%; text-align: left;">Aspek Keterampilan & Pengetahuan</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 15%;">4 (Mahir)</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 15%;">3 (Cakap)</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 15%;">2 (Layak)</th>
              <th style="border: 1px solid #cbd5e1; padding: 3px 5px; width: 15%;">1 (Dasar)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">1</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px;">Pelafalan Bacaan / Praktik Ibadah</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Lancar & tartil benar</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Lancar tajwid cukup</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Terbata tapi bisa</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Perlu bimbingan</td>
            </tr>
            <tr>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">2</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px;">Penguasaan Konsep & Asesmen Sumatif</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Skor > 85</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Skor 75 - 84</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Skor 65 - 74</td>
              <td style="border: 1px solid #cbd5e1; padding: 3px; text-align: center;">Skor < 65</td>
            </tr>
          </tbody>
        </table>

        <!-- Kolom Catatan Guru & Tanda Tangan -->
        <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 8px; padding: 6px 10px; font-size: 8pt; margin-bottom: 6px;">
          <strong>Catatan & Umpan Balik Guru:</strong>
          <div style="height: 20px; border-bottom: 1px dashed #cbd5e1; margin-top: 3px;"></div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-top: auto; padding: 0 15px 4px 15px; font-size: 8.5pt;">
          <div style="text-align: center;">
            Mengetahui,<br><strong>Orang Tua / Wali Siswa</strong><br><br><br>
            ( .................................................... )
          </div>
          <div style="text-align: center;">
            Guru Pengampu,<br><strong>Guru PAI & Budi Pekerti</strong><br><br><br>
            ( .................................................... )
          </div>
        </div>

        <div class="page-footer"><span>${bookData.title} Kelas ${bookData.grade}</span><span>Halaman Penutup & Rubrik</span></div>
      </div>
    `;
  } else {
    assessmentPagesHtml += `
      <div class="page">
        <div class="page-header"><span>Evaluasi Semester</span><span>${bookData.title}</span></div>
        <div class="bab-badge" style="background: #ca8a04;">EVALUASI</div>
        <h2 class="bab-title">Soal Evaluasi Akhir Semester ${bookData.semester}</h2>
        <div style="margin-top: 10px; font-size: 10.5pt;">${renderQuestionList(assessmentList, 0)}</div>
        <div style="background: #f1f5f9; padding: 10px; border-radius: 8px; margin-top: 15px; font-size: 10pt;">
          <strong>🔑 Kunci Jawaban Lengkap:</strong><br>${assessmentList.map((q, i) => `${i + 1}. ${q.answer}`).join(' &nbsp;|&nbsp; ')}
        </div>
        <div class="page-footer"><span>${bookData.title} Kelas ${bookData.grade}</span><span>Halaman Selesai</span></div>
      </div>
    `;
  }

  return `<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>${bookData.title} - Kelas ${bookData.grade}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
    body { font-family: 'Nunito', sans-serif; color: #1e293b; background: #e2e8f0; font-size: 11pt; line-height: 1.5; }
    @page { size: A4 portrait; margin: 0; }
    .page {
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      margin: 15px auto;
      background: #ffffff;
      padding: 10mm 15mm 10mm 15mm;
      position: relative;
      box-shadow: 0 5px 20px rgba(0,0,0,0.1);
      page-break-after: always;
      page-break-inside: avoid;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
    }
    @media print {
      html, body {
        width: 210mm !important;
        margin: 0 !important;
        padding: 0 !important;
        background: transparent !important;
      }
      .page {
        margin: 0 !important;
        box-shadow: none !important;
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        padding: 10mm 15mm 10mm 15mm !important;
        page-break-after: always !important;
        page-break-inside: avoid !important;
        overflow: hidden !important;
      }
      .no-print { display: none !important; }
    }
    .page-header { display: flex; justify-content: space-between; border-bottom: 2px dashed #a7f3d0; padding-bottom: 4px; margin-bottom: 8px; font-size: 9pt; color: #059669; font-weight: 700; text-transform: uppercase; }
    .page-footer { margin-top: auto; display: flex; justify-content: space-between; border-top: 2px dashed #e2e8f0; padding-top: 4px; font-size: 9pt; color: #94a3b8; font-weight: 600; }
    
    /* Cover Page Themed per Grade */
    .cover-page {
      background: ${gradeTheme.gradient};
      border: 5px double ${gradeTheme.border};
      text-align: center;
      padding: 10mm 14mm;
      justify-content: space-between;
    }
    .cover-top-badge {
      display: inline-block;
      background: ${gradeTheme.badgeBg};
      color: white;
      padding: 4px 20px;
      border-radius: 30px;
      font-weight: 700;
      font-size: 10.5pt;
      box-shadow: 0 3px 6px rgba(0,0,0,0.15);
    }
    .cover-title {
      font-size: 22pt;
      font-family: 'Fredoka', sans-serif;
      color: ${gradeTheme.titleColor};
      margin-top: 6px;
      line-height: 1.2;
    }
    .cover-subtitle {
      font-size: 16pt;
      font-family: 'Fredoka', sans-serif;
      color: ${gradeTheme.accent};
    }
    .cover-image-container {
      margin: 6px auto;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-height: 155mm;
    }
    .cover-image-container img {
      max-width: 175mm;
      max-height: 150mm;
      width: auto;
      height: auto;
      border-radius: 14px;
      border: 3px solid ${gradeTheme.border};
      box-shadow: 0 8px 25px rgba(0,0,0,0.12);
      object-fit: contain;
      display: block;
      margin: 0 auto;
    }
    
    .bab-badge { display: inline-flex; align-items: center; color: white; padding: 4px 14px; border-radius: 10px; font-weight: 700; font-size: 10.5pt; font-family: 'Fredoka', sans-serif; }
    .bab-title { font-size: 17pt; font-family: 'Fredoka', sans-serif; color: #064e3b; margin-top: 2px; line-height: 1.2; }
    .box-tujuan { background: #eff6ff; border-left: 5px solid #3b82f6; border-radius: 8px; padding: 6px 10px; margin-bottom: 8px; font-size: 9.5pt; }
    
    /* Hero Illustration Banner (Symmetric, balanced, 48mm height) */
    .chapter-hero-card { margin: 0 auto 12px auto; width: 100%; max-width: 175mm; text-align: center; background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.05); }
    .chapter-hero-img { width: 100%; height: 75mm; object-fit: cover; display: block; margin: 0 auto; }
    .chapter-caption { font-size: 8.8pt; color: #475569; padding: 4px 12px; background: #f1f5f9; border-top: 1px solid #e2e8f0; text-align: center; }
    
    .box-materi { background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 8px 12px; margin-bottom: 6px; }
    .box-materi h3 { font-family: 'Fredoka', sans-serif; color: #0d9488; font-size: 12pt; border-bottom: 1.5px solid #ccfbf1; padding-bottom: 3px; margin-bottom: 6px; }
    .materi-text { font-size: 10.5pt; line-height: 1.6; color: #334155; text-align: justify; }
    
    .box-fun { background: #fefce8; border: 1.5px dashed #facc15; border-radius: 8px; padding: 6px 10px; margin: 6px 0; font-size: 9.5pt; }
    .box-latihan { background: #fdf2f8; border: 1.5px solid #f472b6; border-radius: 8px; padding: 8px 12px; margin-top: 6px; }
    .box-latihan h4 { font-family: 'Fredoka', sans-serif; color: #be185d; font-size: 11pt; margin-bottom: 4px; }
    .soal-item { margin-bottom: 4px; font-size: 9.5pt; line-height: 1.4; }
    .toc-card { display: flex; align-items: center; background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 8px 12px; margin-bottom: 8px; gap: 12px; }
    .toc-badge { padding: 5px 10px; border-radius: 8px; color: white; font-weight: 800; font-size: 10pt; font-family: 'Fredoka', sans-serif; min-width: 60px; text-align: center; }
  </style>
</head>
<body>
  <div style="position: sticky; top: 0; z-index: 999; background: #059669; color: white; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.15);" class="no-print">
    <div><strong>✨ E-Book Siap Cetak:</strong> ${bookData.title} Kelas ${bookData.grade} (${gradeTheme.fase})</div>
    <div style="display: flex; gap: 10px; align-items: center;">
      <button id="btn-toggle-edit" onclick="toggleEditMode()" style="background: #ffffff; color: #065f46; border: none; padding: 6px 16px; border-radius: 20px; font-weight: 700; cursor: pointer; font-size: 10.5pt; display: flex; align-items: center; gap: 6px;">
        ✏️ Edit Teks Langsung
      </button>
      <button onclick="window.print()" style="background: #f59e0b; color: #78350f; border: none; padding: 6px 18px; border-radius: 20px; font-weight: bold; cursor: pointer; font-size: 10.5pt;">🖨️ Cetak / Download PDF</button>
    </div>
  </div>
  <script class="no-print">
    function toggleEditMode() {
      const isEditing = document.body.contentEditable === 'true';
      document.body.contentEditable = !isEditing;
      const btn = document.getElementById('btn-toggle-edit');
      if (!isEditing) {
        btn.innerHTML = '✅ Mode Edit: AKTIF (Klik & ketik teks di lembar)';
        btn.style.background = '#fef08a';
        btn.style.color = '#854d0e';
      } else {
        btn.innerHTML = '✏️ Edit Teks Langsung';
        btn.style.background = '#ffffff';
        btn.style.color = '#065f46';
      }
    }
  </script>

  <!-- COVER THEMED PER GRADE -->
  <div class="page cover-page">
    <div>
      <div class="cover-top-badge">🌟 BUKU SISWA RESMI — ${gradeTheme.fase} 🌟</div>
      <h1 class="cover-title">${bookData.title.toUpperCase()}</h1>
      <div class="cover-subtitle">KELAS ${bookData.grade} SD — SEMESTER ${bookData.semester}</div>
    </div>
    <div class="cover-image-container">
      <img src="${gradeTheme.coverImg}" alt="Cover Kelas ${bookData.grade}" onerror="this.src='/assets/cover_illustration.jpg'">
    </div>
    <div>
      <div style="background: white; border-radius: 12px; padding: 10px 16px; border: 2px solid ${gradeTheme.border}; margin-bottom: 8px;">
        <p style="font-weight: 800; color: ${gradeTheme.titleColor}; font-size: 11.5pt;">📖 ${gradeTheme.coverTag}</p>
      </div>
      <div style="background: #f59e0b; color: white; font-weight: 800; padding: 6px 20px; border-radius: 20px; display: inline-block; font-size: 11pt;">🌿 Sesuai ${bookData.curriculum}</div>
    </div>
  </div>

  <!-- TOC -->
  <div class="page">
    <div class="page-header"><span>Daftar Isi</span><span>${bookData.title} Kelas ${bookData.grade}</span></div>
    <h2 style="font-family: 'Fredoka', sans-serif; color: #064e3b; text-align: center; margin-bottom: 15px;">📑 DAFTAR ISI PEMBELAJARAN</h2>
    ${tocRows}
    <div class="page-footer"><span>${bookData.title} Kelas ${bookData.grade}</span><span>Halaman 2</span></div>
  </div>

  <!-- CHAPTERS (2-PAGE SPREAD PER BAB) -->
  ${chaptersHtml}

  <!-- ASSESSMENT PAGES (20+ SOAL) -->
  ${assessmentPagesHtml}
</body>
</html>`;
}


// Prompt Builder for 8-Page Modul Ajar Deep Learning Per-Bab
function getModulAjarPrompt(subject, grade, semester, curriculum, chapterNumber, chapterTitle, customNotes, referenceText) {
  let prompt = `Anda adalah pakar penyusun modul ajar Kurikulum Merdeka dan konsultan pedagogi Deep Learning untuk Sekolah Dasar (SD) terkemuka di Indonesia.
Tugas Anda adalah menyusun "MODUL AJAR DEEP LEARNING (MINDFUL, MEANINGFUL, JOYFUL) PER-BAB LENGKAP SIAP CETAK (8 HALAMAN)" untuk:
- Mata Pelajaran: ${subject}
- Kelas: ${grade} SD
- Semester: ${semester}
- Bab ke: ${chapterNumber || 1}
- Judul Bab / Topik: ${chapterTitle || "Aku Cinta Al-Qur'an (Mengenal Huruf Hijaiyah & Harakat)"}
- Acuan Kurikulum: ${curriculum || 'CP No. 020 Tahun 2026'}
- Pendekatan: Deep Learning (Mindful, Meaningful, Joyful) berbasis Project Based Learning (PjBL)`;

  if (referenceText && referenceText.trim().length > 0) {
    prompt += `\n\nREFERENSI DOKUMEN MATERI DARI PENGGUNA:\n"""\n${referenceText.substring(0, 25000)}\n"""\nATURAN: Gunakan dan kembangkan materi dari referensi dokumen di atas!`;
  }
  if (customNotes) {
    prompt += `\n\nCATATAN KHUSUS PENGGUNA:\n${customNotes}`;
  }

  prompt += `
Format output WAJIB berupa JSON murni (valid JSON) tanpa awalan/akhiran markdown seperti \`\`\`json.
Struktur JSON yang HARUS dikembalikan:
{
  "subject": "${subject}",
  "grade": "${grade}",
  "semester": "${semester}",
  "curriculum": "${curriculum}",
  "chapterNumber": ${chapterNumber || 1},
  "chapterTitle": "${chapterTitle || 'Topik Pembelajaran'}",
  "theme": "Tema Pembelajaran Ramah Anak",
  "identity": {
    "penyusun": "Guru PAI & Budi Pekerti",
    "instansi": "SD Negeri ...........................................",
    "fase": "Fase A",
    "elemen": "Al-Qur'an dan Hadis",
    "alokasi": "2 Pertemuan (6 Jam Pelajaran @ 35 Menit)",
    "model": "Deep Learning (Mindful, Meaningful, Joyful) berbasis Project Based Learning (PjBL)"
  },
  "cp": "Teks Capaian Pembelajaran resmi sesuai CP No. 020 Tahun 2026 secara lengkap.",
  "tpList": [
    "TP 1.1: Menjelaskan / melafalkan ...",
    "TP 1.2: Mempraktikkan / membedakan ..."
  ],
  "kktp": "Kriteria ketercapaian tujuan pembelajaran konkret...",
  "profilPancasila": [
    { "dimensi": "Beriman & Bertakwa", "deskripsi": "Membaca basmalah dan doa sebelum belajar" },
    { "dimensi": "Gotong Royong", "deskripsi": "Bekerja sama dalam proyek kelompok" },
    { "dimensi": "Mandiri", "deskripsi": "Percaya diri melafalkan materi di depan kelas" },
    { "dimensi": "Bernalar Kritis", "deskripsi": "Menganalisis perbedaan konsep/tanda baca" }
  ],
  "sarana": {
    "media": "LCD Proyektor, Kartu Huruf/Konsep 3D Berwarna, Puzzle Kayu, Gunting Siswa, Audio Murottal",
    "sumber": "Buku Guru & Siswa Kelas ${grade} Kemendikbudristek 2024, Pedoman Tajwid/Iqro', Mushaf Standar Kemenag RI"
  },
  "targetDanPilar": {
    "target": "28 Peserta Didik Reguler Fase A (dilengkapi bimbingan diferensiasi & pengayaan)",
    "pilar": "Mindful (fokus tadabbur), Meaningful (kaitan hidup nyata), Joyful (permainan kartu edukatif)"
  },
  "pemahamanBermakna": "Penjelasan mendalam mengapa materi ini sangat penting bagi kehidupan dunia-akhirat peserta didik...",
  "pertanyaanPemantik": [
    "1. Pertanyaan pemantik 1 yang menggugah rasa ingin tahu siswa...",
    "2. Pertanyaan pemantik 2 yang menghubungkan materi dengan kebiasaan sehari-hari..."
  ],
  "petaAlur": [
    "1. Observasi & Pemahaman Awal",
    "2. Eksplorasi & Artikulasi",
    "3. Pemantapan Makna & Aturan",
    "4. Kreasi Proyek Karya Nyata"
  ],
  "materi": {
    "paragraf1": "Penjelasan paragraf 1 mendalam tentang urgensi topik ini...",
    "paragraf2": "Penjelasan paragraf 2 langkah dan konsep dasar...",
    "subMateriA": {
      "subTitle": "A. Konsep & Pengenalan Inti",
      "content": "Uraian komprehensif sub-materi A minimal 2-3 paragraf panjang..."
    },
    "subMateriB": {
      "subTitle": "B. Kaidah, Praktik & Penerapan",
      "content": "Uraian komprehensif sub-materi B minimal 2-3 paragraf panjang..."
    },
    "adab": "Adab dan budi pekerti terpuji yang menyertai materi ini..."
  },
  "skenario": {
    "pertemuan1": {
      "judul": "Pertemuan 1: Eksplorasi Konsep & Praktik Mandiri (3 JP)",
      "mindful": "Aktivitas pembuka yang menenangkan: hening, doa, tadabbur singkat...",
      "meaningful": "Eksplorasi konsep dan mengaitkan dengan kehidupan nyata siswa...",
      "joyful": "Permainan edukatif, game tebak konsep, atau lagu belajar ceria..."
    },
    "pertemuan2": {
      "judul": "Pertemuan 2: Proyek Karya Kolaboratif & Unjuk Kerja (3 JP)",
      "mindful": "Fokus mengamati contoh proyek karya yang akan dikerjakan...",
      "meaningful": "Bekerja sama dalam kelompok menyelesaikan proyek portofolio...",
      "joyful": "Apresiasi karya, saling memuji hasil proyek teman, dan refleksi bahagia..."
    }
  },
  "lkpd1": {
    "title": "LKPD Pertemuan 1: Lembar Aktivitas Menjodohkan",
    "petunjuk": "Tarik garis lurus dari kotak sebelah kiri ke kotak sebelah kanan yang sesuai!",
    "items": [
      { "left": "Soal / Huruf 1", "right": "Pasangan / Arti 1" },
      { "left": "Soal / Huruf 2", "right": "Pasangan / Arti 2" },
      { "left": "Soal / Huruf 3", "right": "Pasangan / Arti 3" },
      { "left": "Soal / Huruf 4", "right": "Pasangan / Arti 4" }
    ]
  },
  "lkpd2": {
    "title": "LKPD Pertemuan 2: Proyek Flashcard Gunting & Tempel",
    "petunjuk": "Guntinglah kartu-kartu berikut di sepanjang garis putus-putus secara rapi, lalu tempelkan pada lembar kerja portofoliomu!",
    "cards": [
      { "symbol": "Kartu 1", "label": "Keterangan 1", "detail": "Suara / Bunyi 1" },
      { "symbol": "Kartu 2", "label": "Keterangan 2", "detail": "Suara / Bunyi 2" },
      { "symbol": "Kartu 3", "label": "Keterangan 3", "detail": "Suara / Bunyi 3" },
      { "symbol": "Kartu 4", "label": "Keterangan 4", "detail": "Suara / Bunyi 4" },
      { "symbol": "Kartu 5", "label": "Keterangan 5", "detail": "Suara / Bunyi 5" },
      { "symbol": "Kartu 6", "label": "Keterangan 6", "detail": "Suara / Bunyi 6" },
      { "symbol": "Kartu 7", "label": "Keterangan 7", "detail": "Suara / Bunyi 7" },
      { "symbol": "Kartu 8", "label": "Keterangan 8", "detail": "Suara / Bunyi 8" }
    ]
  },
  "asesmen": [
    { "no": 1, "question": "Pertanyaan nomor 1 pemahaman konsep...", "options": ["a. Pilihan 1", "b. Pilihan 2", "c. Pilihan 3"], "answer": "a", "isHots": false },
    { "no": 2, "question": "Pertanyaan nomor 2 penerapan...", "options": ["a. Pilihan 1", "b. Pilihan 2", "c. Pilihan 3"], "answer": "b", "isHots": false },
    { "no": 3, "question": "Pertanyaan nomor 3 pemahaman...", "options": ["a. Pilihan 1", "b. Pilihan 2", "c. Pilihan 3"], "answer": "c", "isHots": false },
    { "no": 4, "question": "Pertanyaan nomor 4 studi kasus nyata...", "options": ["a. Pilihan 1", "b. Pilihan 2", "c. Pilihan 3"], "answer": "a", "isHots": true },
    { "no": 5, "question": "Pertanyaan nomor 5 soal HOTS pemecahan masalah...", "options": ["a. Pilihan 1", "b. Pilihan 2", "c. Pilihan 3"], "answer": "b", "isHots": true }
  ],
  "rubrik": [
    { "kriteria": "Penguasaan Konsep / Pelafalan", "perluBimbingan": "Belum mampu...", "cukup": "Mampu dengan bimbingan...", "baik": "Mampu secara mandiri...", "sangatBaik": "Sangat lancar dan tepat..." },
    { "kriteria": "Penerapan & Kaidah Materi", "perluBimbingan": "Masih keliru...", "cukup": "Tepat sebagian...", "baik": "Tepat dan rapi...", "sangatBaik": "Sangat teliti dan konsisten..." },
    { "kriteria": "Kreativitas & Kerapian Proyek LKPD", "perluBimbingan": "Belum rapi...", "cukup": "Cukup rapi...", "baik": "Rapi dan kreatif...", "sangatBaik": "Sangat rapi, indah, dan inovatif..." },
    { "kriteria": "Sikap Gotong Royong & Karakter", "perluBimbingan": "Pasif...", "cukup": "Mulai terlibat...", "baik": "Aktif bekerja sama...", "sangatBaik": "Sangat antusias, solutif, dan santun..." }
  ]
}`;
  return prompt;
}

// Template Builder for 8-Page Modul Ajar Deep Learning
async function renderModulAjarHtml(modulData) {
  const g = parseInt(modulData.grade) || 1;
  const gradeTheme = getGradeTheme(g, modulData.semester);
  const coverImg = modulData.coverImage || getSmartChapterImage(
    `${modulData.chapterTitle || ''} ${modulData.theme || ''}`,
    `${modulData.materi?.paragraf1 || ''} ${modulData.materi?.subMateriA?.content || ''} ${modulData.subject || ''}`,
    0
  );
  
  const tpItems = (modulData.tpList || []).map(tp => `<li><strong>${tp}</strong></li>`).join('');
  const profilItems = (modulData.profilPancasila || []).map(p => `<div>• <strong>${p.dimensi}:</strong> ${p.deskripsi}</div>`).join('');
  const alurItems = (modulData.petaAlur || []).map(step => `<span style="background: white; padding: 2px 8px; border-radius: 4px; border: 1px solid #cbd5e1;">${step}</span>`).join(' ➔ ');

  const lkpd1Items = (modulData.lkpd1?.items || []).map(item => `
    <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 12px; align-items: center; margin-bottom: 8px;">
      <div style="background: #fdf2f8; border: 2px solid #f472b6; border-radius: 8px; padding: 6px 12px; font-weight: bold; font-size: 11pt; color: #be185d; text-align: center;">${item.left || item.huruf || ''}</div>
      <div style="color: #94a3b8; font-weight: bold;">➔</div>
      <div style="background: #eff6ff; border: 2px solid #60a5fa; border-radius: 8px; padding: 6px 12px; font-weight: 700; font-size: 9.5pt; color: #1e40af; text-align: center;">${item.right || item.arti || item.latin || ''}</div>
    </div>
  `).join('');

  const lkpd2Cards = (modulData.lkpd2?.cards || []).map(card => `
    <div style="border: 2px dashed #059669; background: #ffffff; border-radius: 10px; padding: 8px; text-align: center; position: relative;">
      <span style="position: absolute; top: 2px; right: 4px; font-size: 8pt; color: #94a3b8;">✂️</span>
      <div style="font-size: 22pt; color: #047857; font-weight: bold; font-family: 'Traditional Arabic', serif;">${card.symbol || card.huruf || ''}</div>
      <div style="font-size: 9pt; font-weight: 800; color: #1e293b; margin-top: 2px;">${card.label || card.nama || ''}</div>
      <div style="font-size: 8pt; color: #059669; font-weight: 700;">${card.detail || card.suara || ''}</div>
    </div>
  `).join('');

  const questionsHtml = (modulData.asesmen || []).map((q, idx) => `
    <div style="margin-bottom: 7px; background: ${q.isHots ? '#fffbeb' : '#ffffff'}; border: 1px solid ${q.isHots ? '#f59e0b' : '#e2e8f0'}; border-radius: 8px; padding: 5px 9px; font-size: 9.2pt;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 6px;">
        <div><strong>${idx + 1}. ${q.question}</strong></div>
        ${q.isHots ? '<span style="background: #f59e0b; color: white; font-weight: 800; font-size: 7.5pt; padding: 1px 6px; border-radius: 10px; white-space: nowrap;">🔥 HOTS</span>' : ''}
      </div>
      <div style="margin-top: 3px; margin-left: 10px; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4px; font-size: 8.8pt; color: #334155;">
        ${(q.options || []).map(opt => `<div>${opt}</div>`).join('')}
      </div>
    </div>
  `).join('');

  const rubrikRows = (modulData.rubrik || []).map(r => `
    <tr>
      <td style="padding: 4px 7px; border: 1px solid #cbd5e1; font-weight: 700; color: #166534; background: #f0fdf4;">${r.kriteria}</td>
      <td style="padding: 4px 7px; border: 1px solid #cbd5e1; font-size: 8.2pt;">${r.perluBimbingan}</td>
      <td style="padding: 4px 7px; border: 1px solid #cbd5e1; font-size: 8.2pt;">${r.cukup}</td>
      <td style="padding: 4px 7px; border: 1px solid #cbd5e1; font-size: 8.2pt;">${r.baik}</td>
      <td style="padding: 4px 7px; border: 1px solid #cbd5e1; font-size: 8.2pt;">${r.sangatBaik}</td>
    </tr>
  `).join('');

  return `<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Modul Ajar Deep Learning - ${modulData.subject} Kelas ${modulData.grade} Bab ${modulData.chapterNumber}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
    body { font-family: 'Nunito', sans-serif; color: #1e293b; background: #e2e8f0; font-size: 10pt; line-height: 1.45; }
    @page { size: A4 portrait; margin: 0; }
    .page {
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      margin: 15px auto;
      background: #ffffff;
      padding: 9mm 13mm 9mm 13mm;
      position: relative;
      box-shadow: 0 5px 20px rgba(0,0,0,0.1);
      page-break-after: always;
      page-break-inside: avoid;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
    }
    @media print {
      html, body {
        width: 210mm !important;
        margin: 0 !important;
        padding: 0 !important;
        background: transparent !important;
      }
      .page {
        margin: 0 !important;
        box-shadow: none !important;
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        padding: 9mm 13mm 9mm 13mm !important;
        page-break-after: always !important;
        page-break-inside: avoid !important;
        overflow: hidden !important;
      }
      .no-print { display: none !important; }
    }
    .page-header { display: flex; justify-content: space-between; border-bottom: 2px dashed #a7f3d0; padding-bottom: 3px; margin-bottom: 7px; font-size: 8.5pt; color: #059669; font-weight: 700; text-transform: uppercase; }
    .page-footer { margin-top: auto; display: flex; justify-content: space-between; border-top: 2px dashed #e2e8f0; padding-top: 3px; font-size: 8.5pt; color: #94a3b8; font-weight: 600; }
    
    /* Cover Styling */
    .cover-container {
      background: linear-gradient(180deg, #ecfdf5 0%, #d1fae5 40%, #fef3c7 100%);
      border: 5px double #059669;
      text-align: center;
      padding: 8mm 12mm;
      justify-content: space-between;
    }
    .badge-top { display: inline-block; background: #065f46; color: #fef08a; padding: 4px 18px; border-radius: 20px; font-weight: 800; font-size: 9.5pt; letter-spacing: 0.5px; }
    .title-deep { font-family: 'Fredoka', sans-serif; font-size: 26pt; color: #064e3b; margin-top: 3px; line-height: 1.1; }
    .title-deep span { color: #d97706; font-style: italic; }
    .subtitle-deep { font-family: 'Fredoka', sans-serif; font-size: 13.5pt; color: #047857; margin-top: 2px; }
    .badge-bab { display: inline-flex; align-items: center; gap: 8px; margin-top: 4px; }
    .badge-pill { background: #059669; color: white; padding: 3px 12px; border-radius: 20px; font-weight: 800; font-size: 9pt; }
    .badge-pill.amber { background: #d97706; }
    .badge-pill.teal { background: #0f766e; }

    /* Cover Art Container & Responsive Frame (Adaptive Aspect Ratio, Zero Cut-off, Zero White Box) */
    .cover-art-container {
      margin: 8px auto;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 120mm;
      max-height: 155mm;
      width: 100%;
    }
    .cover-art-img {
      max-width: 175mm;
      max-height: 150mm;
      width: auto;
      height: auto;
      display: block;
      margin: 0 auto;
      border-radius: 12px;
      border: 2.5px solid #059669;
      box-shadow: 0 6px 22px rgba(5,150,105,0.25);
      object-fit: contain;
    }

    .feature-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 5px;
      margin-top: 5px;
    }
    .feature-item {
      background: white;
      border: 1px solid #10b981;
      border-radius: 8px;
      padding: 4px 8px;
      font-size: 8.2pt;
      font-weight: 700;
      color: #065f46;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .section-title {
      font-family: 'Fredoka', sans-serif;
      font-size: 12.5pt;
      color: #065f46;
      border-bottom: 2px solid #a7f3d0;
      padding-bottom: 2px;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .table-info { width: 100%; border-collapse: collapse; font-size: 8.8pt; margin-bottom: 6px; }
    .table-info td { padding: 3.5px 7px; border: 1px solid #cbd5e1; }
    .table-info td.header-col { background: #f0fdf4; font-weight: 700; color: #166534; width: 27%; }

    .card-box {
      background: #ffffff;
      border: 1.5px solid #e2e8f0;
      border-radius: 8px;
      padding: 6px 10px;
      margin-bottom: 6px;
    }
    .card-box.green { border-color: #86efac; background: #f0fdf4; }
    .card-box.amber { border-color: #fcd34d; background: #fffbeb; }
    .card-box.blue { border-color: #93c5fd; background: #eff6ff; }

    .syntax-step {
      display: flex;
      gap: 8px;
      margin-bottom: 5px;
      padding: 5px 8px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #059669;
      border-radius: 6px;
      font-size: 8.8pt;
    }
    .syntax-step .step-badge {
      background: #059669;
      color: white;
      font-weight: 800;
      font-size: 7.8pt;
      padding: 2px 7px;
      border-radius: 12px;
      height: fit-content;
      white-space: nowrap;
    }
    .lkpd-header {
      background: linear-gradient(135deg, #059669, #0f766e);
      color: white;
      padding: 6px 10px;
      border-radius: 8px;
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .lkpd-title { font-family: 'Fredoka', sans-serif; font-size: 12pt; }
    .lkpd-identity {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      background: #f8fafc;
      border: 1.5px dashed #94a3b8;
      border-radius: 8px;
      padding: 5px 10px;
      font-size: 8.2pt;
      margin-bottom: 6px;
    }
  </style>
</head>
<body>

  <!-- TOP BAR CONTROL -->
  <div style="position: sticky; top: 0; z-index: 999; background: #064e3b; color: white; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.2);" class="no-print">
    <div><strong>🌟 MODUL AJAR DEEP LEARNING:</strong> ${modulData.subject} Kelas ${modulData.grade} Bab ${modulData.chapterNumber}</div>
    <div style="display: flex; gap: 10px;">
      <button onclick="window.print()" style="background: #f59e0b; color: #78350f; border: none; padding: 6px 18px; border-radius: 20px; font-weight: bold; cursor: pointer; font-size: 10pt;">🖨️ Cetak / Download PDF (8 Hal)</button>
    </div>
  </div>

  <!-- ==================== HALAMAN 1: COVER MODUL AJAR ==================== -->
  <div class="page cover-container">
    <div>
      <div class="badge-top">🌟 MODUL AJAR UNTUK GURU ${modulData.subject.toUpperCase()} 🌟</div>
      <h1 class="title-deep">MODUL AJAR <span>Deep Learning</span></h1>
      <div class="subtitle-deep">${modulData.subject.toUpperCase()} TERBARU</div>
      <div class="badge-bab">
        <span class="badge-pill">BAB ${modulData.chapterNumber}</span>
        <span class="badge-pill amber">SEMESTER ${modulData.semester}</span>
        <span class="badge-pill teal">KELAS ${modulData.grade} SD</span>
      </div>
      <p style="font-weight: 800; color: #065f46; font-size: 11pt; margin-top: 4px;">📖 Tema: ${modulData.chapterTitle}</p>
    </div>

    <!-- 100% Adaptive Uncropped Artwork (Snug Border, Matches Chapter Title) -->
    <div class="cover-art-container">
      <img class="cover-art-img" src="${coverImg}" alt="Ilustrasi ${modulData.chapterTitle}">
    </div>

    <div>
      <div class="feature-grid">
        <div class="feature-item">✅ Rangkuman Materi Lengkap</div>
        <div class="feature-item">✅ Pendekatan Deep Learning (PjBL)</div>
        <div class="feature-item">✅ LKPD 2 Pertemuan Siswa</div>
        <div class="feature-item">✅ Soal HOTS & Pemecahan Masalah</div>
        <div class="feature-item">✅ Rubrik Penilaian Otentik Guru</div>
        <div class="feature-item">✅ Kartu Peraga Flashcard Gunting</div>
      </div>
      <div style="margin-top: 6px; background: #065f46; color: white; padding: 4px 16px; border-radius: 20px; font-weight: 800; font-size: 9pt; display: inline-block;">
        🌿 Sesuai Capaian Pembelajaran (CP) BKPDM No. 020 Tahun 2026
      </div>
    </div>
  </div>

  <!-- ==================== HALAMAN 2: IDENTITAS & INFORMASI UMUM (FULL SPACE) ==================== -->
  <div class="page">
    <div class="page-header"><span>BAGIAN I: INFORMASI UMUM MODUL AJAR</span><span>${modulData.subject} KELAS ${modulData.grade}</span></div>
    <h2 class="section-title">📋 I. IDENTITAS & DESAIN PEMBELAJARAN</h2>

    <table class="table-info">
      <tr>
        <td class="header-col">Penyusun & Instansi</td>
        <td>${modulData.identity?.penyusun || 'Guru PAI & Budi Pekerti'} / ${modulData.identity?.instansi || 'SD Negeri ...........................................'}</td>
      </tr>
      <tr>
        <td class="header-col">Fase / Kelas / Semester</td>
        <td><strong>${modulData.identity?.fase || 'Fase A'} / Kelas ${modulData.grade} SD / Semester ${modulData.semester}</strong></td>
      </tr>
      <tr>
        <td class="header-col">Elemen Capaian</td>
        <td><strong>${modulData.identity?.elemen || 'Al-Qur\'an dan Hadis'}</strong></td>
      </tr>
      <tr>
        <td class="header-col">Alokasi Waktu</td>
        <td>${modulData.identity?.alokasi || '2 Pertemuan (6 Jam Pelajaran @ 35 Menit)'}</td>
      </tr>
      <tr>
        <td class="header-col">Model & Pendekatan</td>
        <td><strong>${modulData.identity?.model || 'Deep Learning berbasis PjBL'}</strong></td>
      </tr>
    </table>

    <div class="card-box green">
      <strong style="color: #166534; font-size: 9.5pt;">🎯 Capaian Pembelajaran (CP No. 020 Tahun 2026):</strong>
      <p style="margin-top: 2px; font-size: 8.8pt; line-height: 1.45; color: #14532d;">${modulData.cp}</p>
    </div>

    <div class="card-box blue">
      <strong style="color: #1e40af; font-size: 9.5pt;">📌 Tujuan Pembelajaran (TP) & Kriteria Ketercapaian (KKTP):</strong>
      <ul style="margin-left: 16px; margin-top: 3px; font-size: 8.8pt; line-height: 1.45; color: #1e3a8a;">
        ${tpItems}
        <li><strong>KKTP:</strong> ${modulData.kktp}</li>
      </ul>
    </div>

    <div class="card-box amber">
      <strong style="color: #92400e; font-size: 9.5pt;">🌟 Dimensi Profil Pelajar Pancasila & Karakter:</strong>
      <div style="margin-top: 3px; display: grid; grid-template-columns: 1fr 1fr; gap: 4px; font-size: 8.5pt; color: #78350f;">
        ${profilItems}
      </div>
    </div>

    <!-- Media, Sarana & Prasarana -->
    <div class="card-box" style="background: #fafaf9; border-color: #d6d3d1; padding: 5px 8px;">
      <strong style="color: #44403c; font-size: 9.2pt;">🛠️ Sarana, Prasarana & Sumber Belajar:</strong>
      <div style="margin-top: 2px; display: grid; grid-template-columns: 1.2fr 1fr; gap: 6px; font-size: 8.2pt; color: #292524;">
        <div><strong>• Media & Alat:</strong> ${modulData.sarana?.media || 'LCD Proyektor, Kartu Peraga 3D, Puzzle, Gunting & Lem, Audio'}</div>
        <div><strong>• Sumber Belajar:</strong> ${modulData.sarana?.sumber || 'Buku Guru & Siswa Kemendikbudristek, Mushaf Standar Kemenag RI'}</div>
      </div>
    </div>

    <!-- Target & Model Pembelajaran Deep Learning -->
    <div class="card-box" style="background: #fdf4ff; border-color: #f0abfc; padding: 5px 8px;">
      <strong style="color: #86198f; font-size: 9.2pt;">👥 Target Peserta Didik & Kerangka Deep Learning:</strong>
      <div style="margin-top: 2px; display: grid; grid-template-columns: 1fr 1fr; gap: 6px; font-size: 8.2pt; color: #701a75;">
        <div><strong>• Target:</strong> ${modulData.targetDanPilar?.target || '28 Siswa Reguler (diferensiasi bimbingan & pengayaan)'}</div>
        <div><strong>• 3 Pilar:</strong> ${modulData.targetDanPilar?.pilar || 'Mindful (keheningan), Meaningful (relevansi), Joyful (kartu peraga)'}</div>
      </div>
    </div>

    <!-- Pemahaman Bermakna & Pertanyaan Pemantik -->
    <div class="card-box" style="background: #ecfdf5; border-color: #a7f3d0; padding: 5px 8px;">
      <strong style="color: #065f46; font-size: 9.2pt;">💡 Pemahaman Bermakna (Meaningful Learning):</strong>
      <p style="margin-top: 2px; font-size: 8.3pt; color: #047857; line-height: 1.4;">${modulData.pemahamanBermakna}</p>
      <div style="margin-top: 3px; border-top: 1px dashed #6ee7b7; padding-top: 2px;">
        <strong style="color: #065f46; font-size: 8.7pt;">❓ Pertanyaan Pemantik:</strong>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px; margin-top: 1px; font-size: 8.2pt; color: #047857;">
          ${(modulData.pertanyaanPemantik || []).map(q => `<div>${q}</div>`).join('')}
        </div>
      </div>
    </div>

    <!-- Peta Alur Bab -->
    <div style="background: #f1f5f9; border: 1px dashed #94a3b8; border-radius: 6px; padding: 4px 8px; display: flex; align-items: center; justify-content: space-between; font-size: 8pt; font-weight: 700; color: #334155;">
      <span style="color: #0f172a;">🗺️ Alur Belajar:</span>
      ${alurItems}
    </div>

    <div class="page-footer"><span>Modul Ajar Deep Learning — ${modulData.subject} Kelas ${modulData.grade}</span><span>Halaman 2</span></div>
  </div>

  <!-- ==================== HALAMAN 3: MATERI PEMBELAJARAN LENGKAP ==================== -->
  <div class="page">
    <div class="page-header"><span>BAGIAN II: URAIAN MATERI PEMBELAJARAN</span><span>BAB ${modulData.chapterNumber}: ${modulData.chapterTitle.toUpperCase()}</span></div>
    <h2 class="section-title">📖 II. MATERI ESENSIAL: ${modulData.chapterTitle.toUpperCase()}</h2>

    <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
      <div style="flex: 1;">
        <p style="font-size: 9.3pt; line-height: 1.5; text-align: justify; color: #334155;">${modulData.materi?.paragraf1 || ''}</p>
        <p style="font-size: 9.3pt; line-height: 1.5; text-align: justify; color: #334155; margin-top: 4px;">${modulData.materi?.paragraf2 || ''}</p>
      </div>
      <div style="width: 50mm; height: 35mm; border-radius: 10px; overflow: hidden; border: 2px solid #a7f3d0; box-shadow: 0 2px 6px rgba(0,0,0,0.08);">
        <img src="/assets/quran_rehal.jpg" style="width: 100%; height: 100%; object-fit: cover;" alt="Visual Materi">
      </div>
    </div>

    <div class="card-box green">
      <strong style="color: #166534; font-size: 9.8pt;">${modulData.materi?.subMateriA?.subTitle || 'A. Materi Bagian 1'}:</strong>
      <p style="margin-top: 3px; font-size: 9pt; line-height: 1.5; color: #14532d; text-align: justify;">${modulData.materi?.subMateriA?.content || ''}</p>
    </div>

    <div class="card-box blue">
      <strong style="color: #1e40af; font-size: 9.8pt;">${modulData.materi?.subMateriB?.subTitle || 'B. Materi Bagian 2'}:</strong>
      <p style="margin-top: 3px; font-size: 9pt; line-height: 1.5; color: #1e3a8a; text-align: justify;">${modulData.materi?.subMateriB?.content || ''}</p>
    </div>

    <div class="card-box amber">
      <strong style="color: #92400e; font-size: 9.8pt;">🌿 Adab & Budi Pekerti Terpuji:</strong>
      <p style="margin-top: 3px; font-size: 9pt; line-height: 1.5; color: #78350f;">${modulData.materi?.adab || 'Menjaga kebersihan dan adab santun dalam setiap aktivitas belajar.'}</p>
    </div>

    <div class="page-footer"><span>Modul Ajar Deep Learning — ${modulData.subject} Kelas ${modulData.grade}</span><span>Halaman 3</span></div>
  </div>

  <!-- ==================== HALAMAN 4: SKENARIO DEEP LEARNING (PjBL) ==================== -->
  <div class="page">
    <div class="page-header"><span>BAGIAN III: SKENARIO PEMBELAJARAN DEEP LEARNING</span><span>SINTAKS PjBL</span></div>
    <h2 class="section-title">🚀 III. LANGKAH-LANGKAH PEMBELAJARAN (DEEP LEARNING PjBL)</h2>

    <!-- PERTEMUAN 1 -->
    <div class="card-box" style="border-left: 4px solid #059669; margin-bottom: 8px;">
      <h3 style="color: #065f46; font-size: 10.5pt; font-family: 'Fredoka', sans-serif;">📍 ${modulData.skenario?.pertemuan1?.judul || 'Pertemuan 1: Eksplorasi Konsep & Praktik'}</h3>
      <div style="margin-top: 4px;">
        <div class="syntax-step">
          <span class="step-badge" style="background: #0284c7;">1. MINDFUL</span>
          <div><strong>Keheningan & Fokus (Mindful Opening):</strong> ${modulData.skenario?.pertemuan1?.mindful || 'Membaca doa dan fokus tadabbur.'}</div>
        </div>
        <div class="syntax-step">
          <span class="step-badge" style="background: #059669;">2. MEANINGFUL</span>
          <div><strong>Eksplorasi Bermakna (Core Activity):</strong> ${modulData.skenario?.pertemuan1?.meaningful || 'Mengkaji materi dan relevansi dengan kehidupan nyata.'}</div>
        </div>
        <div class="syntax-step">
          <span class="step-badge" style="background: #ea580c;">3. JOYFUL</span>
          <div><strong>Aktivitas Ceria (Joyful Closing):</strong> ${modulData.skenario?.pertemuan1?.joyful || 'Game edukatif dan tepuk anak soleh.'}</div>
        </div>
      </div>
    </div>

    <!-- PERTEMUAN 2 -->
    <div class="card-box" style="border-left: 4px solid #d97706; margin-bottom: 8px;">
      <h3 style="color: #92400e; font-size: 10.5pt; font-family: 'Fredoka', sans-serif;">📍 ${modulData.skenario?.pertemuan2?.judul || 'Pertemuan 2: Proyek Karya Kolaboratif'}</h3>
      <div style="margin-top: 4px;">
        <div class="syntax-step">
          <span class="step-badge" style="background: #0284c7;">1. MINDFUL</span>
          <div><strong>Fokus Perencanaan Proyek:</strong> ${modulData.skenario?.pertemuan2?.mindful || 'Mempersiapkan alat kerja dan pembagian tugas kelompok.'}</div>
        </div>
        <div class="syntax-step">
          <span class="step-badge" style="background: #059669;">2. MEANINGFUL</span>
          <div><strong>Penyelesaian Proyek Karya (PjBL):</strong> ${modulData.skenario?.pertemuan2?.meaningful || 'Membuat karya kartu peraga bersama kelompok.'}</div>
        </div>
        <div class="syntax-step">
          <span class="step-badge" style="background: #ea580c;">3. JOYFUL</span>
          <div><strong>Pameran Karya & Apresiasi Teman:</strong> ${modulData.skenario?.pertemuan2?.joyful || 'Mempresentasikan hasil karya dan refleksi bersama.'}</div>
        </div>
      </div>
    </div>

    <div class="page-footer"><span>Modul Ajar Deep Learning — ${modulData.subject} Kelas ${modulData.grade}</span><span>Halaman 4</span></div>
  </div>

  <!-- ==================== HALAMAN 5: LKPD PERTEMUAN 1 ==================== -->
  <div class="page">
    <div class="page-header"><span>BAGIAN IV: LEMBAR KERJA PESERTA DIDIK (LKPD)</span><span>PERTEMUAN 1</span></div>
    <div class="lkpd-header">
      <div>
        <div class="lkpd-title">📝 ${modulData.lkpd1?.title || 'LKPD Pertemuan 1'}</div>
        <small>Aktivitas Pemahaman Konsep & Pasangan Makna</small>
      </div>
      <div style="background: rgba(255,255,255,0.25); padding: 3px 10px; border-radius: 6px; font-weight: bold; font-size: 8.5pt;">NILAI: ______</div>
    </div>

    <div class="lkpd-identity">
      <div>Nama Siswa: .....................................................</div>
      <div>Kelas / No. Absen: ${modulData.grade} SD / .....</div>
      <div>Hari / Tanggal: .................................................</div>
      <div>Catatan Guru: .................................................</div>
    </div>

    <div class="card-box green">
      <strong style="color: #166534; font-size: 9.5pt;">📌 Petunjuk Pengerjaan:</strong>
      <p style="margin-top: 2px; font-size: 8.8pt; color: #14532d;">${modulData.lkpd1?.petunjuk || 'Tarik garis lurus dari kotak sebelah kiri ke kotak sebelah kanan yang sesuai!'}</p>
    </div>

    <div style="margin: 10px 0;">
      ${lkpd1Items}
    </div>

    <div class="card-box amber" style="margin-top: auto;">
      <strong style="color: #92400e; font-size: 9pt;">😊 Refleksi Perasaan Belajarku Hari Ini:</strong>
      <div style="display: flex; justify-content: space-around; margin-top: 6px; font-size: 14pt;">
        <div>😊 Sangat Bahagia</div>
        <div>🙂 Senang</div>
        <div>😐 Butuh Bantuan</div>
      </div>
    </div>

    <div class="page-footer"><span>Modul Ajar Deep Learning — ${modulData.subject} Kelas ${modulData.grade}</span><span>Halaman 5</span></div>
  </div>

  <!-- ==================== HALAMAN 6: LKPD PERTEMUAN 2 (KARTU GUNTING) ==================== -->
  <div class="page">
    <div class="page-header"><span>BAGIAN V: LKPD PROYEK SISWA (PERTEMUAN 2)</span><span>KARYA KREATIF</span></div>
    <div class="lkpd-header" style="background: linear-gradient(135deg, #d97706, #b45309);">
      <div>
        <div class="lkpd-title">✂️ ${modulData.lkpd2?.title || 'LKPD Pertemuan 2: Proyek Flashcard'}</div>
        <small>Proyek Gunting-Tempel Kartu Peraga Siswa</small>
      </div>
      <div style="background: rgba(255,255,255,0.25); padding: 3px 10px; border-radius: 6px; font-weight: bold; font-size: 8.5pt;">PARAF: ______</div>
    </div>

    <div class="card-box amber">
      <strong style="color: #92400e; font-size: 9.5pt;">📌 Petunjuk Proyek:</strong>
      <p style="margin-top: 2px; font-size: 8.8pt; color: #78350f;">${modulData.lkpd2?.petunjuk || 'Guntinglah kartu-kartu berikut di sepanjang garis putus-putus secara rapi, lalu tempelkan pada lembar kerja portofoliomu!'}</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin: 8px 0;">
      ${lkpd2Cards}
    </div>

    <div style="margin-top: 8px; border: 2px dashed #94a3b8; border-radius: 10px; background: #f8fafc; padding: 12px; min-height: 55mm; text-align: center;">
      <strong style="color: #64748b; font-size: 9pt;">📌 AREA PENEMPELAN HASIL KARYA KELOMPOK SISWA</strong>
      <p style="font-size: 8pt; color: #94a3b8; margin-top: 2px;">Tempelkan kartu-kartu yang sudah digunting rapi di sini bersama kelompokmu.</p>
    </div>

    <div class="page-footer"><span>Modul Ajar Deep Learning — ${modulData.subject} Kelas ${modulData.grade}</span><span>Halaman 6</span></div>
  </div>

  <!-- ==================== HALAMAN 7: ASESMEN SUMATIF & SOAL HOTS ==================== -->
  <div class="page">
    <div class="page-header"><span>BAGIAN VI: ASESMEN SUMATIF BAB</span><span>EVALUASI HASIL BELAJAR</span></div>
    <h2 class="section-title">📝 VI. ASESMEN SUMATIF & SOAL HOTS BAB ${modulData.chapterNumber}</h2>
    
    <div class="card-box green" style="padding: 4px 8px; margin-bottom: 6px;">
      <small style="color: #166534; font-weight: 700;">Petunjuk: Berilah tanda silang (X) pada huruf a, b, atau c pada jawaban yang paling benar!</small>
    </div>

    <div style="margin-top: 4px;">
      ${questionsHtml}
    </div>

    <div style="background: #f1f5f9; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 6px 10px; margin-top: auto; font-size: 8.8pt;">
      <strong>🔑 Kunci Jawaban Lengkap:</strong>
      <div style="margin-top: 2px; color: #065f46; font-weight: bold;">
        ${(modulData.asesmen || []).map((q, i) => `${i + 1}. (${q.answer})`).join(' &nbsp;|&nbsp; ')}
      </div>
    </div>

    <div class="page-footer"><span>Modul Ajar Deep Learning — ${modulData.subject} Kelas ${modulData.grade}</span><span>Halaman 7</span></div>
  </div>

  <!-- ==================== HALAMAN 8: RUBRIK PENILAIAN OTENTIK GURU ==================== -->
  <div class="page">
    <div class="page-header"><span>BAGIAN VII: RUBRIK PENILAIAN OTENTIK GURU</span><span>ASESMEN FORMATIF & SUMATIF</span></div>
    <h2 class="section-title">📊 VII. RUBRIK PENILAIAN OTENTIK GURU (SKOR 1 - 4)</h2>

    <table style="width: 100%; border-collapse: collapse; font-size: 8.2pt; margin-bottom: 8px;">
      <thead>
        <tr style="background: #059669; color: white;">
          <th style="padding: 5px 8px; border: 1px solid #059669; width: 22%;">Kriteria</th>
          <th style="padding: 5px 8px; border: 1px solid #059669; width: 19%;">Perlu Bimbingan (1)</th>
          <th style="padding: 5px 8px; border: 1px solid #059669; width: 19%;">Cukup (2)</th>
          <th style="padding: 5px 8px; border: 1px solid #059669; width: 20%;">Baik (3)</th>
          <th style="padding: 5px 8px; border: 1px solid #059669; width: 20%;">Sangat Baik (4)</th>
        </tr>
      </thead>
      <tbody>
        ${rubrikRows}
      </tbody>
    </table>

    <div class="card-box blue" style="padding: 5px 8px; margin-bottom: 6px;">
      <strong style="color: #1e40af; font-size: 8.8pt;">📐 Pedoman Penskoran:</strong>
      <p style="font-size: 8.2pt; color: #1e3a8a; margin-top: 1px;">
        Nilai Akhir = (Total Skor Perolehan / Skor Maksimal 16) × 100.<br>
        • Kategori: 86–100 (Sangat Mahir) | 71–85 (Cakap) | 56–70 (Berkembang) | &lt;56 (Perlu Pendampingan).
      </p>
    </div>

    <div class="card-box amber" style="padding: 5px 8px; margin-bottom: 6px;">
      <strong style="color: #92400e; font-size: 8.8pt;">🔄 Rencana Tindak Lanjut:</strong>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; font-size: 8.2pt; color: #78350f; margin-top: 2px;">
        <div><strong>• Remedial:</strong> Bimbingan khusus secara fonetik dan tutor sebaya bagi siswa yang belum mencapai KKTP.</div>
        <div><strong>• Pengayaan:</strong> Melafalkan ayat-ayat pendek dalam Juz 'Amma dan proyek memimpin doa kelas.</div>
      </div>
    </div>

    <div style="margin-top: auto; display: flex; justify-content: space-between; font-size: 8.8pt; padding: 0 20px;">
      <div style="text-align: center;">
        Mengetahui,<br>
        Kepala SD Negeri ...........................<br><br><br><br>
        (....................................................)<br>
        NIP. ..............................................
      </div>
      <div style="text-align: center;">
        Guru Mata Pelajaran,<br><br><br><br><br>
        (....................................................)<br>
        NIP. ..............................................
      </div>
    </div>

    <div class="page-footer"><span>Modul Ajar Deep Learning — ${modulData.subject} Kelas ${modulData.grade}</span><span>Halaman 8 (Selesai)</span></div>
  </div>

</body>
</html>`;
}


// API: Generate E-Book Siswa ATAU Modul Ajar Deep Learning Per-Bab
app.post('/api/generate', async (req, res) => {
  try {
    const { 
      mode, 
      subject, 
      grade, 
      semester, 
      curriculum, 
      customNotes, 
      referenceText, 
      chapterNumber, 
      chapterTitle, 
      meetings, 
      modelStyle, 
      provider, 
      apiKey, 
      model, 
      endpoint 
    } = req.body;

    // === MODE: MODUL AJAR PER-BAB ===
    if (mode === 'modul_ajar') {
      console.log(`🚀 Menghasilkan Modul Ajar Deep Learning: ${subject} Kelas ${grade} Bab ${chapterNumber}...`);
      const prompt = getModulAjarPrompt(subject, grade, semester, curriculum, chapterNumber, chapterTitle, customNotes, referenceText);

      let modulData;
      if (provider === 'gemini') {
        if (!apiKey) return res.status(400).json({ error: 'API Key Gemini diperlukan' });
        modulData = await callGemini(prompt, apiKey, model || 'gemini-3.8-flash');
      } else {
        modulData = await callOpenAICompatible(prompt, endpoint || 'http://localhost:11434/v1', apiKey, model);
      }

      if (meetings && modulData.identity) modulData.identity.alokasi = meetings;
      if (modelStyle && modulData.identity) modulData.identity.model = modelStyle;

      // Smart match chapter illustration to chapter title & content accurately
      const smartImg = getSmartChapterImage(
        `${chapterTitle || modulData.chapterTitle || ''} ${modulData.theme || ''}`,
        `${modulData.materi?.paragraf1 || ''} ${modulData.materi?.subMateriA?.content || ''} ${subject || ''}`,
        0
      );
      modulData.coverImage = smartImg;

      const htmlOutput = await renderModulAjarHtml(modulData);
      
      const sanitizedTitle = `Modul_Ajar_${subject}_Kelas_${grade}_Bab_${chapterNumber || 1}`.replace(/[^a-zA-Z0-9_-]/g, '_');
      const fileName = `${sanitizedTitle}_${Date.now()}.html`;
      const filePath = path.join(exportsDir, fileName);
      fs.writeFileSync(filePath, htmlOutput, 'utf8');

      return res.json({
        success: true,
        mode: 'modul_ajar',
        modulData,
        htmlOutput,
        savedFile: `/exports/${fileName}`
      });
    }

    // === MODE: BUKU SISWA 1 SEMESTER (DEFAULT) ===
    console.log(`📘 Menghasilkan E-Book Siswa 1 Semester: ${subject} Kelas ${grade} Sem ${semester}...`);
    let prompt = getSystemPrompt(subject, grade, semester, curriculum, referenceText);
    if (customNotes) {
      prompt += `\n\nCatatan Khusus Pengguna:\n${customNotes}`;
    }

    let bookData;
    if (provider === 'gemini') {
      if (!apiKey) return res.status(400).json({ error: 'API Key Gemini diperlukan' });
      bookData = await callGemini(prompt, apiKey, model || 'gemini-3.8-flash');
    } else {
      bookData = await callOpenAICompatible(prompt, endpoint || 'http://localhost:11434/v1', apiKey, model);
    }

    const htmlOutput = await renderBookHtml(bookData, apiKey);
    
    // Save to exports
    const sanitizedTitle = `${subject}_Kelas_${grade}_Sem_${semester}`.replace(/[^a-zA-Z0-9_-]/g, '_');
    const fileName = `${sanitizedTitle}_${Date.now()}.html`;
    const filePath = path.join(exportsDir, fileName);
    fs.writeFileSync(filePath, htmlOutput, 'utf8');

    res.json({
      success: true,
      mode: 'ebook',
      bookData,
      htmlOutput,
      savedFile: `/exports/${fileName}`
    });
  } catch (err) {
    console.error('Generation Error:', err);
    res.status(500).json({ error: err.message || 'Gagal menghasilkan dokumen' });
  }
});

// Serve exported HTML files
app.use("/exports", express.static(exportsDir));

app.listen(PORT, () => {
  console.log(`🚀 E-Book AI Generator Server berjalan di http://localhost:${PORT}`);
});
