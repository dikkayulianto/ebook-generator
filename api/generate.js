// Vercel Serverless Function: api/generate.js
// Handles structured, rich Indonesian Jabar Beraksi evidence document generation

module.exports = async function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
  );

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method Not Allowed' });
    return;
  }

  try {
    const { indicatorName, evidenceTypes, extraNotes, schoolInfo, apiKey: clientApiKey, model: requestedModel } = req.body || {};

    if (!indicatorName) {
      res.status(400).json({ error: 'Nama indikator wajib diisi.' });
      return;
    }

    const apiKey = (clientApiKey || process.env.GEMINI_API_KEY || '').trim();
    if (!apiKey) {
      res.status(400).json({ error: 'API Key Google Gemini belum diatur. Masukkan API Key pada input web atau konfigurasi environment.' });
      return;
    }

    const sch = schoolInfo || {
      name: 'SD NEGERI 1 KESAMBI',
      address: 'Jalan Kesambi No. 24, Kota Cirebon',
      ks: 'Dra. Hj. Siti Maryam, M.Pd',
      ks_nip: '197505121998032004',
      pengawas: 'Ari Haerani, S.Pd.SD, M.Pd',
      year: '2026'
    };

    const prompt = `Anda adalah Tim Ahli Kurikulum dan Pengawas Resmi Dinas Pendidikan Jawa Barat / Kota Cirebon.
TUGAS UTAMA: Susun naskah dokumen resmi BUKTI FISIK PEMANTAUAN PENGUATAN KARAKTER JABAR BERAKSI untuk satuan pendidikan secara LENGKAP, MENDALAM, DAN MEMILIKI STRUKTUR KEDINASAN BAKU.

WAJIB MEMATUHI SELURUH ATURAN BERIKUT:
1. DILARANG KERAS MENGGUNAKAN BAHASA INGGRIS! Wajib 100% menggunakan Bahasa Indonesia baku kedinasan.
2. DILARANG MEMBERIKAN JAWABAN RINGKAS / PENDEK! Tuliskan setiap bagian secara komprehensif, naratif, jelas, dan realistis untuk sekolah dasar.
3. OUTPUT HARUS MEMILIKI 4 BAGIAN UTAMA DENGAN SISTEMATIKA PERSIS SEPERTI INI:

PEMERINTAH KOTA CIREBON
DINAS PENDIDIKAN
${sch.name.toUpperCase()}
Alamat: ${sch.address}

BUKTI FISIK INSTRUMEN JABAR BERAKSI
INDIKATOR: ${indicatorName.toUpperCase()}
BUKTI FISIK YANG DIMINTA: ${evidenceTypes || 'Surat Tugas, Laporan Kegiatan, Jurnal Log Pembiasaan, Dokumentasi'}

BAGIAN I: SURAT TUGAS RESMI KEPALA SEKOLAH
Nomor: 421.2 / 092 / SD-KS / X / ${sch.year || '2026'}
- Dasar Penugasan: Program Penguatan Pendidikan Karakter (PPK) Jabar Beraksi & Rencana Kerja Tahunan (RKT) ${sch.name}.
- Pejabat Pemberi Tugas: Kepala Sekolah ${sch.name} (${sch.ks}, NIP. ${sch.ks_nip}).
- Personel yang Ditugaskan: Pembina Kesiswaan, Seluruh Guru Kelas (Kelas I s.d. VI), Guru Pendamping, Komite Sekolah, dan Siswa.
- Uraian Tugas: Perencanaan matang, pelaksanaan pembiasaan harian, pembimbingan budi pekerti, serta pelaporan evaluasi berkala.
- Waktu & Lokasi: Terjadwal rutin setiap pekan di lingkungan ${sch.name} dan sekitarnya.

BAGIAN II: LAPORAN PELAKSANAAN KEGIATAN PEMBIASAAN
- Nama Program: Pembiasaan Karakter ${indicatorName}
- Latar Belakang & Tujuan: Menanamkan nilai luhur budi pekerti, ketertiban, empati, dan integritas siswa secara konsisten dan terukur.
- Ruang Lingkup Aktivitas: Jabarkan minimal 3 aktivitas konkret nyata di sekolah (misal: pembiasaan pagi ceria, pendampingan wali kelas, dan kegiatan apresiasi).
- Sasaran & Keterlibatan: Diikuti seluruh siswa kelas 1 s.d. 6 dengan bimbingan dewan guru dan dukungan paguyuban orang tua murid.
- Capaian & Dampak Positif: Partisipasi aktif mencapai >95%, terbentuk budaya positif dan karakter unggul pada siswa.
- Kendala Lapangan: Uraikan kendala riil (seperti penyesuaian waktu dan konsistensi siswa di rumah) serta solusi solutif yang telah diterapkan.
- Rencana Tindak Lanjut: Integrasi berkelanjutan dalam modul ajar intrakurikuler dan Projek Penguatan Profil Pelajar Pancasila (P5).

BAGIAN III: TABEL FORMAT JURNAL / BUKU LOG KEGIATAN PEMBIASAAN
Formatkan dalam tabel markdown berikut dengan data riil:
| No | Hari / Tanggal | Aktivitas Pembiasaan | Catatan Hasil Pengamatan Afektif | Status Keterlaksanaan |
| 1 | Senin, 14/09/${sch.year || '2026'} | Sosialisasi awal dan pelaksanaan pembiasaan pagi di lapangan dan kelas | Seluruh siswa antusias, tertib, dan aktif mendengarkan arahan guru pembina | Terlaksana (100%) |
| 2 | Rabu, 07/10/${sch.year || '2026'} | Pemantauan berkala dan pendampingan khusus oleh wali kelas | 96% siswa konsisten mempraktikkan kebiasaan positif secara mandiri | Terlaksana (98%) |
| 3 | Jumat, 23/10/${sch.year || '2026'} | Rekapitulasi evaluasi bulanan dan pemberian apresiasi bintang karakter | Terjadi peningkatan disiplin dan keharmonisan hubungan antarsiswa di kelas | Terlaksana (100%) |

BAGIAN IV: LEMBAR DOKUMENTASI FOTO & PENGESAHAN KEPALA SEKOLAH
- Keterangan Foto Dokumentasi 1: Pelaksanaan pembiasaan terprogram bersama seluruh peserta didik dan dewan guru di lingkungan sekolah.
- Keterangan Foto Dokumentasi 2: Evaluasi berkala dan koordinasi tindak lanjut bersama wali murid / paguyuban kelas.

Mengetahui,
Kepala ${sch.name}

${sch.ks}
NIP. ${sch.ks_nip}`;

    // Candidates models to query
    const modelsToTry = [
      requestedModel && requestedModel !== 'auto' ? requestedModel : null,
      'gemini-1.5-flash',
      'gemini-1.5-flash-latest',
      'gemini-2.0-flash',
      'gemini-2.5-flash'
    ].filter(Boolean);

    let generatedText = null;
    let lastError = null;

    for (const m of modelsToTry) {
      // Filter out any non-text or TTS models
      if (m.includes('tts') || m.includes('audio') || m.includes('embedding')) continue;

      for (const ver of ['v1beta', 'v1']) {
        try {
          const url = `https://generativelanguage.googleapis.com/${ver}/models/${m}:generateContent?key=${apiKey}`;
          const geminiRes = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] })
          });

          if (geminiRes.ok) {
            const data = await geminiRes.json();
            generatedText = data.candidates?.[0]?.content?.parts?.[0]?.text;
            if (generatedText) break;
          } else {
            const errData = await geminiRes.json().catch(() => ({}));
            lastError = new Error(`${geminiRes.status}: ${errData.error?.message || geminiRes.statusText}`);
          }
        } catch (netErr) {
          lastError = netErr;
        }
      }
      if (generatedText) break;
    }

    if (!generatedText) {
      throw lastError || new Error('Gagal memperoleh respons dari Google Gemini API.');
    }

    res.status(200).json({
      success: true,
      indicator: indicatorName,
      content: generatedText,
      school: sch
    });
  } catch (err) {
    console.error('API Generate Error:', err);
    res.status(500).json({ error: err.message });
  }
};
