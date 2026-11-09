#!/usr/bin/env python3
"""Build all Hopemark deliverable HTML files. Run: python3 build.py"""
import pathlib
from build_lib import *

ROOT = pathlib.Path(__file__).parent
HEAD = ('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>{title}</title><style>{css}</style></head>')

BOARD_CSS = r"""
html,body{margin:0;padding:0;width:1600px;height:1200px;overflow:hidden;background:#EFEAF6}
body{position:relative;font-family:Inter,'Helvetica Neue',Arial,sans-serif;color:#111;
 background:radial-gradient(1200px 800px at 50% 0%,#F6F2FB 0%,#EFEAF6 60%,#E8E1F1 100%)}
.pgw{position:absolute;box-shadow:0 2px 5px rgba(40,20,60,.12),0 22px 50px rgba(60,30,90,.20)}
.cap{position:absolute;left:30px;right:30px;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;
 border-top:1px solid rgba(17,17,17,.2);padding-top:13px}
.cap span{font-size:11px;letter-spacing:.14em;font-weight:600;color:#111}
.cap .c1{text-align:left}.cap .c2{text-align:center;color:#4B4753}.cap .c3{text-align:right}
"""


def write(name, title, css, body):
    (ROOT / name).write_text(HEAD.format(title=title, css=css) + "<body" + body + "</body></html>", encoding="utf-8")
    print("wrote", name)


def two_page_board(name, title, left, right, c1, c2, c3):
    body = (f'>'
            f'<div class="pgw" style="left:30px;top:60px">{left}</div>'
            f'<div class="pgw" style="left:810px;top:60px">{right}</div>'
            f'<div class="cap" style="top:1074px"><span class="c1">{c1}</span><span class="c2">{c2}</span>'
            f'<span class="c3">{c3}</span></div>')
    write(name, title, PAGE_CSS + BOARD_CSS, body)


two_page_board("board1.html", "Hopemark Health – Two-Sided Flyer – Edition A",
               front_a(), back_a("1"),
               "FRONT — US LETTER 8.5&quot; × 11&quot;",
               "HOPEMARK HEALTH · FULL-COLOR CLINICAL EDITION · ZERO ICONS",
               "BACK — BLACK SPINE + WHITE LOGO")
two_page_board("board2.html", "Hopemark Health – Two-Sided Flyer – Edition B",
               front_b(), back_b("2"),
               "EDITION B — FRONT · LAVENDER SPINE",
               "ARCHITECTURAL LAVENDER SPINE · FULL-WIDTH BLACK BARS · ZERO ICONS",
               "EDITION B — BACK · IV KETAMINE PHOTO OPTION 2")

# ------------------------------------------------------------------ print sheets & index
SHEET_CSS = r"""
html,body{margin:0;padding:0;background:#EFEAF6;font-family:Inter,Arial,sans-serif;color:#111}
.sheet{width:760px;box-shadow:0 2px 5px rgba(40,20,60,.12),0 18px 44px rgba(60,30,90,.18);background:#fff}
@page{size:8.5in 11in;margin:0}
@media print{
 html,body{background:#fff;width:auto;height:auto}
 .noprint{display:none!important}
 .stage{display:block!important;padding:0!important;gap:0!important}
 .sheet{width:8.5in;height:11in;overflow:hidden;box-shadow:none;break-after:page;page-break-after:always}
 .sheet:last-child{break-after:auto;page-break-after:auto}
 .sheet .pg{transform:scale(1.073684);transform-origin:0 0}
}
"""


def sheet(x):
    return f'<div class="sheet">{x}</div>'


EDITION_SWITCH_CSS = r"""
[data-ed="A"] .ed-B{display:none!important}
[data-ed="B"] .ed-A{display:none!important}
.ed{display:contents}
"""

PRINT_JS = r"""
<script>
(function(){
 var q=new URLSearchParams(location.search);
 var ed=q.get('ed'), ket=q.get('ket');
 var root=document.getElementById('root');
 if(ed==='A'||ed==='B'){root.setAttribute('data-ed',ed)}
 if(ket==='1'||ket==='2'){document.querySelectorAll('.ed').forEach(function(n){n.setAttribute('data-ket',ket)})}
})();
</script>
"""

