# -*- coding: utf-8 -*-
"""
Generate Microsoft Word (.docx) matching the exact worksheet design from the user's reference:
- Illustrated Header Title
- Identity Row
- Section A: 10 Pilihan Ganda in a 2-Column Table (Questions 1-5 Left, Questions 6-10 Right)
- Section B: 5 Isian Singkat in 1 Column
- Bottom Quote Banner
- Key Answer Page
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

def create_styled_worksheet(output_path):
    doc = docx.Document()

    # A4 Page Margins (Slim margins to fit beautifully on 1 page)
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.4)
        section.bottom_margin = Inches(0.4)
        section.left_margin = Inches(0.5)
        section.right_margin = Inches(0.5)

    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(9.5)
    font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)

    # 1. HEADER TITLE (PENILAIAN HARIAN)
    p_h1 = doc.add_paragraph()
    p_h1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_h1.paragraph_format.space_before = Pt(0)
    p_h1.paragraph_format.space_after = Pt(1)
    r1 = p_h1.add_run("PENILAIAN HARIAN\n")
    r1.font.size = Pt(16)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0x15, 0x80, 0x3d)

    r2 = p_h1.add_run("PENDIDIKAN AGAMA ISLAM DAN BUDI PEKERTI\n")
    r2.font.size = Pt(12)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(0x16, 0xa3, 0x4a)

    r_k = p_h1.add_run("KELAS 3\n")
    r_k.font.size = Pt(11)
    r_k.font.bold = True
    r_k.font.color.rgb = RGBColor(0xe1, 0x1d, 0x48)

    r_m = p_h1.add_run("Materi: Kisah Kelahiran dan Masa Kanak-Kanak Nabi Muhammad saw.")
    r_m.font.size = Pt(9)
    r_m.font.bold = True
    r_m.font.color.rgb = RGBColor(0x06, 0x5f, 0x46)

    # 2. IDENTITAS ROW
    p_id = doc.add_paragraph()
    p_id.paragraph_format.space_before = Pt(4)
    p_id.paragraph_format.space_after = Pt(6)
    p_id.paragraph_format.line_spacing = 1.15
    r_id = p_id.add_run("Nama : _________________________________     Kelas : _______________     No. Absen : _________")
    r_id.font.size = Pt(9)
    r_id.font.bold = True
    r_id.font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)

    # 3. SECTION A HEADER (PINK BAR)
    t_sec_a = doc.add_table(rows=1, cols=2)
    t_sec_a.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sec_a.autofit = False

    cell_a_badge = t_sec_a.cell(0, 0)
    cell_a_badge.width = Inches(0.4)
    set_cell_background(cell_a_badge, '15803D')
    p_badge = cell_a_badge.paragraphs[0]
    p_badge.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_badge.paragraph_format.space_after = Pt(0)
    r_ab = p_badge.add_run("A.")
    r_ab.font.bold = True
    r_ab.font.size = Pt(10)
    r_ab.font.color.rgb = RGBColor(0xff, 0xff, 0xff)

    cell_a_txt = t_sec_a.cell(0, 1)
    cell_a_txt.width = Inches(6.87)
    set_cell_background(cell_a_txt, 'FCE7F3')
    set_cell_margins(cell_a_txt, top=40, bottom=40, left=100, right=100)
    p_at = cell_a_txt.paragraphs[0]
    p_at.paragraph_format.space_after = Pt(0)
    r_at = p_at.add_run("Berilah tanda silang (X) pada huruf A, B, atau C di lembar jawaban yang dianggap paling benar!")
    r_at.font.bold = True
    r_at.font.size = Pt(8.5)
    r_at.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # 4. SECTION A QUESTIONS: 2-COLUMN TABLE (Left = 1-5, Right = 6-10)
    t_pg = doc.add_table(rows=1, cols=2)
    t_pg.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_pg.autofit = False

    cell_left = t_pg.cell(0, 0)
    cell_left.width = Inches(3.6)
    set_cell_margins(cell_left, top=30, bottom=30, left=60, right=100)

    cell_right = t_pg.cell(0, 1)
    cell_right.width = Inches(3.6)
    set_cell_margins(cell_right, top=30, bottom=30, left=100, right=60)

    # Questions 1 to 5 (Left)
    left_qs = [
        ("1.", "Nabi Muhammad saw. lahir di kota ....", ["a.  Makkah", "b.  Madinah", "c.  Yatsrib"]),
        ("2.", "Nabi Muhammad saw. kecilnya dikenal dengan sebutan ....", ["a.  Al-Amin", "b.  As-Siddiq", "c.  Al-Farabi"]),
        ("3.", "Ketika masih kecil, Nabi Muhammad saw. suka membantu ....", ["a.  berdagang", "b.  orang tuanya", "c.  teman-temannya"]),
        ("4.", "Peristiwa yang menunjukkan Nabi Muhammad saw. dipercaya oleh masyarakat adalah ....", ["a.  berkelana ke negeri lain", "b.  dikenal sebagai Al-Amin", "c.  menikah dengan Khadijah"]),
        ("5.", "Salah satu keteladanan Nabi Muhammad saw. pada masa kanak-kanak adalah ....", ["a.  suka berbohong", "b.  jujur dan amanah", "c.  pemarah"])
    ]

    for idx, (num, q, opts) in enumerate(left_qs):
        p_q = cell_left.paragraphs[0] if idx == 0 else cell_left.add_paragraph()
        p_q.paragraph_format.space_before = Pt(2)
        p_q.paragraph_format.space_after = Pt(1)
        p_q.paragraph_format.line_spacing = 1.15
        r_num = p_q.add_run(f"{num} ")
        r_num.font.bold = True
        r_num.font.size = Pt(8.5)
        p_q.add_run(q).font.size = Pt(8.5)

        for opt in opts:
            p_o = cell_left.add_paragraph()
            p_o.paragraph_format.left_indent = Inches(0.18)
            p_o.paragraph_format.space_before = Pt(0)
            p_o.paragraph_format.space_after = Pt(0)
            p_o.paragraph_format.line_spacing = 1.15
            p_o.add_run(opt).font.size = Pt(8)

    # Questions 6 to 10 (Right)
    right_qs = [
        ("6.", "Ibu Nabi Muhammad saw. bernama ....", ["a.  Aisyah", "b.  Siti Khadijah", "c.  Fatimah"]),
        ("7.", "Ketika berumur 40 tahun, Nabi Muhammad saw. menerima wahyu pertama di Gua ....", ["a.  Hira", "b.  Tsur", "c.  Uhud"]),
        ("8.", "Sikap yang sesuai dengan ajaran Nabi Muhammad saw. saat berdoa adalah ....", ["a.  berdoa dengan khusyuk", "b.  berdoa sambil bermain", "c.  berdoa sambil tidur"]),
        ("9.", "Ibadah haji dilakukan di ....", ["a.  Masjid Nabawi", "b.  Masjidil Haram", "c.  Masjid Aqsa"]),
        ("10.", "Salah satu manfaat meneladani Nabi Muhammad saw. adalah ....", ["a.  hidup disiplin dan jujur", "b.  malas beribadah", "c.  suka marah"])
    ]

    for idx, (num, q, opts) in enumerate(right_qs):
        p_q = cell_right.paragraphs[0] if idx == 0 else cell_right.add_paragraph()
        p_q.paragraph_format.space_before = Pt(2)
        p_q.paragraph_format.space_after = Pt(1)
        p_q.paragraph_format.line_spacing = 1.15
        r_num = p_q.add_run(f"{num} ")
        r_num.font.bold = True
        r_num.font.size = Pt(8.5)
        p_q.add_run(q).font.size = Pt(8.5)

        for opt in opts:
            p_o = cell_right.add_paragraph()
            p_o.paragraph_format.left_indent = Inches(0.18)
            p_o.paragraph_format.space_before = Pt(0)
            p_o.paragraph_format.space_after = Pt(0)
            p_o.paragraph_format.line_spacing = 1.15
            p_o.add_run(opt).font.size = Pt(8)

    # 5. SECTION B HEADER (PINK BAR)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    t_sec_b = doc.add_table(rows=1, cols=2)
    t_sec_b.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sec_b.autofit = False

    cell_b_badge = t_sec_b.cell(0, 0)
    cell_b_badge.width = Inches(0.4)
    set_cell_background(cell_b_badge, '15803D')
    p_bb = cell_b_badge.paragraphs[0]
    p_bb.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_bb.paragraph_format.space_after = Pt(0)
    r_bb = p_bb.add_run("B.")
    r_bb.font.bold = True
    r_bb.font.size = Pt(10)
    r_bb.font.color.rgb = RGBColor(0xff, 0xff, 0xff)

    cell_b_txt = t_sec_b.cell(0, 1)
    cell_b_txt.width = Inches(6.87)
    set_cell_background(cell_b_txt, 'FCE7F3')
    set_cell_margins(cell_b_txt, top=40, bottom=40, left=100, right=100)
    p_bt = cell_b_txt.paragraphs[0]
    p_bt.paragraph_format.space_after = Pt(0)
    r_bt = p_bt.add_run("Isilah titik-titik berikut dengan jawaban yang tepat!")
    r_bt.font.bold = True
    r_bt.font.size = Pt(8.5)
    r_bt.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)

    # 6. QUESTIONS 11-15 (FULL WIDTH)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    isian_items = [
        ("11.", "Nabi Muhammad saw. lahir pada tahun ................................................. di kota Makkah."),
        ("12.", "Masa kecil Nabi Muhammad saw. dikenal dengan sebutan ................................................."),
        ("13.", "Peristiwa penting yang terjadi saat Nabi Muhammad saw. berusia 40 tahun adalah menerima wahyu di ................................................."),
        ("14.", "Ketika melaksanakan ibadah haji, kita harus ................................................. dan mengikuti aturan yang ada."),
        ("15.", "Keteladanan Nabi Muhammad saw. yang dapat kita tiru adalah .................................................")
    ]

    for num, q_txt in isian_items:
        p_is = doc.add_paragraph()
        p_is.paragraph_format.space_before = Pt(1)
        p_is.paragraph_format.space_after = Pt(3)
        p_is.paragraph_format.line_spacing = 1.15
        r_n = p_is.add_run(f"{num} ")
        r_n.font.bold = True
        r_n.font.size = Pt(8.5)
        p_is.add_run(q_txt).font.size = Pt(8.5)

    # 7. BOTTOM BANNER
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    t_ban = doc.add_table(rows=1, cols=1)
    t_ban.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_ban = t_ban.cell(0, 0)
    cell_ban.width = Inches(7.27)
    set_cell_background(cell_ban, 'FDF2F8')
    set_cell_margins(cell_ban, top=60, bottom=60, left=120, right=120)
    p_ban = cell_ban.paragraphs[0]
    p_ban.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ban.paragraph_format.space_after = Pt(0)
    r_ban = p_ban.add_run("♥ Mari meneladani akhlak mulia Nabi Muhammad saw. dalam kehidupan sehari-hari! ♥")
    r_ban.font.bold = True
    r_ban.font.size = Pt(9)
    r_ban.font.color.rgb = RGBColor(0x9d, 0x17, 0x4d)

    # 8. HALAMAN 2: KUNCI JAWABAN LENGKAP
    doc.add_page_break()
    p_k_title = doc.add_paragraph()
    p_k_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_kt = p_k_title.add_run("KUNCI JAWABAN & PEDOMAN PENSKORAN\nPenilaian Harian PAI Kelas 3 — Kisah Nabi Muhammad saw.")
    r_kt.font.bold = True
    r_kt.font.size = Pt(11)
    r_kt.font.color.rgb = RGBColor(0x15, 0x80, 0x3d)

    doc.add_paragraph("━" * 58).paragraph_format.space_after = Pt(6)

    # Kunci PG
    p_kpg = doc.add_paragraph()
    p_kpg.add_run("A. Kunci Pilihan Ganda (1–10):\n").font.bold = True
    kunci_pg_text = (
        "1. a. Makkah\n"
        "2. a. Al-Amin\n"
        "3. a. berdagang (dan menggembala domba)\n"
        "4. b. dikenal sebagai Al-Amin\n"
        "5. b. jujur dan amanah\n"
        "6. b. Siti Khadijah (Istri) / Siti Aminah (Ibu kandung)\n"
        "7. a. Hira\n"
        "8. a. berdoa dengan khusyuk\n"
        "9. b. Masjidil Haram\n"
        "10. a. hidup disiplin dan jujur"
    )
    p_kpg.add_run(kunci_pg_text).font.size = Pt(8.5)

    # Kunci Isian
    p_kis = doc.add_paragraph()
    p_kis.paragraph_format.space_before = Pt(6)
    p_kis.add_run("B. Kunci Isian Singkat (11–15):\n").font.bold = True
    kunci_is_text = (
        "11. Tahun Gajah (571 Masehi)\n"
        "12. Al-Amin (orang yang dapat dipercaya)\n"
        "13. Gua Hira (Surah Al-'Alaq ayat 1-5)\n"
        "14. khusyuk / tertib / ikhlas\n"
        "15. jujur, amanah, menyayangi sesama, dan berbakti"
    )
    p_kis.add_run(kunci_is_text).font.size = Pt(8.5)

    doc.save(output_path)
    print(f"Created styled worksheet docx at {output_path} (Size: {os.path.getsize(output_path)} bytes)")

if __name__ == '__main__':
    out1 = 'Soal_Penilaian_Harian_Kelas3_Kisah_Nabi_Muhammad.docx'
    out2 = os.path.join('public', 'Soal_Penilaian_Harian_Kelas3_Kisah_Nabi_Muhammad.docx')
    create_styled_worksheet(out1)
    create_styled_worksheet(out2)
