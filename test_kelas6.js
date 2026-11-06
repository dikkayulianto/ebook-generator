const fs = require('fs');
const serverCode = fs.readFileSync('server.js', 'utf8');

const fnMatch = serverCode.match(/function getSmartChapterImage[\s\S]*?\n\}/);
if (fnMatch) {
  eval(fnMatch[0]);

  const titlesKelas6 = [
    "Membaca, Menulis, dan Membedakan Huruf Hijaiyah Bersambung Serta Bacaan Gunnah",
    "Menjelaskan Surah Pendek Al-Insyirāḥ",
    "Memahami Asmaulhusna: Al-Waliyy, Al-Ḥamīd, Al-‘Adl, dan Aṣ-Ṣabūr",
    "Akhlak Terhadap Tetangga dan Nonmuslim Serta Zakat, Infak, dan Sedekah",
    "Kisah Teladan Kepemimpinan Khulafaurasyidin: Abu Bakar aṣ-Ṣiddīq dan Umar bin Khattab"
  ];

  console.log("=== VERIFIKASI KELAS 6 ===");
  let used6 = new Set(["/assets/cover_penjualan_buku_kelas6.jpg"]);
  titlesKelas6.forEach((t, i) => {
    const matched = getSmartChapterImage(t, '', i, used6);
    console.log(`Bab ${i+1}: ${t}\n -> ${matched}`);
  });
}