# print_sheets.html: 4 pages, per-edition default ketamine option (A = Option 1, B = Option 2)
ps_body = (f' id="root" data-ed="all"><div class="stage" style="display:flex;flex-direction:column;gap:24px;align-items:center;padding:24px 0">'
           f'<div class="ed ed-A" data-ket="1">{sheet(front_a())}{sheet(back_a("toggle"))}</div>'
           f'<div class="ed ed-B" data-ket="2">{sheet(front_b())}{sheet(back_b("toggle"))}</div>'
           f'</div>{PRINT_JS}')
write("print_sheets.html", "Hopemark Health – Print Sheets 8.5 × 11 (Edition A + B)",
      PAGE_CSS + SHEET_CSS + EDITION_SWITCH_CSS, ps_body)

IDX_CSS = r"""
body{min-height:100vh}
.tb{position:sticky;top:0;z-index:10;background:#111;color:#fff;padding:14px 28px;display:flex;flex-wrap:wrap;gap:14px 30px;align-items:center}
.tb .ttl{font-family:'Plus Jakarta Sans',Inter,sans-serif;font-weight:800;font-size:16px;letter-spacing:-.01em;margin-right:auto}
.tb .ttl small{display:block;font-family:Inter,sans-serif;font-weight:500;font-size:11px;color:#cfc4da;letter-spacing:.02em;margin-top:2px}
.grp{display:flex;flex-direction:column;gap:4px}
.grp label{font-size:9px;letter-spacing:.18em;font-weight:600;color:#DFC5EE}
.seg{display:flex;border:1px solid #DFC5EE;border-radius:4px;overflow:hidden}
.seg button{background:transparent;color:#fff;border:0;padding:8px 14px;font:600 12px Inter,sans-serif;cursor:pointer}
.seg button+button{border-left:1px solid #DFC5EE}
.seg button.on{background:#DFC5EE;color:#111}
.act{display:flex;gap:10px;align-items:center}
.btn{background:#DFC5EE;color:#111;border:0;border-radius:4px;padding:10px 16px;font:700 12px Inter,sans-serif;cursor:pointer;text-decoration:none;display:inline-block}
.btn.ghost{background:transparent;color:#fff;border:1px solid #DFC5EE}
.nav{padding:10px 28px;background:#E3D8EE;font-size:12px;display:flex;gap:18px;flex-wrap:wrap}
.nav a{color:#111;font-weight:600}
.stage{display:flex;flex-wrap:wrap;gap:28px;justify-content:center;padding:30px 20px 50px}
.note{text-align:center;font-size:11px;color:#4B4753;padding:0 20px 36px}
"""

IDX_JS = r"""
<script>
(function(){
 var root=document.getElementById('root'), st=document.getElementById('stage');
 var ed='A', ket='1';
 function apply(){
  root.setAttribute('data-ed',ed); st.setAttribute('data-ket',ket);
  document.querySelectorAll('[data-set]').forEach(function(b){
   var k=b.getAttribute('data-set'), v=b.getAttribute('data-val');
   b.classList.toggle('on',(k==='ed'?ed:ket)===v);
  });
  var f='downloads/hopemark-flyer-edition-'+ed+'-ketamine-option-'+ket+'.pdf';
  document.getElementById('dlpdf').setAttribute('href',f);
  document.getElementById('dlpdf').setAttribute('download',f.split('/').pop());
  document.getElementById('edlabel').textContent=(ed==='A'?'Edition A — Black Back Spine + Lavender Front Header':'Edition B — Lavender Spine + Black Bottom Bars');
 }
 document.querySelectorAll('[data-set]').forEach(function(b){
  b.addEventListener('click',function(){
   if(b.getAttribute('data-set')==='ed'){ed=b.getAttribute('data-val')} else {ket=b.getAttribute('data-val')}
   apply();
  });
 });
 document.getElementById('printbtn').addEventListener('click',function(){window.print()});
 apply();
})();
</script>
"""

