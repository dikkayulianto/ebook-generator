import sys
import os
import re
from bs4 import BeautifulSoup
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

def convert_html_to_docx(html_path, docx_path):
    print(f"Reading HTML: {html_path}")
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove no-print top bars and scripts
    for el in soup.find_all(class_='no-print'):
        el.decompose()
    for el in soup.find_all('script'):
        el.decompose()
    for el in soup.find_all('style'):
        el.decompose()

    doc = docx.Document()

    # Standard A4 Margins
    for section in doc.sections:
        section.page_width = Inches(8.27)  # A4
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Detect document type
    is_sas = 'PENILAIAN SUMATIF AKHIR SEMESTER' in soup.get_text() or 'Naskah Soal SAS' in soup.get_text()
    is_modul = 'MODUL AJAR' in soup.get_text()

    pages = soup.find_all(class_='page')
    if not pages:
        pages = [soup.body or soup]

    for p_idx, page in enumerate(pages):
        if p_idx > 0:
            doc.add_page_break()

        process_container(doc, page)

    doc.save(docx_path)
    print(f"Successfully exported DOCX: {docx_path}")

def process_container(doc, container):
    # Iterate through child elements
    for child in container.children:
        if not hasattr(child, 'name') or not child.name:
            continue

        tag = child.name.lower()
        classes = child.get('class', [])
        if isinstance(classes, str):
            classes = classes.split()

        # Handle Kop Wrapper
        if 'kop-wrapper' in classes or tag == 'header':
            render_kop(doc, child)
            continue

        # Handle Identitas Table
        if tag == 'table':
            render_table(doc, child)
            continue

        # Handle Section Banner (e.g. A. PILIHAN GANDA)
        if 'section-banner' in classes or 'sec-banner' in classes:
            render_section_banner(doc, child)
            continue

        # Handle Petunjuk Box
        if 'petunjuk-box' in classes:
            render_callout_box(doc, child, fill_hex="F0FDF4", border_color="16A34A")
            continue

        # Handle Stimulus Box
        if 'stimulus-box' in classes:
            render_callout_box(doc, child, fill_hex="F8FAFC", border_color="059669")
            continue

        # Handle Question Item (PG)
        if 'question-item' in classes:
            render_question_item(doc, child)
            continue

        # Handle Uraian Item
        if 'uraian-item' in classes:
            render_uraian_item(doc, child)
            continue

        # Handle Headings
        if tag in ['h1', 'h2', 'h3', 'h4']:
            render_heading(doc, child, tag)
            continue

        # Handle Paragraphs
        if tag == 'p':
            render_paragraph(doc, child)
            continue

        # Handle Lists
        if tag in ['ul', 'ol']:
            render_list(doc, child, is_ordered=(tag == 'ol'))
            continue

        # Handle Generic Divs recursively
        if tag == 'div':
            process_container(doc, child)

def render_kop(doc, el):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15

    for child in el.children:
        text = child.get_text(strip=True) if hasattr(child, 'get_text') else str(child).strip()
        if not text:
            continue
        classes = child.get('class', []) if hasattr(child, 'get') else []
        if isinstance(classes, str):
            classes = [classes]

        run = p.add_run(text + "\n")
        run.font.name = "Arial"
        if 'kop-kementerian' in classes:
            run.bold = True
            run.font.size = Pt(11)
            run.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)
        elif 'kop-dinas' in classes:
            run.bold = True
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(0x04, 0x78, 0x57) # Emerald
        elif 'kop-title' in classes:
            run.bold = True
            run.font.size = Pt(13)
            run.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)
        elif 'kop-ta' in classes:
            run.bold = True
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
        else:
            run.bold = True
            run.font.size = Pt(11)

    # Double bottom border line
    divider = doc.add_paragraph()
    divider.alignment = WD_ALIGN_PARAGRAPH.CENTER
    divider.paragraph_format.space_before = Pt(0)
    divider.paragraph_format.space_after = Pt(6)
    r_line = divider.add_run("━" * 58)
    r_line.font.name = "Arial"
    r_line.font.size = Pt(10)
    r_line.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

def render_table(doc, table_el):
    rows = table_el.find_all('tr')
    if not rows:
        return

    # Determine num columns
    max_cols = 0
    for r in rows:
        cells = r.find_all(['td', 'th'])
        max_cols = max(max_cols, len(cells))

    if max_cols == 0:
        return

    doc_table = doc.add_table(rows=len(rows), cols=max_cols)
    doc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    doc_table.autofit = True

    is_identitas = 'identitas-grid' in (table_el.get('class') or [])

    for r_idx, r in enumerate(rows):
        cells = r.find_all(['td', 'th'])
        for c_idx, c in enumerate(cells):
            if c_idx >= max_cols:
                continue
            doc_cell = doc_table.cell(r_idx, c_idx)
            text = c.get_text(separator=' ', strip=True)
            doc_cell.text = text

            # Cell formatting
            p = doc_cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.1

            is_header = c.name == 'th' or r_idx == 0 and not is_identitas
            if is_header:
                set_cell_background(doc_cell, "E2E8F0")
                for run in p.runs:
                    run.bold = True
                    run.font.size = Pt(8.5)
                    run.font.name = "Arial"
            else:
                for run in p.runs:
                    run.font.size = Pt(8.5)
                    run.font.name = "Arial"

            set_cell_margins(doc_cell, top=60, bottom=60, left=80, right=80)

            if is_identitas:
                set_cell_borders(doc_cell, 
                                 top={'val': 'single', 'sz': 4, 'color': 'CBD5E1'},
                                 bottom={'val': 'single', 'sz': 4, 'color': 'CBD5E1'},
                                 left={'val': 'single', 'sz': 4, 'color': 'CBD5E1'},
                                 right={'val': 'single', 'sz': 4, 'color': 'CBD5E1'})
            else:
                set_cell_borders(doc_cell, 
                                 top={'val': 'single', 'sz': 4, 'color': 'CBD5E1'},
                                 bottom={'val': 'single', 'sz': 4, 'color': 'CBD5E1'},
                                 left={'val': 'single', 'sz': 4, 'color': 'CBD5E1'},
                                 right={'val': 'single', 'sz': 4, 'color': 'CBD5E1'})

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def render_section_banner(doc, el):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(4)
    
    # Outer box / colored highlight
    text = el.get_text(separator=' — ', strip=True)
    run = p.add_run(f"■ {text}")
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x04, 0x78, 0x57) # Green

