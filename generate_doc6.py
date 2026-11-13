import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

folder_ai = r'c:\Users\DESKTOP\Documents\Antigravity\AI-autoDoc\Bukti_Fisik_Jabar_Beraksi'
folder_lynk = r'c:\Users\DESKTOP\Documents\Antigravity\LYNK.ID\Bukti_Fisik_Jabar_Beraksi'
os.makedirs(folder_ai, exist_ok=True)
os.makedirs(folder_lynk, exist_ok=True)

def create_doc_6():
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color='B0BEC5', sz='4', val='single'):
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

    # ==================== KOP SURAT ====================
    p_kop = doc.add_paragraph()
    p_kop.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kop.paragraph_format.space_after = Pt(2)
    r = p_kop.add_run('PEMERINTAH KOTA CIREBON\nDINAS PENDIDIKAN\nSD NEGERI 1 KESAMBI')
    r.bold = True
    r.font.size = Pt(12)
    r.font.name = 'Arial'

    p_kop2 = doc.add_paragraph()
    p_kop2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kop2.paragraph_format.space_after = Pt(8)
    r2 = p_kop2.add_run('Alamat: Jalan Kesambi Nomor 24, Kecamatan Kesambi, Kota Cirebon 45132\nPosel: sdn1kesambi@cirebonkota.go.id | Laman: disdik.cirebonkota.go.id')
    r2.font.size = Pt(8.5)
    r2.italic = True
    r2.font.name = 'Arial'
    r2.font.color.rgb = RGBColor(100, 100, 100)

    # Double divider
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_after = Pt(12)
    p_div_border = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="double" w:sz="14" w:space="1" w:color="000000"/></w:pBdr>')
    p_div._p.get_or_add_pPr().append(p_div_border)

    # JUDUL DOKUMEN
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(2)
    r_t = p_title.add_run('BUKTI FISIK INSTRUMEN JABAR BERAKSI (POIN 6)')
    r_t.bold = True
    r_t.font.size = Pt(12)
    r_t.font.name = 'Arial'

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_s = p_sub.add_run('INDIKATOR: PEMBIASAAN BERMASYARAKAT\n(Berkas Bukti Fisik: Surat Tugas, Laporan Kegiatan Sosial, Jurnal Pembiasaan, & Dokumentasi)')
    r_s.font.size = Pt(9.5)
    r_s.bold = True
    r_s.font.name = 'Arial'
    r_s.font.color.rgb = RGBColor(13, 71, 161)

    # ==================== BAGIAN 1: SURAT TUGAS RESMI ====================
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(8)
    h1.paragraph_format.space_after = Pt(4)
    r_h1 = h1.add_run('A. SURAT TUGAS PELAKSANAAN KEGIATAN SOSIAL KEMASYARAKATAN')
    r_h1.bold = True
    r_h1.font.size = Pt(10.5)
    r_h1.font.color.rgb = RGBColor(13, 71, 161)

    st_table = doc.add_table(rows=6, cols=2)
    st_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(st_table)

    st_items = [
        ('1. Nomor Surat Tugas', 'Nomor: 421.2 / 084 / SD-KS / X / 2026'),
        ('2. Dasar Penugasan', 'a. Program Penguatan Pendidikan Karakter (PPK) Jabar Beraksi Tahun 2026.\nb. Rencana Kerja Tahunan (RKT) SD Negeri 1 Kesambi Bidang Kesiswaan & Hubungan Masyarakat Tahun Ajaran 2026/2027.'),
        ('3. Pejabat Pemberi Tugas', 'Nama : Dra. Hj. Siti Maryam, M.Pd\nJabatan : Kepala SD Negeri 1 Kesambi\nNIP : 197505121998032004'),
        ('4. Personel yang Ditugaskan', '1. Pembina Kesiswaan & Koordinator Program Pembiasaan\n2. Seluruh Guru Kelas (Kelas I s.d. VI) dan Guru Pendamping\n3. Pengurus Paguyuban Orang Tua Murid / Komite Sekolah\n4. Seluruh Peserta Didik SD Negeri 1 Kesambi'),
        ('5. Uraian Tugas & Tanggung Jawab', '1. Merencanakan, mengorganisasikan, dan mendampingi siswa dalam pelaksanaan Program Pembiasaan Bermasyarakat.\n2. Mengkoordinasikan Aksi Peduli Sesama (Infaq Jumat Berkah), Bakti Kebersihan Lingkungan Sekitar Sekolah (GPS), dan Kunjungan Sosial.\n3. Memastikan ketertiban, keselamatan, dan sopan santun peserta didik selama berinteraksi dengan warga masyarakat.\n4. Menyusun laporan keterlaksanaan program dan dokumentasi kegiatan secara berkala.'),
        ('6. Waktu & Lokasi Penugasan', 'Waktu : Semester Ganjil Tahun Ajaran 2026/2027 (Terjadwal Setiap Pekan ke-2 dan ke-4)\nLokasi : Lingkungan Sekitar SD Negeri 1 Kesambi (RT 01 - RT 04 / RW 03 Kelurahan Kesambi)')
    ]

    col_widths = [Inches(2.0), Inches(4.8)]
    for row_idx, (col0, col1) in enumerate(st_items):
        row = st_table.rows[row_idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = col_widths[0], col_widths[1]
        set_cell_background(c0, 'F5F7FA')
        set_cell_margins(c0, 90, 90, 110, 110)
        set_cell_margins(c1, 90, 90, 110, 110)

        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(col0)
        r0.bold = True
        r0.font.size = Pt(8.5)

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(col1)
        r1.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ==================== BAGIAN 2: LAPORAN KEGIATAN SOSIAL ====================
    h2 = doc.add_paragraph()
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(4)
    r_h2 = h2.add_run('B. LAPORAN PELAKSANAAN KEGIATAN SOSIAL & BERMASYARAKAT')
    r_h2.bold = True
    r_h2.font.size = Pt(10.5)
    r_h2.font.color.rgb = RGBColor(13, 71, 161)

    rep_table = doc.add_table(rows=7, cols=2)
    rep_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(rep_table)

    rep_items = [
        ('1. Nama Program', 'Program Pembiasaan "Siswa Beraksi Nyata: Peduli Lingkungan & Berbagi Kasih Warga"'),
        ('2. Latar Belakang & Tujuan', 'Menumbuhkan kecerdasan sosial, empati kemanusiaan, rasa tanggung jawab warga negara, dan pembiasaan budaya gotong royong sejak dini, agar peserta didik tidak hanya cakap di dalam kelas, namun juga memiliki kepedulian nyata terhadap lingkungan sosial sekitar.'),
        ('3. Ruang Lingkup Aktivitas', 'a. Gerakan Jumat Peduli & Berbagi: Pengumpulan infaq sukarela dan penyaluran paket bekal sehat kepada warga lansia/kurang mampu di sekitar sekolah.\nb. Aksi Bersih Lingkungan Bersama Warga: Kerja bakti pungut sampah terpilah dan pembersihan saluran air jalan pemukiman sekitar sekolah.\nc. Sapa Santun Warga: Pembiasaan tegur sapa, senyum, dan etika santun saat berpapasan dengan warga sekitar.'),
        ('4. Peserta & Keterlibatan', 'Diikuti oleh 284 peserta didik kelas 1 sampai 6, 14 dewan guru, 4 tenaga kependidikan, serta perwakilan paguyuban orang tua murid dan pengurus RW 03 Kesambi.'),
        ('5. Capaian & Dampak Positif', '1. Tingkat partisipasi peserta didik mencapai 96% dalam setiap agenda bakti sosial.\n2. Meningkatnya keakraban, hubungan kekeluargaan, dan rasa saling memiliki antara pihak sekolah dan warga masyarakat sekitar.\n3. Terbentuknya karakter dermawan, rendah hati, dan rasa kepedulian lingkungan pada diri siswa.'),
        ('6. Kendala yang Dihadapi', 'Perbedaan jadwal luang warga sekitar dan faktor cuaca saat musim penghujan sehingga beberapa kegiatan outdoor harus disesuaikan waktunya.'),
        ('7. Evaluasi & Rencana Tindak Lanjut', 'Kegiatan pembiasaan bermasyarakat ditingkatkan menjadi program terintegrasi dengan Projek Penguatan Profil Pelajar Pancasila (P5) tema Rekayasa dan Kearifan Lokal.')
    ]

    for row_idx, (col0, col1) in enumerate(rep_items):
        row = rep_table.rows[row_idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = col_widths[0], col_widths[1]
        set_cell_background(c0, 'F5F7FA')
        set_cell_margins(c0, 90, 90, 110, 110)
        set_cell_margins(c1, 90, 90, 110, 110)

        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(col0)
        r0.bold = True
        r0.font.size = Pt(8.5)

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(col1)
        r1.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ==================== BAGIAN 3: JURNAL LOG PEMBIASAAN SOSIAL ====================
    h3 = doc.add_paragraph()
    h3.paragraph_format.space_before = Pt(8)
    h3.paragraph_format.space_after = Pt(4)
    r_h3 = h3.add_run('C. JURNAL LOG HARIAN & BUKU CATATAN AKTIVITAS SOSIAL PESERTA DIDIK')
    r_h3.bold = True
    r_h3.font.size = Pt(10.5)
    r_h3.font.color.rgb = RGBColor(13, 71, 161)

    log_table = doc.add_table(rows=4, cols=7)
    log_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(log_table)

    headers = ['No', 'Hari/Tanggal', 'Bentuk Kegiatan Sosial', 'Sasaran / Lokasi', 'Peserta / Kls', 'Hasil Pengamatan Karakter', 'Status']
    header_row = log_table.rows[0]
    for idx, text in enumerate(headers):
        cell = header_row.cells[idx]
        set_cell_background(cell, '1565C0')
        set_cell_margins(cell, 90, 90, 70, 70)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(8)
        r.font.color.rgb = RGBColor(255, 255, 255)

    sample_logs = [
        ('1', 'Jumat, 11/09/2026', 'Gerakan Jumat Berkah & Penyaluran Paket Sembako Dhuafa', 'Warga Lansia Sekitar RT 02 RW 03 Kesambi', 'Siswa Kls V & VI, Guru Pendamping', 'Siswa menunjukkan sikap santun, empati tinggi, dan takzim kepada orang tua.', 'Terlaksana\n(100%)'),
        ('2', 'Sabtu, 26/09/2026', 'Aksi Bersih Lingkungan & Gerakan Pungut Sampah (GPS)', 'Jalan Protokol & Taman Depan Sekolah', 'Seluruh Siswa Kls I-VI, Komite', 'Kerja sama tim sangat kompak, antusiasme membersihkan fasilitas umum tinggi.', 'Terlaksana\n(98%)'),
        ('3', 'Jumat, 16/10/2026', 'Kunjungan Silaturahmi & Santunan Anak Yatim Warga Sekitar', 'Aula Kelurahan Kesambi', 'Perwakilan Siswa & Pembina', 'Terbangun ikatan sosial yang hangat dan ketulusan berbagi kebahagiaan.', 'Terlaksana\n(100%)')
    ]

    col_w = [Inches(0.4), Inches(1.0), Inches(1.7), Inches(1.3), Inches(0.9), Inches(1.3), Inches(0.6)]
    for r_idx, data_row in enumerate(sample_logs):
        row = log_table.rows[r_idx + 1]
        bg_col = 'FFFFFF' if r_idx % 2 == 0 else 'F8FAFC'
        for c_idx, val in enumerate(data_row):
            cell = row.cells[c_idx]
            cell.width = col_w[c_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 80, 80, 70, 70)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            if c_idx in [0, 1, 6]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(8)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ==================== BAGIAN 4: DOKUMENTASI FOTO ====================
    h4 = doc.add_paragraph()
    h4.paragraph_format.space_before = Pt(8)
    h4.paragraph_format.space_after = Pt(4)
    r_h4 = h4.add_run('D. LEMBAR DOKUMENTASI FOTO KEGIATAN BERMASYARAKAT')
    r_h4.bold = True
    r_h4.font.size = Pt(10.5)
    r_h4.font.color.rgb = RGBColor(13, 71, 161)

    photo_table = doc.add_table(rows=1, cols=2)
    photo_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(photo_table)

    c0, c1 = photo_table.rows[0].cells[0], photo_table.rows[0].cells[1]
    c0.width, c1.width = Inches(3.4), Inches(3.4)
    set_cell_background(c0, 'FAFAFA')
    set_cell_background(c1, 'FAFAFA')
    set_cell_margins(c0, 120, 120, 120, 120)
    set_cell_margins(c1, 120, 120, 120, 120)

    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.add_run('[ TEMPELKAN FOTO KEGIATAN 1 DI SINI ]\n\nDokumentasi Aksi Jumat Berkah & Penyaluran Paket Bantuan kepada Warga Kurang Mampu Sekitar Sekolah.').font.size = Pt(8)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.add_run('[ TEMPELKAN FOTO KEGIATAN 2 DI SINI ]\n\nDokumentasi Kerja Bakti Bersih Lingkungan dan Saluran Air Bersama Warga RT 02 RW 03 Kesambi.').font.size = Pt(8)

    # ==================== LEMBAR PENGESAHAN ====================
    doc.add_paragraph().paragraph_format.space_after = Pt(14)
    p_ttd_date = doc.add_paragraph()
    p_ttd_date.paragraph_format.space_after = Pt(6)
    p_ttd_date.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_dt = p_ttd_date.add_run('Cirebon, 13 November 2026')
    r_dt.font.size = Pt(9.5)

    sig_table = doc.add_table(rows=1, cols=3)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r in sig_table.rows:
        for c in r.cells:
            tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="0"/><w:bottom w:w="0"/><w:left w:w="0"/><w:right w:w="0"/></w:tcMar>')
            c._tc.get_or_add_tcPr().append(tcMar)

    c0, c1, c2 = sig_table.rows[0].cells[0], sig_table.rows[0].cells[1], sig_table.rows[0].cells[2]
    c0.width, c1.width, c2.width = Inches(2.2), Inches(2.2), Inches(2.4)

    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.add_run('Pembina Kesiswaan,\n\n\n\n\n( ......................................... )\nNIP. .....................................').font.size = Pt(8.5)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.add_run('Ketua Komite Sekolah,\n\n\n\n\n( ......................................... )\n').font.size = Pt(8.5)

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.add_run('Mengetahui,\nKepala SD Negeri 1 Kesambi,\n\n\n\n\nDra. Hj. Siti Maryam, M.Pd\nNIP. 197505121998032004').font.size = Pt(8.5)

    # Save to both folders
    file_name = 'Bukti_Fisik_Poin_6_Pembiasaan_Bermasyarakat.docx'
    out_ai = os.path.join(folder_ai, file_name)
    out_lynk = os.path.join(folder_lynk, file_name)

    doc.save(out_ai)
    doc.save(out_lynk)
    print("SUCCESS_FILE_6_AI:", os.path.abspath(out_ai))
    print("SUCCESS_FILE_6_LYNK:", os.path.abspath(out_lynk))

if __name__ == '__main__':
    create_doc_6()