idx_body = (
    ' id="root" data-ed="A">'
    '<div class="tb noprint">'
    '<div class="ttl">Hopemark Health — Two-Sided Psychiatry Flyer<small id="edlabel"></small></div>'
    '<div class="grp"><label>EDITION</label><div class="seg">'
    '<button data-set="ed" data-val="A">A · Black Back Spine + Lavender Front Header</button>'
    '<button data-set="ed" data-val="B">B · Lavender Spine + Black Bottom Bars</button></div></div>'
    '<div class="grp"><label>IV KETAMINE PHOTO</label><div class="seg">'
    '<button data-set="ket" data-val="1">Option 1</button><button data-set="ket" data-val="2">Option 2</button></div></div>'
    '<div class="act"><button class="btn" id="printbtn">Print / Save 8.5×11 PDF</button>'
    '<a class="btn ghost" id="dlpdf" href="downloads/hopemark-flyer-edition-A-ketamine-option-1.pdf">Download Print-Ready PDF</a>'
    '<a class="btn ghost" href="downloads/hopemark-print-pack.zip">Download PDF + SVG Pack</a></div>'
    '</div>'
    '<div class="nav noprint"><span>Presentation boards:</span>'
    '<a href="board1.html">Board 1 · Edition A</a><a href="board2.html">Board 2 · Edition B</a>'
    '<a href="board3.html">Board 3 · Close-up proof</a><a href="board4.html">Board 4 · Print spec</a>'
    '<a href="print_sheets.html">All print sheets</a></div>'
    f'<div class="stage" id="stage" data-ket="1">'
    f'<div class="ed ed-A">{sheet(front_a())}{sheet(back_a("toggle"))}</div>'
    f'<div class="ed ed-B">{sheet(front_b())}{sheet(back_b("toggle"))}</div></div>'
    '<div class="note noprint">US Letter 8.5&quot; × 11&quot; · two-sided · full-color photography · no icons · QR code links to HopeMark.com</div>'
    + IDX_JS)
write("index.html", "Hopemark Health – Two-Sided Psychiatry Clinic Flyer (8.5 × 11 Print-Ready)",
      PAGE_CSS + SHEET_CSS + EDITION_SWITCH_CSS + IDX_CSS, idx_body)