def render_callout_box(doc, el, fill_hex="F8FAFC", border_color="059669"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    cell = table.cell(0, 0)
    cell.width = Inches(6.67)
    set_cell_background(cell, fill_hex)
    set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
    set_cell_borders(cell, left={'val': 'single', 'sz': 16, 'color': border_color})

    cell.text = el.get_text(separator=' ', strip=True)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    for run in p.runs:
        run.font.size = Pt(8.5)
        run.font.name = "Arial"
        run.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def render_question_item(doc, el):
    q_num = el.find(class_='question-num')
    q_num_text = q_num.get_text(strip=True) if q_num else ''

    stimulus = el.find(class_='stimulus-box')
    q_text = el.find(class_='question-text')
    choices = el.find_all(class_='choice-opt')

    # Main question paragraph
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.line_spacing = 1.15

    r_num = p.add_run(f"{q_num_text} ")
    r_num.bold = True
    r_num.font.name = "Arial"
    r_num.font.size = Pt(9)
    r_num.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)

    if stimulus:
        s_text = stimulus.get_text(strip=True)
        r_stim = p.add_run(f"[{s_text}] ")
        r_stim.italic = True
        r_stim.font.name = "Arial"
        r_stim.font.size = Pt(8.5)
        r_stim.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    if q_text:
        r_text = p.add_run(q_text.get_text(strip=True))
        r_text.font.name = "Arial"
        r_text.font.size = Pt(9)
        r_text.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)

    # Render Choices (2 options per row or indented)
    if choices:
        c_p = doc.add_paragraph()
        c_p.paragraph_format.left_indent = Inches(0.3)
        c_p.paragraph_format.space_before = Pt(1)
        c_p.paragraph_format.space_after = Pt(3)
        c_p.paragraph_format.line_spacing = 1.15

        for i, c in enumerate(choices):
            k = c.find(class_='choice-key')
            v = c.find(class_='choice-val')
            k_text = k.get_text(strip=True) if k else ''
            v_text = v.get_text(strip=True) if v else ''

            r_k = c_p.add_run(f"{k_text} ")
            r_k.bold = True
            r_k.font.name = "Arial"
            r_k.font.size = Pt(8.5)
            r_k.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

            r_v = c_p.add_run(f"{v_text}")
            r_v.font.name = "Arial"
            r_v.font.size = Pt(8.5)

            # Spacing between choices
            if (i + 1) % 2 == 0:
                c_p.add_run("\n")
            else:
                c_p.add_run("       ")

def render_uraian_item(doc, el):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.line_spacing = 1.15

    text = el.get_text(strip=True)
    # Extract question text before writing lines
    clean_text = re.sub(r'[\.\_]{5,}', '', text).strip()
    
    r = p.add_run(clean_text)
    r.font.name = "Arial"
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)

    # Add 3 dashed answering lines
    for _ in range(3):
        lp = doc.add_paragraph()
        lp.paragraph_format.left_indent = Inches(0.3)
        lp.paragraph_format.space_before = Pt(0)
        lp.paragraph_format.space_after = Pt(2)
        lr = lp.add_run("." * 80)
        lr.font.color.rgb = RGBColor(0x94, 0xa3, 0xb8)
        lr.font.size = Pt(8)

def render_heading(doc, el, tag):
    p = doc.add_paragraph()
    level = int(tag[1]) if tag[1].isdigit() else 2
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run(el.get_text(strip=True))
    run.bold = True
    run.font.name = "Arial"
    if level == 1:
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)
    elif level == 2:
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(0x04, 0x78, 0x57)
    else:
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)

def render_paragraph(doc, el):
    text = el.get_text(strip=True)
    if not text:
        return
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.2
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)

def render_list(doc, el, is_ordered=False):
    items = el.find_all('li')
    for idx, li in enumerate(items):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.3)
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.line_spacing = 1.15
        bullet = f"{idx+1}. " if is_ordered else "• "
        r_b = p.add_run(bullet)
        r_b.bold = True
        r_b.font.name = "Arial"
        r_b.font.size = Pt(9)
        r_b.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

        r_text = p.add_run(li.get_text(strip=True))
        r_text.font.name = "Arial"
        r_text.font.size = Pt(9)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python html_to_docx.py <input_html> <output_docx>")
        sys.exit(1)
    convert_html_to_docx(sys.argv[1], sys.argv[2])
