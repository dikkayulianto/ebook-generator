import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    tcPr = cell._tc.get_or_add_tcPr()
    borders_elm = OxmlElement('w:tcBorders')
    
    borders = {'top': top, 'bottom': bottom, 'left': left, 'right': right}
    for border_name, border_style in borders.items():
        if border_style:
            val = border_style.get('val', 'single')
            sz = str(border_style.get('sz', 4))
            space = str(border_style.get('space', 0))
            color = border_style.get('color', 'auto')
            b_elm = parse_xml(f'<w:{border_name} {nsdecls("w")} w:val="{val}" w:sz="{sz}" w:space="{space}" w:color="{color}"/>')
            borders_elm.append(b_elm)
        else:
            b_elm = parse_xml(f'<w:{border_name} {nsdecls("w")} w:val="none"/>')
            borders_elm.append(b_elm)
    tcPr.append(borders_elm)

# ==========================================
# FILE 1: SOAL PENILAIAN HARIAN (KERTAS F4)
# ==========================================
def create_soal_f4_doc():
    doc = docx.Document()
    
    # Kertas F4 / Folio Indonesia: 215 mm x 330 mm = 8.5 in x 13.0 in
    for section in doc.sections:
        section.page_width = Inches(8.5)
        section.page_height = Inches(13.0)
        section.top_margin = Inches(0.4)
        section.bottom_margin = Inches(0.4)
        section.left_margin = Inches(0.45)
        section.right_margin = Inches(0.45)
    
    # Outer Border Box Table (Frame hijau seperti gambar)
    outer_table = doc.add_table(rows=1, cols=1)
    outer_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    outer_table.autofit = False
    
    cell = outer_table.cell(0, 0)
    cell.width = Inches(7.6)
    set_cell_background(cell, "FFFFFF")
    set_cell_margins(cell, top=160, bottom=160, left=200, right=200)
    set_cell_borders(cell, 
                     top={'val': 'single', 'sz': 20, 'color': '16A34A'},
                     bottom={'val': 'single', 'sz': 20, 'color': '16A34A'},
                     left={'val': 'single', 'sz': 20, 'color': '16A34A'},
                     right={'val': 'single', 'sz': 20, 'color': '16A34A'})
    
    # Header Dokumen
    p_header = cell.paragraphs[0]
    p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_header.paragraph_format.space_before = Pt(0)
    p_header.paragraph_format.space_after = Pt(2)
    
    r_top = p_header.add_run("🕌   PENILAIAN HARIAN   📖\n")
    r_top.bold = True
    r_top.font.size = Pt(16)
    r_top.font.name = "Arial Black"
    r_top.font.color.rgb = RGBColor(0x15, 0x80, 0x3D) # Emerald Green
    
    r_sub = p_header.add_run("PENDIDIKAN AGAMA ISLAM DAN BUDI PEKERTI\n")
    r_sub.bold = True
    r_sub.font.size = Pt(12)
    r_sub.font.name = "Arial"
    r_sub.font.color.rgb = RGBColor(0x16, 0x65, 0x34)
    
    r_badge = p_header.add_run(" ★ KELAS 3 ★ \n")
    r_badge.bold = True
    r_badge.font.size = Pt(11)
    r_badge.font.name = "Arial Black"
    r_badge.font.color.rgb = RGBColor(0xF4, 0x3F, 0x5E) # Rose Pink
    
    r_materi = p_header.add_run("Materi: Kisah Kelahiran dan Masa Kanak-Kanak Nabi Muhammad saw.")
    r_materi.bold = True
    r_materi.italic = True
    r_materi.font.size = Pt(10)
    r_materi.font.name = "Arial"
    r_materi.font.color.rgb = RGBColor(0x06, 0x5F, 0x46)
    
    # Baris Identitas Siswa
    p_id = cell.add_paragraph()
    p_id.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_id.paragraph_format.space_before = Pt(6)
    p_id.paragraph_format.space_after = Pt(6)
    r_id = p_id.add_run("Nama : ...............................................   Kelas : .................   No. Absen : ..........")
    r_id.bold = True
    r_id.font.size = Pt(10)
    r_id.font.name = "Arial"
    r_id.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    
    # Section A Header
    p_secA = cell.add_paragraph()
    p_secA.paragraph_format.space_before = Pt(4)
    p_secA.paragraph_format.space_after = Pt(5)
    r_secA_icon = p_secA.add_run(" 🅐 ")
    r_secA_icon.bold = True
    r_secA_icon.font.size = Pt(12)
    r_secA_icon.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
    
    r_secA_text = p_secA.add_run("Berilah tanda silang (X) pada huruf a, b, atau c di lembar jawaban yang paling benar!")
    r_secA_text.bold = True
    r_secA_text.font.size = Pt(9.5)
    r_secA_text.font.name = "Arial"
    r_secA_text.font.color.rgb = RGBColor(0xBE, 0x18, 0x5D)
    
    # Tabel 2 Kolom untuk PG 1-5 (Kiri) dan PG 6-10 (Kanan)
    table_pg = cell.add_table(rows=1, cols=2)
    table_pg.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_pg.autofit = False
    
    col_left = table_pg.cell(0, 0)
    col_right = table_pg.cell(0, 1)
    col_left.width = Inches(3.7)
    col_right.width = Inches(3.7)
    
    set_cell_margins(col_left, top=40, bottom=40, left=60, right=80)
    set_cell_margins(col_right, top=40, bottom=40, left=80, right=60)
    
    set_cell_borders(col_left, right={'val': 'dashed', 'sz': 10, 'color': '86EFAC'})
    set_cell_borders(col_right, left={'val': 'dashed', 'sz': 10, 'color': '86EFAC'})
    
    # Soal Kolom Kiri (1 - 5)
    q_left = [
        ("1. Nabi Muhammad saw. dilahirkan di kota suci ....", 
         [("a", "Madinah"), ("b", "Makkah"), ("c", "Thaif")]),
        ("2. Tahun kelahiran Nabi disebut tahun Gajah karena peristiwa ....",
         [("a", "banyak gajah di kota Makkah"), ("b", "penyerangan Ka'bah oleh tentara bergajah"), ("c", "lomba menunggang gajah")]),
        ("3. Ayah Nabi Muhammad saw. bernama Abdullah. Beliau wafat ketika Nabi ....",
         [("a", "masih dalam kandungan ibunya"), ("b", "sedang berdagang"), ("c", "berusia 10 tahun")]),
        ("4. Ibu yang menyusui Nabi di desa Bani Sa'ad yang sejuk dan asri bernama ....",
         [("a", "Siti Khadijah"), ("b", "Halimah As-Sa'diyah"), ("c", "Fatimah Az-Zahra")]),
        ("5. Ibunda Nabi wafat di desa Abwa saat Nabi berusia 6 tahun, sehingga Nabi menjadi ....",
         [("a", "yatim"), ("b", "piatu"), ("c", "yatim piatu")])
    ]
    
    for i, (q_text, opts) in enumerate(q_left):
        p = col_left.add_paragraph() if i > 0 else col_left.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(q_text)
        r.bold = True
        r.font.size = Pt(9)
        r.font.name = "Arial"
        r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        
        for code, opt_text in opts:
            p_opt = col_left.add_paragraph()
            p_opt.paragraph_format.left_indent = Inches(0.15)
            p_opt.paragraph_format.space_before = Pt(0)
            p_opt.paragraph_format.space_after = Pt(0)
            r_opt = p_opt.add_run(f"{code}.  {opt_text}")
            r_opt.font.size = Pt(8.8)
            r_opt.font.name = "Arial"
            r_opt.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
            
    # Soal Kolom Kanan (6 - 10)
    q_right = [
        ("6. Setelah ibunda wafat, Nabi diasuh kakeknya yang bernama ....",
         [("a", "Abu Thalib"), ("b", "Abdul Muthalib"), ("c", "Abu Lahab")]),
        ("7. Ketika kakeknya wafat saat Nabi berumur 8 tahun, Nabi diasuh oleh pamannya ....",
         [("a", "Abu Jahal"), ("b", "Abu Thalib"), ("c", "Hamzah")]),
        ("8. Pada masa kanak-kanak, Nabi Muhammad saw. membantu pamannya dengan ....",
         [("a", "menangkap ikan di laut"), ("b", "menggembala kambing"), ("c", "membuat pedang")]),
        ("9. Hikmah menggembala kambing sejak kanak-kanak adalah melatih sikap ....",
         [("a", "sombong dan manja"), ("b", "sabar, disiplin, dan mandiri"), ("c", "malas dan mudah mengeluh")]),
        ("10. Sejak masa kanak-kanak, Nabi Muhammad saw. tidak pernah berbohong sehingga dijuluki ....",
         [("a", "Al-Amin (dapat dipercaya)"), ("b", "Al-Farabi"), ("c", "Al-Kindi")])
    ]
    
    for i, (q_text, opts) in enumerate(q_right):
        p = col_right.add_paragraph() if i > 0 else col_right.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(q_text)
        r.bold = True
        r.font.size = Pt(9)
        r.font.name = "Arial"
        r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        
        for code, opt_text in opts:
            p_opt = col_right.add_paragraph()
            p_opt.paragraph_format.left_indent = Inches(0.15)
            p_opt.paragraph_format.space_before = Pt(0)
            p_opt.paragraph_format.space_after = Pt(0)
            r_opt = p_opt.add_run(f"{code}.  {opt_text}")
            r_opt.font.size = Pt(8.8)
            r_opt.font.name = "Arial"
            r_opt.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Section B Header
    p_secB = cell.add_paragraph()
    p_secB.paragraph_format.space_before = Pt(8)
    p_secB.paragraph_format.space_after = Pt(4)
    r_secB_icon = p_secB.add_run(" 🅑 ")
    r_secB_icon.bold = True
    r_secB_icon.font.size = Pt(12)
    r_secB_icon.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
    
    r_secB_text = p_secB.add_run("Isilah titik-titik berikut dengan jawaban yang tepat dan benar!")
    r_secB_text.bold = True
    r_secB_text.font.size = Pt(9.5)
    r_secB_text.font.name = "Arial"
    r_secB_text.font.color.rgb = RGBColor(0xBE, 0x18, 0x5D)
    
    # Soal Bagian B (11 - 15)
    q_secB = [
        "11. Nabi Muhammad saw. lahir pada hari ........................... tanggal 12 Rabiul Awwal Tahun Gajah.",
        "12. Ibu kandung Nabi Muhammad saw. yang berakhlak mulia bernama ...................................",
        "13. Nama 'Muhammad' diberikan oleh kakeknya yaitu Abdul Muthalib, yang artinya orang yang ...........................",
        "14. Nabi Muhammad saw. diasuh oleh pamannya Abu Thalib mulai sejak berusia ........................... tahun.",
        "15. Keteladanan masa kanak-kanak Nabi Muhammad saw. yang dapat kita tiru di sekolah adalah ..........................."
    ]
    
    for q_text in q_secB:
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(2.5)
        p.paragraph_format.space_after = Pt(2.5)
        p.paragraph_format.left_indent = Inches(0.1)
        r = p.add_run(q_text)
        r.font.size = Pt(9)
        r.font.name = "Arial"
        r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    # Footer Banner Motivasi
    p_footer = cell.add_paragraph()
    p_footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_footer.paragraph_format.space_before = Pt(12)
    p_footer.paragraph_format.space_after = Pt(2)
    
    r_ft = p_footer.add_run("🌸 💖  Mari Meneladani Akhlak Mulia Nabi Muhammad saw. Sejak Masa Kanak-Kanak!  💖 🕋")
    r_ft.bold = True
    r_ft.font.size = Pt(9.5)
    r_ft.font.name = "Arial Black"
    r_ft.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)

    out_file_1 = "Soal_Penilaian_Harian_PAI_Kelas3_Kisah_Nabi_Muhammad_F4.docx"
    out_file_2 = os.path.join("public", "Soal_Penilaian_Harian_PAI_Kelas3_Kisah_Nabi_Muhammad_F4.docx")
    doc.save(out_file_1)
    doc.save(out_file_2)
    print(f"File 1 (Soal F4) created: {out_file_1}")