# ------------------------------------------------------------------ board 3: 1:1 close-up proof
B3_CSS = r"""
html,body{margin:0;padding:0;width:1600px;height:1200px;overflow:hidden}
body{position:relative;font-family:Inter,'Helvetica Neue',Arial,sans-serif;color:#111;
 background:radial-gradient(1200px 800px at 50% 0%,#F6F2FB 0%,#EFEAF6 60%,#E8E1F1 100%)}
.ttl{position:absolute;left:20px;right:20px;top:14px;display:flex;justify-content:space-between;font-size:11px;letter-spacing:.14em;font-weight:700}
.ttl span:last-child{color:#4B4753;font-weight:600}
.bcol{position:absolute;top:42px;width:760px;display:flex;flex-direction:column;gap:12px}
.lb{height:22px;display:flex;justify-content:space-between;align-items:center;font-size:9.5px;letter-spacing:.13em;font-weight:700;background:#111;color:#fff;padding:0 10px}
.lb i{font-style:normal;font-weight:500;color:#DFC5EE;letter-spacing:.04em}
.crop{position:relative;width:760px;overflow:hidden;box-shadow:0 2px 5px rgba(40,20,60,.12),0 14px 34px rgba(60,30,90,.18);background:#fff}
.crop .pg{position:absolute;left:0;top:0}
.cmp{display:flex;gap:20px}
.cmp .opt{width:370px}
.cmp .im{width:370px;height:226px;border-radius:6px;overflow:hidden;box-shadow:0 2px 5px rgba(40,20,60,.12),0 14px 34px rgba(60,30,90,.18);background:#fff}
.cmp img{width:100%;height:100%;object-fit:cover;object-position:50% 40%;display:block}
.chk{background:#fff;border-left:4px solid #C8A8E9;padding:10px 16px;font-size:11px;line-height:1.7;box-shadow:0 2px 5px rgba(40,20,60,.1)}
.chk .t{font-size:9.5px;letter-spacing:.16em;font-weight:700;margin-bottom:2px;color:#4B4753}
.cmp .chk{margin-top:10px}
"""
B3_JS = r"""
<script>
document.querySelectorAll('.crop[data-from]').forEach(function(c){
 var pg=c.querySelector('.pg'), pr=pg.getBoundingClientRect();
 function pos(sel,edge){var r=pg.querySelector(sel).getBoundingClientRect();return (edge==='b'?r.bottom:r.top)-pr.top}
 var f=c.dataset.from,t=c.dataset.to;
 var y0=f==='top'?0:pos(f,'t')-parseFloat(c.dataset.pad||0);
 var y1=t==='bottom'?pr.height:pos(t,'b');
 pg.style.top=(-y0)+'px';c.style.height=(y1-y0)+'px';
});
</script>
"""
b3 = (
    '><div class="ttl"><span>BOARD 3 — 1:1 PROOF · EVERY WORD, NUMBER AND PHOTO AT BOARD SCALE (760 PX = 8.5 IN)</span>'
    '<span>FULL COLOR · ZERO ICONS · NO PHOTO FILTERS</span></div>'
    '<div class="bcol" style="left:20px">'
    '<div class="lb"><span>FRONT — HEADER</span><i>logo · title · intro · telehealth badge · consultation photo</i></div>'
    f'<div class="crop" data-from="top" data-to=".hero">{front_a()}</div>'
    '<div class="lb"><span>FRONT — LOCATIONS + BLACK CONTACT BAR</span><i>6 addresses · PHONE · FAX · WEBSITE · QR + HopeMark.com</i></div>'
    f'<div class="crop" data-from=".locs" data-pad="10" data-to="bottom">{front_a()}</div>'
    '<div class="lb"><span>IV KETAMINE PHOTO — OPTION 1 vs OPTION 2</span><i>both full color · eye mask · no IV equipment</i></div>'
    '<div class="cmp">'
    f'<div class="opt"><div class="im"><img src="{IMG["ket1"]}" alt="Option 1"></div><div class="chk"><div class="t">OPTION 1 · OFFICIAL</div>ketamine_official_color.png</div></div>'
    f'<div class="opt"><div class="im"><img src="{IMG["ket2"]}" alt="Option 2"></div><div class="chk"><div class="t">OPTION 2 · STUDIO</div>ketamine_patient_color.jpg</div></div>'
    '</div></div>'
    '<div class="bcol" style="left:820px">'
    '<div class="lb"><span>BACK — BLACK SPINE · DEEP TMS · SPRAVATO® · IV KETAMINE</span><i>1:1</i></div>'
    f'<div class="crop" data-from="top" data-to="bottom">{back_a("1")}</div>'
    '<div class="chk"><div class="t">VERIFY AT A GLANCE</div><b>PHONE</b> 630-656-9393 &nbsp;·&nbsp; <b>FAX</b> 630-385-0290 &nbsp;·&nbsp; <b>WEBSITE</b> HopeMark.com<br>'
    'QR (front bar + back spine) opens https://hopemark.com/ · white box, HopeMark.com directly beneath</div></div>'
    + B3_JS)
write("board3.html", "Hopemark Health – 1:1 Close-Up Proof", PAGE_CSS + B3_CSS, b3)

