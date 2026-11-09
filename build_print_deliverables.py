#!/usr/bin/env python3
"""Deterministic Letter flyer: vector type, native full-color assets, 9 pt bleed."""
from pathlib import Path
import json, re, shutil, zipfile, xml.etree.ElementTree as ET
import fitz
from PIL import Image
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'exports'; OUT.mkdir(exist_ok=True)
TMP=ROOT/'tmp/pdfs'; TMP.mkdir(parents=True,exist_ok=True)
W,H=630,810
BLACK='#111111'; PURPLE='#6B3FA0'; LAV='#DFC5EE'; PALE='#F3EAF9'; WHITE='#FFFFFF'
FONTS={k:fitz.Font(fontfile=f'/System/Library/Fonts/Supplemental/Arial{s}.ttf') for k,s in [('regular',''),('bold',' Bold')]}
D=fitz.open(); COPY=[]; IMAGES=[]
def rgb(h):return tuple(int(h[i:i+2],16)/255 for i in (1,3,5))
def rect(x,y,w,h,c):p.draw_rect(fitz.Rect(x,y,x+w,y+h),color=None,fill=rgb(c),overlay=True)
def text(t,x,y,w,size=10,font='regular',color=BLACK,leading=None):
    COPY.append((len(D)-1,t)); leading=leading or size*1.28
    words=t.split(' '); lines=[]; line=''
    for word in words:
        trial=(line+' '+word) if line else word
        if FONTS[font].text_length(trial,fontsize=size)>w and line:lines.append(line);line=word
        else:line=trial
    if line:lines.append(line)
    for i,line in enumerate(lines):
        assert FONTS[font].text_length(line,fontsize=size)<=w+.1,(line,w)
        baseline=y+size+i*leading
        assert x>=24 and x+w<=606 and baseline<790,(t,baseline)
        p.insert_text((x,baseline),line,fontname=font,fontsize=size,color=rgb(color))
    return y+len(lines)*leading

def img(path,x,y,w,h):
    src=ROOT/path; im=Image.open(src); iw,ih=im.size
    scale=min(w/iw,h/ih);dw,dh=iw*scale,ih*scale
    xx=x+(w-dw)/2;yy=y+(h-dh)/2
    p.insert_image(fitz.Rect(xx,yy,xx+dw,yy+dh),filename=str(src))
    dpi=72/scale
    assert dpi>=299.9,(path,dpi)
    IMAGES.append({'page':len(D),'asset':path,'effective_ppi':round(dpi,1)})

def qr(x,y,s,color=BLACK):
    # Preserve QR geometry as vector rectangles, including its source quiet zone.
    root=ET.parse(ROOT/'assets/processed/qr_hopemark.svg').getroot()
    scale=s/37
    rect(x,y,s,s,WHITE)
    for el in root.iter():
        if el.tag.endswith('rect') and el.get('width')=='1':
            rect(x+(float(el.get('x','0'))+4)*scale,y+(float(el.get('y','0'))+4)*scale,scale,scale,BLACK)
    text('HopeMark.com',x,y+s+4,s,6 if s<50 else 7,'bold',color)

def page():
    global p
    p=D.new_page(width=W,height=H)
    for name,f in FONTS.items():p.insert_font(fontname=name,fontbuffer=f.buffer)
    rect(0,0,W,H,WHITE)
    p.set_trimbox(fitz.Rect(9,9,621,801));p.set_bleedbox(fitz.Rect(0,0,W,H))

def bullets(items,x,y,w,size=10):
    for item in items:
        rect(x,y+5,3,3,PURPLE)
        y=text(item,x+11,y,w-11,size)+5
    return y

