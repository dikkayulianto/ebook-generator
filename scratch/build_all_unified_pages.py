import os
import json
from build_all_product_pages import GRADES_DATA

PASTEL_THEMES = [
    {"bg": "bg-[#e8f8f0]", "border": "border-[#10b981]/20", "pill": "bg-emerald-600", "text": "text-emerald-950"},
    {"bg": "bg-[#f3effe]", "border": "border-[#8b5cf6]/20", "pill": "bg-purple-600", "text": "text-purple-950"},
    {"bg": "bg-[#fff1eb]", "border": "border-[#f97316]/20", "pill": "bg-orange-600", "text": "text-orange-950"},
    {"bg": "bg-[#eff6ff]", "border": "border-[#3b82f6]/20", "pill": "bg-blue-600", "text": "text-blue-950"},
    {"bg": "bg-[#fef9c3]", "border": "border-[#eab308]/30", "pill": "bg-amber-600", "text": "text-amber-950"},
]

def render_bab_list(bab_list):
    html = ""
    for idx, (title, desc) in enumerate(bab_list):
        theme = PASTEL_THEMES[idx % len(PASTEL_THEMES)]
        html += f"""
        <div class="p-3.5 rounded-2xl {theme['bg']} border {theme['border']} flex items-start gap-3">
          <span class="w-6 h-6 rounded-full {theme['pill']} text-white font-bold text-xs flex items-center justify-center shrink-0">{idx+1}</span>
          <div>
            <h3 class="font-bold {theme['text']} text-sm">{title}</h3>
            <p class="text-slate-600 text-xs sm:text-sm mt-0.5">{desc}</p>
          </div>
        </div>"""
    return html