# ------------------------------------------------------------------ board 4: print production spec
B4_CSS = r"""
html,body{margin:0;padding:0;width:1600px;height:1200px;overflow:hidden}
body{position:relative;font-family:Inter,'Helvetica Neue',Arial,sans-serif;color:#111;
 background:radial-gradient(1200px 800px at 50% 0%,#F6F2FB 0%,#EFEAF6 60%,#E8E1F1 100%)}
.hd{position:absolute;left:30px;right:30px;top:22px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid #111;padding-bottom:10px}
.hd b{font-family:'Plus Jakarta Sans',Inter,sans-serif;font-size:20px;letter-spacing:-.02em;font-weight:800}
.hd span{font-size:10.5px;letter-spacing:.14em;font-weight:600;color:#4B4753}
.blk{position:absolute;top:84px;width:535px;height:700px}
.abs{position:absolute}
.bleedr{position:absolute;box-shadow:0 0 0 .5px rgba(224,36,94,.9)}
.pgs{position:absolute;overflow:hidden;box-shadow:0 8px 22px rgba(60,30,90,.22)}
.pgs .pg{transform-origin:0 0}
.trim{position:absolute;outline:.75px solid #111}
.safe{position:absolute;outline:.75px dashed #7A4FB0}
.cm{position:absolute;background:#111}
.bcap{position:absolute;left:0;right:0;top:664px;text-align:center;font-size:10.5px;letter-spacing:.14em;font-weight:700}
.bcap i{font-style:normal;font-weight:500;color:#4B4753;letter-spacing:.06em}
.dimh{position:absolute;font-size:9px;letter-spacing:.1em;font-weight:600;color:#4B4753}
.leg{position:absolute;left:30px;top:798px;width:1070px;display:flex;gap:26px;font-size:10px;font-weight:600;letter-spacing:.06em;align-items:center}
.leg .k{display:inline-block;width:26px;height:0;vertical-align:middle;margin-right:7px}
.sw{position:absolute;top:846px;width:198px;height:262px;background:#fff;box-shadow:0 2px 5px rgba(40,20,60,.1),0 12px 28px rgba(60,30,90,.12)}
.sw .c{height:130px;border-bottom:1px solid #e5e0ea}
.sw .n{padding:12px 14px 0;font-family:'Plus Jakarta Sans',Inter,sans-serif;font-weight:800;font-size:14px;letter-spacing:-.01em}
.sw .u{padding:2px 14px 0;font-size:9.5px;color:#4B4753}
.sw dl{margin:10px 14px 0;font-size:10.5px;line-height:1.7}
.sw dt{display:inline;font-size:8.5px;letter-spacing:.16em;font-weight:700;color:#4B4753}
.sw dd{display:inline;margin:0 0 0 6px;font-weight:600}
.sw dl div{border-top:1px solid #eee7f3}
.pnl{position:absolute;left:1130px;width:440px;background:#fff;box-shadow:0 2px 5px rgba(40,20,60,.1),0 12px 28px rgba(60,30,90,.12)}
.pnl .ph{background:#111;color:#fff;font-size:10px;letter-spacing:.16em;font-weight:700;padding:8px 14px}
.pnl .pb{padding:12px 14px 14px;font-size:11.2px;line-height:1.55}
table.sp{border-collapse:collapse;width:100%}
table.sp td{padding:4.5px 0;border-bottom:1px solid #eee7f3;vertical-align:top}
table.sp td:first-child{font-size:8.8px;letter-spacing:.14em;font-weight:700;color:#4B4753;width:120px;padding-top:6px}
.qv{display:flex;gap:16px;align-items:center}
.qv .qb{background:#fff;border:1px solid #ddd;padding:6px;width:122px;height:122px;flex:0 0 auto}
.qv .qb img{width:100%;height:100%;display:block}
.qv .qt{font-size:11px;font-weight:700;text-align:center;margin-top:4px}
.ok{display:inline-block;background:#DFC5EE;font-size:9px;letter-spacing:.14em;font-weight:700;padding:2px 7px;margin-bottom:5px}
.dl{list-style:none;margin:0;padding:0}
.dl li{display:grid;grid-template-columns:62px 1fr auto;gap:10px;align-items:baseline;padding:6px 0;border-bottom:1px solid #eee7f3;font-size:11px}
.dl li:last-child{border:0}
.dl .f{font-family:'Plus Jakarta Sans',Inter,sans-serif;font-weight:800;font-size:13px}
.dl .s{font-size:8.5px;letter-spacing:.14em;font-weight:700;padding:2px 7px;background:#DFC5EE}
.dl .s.w{background:#eee;color:#4B4753}
.dl a{color:#111;font-weight:600}
"""