# ========================================================
# FILE 2: KUNCI JAWABAN & PEDOMAN PENSKORAN (KERTAS F4)
# ========================================================
def create_kunci_f4_doc():
    doc = docx.Document()
    
    # Kertas F4 / Folio Indonesia: 8.5 in x 13.0 in
    for section in doc.sections:
        section.page_width = Inches(8.5)
        section.page_height = Inches(13.0)
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)
        
    # Header Kunci Jawaban
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(1)
    r1 = p_title.add_run("KUNCI JAWABAN & PEDOMAN PENSKORAN\n")
    r1.bold = True
    r1.font.size = Pt(14)
    r1.font.name = "Arial"
    r1.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
    
    r2 = p_title.add_run("PENILAIAN HARIAN PENDIDIKAN AGAMA ISLAM DAN BUDI PEKERTI\nKELAS 3 SEMESTER 1 (KURIKULUM MERDEKA)\n")
    r2.bold = True
    r2.font.size = Pt(11)
    r2.font.name = "Arial"
    r2.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    
    r3 = p_title.add_run("Materi: Kisah Kelahiran dan Masa Kanak-Kanak Nabi Muhammad saw. (F4 Format)")
    r3.italic = True
    r3.font.size = Pt(9.5)
    r3.font.color.rgb = RGBColor(0x47, 0x55, 0x69)
    
    # Garis Pembatas
    p_line = doc.add_paragraph()
    p_line.paragraph_format.space_before = Pt(2)
    p_line.paragraph_format.space_after = Pt(8)
    r_line = p_line.add_run("—" * 65)
    r_line.font.color.rgb = RGBColor(0x16, 0xA3, 0x4A)
    
    # BAGIAN A: TABEL KUNCI PILIHAN GANDA
    p_secA = doc.add_paragraph()
    p_secA.paragraph_format.space_before = Pt(4)
    p_secA.paragraph_format.space_after = Pt(4)
    r_sa = p_secA.add_run("A. KUNCI JAWABAN PILIHAN GANDA (Bobot: 1 Poin per Soal | Maksimal = 10 Poin)")
    r_sa.bold = True
    r_sa.font.size = Pt(10.5)
    r_sa.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
    
    table_a = doc.add_table(rows=11, cols=4)
    table_a.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_a.autofit = False
    
    headers_a = ["No.", "Kunci", "Pembahasan / Materi ATP", "Skor"]
    col_widths_a = [Inches(0.6), Inches(0.8), Inches(5.1), Inches(0.8)]
    
    hdr_cells_a = table_a.rows[0].cells
    for i, title in enumerate(headers_a):
        hdr_cells_a[i].width = col_widths_a[i]
        set_cell_background(hdr_cells_a[i], "15803D")
        set_cell_margins(hdr_cells_a[i], top=60, bottom=60, left=80, right=80)
        p = hdr_cells_a[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    data_a = [
        ("1", "b", "Makkah (Kota tempat kelahiran Nabi Muhammad saw. di jazirah Arab)", "1"),
        ("2", "b", "Penyerangan Ka'bah oleh tentara bergajah yang dipimpin Raja Abrahah", "1"),
        ("3", "a", "Masih dalam kandungan ibunya (Ayahanda Abdullah wafat sebelum Nabi lahir)", "1"),
        ("4", "b", "Halimah As-Sa'diyah (Ibu asuh yang menyusui Nabi di desa Bani Sa'ad)", "1"),
        ("5", "c", "Yatim piatu (Ibunda Siti Aminah wafat di Abwa ketika Nabi berusia 6 tahun)", "1"),
        ("6", "b", "Abdul Muthalib (Kakek yang memberi nama Muhammad dan sangat menyayangi Nabi)", "1"),
        ("7", "b", "Abu Thalib (Paman yang mengasuh Nabi sejak umur 8 tahun setelah kakek wafat)", "1"),
        ("8", "b", "Menggembala kambing (Membantu paman mencari nafkah dan melatih kemandirian)", "1"),
        ("9", "b", "Sabar, disiplin, dan mandiri (Nilai karakter utama dari pekerjaan menggembala)", "1"),
        ("10", "a", "Al-Amin (Artinya orang yang dapat dipercaya karena kejujuran perkataannya)", "1"),
    ]
    
    for row_idx, row_data in enumerate(data_a, start=1):
        row_cells = table_a.rows[row_idx].cells
        bg_color = "F0FDF4" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].width = col_widths_a[col_idx]
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=50, bottom=50, left=80, right=80)
            set_cell_borders(row_cells[col_idx],
                             top={'val': 'single', 'sz': 4, 'color': 'D1D5DB'},
                             bottom={'val': 'single', 'sz': 4, 'color': 'D1D5DB'},
                             left={'val': 'single', 'sz': 4, 'color': 'D1D5DB'},
                             right={'val': 'single', 'sz': 4, 'color': 'D1D5DB'})
            p = row_cells[col_idx].paragraphs[0]
            if col_idx in [0, 1, 3]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(text)
            r.font.size = Pt(9)
            if col_idx == 1:
                r.bold = True
                r.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)

    # BAGIAN B: TABEL KUNCI ISIAN
    p_secB = doc.add_paragraph()
    p_secB.paragraph_format.space_before = Pt(12)
    p_secB.paragraph_format.space_after = Pt(4)
    r_sb = p_secB.add_run("B. KUNCI JAWABAN ISIAN SINGKAT (Bobot: 2 Poin per Soal | Maksimal = 10 Poin)")
    r_sb.bold = True
    r_sb.font.size = Pt(10.5)
    r_sb.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
    
    table_b = doc.add_table(rows=6, cols=4)
    table_b.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_b.autofit = False
    
    headers_b = ["No.", "Kunci Jawaban Tepat", "Alternatif Jawaban Diterima", "Skor"]
    col_widths_b = [Inches(0.6), Inches(2.5), Inches(3.4), Inches(0.8)]
    
    hdr_cells_b = table_b.rows[0].cells
    for i, title in enumerate(headers_b):
        hdr_cells_b[i].width = col_widths_b[i]
        set_cell_background(hdr_cells_b[i], "15803D")
        set_cell_margins(hdr_cells_b[i], top=60, bottom=60, left=80, right=80)
        p = hdr_cells_b[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    data_b = [
        ("11", "Senin", "Hari Senin / isnain", "2"),
        ("12", "Siti Aminah", "Aminah / Aminah binti Wahab", "2"),
        ("13", "Terpuji", "Orang yang selalu dipuji / terpuji", "2"),
        ("14", "8 (delapan)", "Delapan / 8 tahun", "2"),
        ("15", "Jujur / Amanah / Mandiri", "Suka menolong / rajin / disiplin / sabar", "2"),
    ]
    
    for row_idx, row_data in enumerate(data_b, start=1):
        row_cells = table_b.rows[row_idx].cells
        bg_color = "F0FDF4" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].width = col_widths_b[col_idx]
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=50, bottom=50, left=80, right=80)
            set_cell_borders(row_cells[col_idx],
                             top={'val': 'single', 'sz': 4, 'color': 'D1D5DB'},
                             bottom={'val': 'single', 'sz': 4, 'color': 'D1D5DB'},
                             left={'val': 'single', 'sz': 4, 'color': 'D1D5DB'},
                             right={'val': 'single', 'sz': 4, 'color': 'D1D5DB'})
            p = row_cells[col_idx].paragraphs[0]
            if col_idx in [0, 3]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(text)
            r.font.size = Pt(9)
            if col_idx == 1:
                r.bold = True
                r.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)

    # BAGIAN C: PEDOMAN PENSKORAN & RUMUS NILAI
    p_secC = doc.add_paragraph()
    p_secC.paragraph_format.space_before = Pt(14)
    p_secC.paragraph_format.space_after = Pt(4)
    r_sc = p_secC.add_run("C. PEDOMAN PENSKORAN & PENGHITUNGAN NILAI AKHIR")
    r_sc.bold = True
    r_sc.font.size = Pt(10.5)
    r_sc.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
    
    info_points = [
        "1. Skor Maksimal Bagian A (Pilihan Ganda) = 10 x 1 = 10 poin.",
        "2. Skor Maksimal Bagian B (Isian Singkat) = 5 x 2 = 10 poin.",
        "3. Total Skor Maksimal Keseluruhan = 10 + 10 = 20 poin."
    ]
    for pt in info_points:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.2)
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(pt)
        r.font.size = Pt(9.5)
        
    p_box = doc.add_paragraph()
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_box.paragraph_format.space_before = Pt(6)
    p_box.paragraph_format.space_after = Pt(14)
    r_bx = p_box.add_run("RUMUS NILAI AKHIR (SKALA 0 - 100):\nNilai Akhir = ((Skor Pilihan Ganda + Skor Isian) / 20) x 100")
    r_bx.bold = True
    r_bx.font.size = Pt(11)
    r_bx.font.color.rgb = RGBColor(0x06, 0x5F, 0x46)
    
    # Tanda Tangan Guru & Orang Tua
    table_ttd = doc.add_table(rows=1, cols=2)
    table_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_ttd.autofit = False
    
    c_wali = table_ttd.cell(0, 0)
    c_guru = table_ttd.cell(0, 1)
    c_wali.width = Inches(3.6)
    c_guru.width = Inches(3.6)
    
    p_w = c_wali.paragraphs[0]
    p_w.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_w.add_run("Mengetahui,\nOrang Tua / Wali Siswa\n\n\n\n\n( .................................................. )")
    
    p_g = c_guru.paragraphs[0]
    p_g.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_g.add_run("...................., .............................. 2026\nGuru Pendidikan Agama Islam\n\n\n\n\n( .................................................. )")

    out_file_1 = "Kunci_Jawaban_Penilaian_Harian_PAI_Kelas3_Bab5_F4.docx"
    out_file_2 = os.path.join("public", "Kunci_Jawaban_Penilaian_Harian_PAI_Kelas3_Bab5_F4.docx")
    doc.save(out_file_1)
    doc.save(out_file_2)
    print(f"File 2 (Kunci F4) created: {out_file_1}")

if __name__ == "__main__":
    create_soal_f4_doc()
    create_kunci_f4_doc()