# ========================================================
# 1. MODUL AJAR (KELAS 1-6)
# ========================================================
def generate_modul_page(grade):
    data = GRADES_DATA[grade]
    fase = data["fase"]
    title = f"Modul Ajar PAI Kelas {grade} SD Kurikulum Merdeka (Deep Learning)"
    desc = f"Modul ajar Deep Learning PAI Kelas {grade} SD Kurikulum Merdeka 8 halaman lengkap dengan LKPD dan rubrik KKTP format Word dan PDF."
    canonical = f"https://bahanajarbuguru.my.id/modul-ajar-pai-kelas-{grade}.html"
    cover_img = "/assets/cover_illustration.jpg"
    preview_img = "/assets/carousel_modul_ajar_slide2.jpg"

    bab_html = render_bab_list(data["bab_list"])

    other_modul_links = "".join([
        f"""<a href="/modul-ajar-pai-kelas-{g}.html" class="p-3.5 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 text-xs font-semibold flex items-center justify-between text-slate-800 hover:text-emerald-950 transition-colors">
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
  <meta property="og:image" content="https://bahanajarbuguru.my.id{cover_img}">
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
        "image": "https://bahanajarbuguru.my.id{cover_img}",
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
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Apakah file modul ajar bisa diedit?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Bisa. Modul disediakan dalam format Microsoft Word (.docx) lengkap sehingga guru bebas mengedit identitas sekolah, tujuan, dan alokasi waktu."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Apa yang dimaksud dengan pendekatan Deep Learning?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Modul ajar mengintegrasikan 3 pilar: Mindful Learning (kesadaran penuh), Meaningful Learning (kebermaknaan kontekstual), dan Joyful Learning (kegiatan menyenangkan ramah anak)."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Apakah sudah dilengkapi LKPD dan Rubrik KKTP?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Ya, modul 8 halaman mencakup Lembar Kerja Peserta Didik (LKPD) berdiferensiasi serta rubrik Kriteria Ketercapaian Tujuan Pembelajaran (KKTP)."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <!-- Tailwind CSS & Fonts matching Homepage Theme -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Outfit"', '"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
          }},
          colors: {{
            canvas: '#ccebe0',
            appBg: '#faf7f2',
            sidebarBg: '#f3eee8',
            panelBg: '#f5efe6',
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

  <style>
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: #faf7f2; }}
    ::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 9999px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #94a3b8; }}
  </style>
</head>
<body class="bg-canvas min-h-screen p-2 sm:p-4 lg:p-6 flex flex-col justify-start items-center font-sans antialiased text-slate-800">

  <!-- MAIN APP MOCKUP CONTAINER -->
  <div class="w-full max-w-[1400px] bg-appBg rounded-[28px] sm:rounded-[36px] shadow-2xl shadow-emerald-950/15 border border-[#e5dfd5] overflow-hidden flex flex-col">

    <!-- TOP WINDOW CHROME -->
    <div class="bg-white/80 backdrop-blur border-b border-[#ece6dc] px-4 sm:px-6 py-3 flex items-center justify-between gap-4 select-none sticky top-0 z-40">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-[#ff5f56] border border-[#e0443e] inline-block"></span>
        <span class="w-3 h-3 rounded-full bg-[#ffbd2e] border border-[#dea123] inline-block"></span>
        <span class="w-3 h-3 rounded-full bg-[#27c93f] border border-[#1aab29] inline-block"></span>
      </div>

      <div class="flex-1 max-w-md mx-auto hidden sm:flex items-center justify-center gap-2 px-3.5 py-1 rounded-full bg-slate-100/90 border border-slate-200/80 text-xs text-slate-700 font-medium">
        <svg class="w-3 h-3 text-emerald-600" viewBox="0 0 24 24" fill="currentColor">
          <path fill-rule="evenodd" d="M12 1.5a5.25 5.25 0 00-5.25 5.25v3a3 3 0 00-3 3v6.75a3 3 0 003 3h10.5a3 3 0 003-3v-6.75a3 3 0 00-3-3v-3c0-2.9-2.35-5.25-5.25-5.25zm3.75 8.25v-3a3.75 3.75 0 00-7.5 0v3h7.5z" clip-rule="evenodd" />
        </svg>
        <span class="truncate font-semibold">bahanajarbuguru.my.id/modul-ajar-pai-kelas-{grade}.html</span>
      </div>

      <div class="flex items-center gap-2">
        <a href="/" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 text-xs font-bold border border-slate-200 shadow-xs transition-colors">
          <span>&larr; Beranda</span>
        </a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold shadow-xs transition-all">
          <span>Toko Lynk.id &rarr;</span>
        </a>
      </div>
    </div>

    <!-- ANNOUNCEMENT BANNER -->
    <aside aria-label="Status Pratinjau Terlindungi" class="bg-[#1b2533] text-emerald-100 text-[11px] sm:text-xs py-2 px-4 text-center font-medium flex items-center justify-center gap-2">
      <span>🔒 <strong>Mode Pratinjau Terlindungi:</strong> Naskah asli Microsoft Word (.docx) 8 halaman &amp; PDF siap pakai dapat diunduh di Lynk.id.</span>
    </aside>

    <!-- INNER 3-COLUMN WORKSPACE -->
    <div class="flex-1 flex flex-col lg:flex-row p-3 sm:p-5 lg:p-6 gap-5 lg:gap-6 items-start relative">

      <!-- COLUMN 1: LEFT FLOATING ICON DOCK -->
      <aside aria-label="Navigasi Menu Cepat" class="hidden lg:flex flex-col items-center justify-between w-16 bg-sidebarBg rounded-3xl p-3 py-5 sticky top-20 self-start shrink-0 border border-[#e8dfd5] shadow-xs z-30">
        <div class="space-y-6 flex flex-col items-center">
          <a href="/" class="w-10 h-10 rounded-2xl bg-emerald-600 text-white flex items-center justify-center font-black text-sm shadow-sm" title="Kembali ke Beranda">
            BG
          </a>

          <nav class="flex flex-col items-center gap-3">
            <a href="/" class="w-11 h-11 rounded-full bg-white hover:bg-slate-100 text-slate-700 flex items-center justify-center border border-slate-200 transition-colors" title="Katalog Beranda">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
            </a>
            <a href="/bank-soal-sas-pai-sd.html" class="w-11 h-11 rounded-full bg-white hover:bg-slate-100 text-slate-700 flex items-center justify-center border border-slate-200 transition-colors" title="Bank Soal SAS">
              <span class="text-base">📝</span>
            </a>
            <a href="/modul-ajar-pai-sd.html" class="w-11 h-11 rounded-full bg-slate-900 text-white flex items-center justify-center shadow" title="Modul Ajar Deep Learning">
              <span class="text-base">🚀</span>
            </a>
            <a href="/buku-siswa-pai-sd.html" class="w-11 h-11 rounded-full bg-white hover:bg-slate-100 text-slate-700 flex items-center justify-center border border-slate-200 transition-colors" title="Buku Siswa PAI">
              <span class="text-base">📘</span>
            </a>
          </nav>
        </div>

        <div class="flex flex-col items-center gap-3 pt-6 border-t border-[#e2d8cd]">
          <a href="/#profil-guru" class="w-10 h-10 rounded-full overflow-hidden border-2 border-emerald-600/40 shadow-sm block" title="Profil Bahan Ajar Bu Guru">
            <img src="/assets/avatar_profile_buguru.jpg" alt="Foto Profil" class="w-full h-full object-cover">
          </a>
        </div>
      </aside>

      <!-- COLUMN 2: CENTER MAIN CONTENT -->
      <main class="flex-1 w-full space-y-6">

        <nav aria-label="Breadcrumb" class="flex items-center gap-2 text-xs font-semibold text-slate-500">
          <a href="/" class="hover:text-emerald-700 transition-colors">Beranda</a>
          <span>&rsaquo;</span>
          <a href="/modul-ajar-pai-sd.html" class="hover:text-emerald-700 transition-colors">Modul Ajar PAI SD</a>
          <span>&rsaquo;</span>
          <span class="text-slate-900 font-bold">Modul Ajar PAI Kelas {grade}</span>
        </nav>

        <header class="space-y-3 pt-1">
          <div class="flex flex-wrap items-center gap-2">
            <span class="px-3.5 py-1 rounded-full bg-purple-100 text-purple-950 font-bold text-xs border border-purple-200">
              Kurikulum Merdeka • CP No. 020 • {fase} (Kelas {grade} SD)
            </span>
            <span class="px-3.5 py-1 rounded-full bg-amber-100 text-amber-950 font-bold text-xs border border-amber-300">
              🚀 3 Siklus Deep Learning
            </span>
          </div>

          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight leading-snug">
            {title}
          </h1>

          <div class="space-y-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-normal pt-1">
            <p>
              Perangkat ajar Modul Ajar Pendidikan Agama Islam dan Budi Pekerti (PAI &amp; BP) Kelas {grade} SD Kurikulum Merdeka dirancang komprehensif 8 halaman per materi untuk memenuhi standar supervisi akademik dinas pendidikan.
            </p>
            <p>
              Menerapkan siklus <strong>Deep Learning</strong> (Mindful, Meaningful, Joyful Learning), modul ini dilengkapi skenario diferensiasi, Lembar Kerja Peserta Didik (LKPD) siap cetak, serta instrumen asesmen Kriteria Ketercapaian Tujuan Pembelajaran (KKTP).
            </p>
          </div>
        </header>

        <!-- SECTION: 3 PILAR DEEP LEARNING -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
            <span>✨</span>
            <span>3 Pilar Inti Pendekatan Deep Learning</span>
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3.5 text-xs sm:text-sm">
            <div class="p-4 rounded-2xl bg-[#f3effe] border border-[#8b5cf6]/20 space-y-1.5">
              <span class="text-2xl block">🧘</span>
              <h3 class="font-extrabold text-purple-950">1. Mindful Learning</h3>
              <p class="text-slate-600 text-xs leading-relaxed">Membangun kesadaran penuh, kehadiran emosional, dan fokus adab islami peserta didik sebelum memulai penyerapan materi.</p>
            </div>
            <div class="p-4 rounded-2xl bg-[#e8f8f0] border border-[#10b981]/20 space-y-1.5">
              <span class="text-2xl block">💡</span>
              <h3 class="font-extrabold text-emerald-950">2. Meaningful Learning</h3>
              <p class="text-slate-600 text-xs leading-relaxed">Mengaitkan ayat Al-Qur'an dan nilai akhlak langsung dengan fenomena kehidupan nyata siswa di rumah dan madrasah.</p>
            </div>
            <div class="p-4 rounded-2xl bg-[#fff1eb] border border-[#f97316]/20 space-y-1.5">
              <span class="text-2xl block">🎨</span>
              <h3 class="font-extrabold text-orange-950">3. Joyful Learning</h3>
              <p class="text-slate-600 text-xs leading-relaxed">Aktivitas belajar berbasis permainan edukatif, diskusi visual, dan proyek kelompok yang membahagiakan anak usia SD.</p>
            </div>
          </div>
        </section>

        <!-- SECTION: KELENGKAPAN 8 HALAMAN -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
            <span>📋</span>
            <span>Kelengkapan Dokumen Modul Ajar (8 Halaman)</span>
          </h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-medium">
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#eff6ff] border border-[#3b82f6]/20">
              <span class="text-blue-700 font-bold text-base">✓</span>
              <span><strong>Identitas &amp; Capaian Pembelajaran:</strong> Memuat CP No. 020, Tujuan Pembelajaran (TP), dan profil pelajar Pancasila.</span>
            </div>
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#fef9c3] border border-[#eab308]/30">
              <span class="text-amber-800 font-bold text-base">✓</span>
              <span><strong>Pemahaman Bermakna:</strong> Pertanyaan pemantik kontekstual yang merangsang nalar kritis siswa.</span>
            </div>
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#e8f8f0] border border-[#10b981]/20">
              <span class="text-emerald-700 font-bold text-base">✓</span>
              <span><strong>Skenario Pembelajaran Diferensiasi:</strong> Langkah pendahuluan, inti, dan penutup untuk keragaman gaya belajar siswa.</span>
            </div>
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#fff1eb] border border-[#f97316]/20">
              <span class="text-orange-700 font-bold text-base">✓</span>
              <span><strong>LKPD Siap Pakai:</strong> Lembar kerja siswa mandiri dan kelompok yang interaktif.</span>
            </div>
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#f3effe] border border-[#8b5cf6]/20">
              <span class="text-purple-700 font-bold text-base">✓</span>
              <span><strong>Rubrik Asesmen KKTP:</strong> Pedoman penilaian sikap spiritual, sosial, dan unjuk kerja terukur.</span>
            </div>
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#ffe4e6] border border-[#f43f5e]/20">
              <span class="text-rose-700 font-bold text-base">✓</span>
              <span><strong>Format Word (.docx) &amp; PDF:</strong> 100% bebas diedit nama sekolah, logo, dan nama pendidik.</span>
            </div>
          </div>
        </section>

        <!-- SECTION: MATERI YANG DIPELAJARI -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
            <span>📖</span>
            <span>Materi Pembelajaran Semester 1 (Kelas {grade})</span>
          </h2>
          <p class="text-xs sm:text-sm text-slate-600">Modul ajar disusun lengkap untuk 5 bab materi semester ganjil:</p>
          <div class="space-y-3 text-xs sm:text-sm">
            {bab_html}
          </div>
        </section>

        <!-- SECTION: CUPLIKAN NASKAH MODUL (PREVIEW) -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h2 class="text-lg sm:text-xl font-black text-slate-900 flex items-center gap-2">
              <span>🔍</span>
              <span>Cuplikan Naskah Modul Ajar (Preview)</span>
            </h2>
            <span class="text-xs font-bold text-slate-500 bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
              Pratinjau Dokumen Asli
            </span>
          </div>

          <p class="text-xs sm:text-sm text-slate-600">
            Berikut cuplikan visual layout naskah modul ajar dan lembar skenario LKPD peserta didik kelas {grade}:
          </p>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-5 pt-1">
            <div class="rounded-3xl overflow-hidden border border-slate-200/90 bg-slate-50 shadow-xs flex flex-col justify-between group">
              <div class="p-3 text-center border-b border-slate-200/80 bg-white flex items-center justify-between">
                <span class="text-xs font-black text-slate-800">1. Cover &amp; Identitas Modul</span>
                <span class="text-[10px] font-bold text-purple-700 bg-purple-50 px-2 py-0.5 rounded-full border border-purple-200">Format Word</span>
              </div>
              <div class="p-3 flex items-center justify-center bg-[#faf7f2]">
                <img src="{cover_img}" alt="Cover Modul Ajar PAI Kelas {grade} SD" loading="lazy" class="w-full aspect-[3/4] object-cover rounded-2xl shadow-xs transition-transform duration-300 group-hover:scale-[1.02]">
              </div>
              <div class="p-3 text-center text-xs font-semibold text-slate-500 border-t border-slate-200/80 bg-white">
                <em>Modul Ajar Deep Learning Fase {fase}</em>
              </div>
            </div>

            <div class="rounded-3xl overflow-hidden border border-purple-200 bg-purple-50/30 shadow-xs flex flex-col justify-between group relative">
              <div class="p-3 text-center border-b border-purple-100 bg-white flex items-center justify-between">
                <span class="text-xs font-black text-purple-950 flex items-center gap-1.5">
                  <span>📄</span> <span>2. Skenario &amp; LKPD Modul</span>
                </span>
                <span class="text-[10px] font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">Sampel Asli</span>
              </div>
              <div class="p-3 flex items-center justify-center bg-[#faf7f2] relative cursor-pointer" onclick="openLightbox('{preview_img}', 'Pratinjau Lembar Skenario &amp; LKPD Modul Ajar Kelas {grade}')">
                <img src="{preview_img}" alt="Cuplikan Skenario Modul Ajar PAI Kelas {grade}" loading="lazy" class="w-full aspect-[3/4] object-cover rounded-2xl shadow-xs transition-transform duration-300 group-hover:scale-[1.02] bg-white">
                <div class="absolute inset-0 flex items-center justify-center bg-black/10 opacity-0 group-hover:opacity-100 transition-opacity rounded-2xl">
                  <span class="px-4 py-2 rounded-full bg-slate-900/90 text-white text-xs font-bold shadow-lg flex items-center gap-1.5 backdrop-blur-xs">
                    <span>🔍</span> <span>Klik untuk Perbesar</span>
                  </span>
                </div>
              </div>
              <div class="p-3 border-t border-purple-100 bg-white flex items-center justify-between gap-2">
                <button onclick="openLightbox('{preview_img}', 'Pratinjau Lembar Skenario &amp; LKPD Modul Ajar Kelas {grade}')" class="text-xs font-bold text-purple-700 hover:text-purple-800 transition-colors inline-flex items-center gap-1">
                  <span>🔍</span> <span>Perbesar Lembar</span>
                </button>
                <a href="/preview_modul.html?kelas={grade}" class="text-xs font-bold text-slate-800 hover:text-slate-950 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 transition-colors inline-flex items-center gap-1">
                  <span>📖 Reader Interaktif &rarr;</span>
                </a>
              </div>
            </div>
          </div>
        </section>

        <!-- SECTION: CARA MENDAPATKAN MODUL LENGKAP -->
        <section class="bg-gradient-to-br from-purple-50 via-teal-50 to-emerald-50 rounded-3xl p-6 sm:p-8 border border-purple-200 space-y-4 shadow-xs text-center">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white text-purple-800 font-extrabold text-xs shadow-2xs border border-purple-100">
            <span>🚀 Paket Lengkap 1 Semester</span>
          </div>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Cara Mendapatkan Modul Ajar Lengkap</h2>
          <p class="text-xs sm:text-sm text-slate-700 leading-relaxed max-w-xl mx-auto">
            Naskah lengkap Modul Ajar PAI Kelas {grade} SD siap unduh di toko resmi Lynk.id Bahan Ajar Bu Guru:
          </p>
          
          <div class="max-w-md mx-auto bg-white/90 backdrop-blur-xs rounded-2xl p-5 border border-purple-200 text-xs sm:text-sm space-y-2.5 text-left font-medium shadow-xs">
            <div class="flex items-center justify-between border-b border-slate-100 pb-2">
              <span class="text-slate-500">Format Dokumen</span>
              <span class="font-bold text-slate-900">Word (.docx) &amp; PDF Siap Pakai</span>
            </div>
            <div class="flex items-center justify-between border-b border-slate-100 pb-2">
              <span class="text-slate-500">Harga Promo</span>
              <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400 line-through">Rp 35.000</span>
                <span class="font-black text-purple-700 text-base">Rp 25.000</span>
                <span class="text-[9px] bg-red-100 text-red-700 font-extrabold px-1.5 py-0.5 rounded-full">Hemat 28%</span>
              </div>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-slate-500">Metode Pembayaran</span>
              <span class="font-bold text-slate-900 text-right">QRIS, GoPay, OVO, ShopeePay, Transfer Bank</span>
            </div>
          </div>

          <div class="pt-2">
            <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-black text-sm shadow-md transition-all hover:scale-105 active:scale-95">
              <span>Beli Modul Lengkap di Lynk.id</span>
              <span>&rarr;</span>
            </a>
            <p class="text-[11px] text-slate-500 mt-2">
              Tautan unduhan Word dan PDF otomatis aktif di layar konfirmasi dan dikirim ke WhatsApp/email Anda.
            </p>
          </div>
        </section>

        <!-- SECTION: FAQ -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
            <span>❓</span>
            <span>Pertanyaan yang Sering Diajukan (FAQ)</span>
          </h2>
          <div class="space-y-3 text-xs sm:text-sm">
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-1">
              <h3 class="font-extrabold text-slate-900 text-sm">Apakah file modul ajar bisa diedit?</h3>
              <p class="text-slate-600 leading-relaxed">Bisa. Format Microsoft Word (.docx) dapat disesuaikan sepenuhnya, termasuk mengganti nama sekolah, kepala sekolah, nama guru pengampu, dan alokasi waktu.</p>
            </div>
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-1">
              <h3 class="font-extrabold text-slate-900 text-sm">Apakah sudah sesuai acuan CP Kemendikbudristek?</h3>
              <p class="text-slate-600 leading-relaxed">Sangat sesuai. Modul mengacu pada Capaian Pembelajaran (CP) No. 020 Kemendikbudristek untuk SD Fase {fase}.</p>
            </div>
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-1">
              <h3 class="font-extrabold text-slate-900 text-sm">Bagaimana cara menerima file setelah checkout?</h3>
              <p class="text-slate-600 leading-relaxed">File Word dan PDF dapat langsung diunduh seketika setelah pembayaran Anda terverifikasi oleh Lynk.id.</p>
            </div>
          </div>
        </section>

        <!-- SECTION: INTERNAL LINKS -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
            <span>🔗</span>
            <span>Perangkat PAI Kelas {grade} Lainnya</span>
          </h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-semibold">
            <a href="/soal-sas-pai-kelas-{grade}.html" class="p-4 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
              <span class="flex items-center gap-2"><span>📝</span> <span>Soal SAS PAI Kelas {grade}</span></span>
              <span>&rarr;</span>
            </a>
            <a href="/buku-siswa-pai-kelas-{grade}.html" class="p-4 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
              <span class="flex items-center gap-2"><span>📘</span> <span>Buku Siswa PAI Kelas {grade}</span></span>
              <span>&rarr;</span>
            </a>
            <a href="/modul-ajar-pai-sd.html" class="p-4 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
              <span class="flex items-center gap-2"><span>🚀</span> <span>Semua Modul Ajar PAI SD</span></span>
              <span>&rarr;</span>
            </a>
            <a href="/" class="p-4 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
              <span class="flex items-center gap-2"><span>🏠</span> <span>Kembali ke Halaman Utama</span></span>
              <span>&rarr;</span>
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

      <!-- COLUMN 3: RIGHT FLOATING SUMMARY & CHECKOUT SIDEBAR -->
      <aside aria-label="Rincian Berkas dan Pembelian" class="w-full lg:w-80 bg-panelBg rounded-3xl p-5 sm:p-6 space-y-6 shrink-0 border border-[#e8dfd5] sticky top-20 self-start">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black text-slate-900 flex items-center gap-1.5">
            <span>📦</span> <span>Modul Ajar Kelas {grade}</span>
          </span>
          <span class="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-purple-100 text-purple-900 border border-purple-300">
            Tersedia
          </span>
        </div>

        <div class="aspect-[3/4] rounded-2xl overflow-hidden border border-black/10 shadow-xs bg-white">
          <img src="{cover_img}" alt="Cover Modul Ajar PAI Kelas {grade}" class="w-full h-full object-cover">
        </div>

        <div class="p-4 rounded-2xl bg-white border border-[#e2d8cd] space-y-2">
          <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">Harga Promo Spesial:</span>
          <div class="flex items-baseline gap-2">
            <span class="text-2xl font-black text-slate-950">Rp 25.000</span>
            <span class="text-xs text-slate-400 font-bold line-through">Rp 35.000</span>
          </div>
          <p class="text-[11px] text-slate-600 leading-relaxed">
            Format Word (.docx) 8 halaman &amp; PDF siap pakai supervisi dinas.
          </p>
          <div class="pt-2">
            <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="w-full py-3 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-black text-xs text-center shadow transition-all block">
              Beli Sekarang via Lynk.id &rarr;
            </a>
          </div>
        </div>

        <div class="space-y-2 text-xs text-slate-600 font-medium">
          <div class="flex items-center gap-2">
            <span class="text-emerald-600">✓</span>
            <span>100% Word (.docx) Dapat Diedit</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-emerald-600">✓</span>
            <span>Siklus Mindful, Meaningful, Joyful</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-emerald-600">✓</span>
            <span>LKPD &amp; Rubrik KKTP Lengkap</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-emerald-600">✓</span>
            <span>Unduh Instan Setelah Bayar</span>
          </div>
        </div>

        <div class="pt-2 border-t border-[#e2d8cd] text-center">
          <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest block mb-2">Metode Pembayaran Resmi</span>
          <div class="flex flex-wrap items-center justify-center gap-1.5 text-[11px] font-bold text-slate-700">
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">QRIS</span>
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">GoPay</span>
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">OVO</span>
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">ShopeePay</span>
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">Transfer</span>
          </div>
        </div>
      </aside>

    </div>

    <!-- FOOTER -->
    <footer class="bg-white border-t border-[#ece6dc] py-6 px-6 text-xs text-slate-500">
      <div class="max-w-[1400px] mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
        <div><span class="font-bold text-slate-800">Bahan Ajar Bu Guru</span> &bull; Kurikulum Merdeka CP No. 020</div>
        <div class="flex items-center gap-4 font-semibold">
          <a href="/kebijakan-privasi.html" class="hover:text-slate-800 transition-colors">Kebijakan Privasi</a>
          <a href="/syarat-ketentuan.html" class="hover:text-slate-800 transition-colors">Syarat &amp; Ketentuan</a>
          <a href="/tentang-kami.html" class="hover:text-slate-800 transition-colors">Tentang Kami</a>
          <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="text-emerald-700 hover:underline">Toko Lynk.id &rarr;</a>
        </div>
      </div>
    </footer>

  </div>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-3 sm:p-6" onclick="closeLightbox(event)">
    <div class="relative max-w-4xl max-h-[92vh] bg-white rounded-3xl p-4 sm:p-6 overflow-hidden flex flex-col shadow-2xl" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <h3 id="lightbox-title" class="font-black text-slate-900 text-sm sm:text-base">Pratinjau Modul Ajar</h3>
        <button onclick="closeLightbox()" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold flex items-center justify-center text-sm transition-colors">
          ✕
        </button>
      </div>
      <div class="flex-1 overflow-auto py-4 flex items-center justify-center bg-slate-50 rounded-2xl border border-slate-200/80 my-2">
        <img id="lightbox-img" src="" alt="Pratinjau Modul Ajar" class="max-w-full max-h-[70vh] object-contain shadow-md rounded-xl">
      </div>
      <div class="pt-2 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
        <span class="text-slate-500 font-medium">Modul lengkap format Word (.docx) dapat diunduh langsung di Lynk.id.</span>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="px-5 py-2 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-bold transition-all shadow-xs">
          Beli Modul Lengkap di Lynk.id &rarr;
        </a>
      </div>
    </div>
  </div>

  <script>
    function openLightbox(src, title) {{
      document.getElementById('lightbox-img').src = src;
      document.getElementById('lightbox-title').textContent = title || 'Pratinjau Modul Ajar';
      const modal = document.getElementById('lightbox-modal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }}
    function closeLightbox(event) {{
      const modal = document.getElementById('lightbox-modal');
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }}
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') closeLightbox();
    }});
  </script>

</body>
</html>
"""
    return html

# ========================================================
# 2. BUKU SISWA (KELAS 1-6)
# ========================================================
def generate_buku_page(grade):
    data = GRADES_DATA[grade]
    fase = data["fase"]
    title = f"Buku Siswa PAI Kelas {grade} SD Kurikulum Merdeka Semester 1"
    desc = f"Naskah Buku Siswa PAI & BP SD Kelas {grade} Kurikulum Merdeka Semester 1 edisi bergambar format Word (.docx) dan PDF siap pakai."
    canonical = f"https://bahanajarbuguru.my.id/buku-siswa-pai-kelas-{grade}.html"
    cover_img = f"/assets/cover_penjualan_buku_kelas{grade}.jpg"
    preview_img = f"/assets/slide2_penjualan_buku_kelas{grade}.jpg"

    bab_html = render_bab_list(data["bab_list"])

    other_buku_links = "".join([
        f"""<a href="/buku-siswa-pai-kelas-{g}.html" class="p-3.5 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 text-xs font-semibold flex items-center justify-between text-slate-800 hover:text-emerald-950 transition-colors">
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
  <meta property="og:image" content="https://bahanajarbuguru.my.id{cover_img}">
  <meta property="og:url" content="{canonical}">

  <!-- Schema.org Product -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Product",
        "name": "Buku Siswa PAI & BP SD Kelas {grade} Kurikulum Merdeka",
        "description": "Naskah buku materi pembelajaran PAI SD Kelas {grade} Semester 1 format Word dan PDF sesuai CP No. 020.",
        "image": "https://bahanajarbuguru.my.id{cover_img}",
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
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Apakah buku siswa bisa dicetak langsung?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Bisa. Anda mendapatkan file PDF resolusi tinggi siap cetak (A4) yang rapi, dan file Word (.docx) jika ingin menyesuaikan logo sekolah."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Apakah buku dilengkapi materi tajwid dan komik?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Ya, buku diperkaya dengan visual komik akhlak teladan islami, ilustrasi warna ramah anak, dan kaidah tajwid dasar terpadu."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <!-- Tailwind CSS & Fonts matching Homepage Theme -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Outfit"', '"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
          }},
          colors: {{
            canvas: '#ccebe0',
            appBg: '#faf7f2',
            sidebarBg: '#f3eee8',
            panelBg: '#f5efe6',
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

  <style>
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: #faf7f2; }}
    ::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 9999px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #94a3b8; }}
  </style>
</head>
<body class="bg-canvas min-h-screen p-2 sm:p-4 lg:p-6 flex flex-col justify-start items-center font-sans antialiased text-slate-800">

  <!-- MAIN APP MOCKUP CONTAINER -->
  <div class="w-full max-w-[1400px] bg-appBg rounded-[28px] sm:rounded-[36px] shadow-2xl shadow-emerald-950/15 border border-[#e5dfd5] overflow-hidden flex flex-col">

    <!-- TOP WINDOW CHROME -->
    <div class="bg-white/80 backdrop-blur border-b border-[#ece6dc] px-4 sm:px-6 py-3 flex items-center justify-between gap-4 select-none sticky top-0 z-40">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-[#ff5f56] border border-[#e0443e] inline-block"></span>
        <span class="w-3 h-3 rounded-full bg-[#ffbd2e] border border-[#dea123] inline-block"></span>
        <span class="w-3 h-3 rounded-full bg-[#27c93f] border border-[#1aab29] inline-block"></span>
      </div>

      <div class="flex-1 max-w-md mx-auto hidden sm:flex items-center justify-center gap-2 px-3.5 py-1 rounded-full bg-slate-100/90 border border-slate-200/80 text-xs text-slate-700 font-medium">
        <svg class="w-3 h-3 text-emerald-600" viewBox="0 0 24 24" fill="currentColor">
          <path fill-rule="evenodd" d="M12 1.5a5.25 5.25 0 00-5.25 5.25v3a3 3 0 00-3 3v6.75a3 3 0 003 3h10.5a3 3 0 003-3v-6.75a3 3 0 00-3-3v-3c0-2.9-2.35-5.25-5.25-5.25zm3.75 8.25v-3a3.75 3.75 0 00-7.5 0v3h7.5z" clip-rule="evenodd" />
        </svg>
        <span class="truncate font-semibold">bahanajarbuguru.my.id/buku-siswa-pai-kelas-{grade}.html</span>
      </div>

      <div class="flex items-center gap-2">
        <a href="/" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 text-xs font-bold border border-slate-200 shadow-xs transition-colors">
          <span>&larr; Beranda</span>
        </a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold shadow-xs transition-all">
          <span>Toko Lynk.id &rarr;</span>
        </a>
      </div>
    </div>

    <!-- ANNOUNCEMENT BANNER -->
    <aside aria-label="Status Pratinjau Terlindungi" class="bg-[#1b2533] text-emerald-100 text-[11px] sm:text-xs py-2 px-4 text-center font-medium flex items-center justify-center gap-2">
      <span>🔒 <strong>Mode Pratinjau Terlindungi:</strong> Naskah asli Microsoft Word (.docx) &amp; PDF siap cetak full-color dapat diunduh di Lynk.id.</span>
    </aside>

    <!-- INNER 3-COLUMN WORKSPACE -->
    <div class="flex-1 flex flex-col lg:flex-row p-3 sm:p-5 lg:p-6 gap-5 lg:gap-6 items-start relative">

      <!-- COLUMN 1: LEFT FLOATING ICON DOCK -->
      <aside aria-label="Navigasi Menu Cepat" class="hidden lg:flex flex-col items-center justify-between w-16 bg-sidebarBg rounded-3xl p-3 py-5 sticky top-20 self-start shrink-0 border border-[#e8dfd5] shadow-xs z-30">
        <div class="space-y-6 flex flex-col items-center">
          <a href="/" class="w-10 h-10 rounded-2xl bg-emerald-600 text-white flex items-center justify-center font-black text-sm shadow-sm" title="Kembali ke Beranda">
            BG
          </a>

          <nav class="flex flex-col items-center gap-3">
            <a href="/" class="w-11 h-11 rounded-full bg-white hover:bg-slate-100 text-slate-700 flex items-center justify-center border border-slate-200 transition-colors" title="Katalog Beranda">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
            </a>
            <a href="/bank-soal-sas-pai-sd.html" class="w-11 h-11 rounded-full bg-white hover:bg-slate-100 text-slate-700 flex items-center justify-center border border-slate-200 transition-colors" title="Bank Soal SAS">
              <span class="text-base">📝</span>
            </a>
            <a href="/modul-ajar-pai-sd.html" class="w-11 h-11 rounded-full bg-white hover:bg-slate-100 text-slate-700 flex items-center justify-center border border-slate-200 transition-colors" title="Modul Ajar Deep Learning">
              <span class="text-base">🚀</span>
            </a>
            <a href="/buku-siswa-pai-sd.html" class="w-11 h-11 rounded-full bg-slate-900 text-white flex items-center justify-center shadow" title="Buku Siswa PAI">
              <span class="text-base">📘</span>
            </a>
          </nav>
        </div>

        <div class="flex flex-col items-center gap-3 pt-6 border-t border-[#e2d8cd]">
          <a href="/#profil-guru" class="w-10 h-10 rounded-full overflow-hidden border-2 border-emerald-600/40 shadow-sm block" title="Profil Bahan Ajar Bu Guru">
            <img src="/assets/avatar_profile_buguru.jpg" alt="Foto Profil" class="w-full h-full object-cover">
          </a>
        </div>
      </aside>

      <!-- COLUMN 2: CENTER MAIN CONTENT -->
      <main class="flex-1 w-full space-y-6">

        <nav aria-label="Breadcrumb" class="flex items-center gap-2 text-xs font-semibold text-slate-500">
          <a href="/" class="hover:text-emerald-700 transition-colors">Beranda</a>
          <span>&rsaquo;</span>
          <a href="/buku-siswa-pai-sd.html" class="hover:text-emerald-700 transition-colors">Buku Siswa PAI SD</a>
          <span>&rsaquo;</span>
          <span class="text-slate-900 font-bold">Buku Siswa PAI Kelas {grade}</span>
        </nav>

        <header class="space-y-3 pt-1">
          <div class="flex flex-wrap items-center gap-2">
            <span class="px-3.5 py-1 rounded-full bg-sky-100 text-sky-950 font-bold text-xs border border-sky-200">
              Semester 1 Penuh • CP No. 020 • {fase} (Kelas {grade} SD)
            </span>
            <span class="px-3.5 py-1 rounded-full bg-amber-100 text-amber-950 font-bold text-xs border border-amber-300">
              📘 Edisi Full Color Ramah Anak
            </span>
          </div>

          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight leading-snug">
            {title}
          </h1>

          <div class="space-y-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-normal pt-1">
            <p>
              Naskah buku materi ajar peserta didik Pendidikan Agama Islam dan Budi Pekerti (PAI &amp; BP) Kelas {grade} SD untuk semester ganjil (Semester 1). Disusun dengan bahasa yang komunikatif, visual full color ramah anak, dan ilustrasi Islami yang menginspirasi budi pekerti luhur.
            </p>
            <p>
              Tersedia dalam format Microsoft Word (.docx) siap sunting identitas madrasah/sekolah dan PDF beresolusi tinggi siap cetak langsung.
            </p>
          </div>
        </header>

        <!-- SECTION: KEUNGGULAN BUKU -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
            <span>⭐</span>
            <span>Keunggulan Buku Siswa PAI Kelas {grade}</span>
          </h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-medium">
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#eff6ff] border border-[#3b82f6]/20">
              <span class="text-blue-700 font-bold text-base">✓</span>
              <span><strong>Full Color &amp; Ilustrasi Ramah Anak:</strong> Desain halaman menarik yang membangkitkan keceriaan belajar anak usia sekolah dasar.</span>
            </div>
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#e8f8f0] border border-[#10b981]/20">
              <span class="text-emerald-700 font-bold text-base">✓</span>
              <span><strong>Teks &amp; Font Nyaman Dibaca:</strong> Pemilihan tipografi berukuran proporsional yang memudahkan anak membaca lafal Arab dan terjemahan.</span>
            </div>
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#f3effe] border border-[#8b5cf6]/20">
              <span class="text-purple-700 font-bold text-base">✓</span>
              <span><strong>Kisah Teladan &amp; Komik Karakter:</strong> Cerita nabi dan akhlak mulia disajikan ringkas dan sarat hikmah teladan.</span>
            </div>
            <div class="flex items-start gap-2.5 p-3.5 rounded-2xl bg-[#fff1eb] border border-[#f97316]/20">
              <span class="text-orange-700 font-bold text-base">✓</span>
              <span><strong>Lembar Aktivitas Siswa:</strong> Tantangan mandiri, lembar refleksi islami, dan kuis seru di setiap akhir bab.</span>
            </div>
          </div>
        </section>

        <!-- SECTION: DAFTAR BAB -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
            <span>📖</span>
            <span>Daftar Bab Pembelajaran (Semester 1 Kelas {grade})</span>
          </h2>
          <p class="text-xs sm:text-sm text-slate-600">Materi buku siswa tersusun rapi untuk 5 bab pokok kurikulum merdeka:</p>
          <div class="space-y-3 text-xs sm:text-sm">
            {bab_html}
          </div>
        </section>

        <!-- SECTION: CUPLIKAN HALAMAN BUKU (PREVIEW) -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h2 class="text-lg sm:text-xl font-black text-slate-900 flex items-center gap-2">
              <span>🔍</span>
              <span>Cuplikan Halaman Buku (Preview)</span>
            </h2>
            <span class="text-xs font-bold text-slate-500 bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
              Pratinjau Halaman Asli
            </span>
          </div>

          <p class="text-xs sm:text-sm text-slate-600">
            Berikut cuplikan visual cover depan dan isi halaman materi buku siswa PAI kelas {grade}:
          </p>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-5 pt-1">
            <div class="rounded-3xl overflow-hidden border border-slate-200/90 bg-slate-50 shadow-xs flex flex-col justify-between group">
              <div class="p-3 text-center border-b border-slate-200/80 bg-white flex items-center justify-between">
                <span class="text-xs font-black text-slate-800">1. Cover Buku Siswa</span>
                <span class="text-[10px] font-bold text-sky-700 bg-sky-50 px-2 py-0.5 rounded-full border border-sky-200">Full Color</span>
              </div>
              <div class="p-3 flex items-center justify-center bg-[#faf7f2]">
                <img src="{cover_img}" alt="Cover Buku Siswa PAI Kelas {grade} SD" loading="lazy" class="w-full aspect-[3/4] object-cover rounded-2xl shadow-xs transition-transform duration-300 group-hover:scale-[1.02]">
              </div>
              <div class="p-3 text-center text-xs font-semibold text-slate-500 border-t border-slate-200/80 bg-white">
                <em>Cover Resmi Buku Siswa Semester 1</em>
              </div>
            </div>

            <div class="rounded-3xl overflow-hidden border border-sky-200 bg-sky-50/30 shadow-xs flex flex-col justify-between group relative">
              <div class="p-3 text-center border-b border-sky-100 bg-white flex items-center justify-between">
                <span class="text-xs font-black text-sky-950 flex items-center gap-1.5">
                  <span>📄</span> <span>2. Cuplikan Isi Halaman</span>
                </span>
                <span class="text-[10px] font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">Sampel Asli</span>
              </div>
              <div class="p-3 flex items-center justify-center bg-[#faf7f2] relative cursor-pointer" onclick="openLightbox('{preview_img}', 'Pratinjau Isi Halaman Buku Siswa PAI Kelas {grade}')">
                <img src="{preview_img}" alt="Cuplikan Isi Halaman Buku Siswa PAI Kelas {grade}" loading="lazy" class="w-full aspect-[3/4] object-cover rounded-2xl shadow-xs transition-transform duration-300 group-hover:scale-[1.02] bg-white">
                <div class="absolute inset-0 flex items-center justify-center bg-black/10 opacity-0 group-hover:opacity-100 transition-opacity rounded-2xl">
                  <span class="px-4 py-2 rounded-full bg-slate-900/90 text-white text-xs font-bold shadow-lg flex items-center gap-1.5 backdrop-blur-xs">
                    <span>🔍</span> <span>Klik untuk Perbesar</span>
                  </span>
                </div>
              </div>
              <div class="p-3 border-t border-sky-100 bg-white flex items-center justify-between gap-2">
                <button onclick="openLightbox('{preview_img}', 'Pratinjau Isi Halaman Buku Siswa PAI Kelas {grade}')" class="text-xs font-bold text-sky-700 hover:text-sky-800 transition-colors inline-flex items-center gap-1">
                  <span>🔍</span> <span>Perbesar Halaman</span>
                </button>
                <a href="/preview_buku.html?kelas={grade}" class="text-xs font-bold text-slate-800 hover:text-slate-950 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 transition-colors inline-flex items-center gap-1">
                  <span>📖 Reader Interaktif &rarr;</span>
                </a>
              </div>
            </div>
          </div>
        </section>

        <!-- SECTION: CARA MENDAPATKAN BUKU LENGKAP -->
        <section class="bg-gradient-to-br from-sky-50 via-teal-50 to-emerald-50 rounded-3xl p-6 sm:p-8 border border-sky-200 space-y-4 shadow-xs text-center">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white text-sky-800 font-extrabold text-xs shadow-2xs border border-sky-100">
            <span>✨ 1 Semester Penuh</span>
          </div>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Cara Mendapatkan Buku Lengkap</h2>
          <p class="text-xs sm:text-sm text-slate-700 leading-relaxed max-w-xl mx-auto">
            Naskah lengkap Buku Siswa PAI Kelas {grade} siap unduh di toko resmi Lynk.id Bahan Ajar Bu Guru:
          </p>
          
          <div class="max-w-md mx-auto bg-white/90 backdrop-blur-xs rounded-2xl p-5 border border-sky-200 text-xs sm:text-sm space-y-2.5 text-left font-medium shadow-xs">
            <div class="flex items-center justify-between border-b border-slate-100 pb-2">
              <span class="text-slate-500">Format Dokumen</span>
              <span class="font-bold text-slate-900">Word (.docx) &amp; PDF Siap Cetak</span>
            </div>
            <div class="flex items-center justify-between border-b border-slate-100 pb-2">
              <span class="text-slate-500">Harga Promo</span>
              <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400 line-through">Rp 45.000</span>
                <span class="font-black text-sky-700 text-base">Rp 35.000</span>
                <span class="text-[9px] bg-red-100 text-red-700 font-extrabold px-1.5 py-0.5 rounded-full">Hemat 22%</span>
              </div>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-slate-500">Metode Pembayaran</span>
              <span class="font-bold text-slate-900 text-right">QRIS, GoPay, OVO, ShopeePay, Transfer Bank</span>
            </div>
          </div>

          <div class="pt-2">
            <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-black text-sm shadow-md transition-all hover:scale-105 active:scale-95">
              <span>Beli Buku Lengkap di Lynk.id</span>
              <span>&rarr;</span>
            </a>
            <p class="text-[11px] text-slate-500 mt-2">
              Tautan unduhan Word dan PDF otomatis aktif di layar konfirmasi dan dikirim ke WhatsApp/email Anda.
            </p>
          </div>
        </section>

        <!-- SECTION: FAQ -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
            <span>❓</span>
            <span>Pertanyaan yang Sering Diajukan (FAQ)</span>
          </h2>
          <div class="space-y-3 text-xs sm:text-sm">
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-1">
              <h3 class="font-extrabold text-slate-900 text-sm">Apakah buku bisa dicetak mandiri di sekolah?</h3>
              <p class="text-slate-600 leading-relaxed">Bisa. Format PDF beresolusi tinggi tanpa watermark siap dicetak dalam format buku A4 oleh pihak sekolah maupun orang tua.</p>
            </div>
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-1">
              <h3 class="font-extrabold text-slate-900 text-sm">Apakah materi mencakup seluruh bab semester 1?</h3>
              <p class="text-slate-600 leading-relaxed">Ya, buku memuat 5 bab lengkap semester 1 sesuai Capaian Pembelajaran (CP) No. 020 Kemendikbudristek.</p>
            </div>
          </div>
        </section>

        <!-- SECTION: INTERNAL LINKS -->
        <section class="bg-white rounded-3xl p-6 sm:p-7 border border-[#e5ded4] space-y-4 shadow-xs">
          <h2 class="text-lg sm:text-xl font-black text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
            <span>🔗</span>
            <span>Perangkat PAI Kelas {grade} Lainnya</span>
          </h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm font-semibold">
            <a href="/soal-sas-pai-kelas-{grade}.html" class="p-4 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
              <span class="flex items-center gap-2"><span>📝</span> <span>Soal SAS PAI Kelas {grade}</span></span>
              <span>&rarr;</span>
            </a>
            <a href="/modul-ajar-pai-kelas-{grade}.html" class="p-4 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
              <span class="flex items-center gap-2"><span>🚀</span> <span>Modul Ajar PAI Kelas {grade}</span></span>
              <span>&rarr;</span>
            </a>
            <a href="/buku-siswa-pai-sd.html" class="p-4 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
              <span class="flex items-center gap-2"><span>📘</span> <span>Semua Buku Siswa PAI SD</span></span>
              <span>&rarr;</span>
            </a>
            <a href="/" class="p-4 rounded-2xl bg-slate-50 hover:bg-emerald-50 border border-slate-200 hover:border-emerald-200 transition-all flex items-center justify-between text-slate-800 hover:text-emerald-950">
              <span class="flex items-center gap-2"><span>🏠</span> <span>Kembali ke Halaman Utama</span></span>
              <span>&rarr;</span>
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

      <!-- COLUMN 3: RIGHT FLOATING SUMMARY & CHECKOUT SIDEBAR -->
      <aside aria-label="Rincian Berkas dan Pembelian" class="w-full lg:w-80 bg-panelBg rounded-3xl p-5 sm:p-6 space-y-6 shrink-0 border border-[#e8dfd5] sticky top-20 self-start">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black text-slate-900 flex items-center gap-1.5">
            <span>📦</span> <span>Buku Siswa Kelas {grade}</span>
          </span>
          <span class="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-sky-100 text-sky-900 border border-sky-300">
            Tersedia
          </span>
        </div>

        <div class="aspect-[3/4] rounded-2xl overflow-hidden border border-black/10 shadow-xs bg-white">
          <img src="{cover_img}" alt="Cover Buku Siswa PAI Kelas {grade}" class="w-full h-full object-cover">
        </div>

        <div class="p-4 rounded-2xl bg-white border border-[#e2d8cd] space-y-2">
          <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">Harga Promo Spesial:</span>
          <div class="flex items-baseline gap-2">
            <span class="text-2xl font-black text-slate-950">Rp 35.000</span>
            <span class="text-xs text-slate-400 font-bold line-through">Rp 45.000</span>
          </div>
          <p class="text-[11px] text-slate-600 leading-relaxed">
            Format Word (.docx) &amp; PDF siap cetak resolusi tinggi full color.
          </p>
          <div class="pt-2">
            <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="w-full py-3 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-black text-xs text-center shadow transition-all block">
              Beli Sekarang via Lynk.id &rarr;
            </a>
          </div>
        </div>

        <div class="space-y-2 text-xs text-slate-600 font-medium">
          <div class="flex items-center gap-2">
            <span class="text-emerald-600">✓</span>
            <span>100% Word (.docx) Dapat Diedit</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-emerald-600">✓</span>
            <span>PDF Siap Cetak Full Color</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-emerald-600">✓</span>
            <span>Ilustrasi Ramah Anak &amp; Komik</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-emerald-600">✓</span>
            <span>Unduh Instan Setelah Bayar</span>
          </div>
        </div>

        <div class="pt-2 border-t border-[#e2d8cd] text-center">
          <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest block mb-2">Metode Pembayaran Resmi</span>
          <div class="flex flex-wrap items-center justify-center gap-1.5 text-[11px] font-bold text-slate-700">
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">QRIS</span>
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">GoPay</span>
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">OVO</span>
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">ShopeePay</span>
            <span class="px-2 py-1 bg-white rounded-lg border border-slate-200">Transfer</span>
          </div>
        </div>
      </aside>

    </div>

    <!-- FOOTER -->
    <footer class="bg-white border-t border-[#ece6dc] py-6 px-6 text-xs text-slate-500">
      <div class="max-w-[1400px] mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
        <div><span class="font-bold text-slate-800">Bahan Ajar Bu Guru</span> &bull; Kurikulum Merdeka CP No. 020</div>
        <div class="flex items-center gap-4 font-semibold">
          <a href="/kebijakan-privasi.html" class="hover:text-slate-800 transition-colors">Kebijakan Privasi</a>
          <a href="/syarat-ketentuan.html" class="hover:text-slate-800 transition-colors">Syarat &amp; Ketentuan</a>
          <a href="/tentang-kami.html" class="hover:text-slate-800 transition-colors">Tentang Kami</a>
          <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="text-emerald-700 hover:underline">Toko Lynk.id &rarr;</a>
        </div>
      </div>
    </footer>

  </div>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-3 sm:p-6" onclick="closeLightbox(event)">
    <div class="relative max-w-4xl max-h-[92vh] bg-white rounded-3xl p-4 sm:p-6 overflow-hidden flex flex-col shadow-2xl" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <h3 id="lightbox-title" class="font-black text-slate-900 text-sm sm:text-base">Pratinjau Buku Siswa</h3>
        <button onclick="closeLightbox()" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold flex items-center justify-center text-sm transition-colors">
          ✕
        </button>
      </div>
      <div class="flex-1 overflow-auto py-4 flex items-center justify-center bg-slate-50 rounded-2xl border border-slate-200/80 my-2">
        <img id="lightbox-img" src="" alt="Pratinjau Buku Siswa" class="max-w-full max-h-[70vh] object-contain shadow-md rounded-xl">
      </div>
      <div class="pt-2 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
        <span class="text-slate-500 font-medium">Buku lengkap format Word (.docx) &amp; PDF dapat diunduh langsung di Lynk.id.</span>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="px-5 py-2 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-bold transition-all shadow-xs">
          Beli Buku Lengkap di Lynk.id &rarr;
        </a>
      </div>
    </div>
  </div>

  <script>
    function openLightbox(src, title) {{
      document.getElementById('lightbox-img').src = src;
      document.getElementById('lightbox-title').textContent = title || 'Pratinjau Buku Siswa';
      const modal = document.getElementById('lightbox-modal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }}
    function closeLightbox(event) {{
      const modal = document.getElementById('lightbox-modal');
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }}
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') closeLightbox();
    }});
  </script>

</body>
</html>
"""
    return html

# ========================================================
# 3. CATEGORY HUB PAGES
# ========================================================
def generate_hub_page(cat):
    configs = {
        "soal": {
            "title": "Bank Soal SAS PAI SD Kelas 1-6 Kurikulum Merdeka",
            "desc": "Kumpulan naskah bank soal Sumatif Akhir Semester (SAS) PAI SD Kelas 1, 2, 3, 4, 5, 6 Kurikulum Merdeka lengkap kunci jawaban dan kisi-kisi CP 020.",
            "canonical": "https://bahanajarbuguru.my.id/bank-soal-sas-pai-sd.html",
            "h1": "Bank Soal SAS PAI SD Kelas 1–6 Kurikulum Merdeka",
            "icon": "📝",
            "badge": "Bank Soal SAS Lengkap",
            "prefix": "soal-sas-pai-kelas-",
            "item_title": lambda g: f"Soal SAS PAI Kelas {g} SD",
            "item_desc": lambda g: f"Naskah 25 butir soal (PG, Isian, Uraian HOTS), kunci jawaban, rubrik skor, dan matriks kisi-kisi CP 020.",
            "cover_key": "cover_soal",
            "price": "Rp 15.000",
            "color": "emerald"
        },
        "modul": {
            "title": "Modul Ajar PAI SD Kelas 1-6 Kurikulum Merdeka (Deep Learning)",
            "desc": "Katalog modul ajar Deep Learning PAI SD Kelas 1 sampai 6 Kurikulum Merdeka 8 halaman lengkap dengan LKPD dan rubrik KKTP format Word dan PDF.",
            "canonical": "https://bahanajarbuguru.my.id/modul-ajar-pai-sd.html",
            "h1": "Modul Ajar Deep Learning PAI SD (Kelas 1–6)",
            "icon": "🚀",
            "badge": "Modul Ajar 8 Halaman",
            "prefix": "modul-ajar-pai-kelas-",
            "item_title": lambda g: f"Modul Ajar PAI Kelas {g} SD",
            "item_desc": lambda g: f"Modul 8 halaman siklus Mindful, Meaningful, Joyful Learning, LKPD diferensiasi, rubrik KKTP.",
            "cover_key": "cover_modul",
            "price": "Rp 25.000",
            "color": "purple"
        },
        "buku": {
            "title": "Buku Siswa PAI SD Kelas 1-6 Kurikulum Merdeka Semester 1",
            "desc": "Koleksi buku teks siswa PAI & BP SD Kelas 1 sampai 6 Kurikulum Merdeka Semester 1 edisi full color ramah anak format Word dan PDF siap cetak.",
            "canonical": "https://bahanajarbuguru.my.id/buku-siswa-pai-sd.html",
            "h1": "Buku Siswa PAI & BP SD Kelas 1–6 (Semester 1)",
            "icon": "📘",
            "badge": "Buku Teks Full Color",
            "prefix": "buku-siswa-pai-kelas-",
            "item_title": lambda g: f"Buku Siswa PAI Kelas {g} SD",
            "item_desc": lambda g: f"Buku teks siswa 1 semester penuh, ilustrasi islami ramah anak, kaidah tajwid, dan komik akhlak.",
            "cover_key": "cover_buku",
            "price": "Rp 35.000",
            "color": "sky"
        }
    }

    cfg = configs[cat]
    cards_html = ""
    for g in range(1, 7):
        data = GRADES_DATA[g]
        theme = PASTEL_THEMES[(g-1) % len(PASTEL_THEMES)]
        cover = data[cfg["cover_key"]]
        url = f"/{cfg['prefix']}{g}.html"
        cards_html += f"""
        <article class="p-5 rounded-3xl {theme['bg']} border {theme['border']} flex flex-col justify-between shadow-xs hover:shadow-md transition-all hover:-translate-y-1">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full text-xs font-black {theme['pill']} text-white shadow-xs">
                Kelas {g} SD
              </span>
              <span class="text-xs font-black text-slate-900">{cfg['price']}</span>
            </div>
            <div class="flex gap-4 items-start pt-1">
              <div class="w-20 aspect-[3/4] rounded-2xl overflow-hidden border border-black/10 shrink-0 bg-white shadow-xs">
                <img src="{cover}" alt="{cfg['item_title'](g)}" class="w-full h-full object-cover">
              </div>
              <div class="space-y-1 min-w-0">
                <h3 class="font-black text-slate-900 text-sm leading-snug">{cfg['item_title'](g)}</h3>
                <p class="text-xs text-slate-600 line-clamp-3 leading-relaxed">{cfg['item_desc'](g)}</p>
                <span class="text-[10px] font-bold text-slate-500 block pt-1">Fase {data['fase']} &bull; CP No. 020</span>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-black/10 flex items-center justify-between">
            <a href="{url}" class="px-4 py-2 rounded-full text-xs font-bold bg-white hover:bg-slate-100 text-slate-800 border border-slate-200 transition-colors">
              Lihat Detail &rarr;
            </a>
            <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="px-4 py-2 rounded-full text-xs font-black bg-slate-900 hover:bg-slate-800 text-white shadow-xs transition-all">
              Beli
            </a>
          </div>
        </article>"""

    html = f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cfg['title']}</title>
  
  <link rel="canonical" href="{cfg['canonical']}">
  <meta name="description" content="{cfg['desc']}">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{cfg['title']}">
  <meta property="og:description" content="{cfg['desc']}">
  <meta property="og:url" content="{cfg['canonical']}">

  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Outfit"', '"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
          }},
          colors: {{
            canvas: '#ccebe0',
            appBg: '#faf7f2',
            sidebarBg: '#f3eee8',
            panelBg: '#f5efe6',
          }}
        }}
      }}
    }}
  </script>