def bleed_block(left, page_html, bg, caption):
    W = 477.0                       # trim width on board (px)
    ppi = W / 8.5
    b = 0.125 * ppi
    sf = 0.25 * ppi
    H = W * 11 / 8.5
    m = 24.0
    tl, tt = m + b, m + b           # trim origin inside block
    sc = W / 760
    parts = [
        f'<div class="bleedr" style="left:{m}px;top:{m}px;width:{W+2*b}px;height:{H+2*b}px;background:{bg}"></div>',
        f'<div class="pgs" style="left:{tl}px;top:{tt}px;width:{W}px;height:{H}px"><div class="pg-wrap" style="width:760px;transform:scale({sc});transform-origin:0 0">{page_html}</div></div>',
        f'<div class="safe" style="left:{tl+sf}px;top:{tt+sf}px;width:{W-2*sf}px;height:{H-2*sf}px"></div>',
        f'<div class="trim" style="left:{tl}px;top:{tt}px;width:{W}px;height:{H}px"></div>',
    ]
    L = 12
    gap = b + 3
    for (cx, cy) in [(tl, tt), (tl + W, tt), (tl, tt + H), (tl + W, tt + H)]:
        sx = -1 if cx == tl else 1
        sy = -1 if cy == tt else 1
        # horizontal mark
        x0 = cx + sx * gap if sx > 0 else cx - gap - L
        parts.append(f'<div class="cm" style="left:{x0}px;top:{cy-0.4}px;width:{L}px;height:.8px"></div>')
        y0 = cy + sy * gap if sy > 0 else cy - gap - L
        parts.append(f'<div class="cm" style="left:{cx-0.4}px;top:{y0}px;width:.8px;height:{L}px"></div>')
    parts.append(f'<div class="dimh" style="left:{tl}px;top:2px">8.5 in</div>')
    parts.append(f'<div class="bcap" style="top:{tt+H+b+18}px">{caption}</div>')
    return f'<div class="blk" style="left:{left}px">' + "".join(parts) + '</div>'


def swatch(x, hexc, name, use, rgb, cmyk, extra=""):
    ln = "border-bottom:1px solid #e5e0ea"
    return (f'<div class="sw" style="left:{x}px"><div class="c" style="background:{hexc}"></div>'
            f'<div class="n">{name}</div><div class="u">{use}</div>'
            f'<dl><div><dt>HEX</dt><dd>{hexc}</dd></div><div><dt>RGB</dt><dd>{rgb}</dd></div>'
            f'<div><dt>CMYK≈</dt><dd>{cmyk}</dd></div>{extra}</dl></div>')


