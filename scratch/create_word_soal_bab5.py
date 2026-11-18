# -*- coding: utf-8 -*-
"""
Generate Microsoft Word (.docx) for:
Soal Ulangan Harian PAI & Budi Pekerti Kelas 3 SD Bab 5
Kisah Nabi Muhammad saw. Sebelum dan Sesudah Menjadi Rasul (Periode Makkah)
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import os

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_background(cell, color_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tcPr.append(shd)

def create_soal_docx(output_path):
    doc = docx.Document()

    # Page Setup: A4, 2 cm margins
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Base style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(10)
    font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)

    # 1. KOP RESMI
    p_kop1 = doc.add_paragraph()
    p_kop1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kop1.paragraph_format.space_after = Pt(2)
    p_kop1.paragraph_format.line_spacing = 1.15
    run1 = p_kop1.add_run("PEMERINTAH KABUPATEN / KOTA ........................................................\nDINAS PENDIDIKAN DAN KEBUDAYAAN\n")
    run1.font.size = Pt(9.5)
    run1.font.bold = True
    run1.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    run_school = p_kop1.add_run("SD / MI ............................................................................................................\n")
    run_school.font.size = Pt(11.5)
    run_school.font.bold = True
    run_school.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(2)
    p_title.paragraph_format.space_after = Pt(2)
    run_title = p_title.add_run("ASESMEN SUMATIF LINGKUP MATERI / ULANGAN HARIAN\n")
    run_title.font.size = Pt(12)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    run_sub = p_title.add_run("MATA PELAJARAN: PAI & BUDI PEKERTI • KELAS 3 SD SEMESTER 1\n")
    run_sub.font.size = Pt(9.5)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    run_kur = p_title.add_run("Kurikulum Merdeka (Keputusan BSKAP No. 020/2026) • Alokasi Waktu: 60 Menit")
    run_kur.font.size = Pt(8.5)
    run_kur.font.italic = True
    run_kur.font.color.rgb = RGBColor(0x64, 0x74, 0x8b)

    # Double Border Line
    p_line = doc.add_paragraph()
    p_line.paragraph_format.space_after = Pt(8)
    run_line = p_line.add_run("━" * 58)
    run_line.font.bold = True
    run_line.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)
    run_line.font.size = Pt(10)

    # 2. IDENTITAS SISWA & NILAI (TABEL)
    table_id = doc.add_table(rows=1, cols=2)
    table_id.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_id.autofit = False

    # Left cell: identitas
    cell_left = table_id.cell(0, 0)
    cell_left.width = Inches(4.7)
    set_cell_background(cell_left, 'F8FAFC')
    set_cell_margins(cell_left, top=120, bottom=120, left=150, right=150)
    p_id = cell_left.paragraphs[0]
    p_id.paragraph_format.line_spacing = 1.3
    p_id.paragraph_format.space_after = Pt(0)
    p_id.add_run("Nama Lengkap : ........................................................................\n").font.size = Pt(9)
    p_id.add_run("Nomor Absen  : .................... / Kelas: 3 (Tiga) SD\n").font.size = Pt(9)
    p_id.add_run("Hari / Tanggal : ........................................................................").font.size = Pt(9)

    # Right cell: kotak nilai
    cell_right = table_id.cell(0, 1)
    cell_right.width = Inches(1.9)
    set_cell_background(cell_right, 'F0FDF4')
    set_cell_margins(cell_right, top=120, bottom=120, left=100, right=100)
    p_val = cell_right.paragraphs[0]
    p_val.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_val.paragraph_format.space_after = Pt(2)
    run_hdr = p_val.add_run("NILAI / PARAF GURU\n")
    run_hdr.font.size = Pt(8.5)
    run_hdr.font.bold = True
    run_hdr.font.color.rgb = RGBColor(0x16, 0x65, 0x34)
    run_score = p_val.add_run("...... / ......")
    run_score.font.size = Pt(16)
    run_score.font.bold = True
    run_score.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    # Petunjuk Umum
    p_petunjuk = doc.add_paragraph()
    p_petunjuk.paragraph_format.space_before = Pt(8)
    p_petunjuk.paragraph_format.space_after = Pt(8)
    r_pet = p_petunjuk.add_run("PETUNJUK UMUM: ")
    r_pet.font.bold = True
    r_pet.font.size = Pt(8.5)
    r_pet_txt = p_petunjuk.add_run("1. Berdoalah sebelum mulai mengerjakan soal. 2. Tuliskan nama dan nomor pada kolom yang tersedia. 3. Kerjakan terlebih dahulu soal yang dianggap mudah. 4. Teliti kembali pekerjaan sebelum diserahkan.")
    r_pet_txt.font.size = Pt(8.5)
    r_pet_txt.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    # MATERI BADGE
    p_mat = doc.add_paragraph()
    p_mat.paragraph_format.space_after = Pt(8)
    r_mat = p_mat.add_run("MATERI: BAB 5 — KISAH NABI MUHAMMAD SAW. SEBELUM & SESUDAH MENJADI RASUL (PERIODE MAKKAH)")
    r_mat.font.bold = True
    r_mat.font.size = Pt(9.5)
    r_mat.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    # ========================================================
    # BAGIAN A: PILIHAN GANDA (10 BUTIR)
    # ========================================================
    p_sec_a = doc.add_paragraph()
    p_sec_a.paragraph_format.space_before = Pt(4)
    p_sec_a.paragraph_format.space_after = Pt(4)
    r_sec_a = p_sec_a.add_run("BAGIAN A: PILIHAN GANDA")
    r_sec_a.font.bold = True
    r_sec_a.font.size = Pt(10)
    p_sec_a.add_run(" (Berilah tanda silang (X) pada huruf A, B, atau C di depan jawaban yang benar!)").font.italic = True

    pg_questions = [
        ("1.", "Nabi Muhammad saw. dilahirkan di Kota Makkah pada tanggal 12 Rabiul Awal. Tahun kelahiran beliau dinamakan Tahun Gajah karena bertepatan dengan peristiwa ...",
         "A. Terjadinya perang besar antarsuku di Jazirah Arab\nB. Penyerbuan pasukan bergajah Raja Abrahah yang hendak menghancurkan Ka'bah\nC. Terjadinya peristiwa banjir bandang yang melanda Kota Makkah"),
        ("2.", "Ayah Nabi Muhammad saw. bernama Abdullah yang wafat ketika beliau masih berada dalam kandungan ibunya. Oleh karena itu, sejak lahir Nabi Muhammad saw. berstatus sebagai anak ...",
         "A. Piatu\nB. Yatim\nC. Yatim piatu"),
        ("3.", "Semasa bayi, Nabi Muhammad saw. disusukan dan diasuh oleh seorang wanita berakhlak mulia dari perkampungan Bani Sa'ad yang bernama ...",
         "A. Halimah As-Sa'diyah\nB. Ummu Aiman\nC. Fatimah binti Asad"),
        ("4.", "Ketika Nabi Muhammad saw. berusia 8 tahun, kakek tercintanya Abdul Muthalib wafat. Setelah itu, beliau diasuh dan dilindungi dengan penuh kasih sayang oleh pamannya yang bernama ...",
         "A. Abu Lahab\nB. Abu Jahal\nC. Abu Thalib"),
        ("5.", "Sejak usia muda, Nabi Muhammad saw. dikenal sangat jujur dalam perkataan maupun perbuatan dan tidak pernah berbohong, sehingga penduduk Makkah memberinya gelar kehormatan ...",
         "A. Al-Faruq\nB. Al-Amin\nC. As-Siddiq"),
        ("6.", "Ketika terjadi perselisihan antarpemimpin suku Quraisy mengenai siapa yang berhak meletakkan batu Hajar Aswad di dinding Ka'bah, Nabi Muhammad saw. menyelesaikannya dengan cara bijak, yaitu ...",
         "A. Meletakkannya sendiri tanpa melibatkan suku-suku lain\nB. Membentangkan kain sorban agar perwakilan setiap suku bersama-sama memegang ujung kainnya\nC. Mengundi dengan anak panah"),
        ("7.", "Wahyu pertama yang diterima oleh Nabi Muhammad saw. saat bertahannuts di Gua Hira adalah ...",
         "A. Surah Al-Fatihah ayat 1–7\nB. Surah Al-'Alaq ayat 1–5\nC. Surah Al-Ikhlas ayat 1–4"),
        ("8.", "Peristiwa turunnya wahyu pertama menandai pengangkatan Nabi Muhammad saw. menjadi nabi dan rasul utusan Allah, yang terjadi ketika beliau berusia ...",
         "A. 25 Tahun\nB. 35 Tahun\nC. 40 Tahun"),
        ("9.", "Pada masa awal dakwah di Kota Makkah, Rasulullah saw. menyebarkan ajaran Islam secara sembunyi-sembunyi (sirriyah) yang berpusat di rumah seorang sahabat bernama ...",
         "A. Abu Bakar As-Siddiq\nB. Arqam bin Abi Arqam\nC. Umar bin Khattab"),
        ("10.", "Ketika Nabi Muhammad saw. mulai menyebarkan dakwah secara terang-terangan (jahriyah) di Bukit Shafa, kerabat beliau yang paling keras menentang, mencela, dan menghalangi dakwah Islam adalah ...",
         "A. Abu Thalib\nB. Abu Lahab\nC. Hamzah bin Abdul Muthalib")
    ]

    for num, q_text, opt_text in pg_questions:
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(2)
        p_q.paragraph_format.space_after = Pt(1)
        p_q.paragraph_format.line_spacing = 1.15
        r_num = p_q.add_run(f"{num} ")
        r_num.font.bold = True
        p_q.add_run(q_text)

        p_opt = doc.add_paragraph()
        p_opt.paragraph_format.left_indent = Inches(0.25)
        p_opt.paragraph_format.space_before = Pt(0)
        p_opt.paragraph_format.space_after = Pt(4)
        p_opt.paragraph_format.line_spacing = 1.15
        p_opt.add_run(opt_text)

    # ========================================================
    # BAGIAN B: ISIAN SINGKAT (5 BUTIR)
    # ========================================================
    p_sec_b = doc.add_paragraph()
    p_sec_b.paragraph_format.space_before = Pt(8)
    p_sec_b.paragraph_format.space_after = Pt(4)
    r_sec_b = p_sec_b.add_run("BAGIAN B: ISIAN SINGKAT")
    r_sec_b.font.bold = True
    r_sec_b.font.size = Pt(10)
    p_sec_b.add_run(" (Isilah titik-titik di bawah ini dengan jawaban yang tepat dan benar!)").font.italic = True

    isian_questions = [
        ("1.", "Ibunda Nabi Muhammad saw. yang wafat di Desa Abwa saat beliau masih berusia 6 tahun bernama Siti ....................................................................."),
        ("2.", "Gelar kehormatan Al-Amin yang disandang oleh Nabi Muhammad saw. memiliki arti orang yang ....................................................................."),
        ("3.", "Tempat menyendiri (tahannuts) yang digunakan Nabi Muhammad saw. untuk beribadah dan merenung sebelum menerima wahyu adalah Gua ....................................................................."),
        ("4.", "Malaikat agung yang diutus oleh Allah Swt. untuk menyampaikan wahyu Al-Qur'an kepada Nabi Muhammad saw. adalah Malaikat ....................................................................."),
        ("5.", "Golongan orang-orang mulia yang pertama kali memeluk agama Islam pada masa awal dakwah Rasulullah saw. disebut kelompok As-Sabiqunal .....................................................................")
    ]

    for num, q_text in isian_questions:
        p_is = doc.add_paragraph()
        p_is.paragraph_format.space_before = Pt(2)
        p_is.paragraph_format.space_after = Pt(4)
        p_is.paragraph_format.line_spacing = 1.25
        r_num = p_is.add_run(f"{num} ")
        r_num.font.bold = True
        p_is.add_run(q_text)

    # ========================================================
    # HALAMAN BARU: KUNCI JAWABAN & PEDOMAN PENSKORAN
    # ========================================================
    doc.add_page_break()

    p_kj_hdr = doc.add_paragraph()
    p_kj_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kj_hdr.paragraph_format.space_after = Pt(2)
    r_kj_t = p_kj_hdr.add_run("LEMBAR KUNCI JAWABAN DAN PEDOMAN PENSKORAN\n")
    r_kj_t.font.bold = True
    r_kj_t.font.size = Pt(11.5)
    r_kj_t.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    r_kj_sub = p_kj_hdr.add_run("Ulangan Harian PAI & BP Kelas 3 SD • Bab 5: Periode Makkah")
    r_kj_sub.font.bold = True
    r_kj_sub.font.size = Pt(9.5)
    r_kj_sub.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    doc.add_paragraph("━" * 58).paragraph_format.space_after = Pt(8)

    # Kunci Bagian A
    p_k_a = doc.add_paragraph()
    p_k_a.paragraph_format.space_after = Pt(2)
    r_k_a = p_k_a.add_run("I. KUNCI JAWABAN PILIHAN GANDA (BAGIAN A)")
    r_k_a.font.bold = True
    r_k_a.font.size = Pt(10)

    # Table for PG Keys (2 rows x 5 cols)
    t_pg = doc.add_table(rows=2, cols=5)
    t_pg.alignment = WD_TABLE_ALIGNMENT.CENTER
    pg_keys = [
        ("No. 1", "B (Raja Abrahah)"),
        ("No. 2", "B (Yatim)"),
        ("No. 3", "A (Halimah As-Sa'diyah)"),
        ("No. 4", "C (Abu Thalib)"),
        ("No. 5", "B (Al-Amin)"),
        ("No. 6", "B (Membentangkan Kain)"),
        ("No. 7", "B (Al-'Alaq: 1-5)"),
        ("No. 8", "C (40 Tahun)"),
        ("No. 9", "B (Arqam bin Abi Arqam)"),
        ("No. 10", "B (Abu Lahab)")
    ]

    for idx, (no, ans) in enumerate(pg_keys):
        row = idx // 5
        col = idx % 5
        cell = t_pg.cell(row, col)
        cell.width = Inches(1.3)
        set_cell_background(cell, 'F1F5F9' if row == 0 else 'FFFFFF')
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p_c = cell.paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c.paragraph_format.space_after = Pt(0)
        p_c.paragraph_format.line_spacing = 1.1
        r_no = p_c.add_run(f"{no}\n")
        r_no.font.bold = True
        r_no.font.size = Pt(8.5)
        r_ans = p_c.add_run(ans)
        r_ans.font.size = Pt(8)
        r_ans.font.bold = True
        r_ans.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    # Kunci Bagian B
    p_k_b = doc.add_paragraph()
    p_k_b.paragraph_format.space_before = Pt(8)
    p_k_b.paragraph_format.space_after = Pt(2)
    r_k_b = p_k_b.add_run("II. KUNCI JAWABAN ISIAN SINGKAT (BAGIAN B)")
    r_k_b.font.bold = True
    r_k_b.font.size = Pt(10)

    isian_keys = [
        ("1.", "Aminah / Siti Aminah"),
        ("2.", "Dapat dipercaya / Terpercaya / Amanah"),
        ("3.", "Hira (Gua Hira di Jabal Nur)"),
        ("4.", "Jibril a.s."),
        ("5.", "Awwalun (As-Sabiqunal Awwalun)")
    ]

    for num, ans_text in isian_keys:
        p_ik = doc.add_paragraph()
        p_ik.paragraph_format.left_indent = Inches(0.2)
        p_ik.paragraph_format.space_before = Pt(1)
        p_ik.paragraph_format.space_after = Pt(1)
        r_n = p_ik.add_run(f"{num} ")
        r_n.font.bold = True
        r_a = p_ik.add_run(ans_text)
        r_a.font.bold = True
        r_a.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    # PEDOMAN PENSKORAN TABLE
    p_rub = doc.add_paragraph()
    p_rub.paragraph_format.space_before = Pt(8)
    p_rub.paragraph_format.space_after = Pt(4)
    r_rub = p_rub.add_run("III. PEDOMAN PENSKORAN & PENILAIAN (SKOR MAKSIMAL = 100 POIN)")
    r_rub.font.bold = True
    r_rub.font.size = Pt(10)

    t_rub = doc.add_table(rows=4, cols=4)
    t_rub.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Bentuk Soal", "Jumlah Butir", "Bobot per Butir", "Skor Maksimal"]
    rows_data = [
        ["Pilihan Ganda (PG)", "10 Butir", "6 Poin", "60 Poin"],
        ["Isian Singkat", "5 Butir", "8 Poin", "40 Poin"],
        ["TOTAL SKOR MAKSIMAL", "15 Butir", "-", "100 POIN SEMPURNA"]
    ]

    for c_idx, h in enumerate(headers):
        cell = t_rub.cell(0, c_idx)
        set_cell_background(cell, '0F172A')
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p_h = cell.paragraphs[0]
        p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_h.paragraph_format.space_after = Pt(0)
        r_h = p_h.add_run(h)
        r_h.font.bold = True
        r_h.font.size = Pt(8.5)
        r_h.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for r_idx, r_data in enumerate(rows_data, start=1):
        for c_idx, val in enumerate(r_data):
            cell = t_rub.cell(r_idx, c_idx)
            bg = 'F8FAFC' if r_idx % 2 == 1 else 'FFFFFF'
            if r_idx == 3:
                bg = 'ECFDF5'
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
            p_c = cell.paragraphs[0]
            p_c.paragraph_format.space_after = Pt(0)
            if c_idx > 0:
                p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_c = p_c.add_run(val)
            r_c.font.size = Pt(8.5)
            if r_idx == 3:
                r_c.font.bold = True
                r_c.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    # Rumus Nilai
    p_rumus = doc.add_paragraph()
    p_rumus.paragraph_format.space_before = Pt(6)
    p_rumus.paragraph_format.space_after = Pt(12)
    p_rumus.paragraph_format.left_indent = Inches(0.1)
    r_rum = p_rumus.add_run("Perhitungan Nilai Akhir (NA) = (Skor Perolehan PG) + (Skor Perolehan Isian)")
    r_rum.font.bold = True
    r_rum.font.italic = True
    r_rum.font.size = Pt(8.5)
    r_rum.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # LEMBAR TANDA TANGAN BLANK TEMPLATE
    t_ttd = doc.add_table(rows=1, cols=2)
    t_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_ks = t_ttd.cell(0, 0)
    cell_ks.width = Inches(3.3)
    p_ks = cell_ks.paragraphs[0]
    p_ks.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ks.paragraph_format.line_spacing = 1.2
    p_ks.paragraph_format.space_after = Pt(0)
    p_ks.add_run("Mengetahui,\nKepala Sekolah .................................................\n\n\n\n\n").font.size = Pt(9)
    r_n_ks = p_ks.add_run("( ............................................................ )\n")
    r_n_ks.font.bold = True
    r_n_ks.font.underline = True
    r_n_ks.font.size = Pt(9)
    p_ks.add_run("NIP. ............................................................").font.size = Pt(8.5)

    cell_gr = t_ttd.cell(0, 1)
    cell_gr.width = Inches(3.3)
    p_gr = cell_gr.paragraphs[0]
    p_gr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_gr.paragraph_format.line_spacing = 1.2
    p_gr.paragraph_format.space_after = Pt(0)
    p_gr.add_run("........................, ...... ........................ 2026\nGuru Pengampu PAI & BP\n\n\n\n\n").font.size = Pt(9)
    r_n_gr = p_gr.add_run("( ............................................................ )\n")
    r_n_gr.font.bold = True
    r_n_gr.font.underline = True
    r_n_gr.font.size = Pt(9)
    p_gr.add_run("NIP. ............................................................").font.size = Pt(8.5)

    doc.save(output_path)
    print(f"Document successfully created at {output_path} (Size: {os.path.getsize(output_path)} bytes)")

if __name__ == '__main__':
    out1 = 'Soal_Ulangan_Harian_PAI_Kelas3_Bab5_Periode_Makkah.docx'
    out2 = os.path.join('public', 'Soal_Ulangan_Harian_PAI_Kelas3_Bab5_Periode_Makkah.docx')
    create_soal_docx(out1)
    create_soal_docx(out2)
