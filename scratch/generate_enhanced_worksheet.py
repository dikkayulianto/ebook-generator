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

def create_styled_document():
    doc = docx.Document()
    
    # Set page margins to narrow (0.4 inch) so it fits beautifully on 1 page
    for section in doc.sections:
        section.top_margin = Inches(0.35)
        section.bottom_margin = Inches(0.35)
        section.left_margin = Inches(0.4)
        section.right_margin = Inches(0.4)
        section.page_width = Inches(8.27)  # A4
        section.page_height = Inches(11.69)
    
    # Outer Border Box Table (like the green container in reference)
    outer_table = doc.add_table(rows=1, cols=1)
    outer_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    outer_table.autofit = False
    
    cell = outer_table.cell(0, 0)
    cell.width = Inches(7.47)
    set_cell_background(cell, "FFFFFF")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    set_cell_borders(cell, 
                     top={'val': 'single', 'sz': 18, 'color': '2E7D32'},
                     bottom={'val': 'single', 'sz': 18, 'color': '2E7D32'},
                     left={'val': 'single', 'sz': 18, 'color': '2E7D32'},
                     right={'val': 'single', 'sz': 18, 'color': '2E7D32'})
    
    # Inside the container cell, we add content
    p_header = cell.paragraphs[0]
    p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_header.paragraph_format.space_before = Pt(0)
    p_header.paragraph_format.space_after = Pt(1)
    
    r_top = p_header.add_run("🕌  PENILAIAN HARIAN  📖\n")
    r_top.bold = True
    r_top.font.size = Pt(15)
    r_top.font.name = "Arial Black"
    r_top.font.color.rgb = RGBColor(0x1B, 0x5E, 0x20) # Deep Green
    
    r_sub = p_header.add_run("PENDIDIKAN AGAMA ISLAM DAN BUDI PEKERTI\n")
    r_sub.bold = True
    r_sub.font.size = Pt(11)
    r_sub.font.name = "Arial"
    r_sub.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32)
    
    r_badge = p_header.add_run(" ★ KELAS 3 ★ \n")
    r_badge.bold = True
    r_badge.font.size = Pt(10)
    r_badge.font.name = "Arial Black"
    r_badge.font.color.rgb = RGBColor(0xE9, 0x1E, 0x63) # Bright Pink
    
    r_materi = p_header.add_run("Materi: Kelahiran dan Masa Kanak-Kanak Nabi Muhammad saw.")
    r_materi.italic = True
    r_materi.bold = True
    r_materi.font.size = Pt(9.5)
    r_materi.font.name = "Arial"
    r_materi.font.color.rgb = RGBColor(0x00, 0x4D, 0x40)
    
    # Identity Box
    p_id = cell.add_paragraph()
    p_id.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_id.paragraph_format.space_before = Pt(4)
    p_id.paragraph_format.space_after = Pt(4)
    r_id = p_id.add_run("Nama : ...............................................   Kelas : .................   No. Absen : ..........")
    r_id.bold = True
    r_id.font.size = Pt(9.5)
    r_id.font.name = "Arial"
    r_id.font.color.rgb = RGBColor(0x37, 0x47, 0x4F)
    
    # Section A Header
    p_secA = cell.add_paragraph()
    p_secA.paragraph_format.space_before = Pt(3)
    p_secA.paragraph_format.space_after = Pt(4)
    r_secA_icon = p_secA.add_run(" 🅐 ")
    r_secA_icon.bold = True
    r_secA_icon.font.size = Pt(11)
    r_secA_icon.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32)
    
    r_secA_text = p_secA.add_run("Berilah tanda silang (X) pada huruf a, b, atau c di lembar jawaban yang paling benar!")
    r_secA_text.bold = True
    r_secA_text.font.size = Pt(9)
    r_secA_text.font.name = "Arial"
    r_secA_text.font.color.rgb = RGBColor(0xC2, 0x18, 0x5B)
    
    # 2-Column Table for Section A (PG 1-5 Left, PG 6-10 Right)
    table_pg = cell.add_table(rows=1, cols=2)
    table_pg.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_pg.autofit = False
    
    col_left = table_pg.cell(0, 0)
    col_right = table_pg.cell(0, 1)
    col_left.width = Inches(3.6)
    col_right.width = Inches(3.6)
    
    set_cell_margins(col_left, top=30, bottom=30, left=50, right=70)
    set_cell_margins(col_right, top=30, bottom=30, left=70, right=50)
    
    set_cell_borders(col_left, right={'val': 'dashed', 'sz': 8, 'color': '81C784'})
    set_cell_borders(col_right, left={'val': 'dashed', 'sz': 8, 'color': '81C784'})
    
    # Questions Left (1 - 5)
    q_left = [
        ("1. Nabi Muhammad saw. dilahirkan di kota suci ....", 
         [("a", "Madinah"), ("b", "Makkah"), ("c", "Thaif")]),
        ("2. Nabi Muhammad saw. lahir pada tahun Gajah, karena bertepatan peristiwa ....",
         [("a", "banyak gajah di kota Makkah"), ("b", "penyerangan Ka'bah oleh tentara bergajah"), ("c", "lomba menunggang gajah")]),
        ("3. Ayah Nabi Muhammad saw. bernama Abdullah. Beliau wafat ketika Nabi ....",
         [("a", "masih dalam kandungan ibunya"), ("b", "berusia 10 tahun"), ("c", "sudah dewasa")]),
        ("4. Ibu yang menyusui Nabi di desa Bani Sa'ad yang sejuk dan asri bernama ....",
         [("a", "Siti Khadijah"), ("b", "Halimah As-Sa'diyah"), ("c", "Fatimah Az-Zahra")]),
        ("5. Ibunda Nabi wafat di desa Abwa saat Nabi berusia 6 tahun, sehingga Nabi menjadi ....",
         [("a", "yatim"), ("b", "piatu"), ("c", "yatim piatu")])
    ]
    
    for i, (q_text, opts) in enumerate(q_left):
        p = col_left.add_paragraph() if i > 0 else col_left.paragraphs[0]
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(q_text)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.name = "Arial"
        r.font.color.rgb = RGBColor(0x21, 0x21, 0x21)
        
        for code, opt_text in opts:
            p_opt = col_left.add_paragraph()
            p_opt.paragraph_format.left_indent = Inches(0.12)
            p_opt.paragraph_format.space_before = Pt(0)
            p_opt.paragraph_format.space_after = Pt(0)
            r_opt = p_opt.add_run(f"{code}.  {opt_text}")
            r_opt.font.size = Pt(8.2)
            r_opt.font.name = "Arial"
            r_opt.font.color.rgb = RGBColor(0x42, 0x42, 0x42)
            
    # Questions Right (6 - 10)
    q_right = [
        ("6. Setelah ibu wafat, Nabi Muhammad saw. diasuh kakeknya yang bernama ....",
         [("a", "Abu Thalib"), ("b", "Abdul Muthalib"), ("c", "Abu Lahab")]),
        ("7. Ketika kakeknya wafat saat Nabi berumur 8 tahun, Nabi diasuh oleh pamannya ....",
         [("a", "Abu Jahal"), ("b", "Abu Thalib"), ("c", "Hamzah")]),
        ("8. Pada masa kanak-kanak, Nabi Muhammad saw. gemar membantu pamannya dengan ....",
         [("a", "menangkap ikan di laut"), ("b", "menggembala kambing"), ("c", "membuat pedang")]),
        ("9. Hikmah menggembala kambing sejak masa kanak-kanak adalah melatih sikap ....",
         [("a", "sombong dan manja"), ("b", "sabar, disiplin, dan mandiri"), ("c", "malas dan mengeluh")]),
        ("10. Sejak kecil Nabi Muhammad saw. tidak pernah berbohong, sehingga dijuluki ....",
         [("a", "Al-Amin (dapat dipercaya)"), ("b", "Al-Farabi"), ("c", "Al-Kindi")])
    ]
    
    for i, (q_text, opts) in enumerate(q_right):
        p = col_right.add_paragraph() if i > 0 else col_right.paragraphs[0]
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(q_text)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.name = "Arial"
        r.font.color.rgb = RGBColor(0x21, 0x21, 0x21)
        
        for code, opt_text in opts:
            p_opt = col_right.add_paragraph()
            p_opt.paragraph_format.left_indent = Inches(0.12)
            p_opt.paragraph_format.space_before = Pt(0)
            p_opt.paragraph_format.space_after = Pt(0)
            r_opt = p_opt.add_run(f"{code}.  {opt_text}")
            r_opt.font.size = Pt(8.2)
            r_opt.font.name = "Arial"
            r_opt.font.color.rgb = RGBColor(0x42, 0x42, 0x42)

    # Section B Header
    p_secB = cell.add_paragraph()
    p_secB.paragraph_format.space_before = Pt(5)
    p_secB.paragraph_format.space_after = Pt(3)
    r_secB_icon = p_secB.add_run(" 🅑 ")
    r_secB_icon.bold = True
    r_secB_icon.font.size = Pt(11)
    r_secB_icon.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32)
    
    r_secB_text = p_secB.add_run("Isilah titik-titik berikut dengan jawaban yang tepat dan benar!")
    r_secB_text.bold = True
    r_secB_text.font.size = Pt(9)
    r_secB_text.font.name = "Arial"
    r_secB_text.font.color.rgb = RGBColor(0xC2, 0x18, 0x5B)
    
    # Section B Questions (11 - 15)
    q_secB = [
        "11. Nabi Muhammad saw. lahir pada hari ........................... tanggal 12 Rabiul Awwal Tahun Gajah.",
        "12. Ibu kandung Nabi Muhammad saw. yang berakhlak mulia bernama ...................................",
        "13. Nama 'Muhammad' diberikan oleh kakeknya yaitu Abdul Muthalib, yang artinya orang yang ...........................",
        "14. Nabi Muhammad saw. diasuh oleh pamannya Abu Thalib mulai sejak berusia ........................... tahun.",
        "15. Keteladanan masa kanak-kanak Nabi Muhammad saw. yang dapat kita tiru di sekolah adalah ..........................."
    ]
    
    for q_text in q_secB:
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.left_indent = Inches(0.08)
        r = p.add_run(q_text)
        r.font.size = Pt(8.5)
        r.font.name = "Arial"
        r.font.color.rgb = RGBColor(0x21, 0x21, 0x21)
    
    # Footer Banner
    p_footer = cell.add_paragraph()
    p_footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_footer.paragraph_format.space_before = Pt(6)
    p_footer.paragraph_format.space_after = Pt(1)
    
    r_ft = p_footer.add_run("🌸 💖  Mari Meneladani Akhlak Mulia Nabi Muhammad saw. Sejak Masa Kanak-Kanak!  💖 🕋")
    r_ft.bold = True
    r_ft.font.size = Pt(9)
    r_ft.font.name = "Arial Black"
    r_ft.font.color.rgb = RGBColor(0x1B, 0x5E, 0x20)
    
    # PAGE 2: Kunci Jawaban & Rubrik Penilaian
    doc.add_page_break()
    
    p_kunci_head = doc.add_paragraph()
    p_kunci_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_kh = p_kunci_head.add_run("KUNCI JAWABAN & PEDOMAN PENSKORAN\nPENILAIAN HARIAN PAI KELAS 3 BAB 5")
    r_kh.bold = True
    r_kh.font.size = Pt(13)
    r_kh.font.name = "Arial"
    r_kh.font.color.rgb = RGBColor(0x1B, 0x5E, 0x20)
    
    # Kunci PG
    p_kpg = doc.add_paragraph()
    p_kpg.paragraph_format.space_before = Pt(8)
    r_kpg_t = p_kpg.add_run("A. Kunci Jawaban Pilihan Ganda (Skor per nomor = 1, Total = 10)")
    r_kpg_t.bold = True
    r_kpg_t.font.size = Pt(10)
    
    kunci_pg_items = [
        "1. b. Makkah (Kota kelahiran Nabi)",
        "2. b. penyerangan Ka'bah oleh tentara bergajah (Raja Abrahah)",
        "3. a. masih dalam kandungan ibunya (Ayahanda wafat saat Nabi dalam kandungan)",
        "4. b. Halimah As-Sa'diyah (Ibu asuh dari Bani Sa'ad)",
        "5. c. yatim piatu (Ibu wafat saat usia 6 tahun di Abwa)",
        "6. b. Abdul Muthalib (Kakek yang sangat menyayangi Nabi)",
        "7. b. Abu Thalib (Paman yang mengasuh Nabi sejak usia 8 tahun)",
        "8. b. menggembala kambing (Membantu paman mencari nafkah)",
        "9. b. sabar, disiplin, dan mandiri (Nilai karakter dari menggembala)",
        "10. a. Al-Amin (Artinya orang yang dapat dipercaya karena kejujurannya)"
    ]
    for k in kunci_pg_items:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.2)
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(k)
        r.font.size = Pt(9.5)
        
    # Kunci Isian
    p_kisian = doc.add_paragraph()
    p_kisian.paragraph_format.space_before = Pt(8)
    r_kisian_t = p_kisian.add_run("B. Kunci Jawaban Isian (Skor per nomor = 2, Total = 10)")
    r_kisian_t.bold = True
    r_kisian_t.font.size = Pt(10)
    
    kunci_isian_items = [
        "11. Senin (12 Rabiul Awwal Tahun Gajah / 571 M)",
        "12. Siti Aminah (Aminah binti Wahab)",
        "13. Terpuji (nama yang diharapkan selalu dipuji di bumi dan di langit)",
        "14. 8 (delapan) tahun setelah kakeknya wafat",
        "15. Jujur, amanah, mandiri, rajin, suka membantu, dan sabar (kebijakan guru)"
    ]
    for k in kunci_isian_items:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.2)
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(k)
        r.font.size = Pt(9.5)
        
    # Rubrik Penskoran
    p_rubrik = doc.add_paragraph()
    p_rubrik.paragraph_format.space_before = Pt(10)
    r_rb_t = p_rubrik.add_run("C. Rumus Perhitungan Nilai Akhir:")
    r_rb_t.bold = True
    r_rb_t.font.size = Pt(10)
    
    p_rumus = doc.add_paragraph()
    p_rumus.paragraph_format.left_indent = Inches(0.2)
    p_rumus.paragraph_format.space_before = Pt(3)
    p_rumus.paragraph_format.space_after = Pt(3)
    r_rumus = p_rumus.add_run("Nilai Akhir = ((Skor Pilihan Ganda + Skor Isian) / 20) x 100")
    r_rumus.bold = True
    r_rumus.font.size = Pt(10.5)
    r_rumus.font.color.rgb = RGBColor(0x00, 0x4D, 0x40)

    # Save
    out_path_1 = "Soal_Penilaian_Harian_Kelas3_Kelahiran_Nabi_Muhammad.docx"
    out_path_2 = os.path.join("public", "Soal_Penilaian_Harian_Kelas3_Kelahiran_Nabi_Muhammad.docx")
    doc.save(out_path_1)
    doc.save(out_path_2)
    print(f"Word doc created successfully at {out_path_1} and {out_path_2}")

if __name__ == "__main__":
    create_styled_document()