bg_front = "linear-gradient(90deg,#DFC5EE 52%,#fff 52%) top/100% 37% no-repeat,linear-gradient(#111,#111) bottom/100% 11% no-repeat,#fff"
bg_back = "linear-gradient(90deg,#111 34%,#fff 34%)"
sw_x = [30, 244, 458, 672, 886]
b4 = (
    '><div class="hd"><b>Board 4 — Print Production Spec Sheet</b>'
    '<span>US LETTER 8.5 × 11 IN · TWO-SIDED · 0.125 IN BLEED · EDITION A SHOWN (EDITION B USES THE SAME SPEC)</span></div>'
    + bleed_block(30, front_a(), bg_front, 'SIDE 1 — FRONT <i>· trim 8.5 × 11 in · with bleed 8.75 × 11.25 in</i>')
    + bleed_block(585, back_a("1"), bg_back, 'SIDE 2 — BACK <i>· black spine bleeds off left, top and bottom</i>')
    + '<div class="leg"><span><span class="k" style="border-top:2px solid #111"></span>TRIM LINE 8.5 × 11 in</span>'
      '<span><span class="k" style="border-top:2px solid #E0245E"></span>BLEED 0.125 in</span>'
      '<span><span class="k" style="border-top:2px dashed #7A4FB0"></span>SAFE AREA 0.25 in</span>'
      '<span><span class="k" style="border-top:2px solid #111;width:10px"></span>CROP MARKS</span></div>'
    + swatch(sw_x[0], "#DFC5EE", "Hopemark Lavender", "Front hero · Edition B spines", "223 · 197 · 238", "6 / 17 / 0 / 7")
    + swatch(sw_x[1], "#111111", "Rich Black", "Back spine · contact bars · badge", "17 · 17 · 17", "0 / 0 / 0 / 93",
             '<div><dt>BUILD</dt><dd>C60 M40 Y40 K100</dd></div>')
    + swatch(sw_x[2], "#FFFFFF", "Pure White", "Paper · text on black", "255 · 255 · 255", "0 / 0 / 0 / 0")
    + swatch(sw_x[3], "#C8A8E9", "Lavender Accent", "Bullets · rules · 1 in 3* stat tint", "200 · 168 · 233", "14 / 28 / 0 / 9")
    + swatch(sw_x[4], "#F4ECF9", "Soft Lavender", "Location cards · callouts · visual cards", "244 · 236 · 249", "2 / 5 / 0 / 2")
    + '<div class="abs" style="left:30px;top:1166px;font-size:9px;color:#4B4753;letter-spacing:.03em;width:1070px">CMYK values are a straight RGB-to-CMYK conversion for reference. Final press values are set from the printer’s ICC profile and a hard proof before release.</div>'
    # right panels
    + '<div class="pnl" style="top:84px"><div class="ph">PRINT SPECIFICATION</div><div class="pb"><table class="sp">'
      '<tr><td>TRIM SIZE</td><td>8.5 × 11 in (215.9 × 279.4 mm), portrait</td></tr>'
      '<tr><td>BLEED</td><td>0.125 in (3.18 mm) on all sides → 8.75 × 11.25 in</td></tr>'
      '<tr><td>SAFE AREA</td><td>0.25 in inside trim for all text and QR codes</td></tr>'
      '<tr><td>SIDES</td><td>2 — front (clinic overview) and back (treatment-resistant depression)</td></tr>'
      '<tr><td>COLOR</td><td>Full-color photography, no grayscale or monochrome filters</td></tr>'
      '<tr><td>TYPE</td><td>Plus Jakarta Sans + Inter, embedded in the PDF</td></tr>'
      '<tr><td>ICONS</td><td>None. Contact labels are set as type: PHONE · FAX · WEBSITE</td></tr>'
      '</table></div></div>'
    + f'<div class="pnl" style="top:430px"><div class="ph">LIVE QR VERIFICATION</div><div class="pb"><div class="qv">'
      f'<div><div class="qb"><img src="{IMG["qr"]}" alt="QR code"></div><div class="qt">HopeMark.com</div></div>'
      '<div><span class="ok">DECODED · MATCHES</span><br><b>https://hopemark.com/</b><br>'
      'The vector file <b>qr_hopemark.svg</b> and the raster copy were both decoded with a QR reader on 2026-11-09. '
      'On the flyer the QR sits in a white box with HopeMark.com printed directly beneath it, on the front bar and the back spine.</div>'
      '</div></div></div>'
    + '<div class="pnl" style="top:736px"><div class="ph">DELIVERABLES</div><div class="pb"><ul class="dl">'
      '<li><span class="f">.PDF</span><span>Print-ready 8.5 × 11 in, both sides · <a href="downloads/hopemark-flyer-edition-A-ketamine-option-1.pdf">A</a> · <a href="downloads/hopemark-flyer-edition-B-ketamine-option-2.pdf">B</a></span><span class="s">NOW</span></li>'
      '<li><span class="f">.PDF</span><span>Press file with 0.125 in bleed and crop marks</span><span class="s w">NOW</span></li>'
      f'<li><span class="f">.SVG</span><span>QR code vector · <a href="{IMG["qr"]}">qr_hopemark.svg</a></span><span class="s">NOW</span></li>'
      '<li><span class="f">.AI/.EPS</span><span>Editable layered artwork</span><span class="s w">NOW</span></li>'
      '<li><span class="f">.HTML</span><span>Source of this site · <a href="index.html">index.html</a></span><span class="s">NOW</span></li>'
      '</ul></div></div>')
write("board4.html", "Hopemark Health – Print Production Spec Sheet", PAGE_CSS + B4_CSS, b4)
