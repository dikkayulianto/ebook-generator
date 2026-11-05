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
function getGradeTheme(grade) {
  const g = parseInt(grade) || 1;
  const themes = {
    1: {
      fase: "FASE A",
      gradient: "linear-gradient(180deg, #ecfdf5 0%, #d1fae5 45%, #fef3c7 100%)",
      border: "#059669",
      accent: "#b45309",
      titleColor: "#064e3b",
      badgeBg: "#059669",
      coverImg: "/assets/cover_illustration.jpg",
      coverTag: "Mengenal Dasar Keislaman & Budi Pekerti"
    },
    2: {
      fase: "FASE A",
      gradient: "linear-gradient(180deg, #f0f9ff 0%, #e0f2fe 45%, #fef3c7 100%)",
      border: "#0284c7",
      accent: "#0369a1",
      titleColor: "#0c4a6e",
      badgeBg: "#0284c7",
      coverImg: "/assets/cover_kelas2.jpg",
      coverTag: "Belajar Huruf Bersambung & Ketaatan Ibadah"
    },
    3: {
      fase: "FASE B",
      gradient: "linear-gradient(180deg, #faf5ff 0%, #ede9fe 45%, #fef3c7 100%)",
      border: "#7c3aed",
      accent: "#6d28d9",
      titleColor: "#4c1d95",
      badgeBg: "#7c3aed",
      coverImg: "/assets/cover_kelas3.jpg",
      coverTag: "Mendalami Shalat, Zikir, & Sifat Terpuji"
    },
    4: {
      fase: "FASE B",
      gradient: "linear-gradient(180deg, #fff7ed 0%, #ffedd5 45%, #fef3c7 100%)",
      border: "#ea580c",
      accent: "#c2410c",
      titleColor: "#7c2d12",
      badgeBg: "#ea580c",
      coverImg: "/assets/cover_kelas4.jpg",
      coverTag: "Memahami Tanda Baligh & Akhlak Mulia"
    },
    5: {
      fase: "FASE C",
      gradient: "linear-gradient(180deg, #f0fdf4 0%, #dcfce7 45%, #fef3c7 100%)",
      border: "#16a34a",
      accent: "#15803d",
      titleColor: "#14532d",
      badgeBg: "#16a34a",
      coverImg: "/assets/cover_kelas5.jpg",
      coverTag: "Menerapkan Toleransi, Zakat, & Ukhuwah"
    },
    6: {
      fase: "FASE C",
      gradient: "linear-gradient(180deg, #fdf2f8 0%, #fce7f3 45%, #fef3c7 100%)",
      border: "#db2777",
      accent: "#be185d",
      titleColor: "#831843",
      badgeBg: "#db2777",
      coverImg: "/assets/cover_kelas6.jpg",
      coverTag: "Memantapkan Iman Hari Akhir & Kepemimpinan"
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

  // === PRIORITY 1: MATCH BY CHAPTER TITLE (Highest Accuracy) ===

  // 1. Tasbih / Menyucikan Allah / Zikir / Subhanallah
  if (t.match(/tasbih|subhanallah|menyucikan\s+allah|zikir|memuji\s+allah/)) {
    return pick(['/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }

  // 2. Rukun Islam / Syahadat / Syahadatain / Dua Kalimat Syahadat
  if (t.match(/rukun\s+islam|syahadat|syahadatain|kalimat\s+syahadat/)) {
    return pick(['/assets/rukun_islam.jpg', '/assets/boy_praying.jpg']);
  }

  // 3. Rukun Iman / 6 Rukun Iman / Meyakini Rukun Iman
  if (t.match(/rukun\s+iman|enam\s+rukun\s+iman|iman\s+kepada|meyakini\s+rukun\s+iman/)) {
    return pick(['/assets/rukun_iman.jpg', '/assets/boy_praying.jpg']);
  }
  
  // 4. Shalat / Salat / Ibadah Fardhu / Sujud
  if (t.match(/salat|sholat|solat|sujud|ruku|adzan|iqamah|waktu|fardu/)) {
    return pick(['/assets/sholat_berjamaah.jpg', '/assets/boy_praying.jpg']);
  }

  // 5. Asmaul Husna / Sifat-Sifat Allah
  if (t.match(/asmaul|husna|nama.*allah|ar-rahman|ar-rahim|al-quddus|as-salam|al-malik|al-mu'min|tauhid/)) {
    return pick(['/assets/asmaul_husna.jpg', '/assets/boy_praying.jpg']);
  }

  // 6. Hijaiyah / Huruf Arab / Makhraj / Harakat / Bersambung
  if (t.match(/hijaiyah|harakat|huruf|makhraj|makhārijul|bersambung|tanwin|fathah|kasrah|dhammah/)) {
    return pick(['/assets/cover_kelas2.jpg', '/assets/quran_rehal.jpg']);
  }

  // 7. Surah / Al-Qur'an / Membaca Al-Qur'an / Juz Amma
  if (t.match(/surah|an-nas|al-falaq|al-fatihah|al-ikhlas|qur'?an|tadarus|tajwid|tartil|tilawah/)) {
    return pick(['/assets/quran_rehal.jpg', '/assets/cover_kelas3.jpg']);
  }

  // 8. Wudhu / Thaharah / Bersuci / PHBS / Pola Hidup Bersih & Sehat
  if (t.match(/wudhu|wudu|thaharah|bersuci|istinja|mandi|najis|cuci|bersih|phbs|sehat/)) {
    return pick(['/assets/wudu_girl.jpg', '/assets/menjaga_alam.jpg']);
  }

  // 9. Zakat / Sedekah / Infaq / Berbagi / Tolong Menolong
  if (t.match(/zakat|sedekah|infaq|infak|berbagi|dermawan|kedermawanan|tolong|peduli/)) {
    return pick(['/assets/sedekah_berbagi.jpg', '/assets/cover_kelas4.jpg']);
  }

  // 10. Adab / Sopan Santun / Hormat Orang Tua & Guru
  if (t.match(/orang\s*tua|ibu|ayah|guru|adab|sopan|hormat|santun|birrul|akhlak/)) {
    return pick(['/assets/adab_orangtua.jpg', '/assets/cover_kelas4.jpg']);
  }

  // 11. Menjaga Alam / Lingkungan / Ciptaan Allah
  if (t.match(/alam|lingkungan|pohon|tanaman|bumi|ciptaan|hewan|flora|fauna/)) {
    return pick(['/assets/menjaga_alam.jpg', '/assets/cover_kelas5.jpg']);
  }

  // 12. Kisah Nabi / Rasul / Sahabat / Keteladanan / Adam / Ibrahim / Muhammad / Surga
  if (t.match(/nabi|rasul|kisah|mukjizat|adam|ibrahim|muhammad|hijrah|sahabat|surga|jannah/)) {
    return pick(['/assets/jannah_garden.jpg', '/assets/cover_kelas5.jpg']);
  }

  // 13. Doa / Ketakwaan / Hari Akhir
  if (t.match(/doa|kiamat|hari\s*akhir|takdir|qada|qadar/)) {
    return pick(['/assets/boy_praying.jpg', '/assets/tasbih_zikir.jpg']);
  }

  // === PRIORITY 2: MATCH BY CONTENT (Strict Multi-word Phrases) ===
  if (c.match(/kalimat\s+tasbih|ucapan\s+subhanallah|membaca\s+tasbih|berzikir/)) {
    return pick(['/assets/tasbih_zikir.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/lima\s+rukun\s+islam|dua\s+kalimat\s+syahadat|syahadatain/)) {
    return pick(['/assets/rukun_islam.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/enam\s+rukun\s+iman|iman\s+kepada\s+allah|iman\s+kepada\s+malaikat/)) {
    return pick(['/assets/rukun_iman.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/melaksanakan\s+salat|shalat\s+berjamaah|bacaan\s+ruku|bacaan\s+sujud|salat\s+fardu/)) {
    return pick(['/assets/sholat_berjamaah.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/asmaul\s*husna|ar-rahman|ar-rahim|al-quddus|as-salam|al-malik|al-mu'min/)) {
    return pick(['/assets/asmaul_husna.jpg', '/assets/boy_praying.jpg']);
  }
  if (c.match(/huruf\s+hijaiyah|harakat|tanda\s+baca\s+arab|makharijul/)) {
    return pick(['/assets/cover_kelas2.jpg', '/assets/quran_rehal.jpg']);
  }
  if (c.match(/surah\s+an-nas|surah\s+al-falaq|surah\s+al-fatihah|al-qur'?an\s+adalah|membaca\s+surah/)) {
    return pick(['/assets/quran_rehal.jpg', '/assets/cover_kelas3.jpg']);
  }
  if (c.match(/tata\s+cara\s+wudhu|berwudhu|rukun\s+wudhu|hidup\s+bersih|kebersihan/)) {
    return pick(['/assets/wudu_girl.jpg', '/assets/menjaga_alam.jpg']);
  }
  if (c.match(/mengeluarkan\s+zakat|bersedekah|infak|memberi\s+bantuan/)) {
    return pick(['/assets/sedekah_berbagi.jpg', '/assets/cover_kelas4.jpg']);
  }
  if (c.match(/berbakti\s+kepada\s+orang\s*tua|menghormati\s+guru|sopan\s+santun/)) {
    return pick(['/assets/adab_orangtua.jpg', '/assets/cover_kelas4.jpg']);
  }
  if (c.match(/menjaga\s+kelestarian|merawat\s+lingkungan|ciptaan\s+allah\s+di\s+bumi/)) {
    return pick(['/assets/menjaga_alam.jpg', '/assets/cover_kelas5.jpg']);
  }
  if (c.match(/kisah\s+nabi|keteladanan\s+rasul|nabi\s+adam|mukjizat/)) {
    return pick(['/assets/jannah_garden.jpg', '/assets/cover_kelas5.jpg']);
  }

  // === PRIORITY 3: ROTATING DIVERSE FALLBACKS ===
  const diverseLibrary = [
    '/assets/tasbih_zikir.jpg',
    '/assets/rukun_islam.jpg',
    '/assets/rukun_iman.jpg',
    '/assets/cover_kelas2.jpg',
    '/assets/asmaul_husna.jpg',
    '/assets/sholat_berjamaah.jpg',
    '/assets/quran_rehal.jpg',
    '/assets/wudu_girl.jpg',
    '/assets/sedekah_berbagi.jpg',
    '/assets/adab_orangtua.jpg',
    '/assets/menjaga_alam.jpg',
    '/assets/jannah_garden.jpg',
    '/assets/boy_praying.jpg'
  ];
  return pick(diverseLibrary);
}

// Template Builder: Convert JSON into Printable A4 HTML with Balanced Two-Spread Layout
async function renderBookHtml(bookData, apiKey) {
  const gradeTheme = getGradeTheme(bookData.grade);

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
    .cover-page { background: ${gradeTheme.gradient}; border: 5px double ${gradeTheme.border}; text-align: center; padding: 10mm 14mm; justify-content: space-between; }
    .cover-top-badge { display: inline-block; background: ${gradeTheme.badgeBg}; color: white; padding: 4px 20px; border-radius: 30px; font-weight: 700; font-size: 10.5pt; box-shadow: 0 3px 6px rgba(0,0,0,0.15); }
    .cover-title { font-size: 22pt; font-family: 'Fredoka', sans-serif; color: ${gradeTheme.titleColor}; margin-top: 6px; line-height: 1.2; }
    .cover-subtitle { font-size: 16pt; font-family: 'Fredoka', sans-serif; color: ${gradeTheme.accent}; }
    .cover-image-container { margin: 8px auto; width: 100%; max-width: 175mm; height: 162mm; border-radius: 16px; overflow: hidden; border: 4px solid #fff; box-shadow: 0 8px 25px rgba(0,0,0,0.12); background: #ffffff; display: flex; align-items: center; justify-content: center; }
    .cover-image-container img { width: 100%; height: 100%; object-fit: contain; display: block; margin: 0 auto; }
    
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

// API: Generate E-Book
app.post('/api/generate', async (req, res) => {
  try {
    const { subject, grade, semester, curriculum, customNotes, referenceText, provider, apiKey, model, endpoint } = req.body;
    let prompt = getSystemPrompt(subject, grade, semester, curriculum, referenceText);
    if (customNotes) {
      prompt += `\n\nCatatan Khusus Pengguna:\n${customNotes}`;
    }

    let bookData;
    if (provider === 'gemini') {
      if (!apiKey) return res.status(400).json({ error: 'API Key Gemini diperlukan' });
      bookData = await callGemini(prompt, apiKey, model || 'gemini-3.8-flash');
    } else {
      // Hermes / Local LLM / Ollama
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
      bookData,
      htmlOutput,
      savedFile: `/exports/${fileName}`
    });
  } catch (err) {
    console.error('Generation Error:', err);
    res.status(500).json({ error: err.message || 'Gagal menghasilkan e-book' });
  }
});

// Serve exported HTML files
app.use('/exports', express.static(exportsDir));

app.listen(PORT, () => {
  console.log(`🚀 E-Book AI Generator Server berjalan di http://localhost:${PORT}`);
});