page()
rect(0,0,W,139,LAV)
img('assets/processed/logo_horizontal_dark_h.png',33,26,125,33)
text('Comprehensive Psychiatric Care',33,69,564,28,'bold',BLACK)
text('Your Trusted Referral Partner',33,108,564,14,'bold',PURPLE)
intro='Hopemark Health provides evidence-based psychiatric care for children, adolescents, and adults. Our multidisciplinary team supports accurate diagnosis, individualized treatment, and coordination with referring providers.'
text(intro,33,158,295,11,leading=15)
img('assets/processed/consultation_color.jpg',346,154,251,141)
rect(33,267,235,24,BLACK)
text('In-person or telehealth visits available.',43,273,218,9.5,'bold',WHITE)
text('Clinical Services',33,312,270,17,'bold',PURPLE)
bullets(['Psychiatric evaluations and medication management','Psychotherapy','Neuropsychological testing','Child and adolescent psychiatry','Sleep medicine','Genetic testing – pharmacogenomics','Substance use treatment and medically assisted recovery'],33,342,270,10.5)
text('Conditions We Treat',330,312,267,17,'bold',PURPLE)
y=bullets(['Major depressive disorder','Anxiety and panic disorders','Post-traumatic stress disorder (PTSD)','Bipolar disorder','Obsessive-compulsive disorder (OCD)','Substance use disorders'],330,342,267,10)
text('Our Clinical Team',330,462,267,15,'bold',PURPLE)
bullets(['Psychiatrists','Psychiatric mental health nurse practitioners','Psychologists','Physician assistants','Licensed counselors and therapists'],330,487,267,9.5)
rect(33,576,564,1,LAV)
text('Hopemark Clinic Locations',33,586,564,16,'bold',PURPLE)
clinics=[('Chicago – Millennium Park','8 S. Michigan Avenue, Suite 1505, Chicago, IL 60603'),('Chicago – West Loop','566 W. Lake Street, Suite 200, Chicago, IL 60661'),('Hoffman Estates','1721 Moon Lake Boulevard, Suite 201, Hoffman Estates, IL 60169'),('Naperville','1284 Rickert Drive, Suite 200, Naperville, IL 60540'),('Oak Brook','1200 Harger Road, Suite 200, Oak Brook, IL 60523'),('Orland Park','14489 John Humphrey Drive, Suite 202, Orland Park, IL 60462')]
for i,(name,address) in enumerate(clinics):
    x=33+(i%3)*191;y=614+(i//3)*48
    rect(x,y-4,182,42,PALE)
    text(name,x+6,y,170,8.8,'bold');text(address,x+6,y+14,170,8.2,leading=10)
rect(0,721,W,89,BLACK)
text('Referrals and appointments',33,736,440,14,'bold',WHITE)
text('PHONE  630-656-9393',33,761,210,10,'bold',WHITE)
text('FAX  630-385-0290',270,761,220,10,'regular',WHITE)
text('WEBSITE  HopeMark.com',33,779,440,9,'regular',WHITE)
qr(528,725,52,WHITE)

page()
rect(0,0,217,H,BLACK)
img('assets/processed/logo_horizontal_white.png',33,31,122,32)
text('Treatment-Resistant Depression',33,84,163,16,'bold',WHITE,leading=21)
text('More options. Renewed hope.',33,134,163,11,'bold',LAV)
rect(33,162,160,0.8,LAV)
text('What Is Treatment-Resistant Depression?',33,178,163,12.5,'bold',WHITE,leading=16)
y=text('When depression has not improved enough after at least two antidepressants taken at an adequate dose for an adequate length of time, it may be treatment-resistant depression (TRD).',33,234,160,9.8, color=WHITE,leading=13.8)
text('Symptoms such as persistent sadness, low energy, and loss of interest can continue to affect everyday life.',33,y+10,160,9.8,color=WHITE,leading=13.8)
rect(33,408,160,0.8,LAV)
text('How Common Is It?',33,424,163,12.5,'bold',WHITE)
text('About',33,450,163,10,color=WHITE)
text('1 in 3*',33,465,163,38,'bold',LAV)
text('A U.S. study estimated that approximately one-third of adults receiving medication for major depression had treatment-resistant depression.',33,516,163,9.5,color=WHITE,leading=13)
rect(33,604,160,0.8,LAV)
text('Discuss treatment options with our team.',33,618,163,10.5,'bold',WHITE,leading=14)
text('PHONE  630-656-9393',33,658,165,9.5,'bold',WHITE)
text('FAX  630-385-0290',33,676,165,9.5,color=WHITE)
text('WEBSITE  HopeMark.com',33,694,165,9.5,color=WHITE)
qr(33,718,54,WHITE)
rect(237,31,360,94,PALE)
text('How Hopemark Health Can Help',250,43,334,15.5,'bold',PURPLE)
text("Our team reviews each patient's symptoms and treatment history to build a personalized plan that may include novel therapies, medication management, and psychotherapy.",250,69,334,9.8,leading=13.5)
text('Deep TMS',237,140,360,20,'bold',PURPLE)
text('Deep Transcranial Magnetic Stimulation',237,165,360,10,'bold')
y=text('What it is and how it works: A noninvasive treatment that uses magnetic pulses to stimulate brain networks involved in mood and OCD. FDA-cleared for depression and as an additional treatment for OCD.',237,184,360,9.4,leading=12.2)
y=text('Potential benefits: May reduce persistent depression symptoms. An OCD-specific treatment protocol may reduce obsessive thoughts and compulsive behaviors.',237,y+6,360,9.4,leading=12.2)
rect(237,278,360,96,PALE)
img('assets/processed/brainsway_tms_hd.png',252,283,84,86)
img('assets/processed/brains_pair_hd.png',362,286,188,60)
text('Before TMS',382,349,70,7.5,'bold')
text('Potential response after TMS',466,349,118,7.5,'bold')
text('Educational visualization. Results vary.',382,362,195,7,color=PURPLE)
rect(237,386,360,.8,LAV)
text('Spravato®',237,398,360,20,'bold',PURPLE)
text('Esketamine Nasal Spray',237,423,360,10,'bold')
y=text("What it is and how it works: An FDA-approved prescription nasal spray for adults with treatment-resistant depression. It acts on NMDA receptors in the brain's glutamate system.",237,443,212,9.4,leading=12.2)
y=text('Potential benefits: May reduce depression symptoms, with improvement observed as early as approximately 24 hours in clinical trials. It can be used with or without an oral antidepressant for TRD.',237,y+6,212,9.4,leading=12.2)
assert y<596,y
img('assets/processed/spravato_hd.png',458,430,138,115)
rect(237,594,360,.8,LAV)
text('IV Ketamine',237,606,360,20,'bold',PURPLE)
y=text("What it is and how it works: Low-dose ketamine delivered through an IV. It acts on NMDA receptors in the brain's glutamate system and is used off-label for depression.",237,633,212,9.4,leading=12.2)
y=text('Potential benefits: May relieve depression symptoms within hours for some patients when standard treatments have not provided enough relief. Additional treatments may be needed to maintain benefits.',237,y+6,212,9.4,leading=12.2)
assert y<757,y
img('assets/processed/ketamine_official_hd.png',458,630,138,78)
text('*In a 2021 U.S. study, an estimated 30.9% of adults with medication-treated major depression had treatment-resistant depression. Source: Zhdanava et al., Journal of Clinical Psychiatry. 2021;82(2):20m13699.',237,760,360,6.8,leading=8.5)
D.set_metadata({'title':'Hopemark Health | Two-Sided Flyer','author':'','subject':'US Letter with 0.125 inch bleed','creator':'Parametric print production','producer':'Vector PDF'})
D.subset_fonts()
pdf=OUT/'Hopemark_Health_Two_Sided_Flyer_Print_Ready.pdf'
D.save(pdf,garbage=4,deflate=True)
# Outline glyphs for self-contained, editable vector geometry; retain raster originals.
for i,side in enumerate(['Front','Back']):
    svg=D[i].get_svg_image(text_as_path=True)
    svg=re.sub(r'<svg ', '<svg ',svg,count=1)
    svg=re.sub(r'width="630" height="810"', 'width="8.75in" height="11.25in"',svg,count=1)
    (OUT/f'Hopemark_{side}_8.5x11_Bleed.svg').write_text(svg)
    D[i].get_pixmap(dpi=300).save(TMP/f'{side}_300dpi.png')
# Check all required copy survives embedding and extraction (whitespace only normalized).
normalize=lambda s:' '.join(s.replace('\u00ad','-').replace('\u037e',';').split())
for i,t in COPY:
    assert normalize(t) in normalize(D[i].get_text()),f'Missing text: {t}'
for pg in D:
    assert tuple(pg.trimbox)==(9,9,621,801)
    assert tuple(pg.bleedbox)==(0,0,630,810)
readme='''HOPemark Health — Print specification

Files: two-page vector PDF (front, back), two outlined SVG masters, QR SVG/PNG.
Trim: 8.5 × 11 inches (612 × 792 pt).
Media/Bleed: 8.75 × 11.25 inches (630 × 810 pt).
Bleed: 0.125 inch / 9 pt on each edge. PDF TrimBox: [9, 9, 621, 801].
Print at 100% scale; duplex long-edge binding. Crop to TrimBox; do not fit to page.
No printer marks are placed inside the bleed. Printer may add marks externally.
Typography and geometric elements are vector; PDF fonts are embedded/subset.
SVG type is outlined to avoid font substitution. Photographs and official logos
remain embedded full-color raster assets; every placement is at least 300 PPI.
A PDF has no single DPI: all raster placements meet 300 PPI; proofs render at 300 DPI.
RGB brand palette and supplied full-color imagery are preserved. This is not a
certified PDF/X file. The print provider should apply its own ICC conversion for
its paper/press; no unapproved generic CMYK profile has been imposed.
Required source citation is retained verbatim. No production staff names included.
QR destination: https://hopemark.com/.
Both 300 DPI flyer proofs and standalone QR were decoded successfully.
HTTP verification: destination redirects to https://hopemarkhealth.com/;
the destination returned HTTP 403 to the automated request. Live page content
was not verified.
Rebuild using build_print_deliverables.py with PyMuPDF and Pillow available.
'''
(OUT/'PRINT_SPECIFICATIONS_README.txt').write_text(readme)
# Export QR with the same four-module quiet zone used on both flyer sides.
qrroot=ET.parse(ROOT/'assets/processed/qr_hopemark.svg').getroot()
qrparts=['<svg xmlns="http://www.w3.org/2000/svg" width="370" height="370" viewBox="0 0 37 37"><rect width="37" height="37" fill="white"/>']
for el in qrroot.iter():
    if el.tag.endswith('rect') and el.get('width')=='1':
        qrparts.append(f'<rect x="{int(el.get("x"))+4}" y="{int(el.get("y"))+4}" width="1" height="1" fill="#111111"/>')
qrparts.append('</svg>')
(OUT/'qr_hopemark.svg').write_text(''.join(qrparts))
qdoc=fitz.open(stream=''.join(qrparts).encode(),filetype='svg')
qp=fitz.open('pdf',qdoc.convert_to_pdf())
qp[0].get_pixmap().save(OUT/'qr_hopemark.png')
report={'pages':2,'trim_inches':[8.5,11],'bleed_inches':.125,'proof_pixels':[2625,3375],'copy_blocks_checked':len(COPY),'images':IMAGES,'minimum_image_ppi':min(i['effective_ppi'] for i in IMAGES)}
(TMP/'preflight.json').write_text(json.dumps(report,indent=2))
with zipfile.ZipFile(OUT/'Hopemark_Health_Flyer_Master_Pack.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in [pdf,OUT/'Hopemark_Front_8.5x11_Bleed.svg',OUT/'Hopemark_Back_8.5x11_Bleed.svg',OUT/'qr_hopemark.svg',OUT/'qr_hopemark.png',OUT/'PRINT_SPECIFICATIONS_README.txt']:z.write(f,f.name)
print(json.dumps(report,indent=2))