</head>
<body class="bg-canvas min-h-screen p-2 sm:p-4 lg:p-6 flex flex-col justify-start items-center font-sans antialiased text-slate-800">

  <div class="w-full max-w-[1400px] bg-appBg rounded-[28px] sm:rounded-[36px] shadow-2xl shadow-emerald-950/15 border border-[#e5dfd5] overflow-hidden flex flex-col">

    <!-- TOP WINDOW CHROME -->
    <div class="bg-white/80 backdrop-blur border-b border-[#ece6dc] px-4 sm:px-6 py-3 flex items-center justify-between gap-4 select-none sticky top-0 z-40">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-[#ff5f56] border border-[#e0443e] inline-block"></span>
        <span class="w-3 h-3 rounded-full bg-[#ffbd2e] border border-[#dea123] inline-block"></span>
        <span class="w-3 h-3 rounded-full bg-[#27c93f] border border-[#1aab29] inline-block"></span>
      </div>

      <div class="flex-1 max-w-md mx-auto hidden sm:flex items-center justify-center gap-2 px-3.5 py-1 rounded-full bg-slate-100/90 border border-slate-200/80 text-xs text-slate-700 font-medium">
        <svg class="w-3 h-3 text-emerald-600" viewBox="0 0 24 24" fill="currentColor">
          <path fill-rule="evenodd" d="M12 1.5a5.25 5.25 0 00-5.25 5.25v3a3 3 0 00-3 3v6.75a3 3 0 003 3h10.5a3 3 0 003-3v-6.75a3 3 0 00-3-3v-3c0-2.9-2.35-5.25-5.25-5.25zm3.75 8.25v-3a3.75 3.75 0 00-7.5 0v3h7.5z" clip-rule="evenodd" />
        </svg>
        <span class="truncate font-semibold">{cfg['canonical'].replace('https://', '')}</span>
      </div>

      <div class="flex items-center gap-2">
        <a href="/" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 text-xs font-bold border border-slate-200 shadow-xs transition-colors">
          <span>&larr; Beranda</span>
        </a>
        <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold shadow-xs transition-all">
          <span>Toko Lynk.id &rarr;</span>
        </a>
      </div>
    </div>

    <!-- MAIN BODY -->
    <div class="p-4 sm:p-6 lg:p-8 space-y-6">
      <nav aria-label="Breadcrumb" class="flex items-center gap-2 text-xs font-semibold text-slate-500">
        <a href="/" class="hover:text-emerald-700 transition-colors">Beranda</a>
        <span>&rsaquo;</span>
        <span class="text-slate-900 font-bold">{cfg['badge']}</span>
      </nav>

      <header class="space-y-3">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-white text-slate-900 font-bold text-xs border border-slate-200 shadow-xs">
          <span>{cfg['icon']}</span> <span>{cfg['badge']} (Kelas 1–6 SD)</span>
        </div>
        <h1 class="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight leading-snug">
          {cfg['h1']}
        </h1>
        <p class="text-xs sm:text-sm text-slate-600 max-w-3xl leading-relaxed">
          {cfg['desc']} Pilih jenjang kelas di bawah ini untuk melihat pratinjau halaman, daftar bab, contoh materi, serta berkas naskah lengkap format Word (.docx) dan PDF.
        </p>
      </header>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 pt-2">
        {cards_html}
      </div>
    </div>

    <!-- FOOTER -->
    <footer class="bg-white border-t border-[#ece6dc] py-6 px-6 text-xs text-slate-500 mt-6">
      <div class="max-w-[1400px] mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
        <div><span class="font-bold text-slate-800">Bahan Ajar Bu Guru</span> &bull; Kurikulum Merdeka CP No. 020</div>
        <div class="flex items-center gap-4 font-semibold">
          <a href="/kebijakan-privasi.html" class="hover:text-slate-800 transition-colors">Kebijakan Privasi</a>
          <a href="/syarat-ketentuan.html" class="hover:text-slate-800 transition-colors">Syarat &amp; Ketentuan</a>
          <a href="/tentang-kami.html" class="hover:text-slate-800 transition-colors">Tentang Kami</a>
          <a href="https://lynk.id/bahanajarbuguru" target="_blank" rel="sponsored nofollow noopener" class="text-emerald-700 hover:underline">Toko Lynk.id &rarr;</a>
        </div>
      </div>
    </footer>

  </div>

</body>
</html>
"""
    return html

def main():
    print("Building all unified Modul Ajar, Buku Siswa, and Category Hubs...")
    for grade in range(1, 7):
        # Modul Ajar
        modul_html = generate_modul_page(grade)
        modul_path = f"public/modul-ajar-pai-kelas-{grade}.html"
        with open(modul_path, "w", encoding="utf-8") as f:
            f.write(modul_html)
        print(f"Generated: {modul_path}")

        # Buku Siswa
        buku_html = generate_buku_page(grade)
        buku_path = f"public/buku-siswa-pai-kelas-{grade}.html"
        with open(buku_path, "w", encoding="utf-8") as f:
            f.write(buku_html)
        print(f"Generated: {buku_path}")

    # Hub Pages
    for cat in ["soal", "modul", "buku"]:
        hub_html = generate_hub_page(cat)
        fn_map = {
            "soal": "public/bank-soal-sas-pai-sd.html",
            "modul": "public/modul-ajar-pai-sd.html",
            "buku": "public/buku-siswa-pai-sd.html"
        }
        with open(fn_map[cat], "w", encoding="utf-8") as f:
            f.write(hub_html)
        print(f"Generated Hub: {fn_map[cat]}")

if __name__ == "__main__":
    main()
