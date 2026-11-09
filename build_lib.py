#!/usr/bin/env python3
"""Hopemark flyer: shared page markup + CSS. Used by build.py (boards, index, print sheets).
All copy is verbatim from the contest brief. ZERO icons, ZERO filters on photos.
"""
import html

P = "assets/processed/"
IMG = {
    "logo_dark": P + "logo_horizontal_dark_h.png",
    "logo_white": P + "logo_horizontal_white.png",
    "consult": P + "consultation_color.jpg",
    "tms": "assets/brainsway_tms.jpg",
    "brains": P + "brains_pair_clean.png",
    "spravato": "assets/spravato.jpg",
    "ket1": P + "ketamine_official_color.png",
    "ket2": P + "ketamine_patient_color.jpg",
    "qr": P + "qr_hopemark.svg",
}

PHONE, FAX, WEB = "630-656-9393", "630-385-0290", "HopeMark.com"

SERVICES = [
    "Psychiatric evaluations and medication management",
    "Psychotherapy",
    "Neuropsychological testing",
    "Child and adolescent psychiatry",
    "Sleep medicine",
    "Genetic testing – pharmacogenomics",
    "Substance use treatment and medically assisted recovery",
]
CONDITIONS = [
    "Major depressive disorder",
    "Anxiety and panic disorders",
    "Post-traumatic stress disorder (PTSD)",
    "Bipolar disorder",
    "Obsessive-compulsive disorder (OCD)",
    "Substance use disorders",
]
TEAM = [
    "Psychiatrists",
    "Psychiatric mental health nurse practitioners",
    "Psychologists",
    "Physician assistants",
    "Licensed counselors and therapists",
]
LOCATIONS = [
    ("Chicago – Millennium Park", "8 S. Michigan Avenue, Suite 1505, Chicago, IL 60603"),
    ("Chicago – West Loop", "566 W. Lake Street, Suite 200, Chicago, IL 60661"),
    ("Hoffman Estates", "1721 Moon Lake Boulevard, Suite 201, Hoffman Estates, IL 60169"),
    ("Naperville", "1284 Rickert Drive, Suite 200, Naperville, IL 60540"),
    ("Oak Brook", "1200 Harger Road, Suite 200, Oak Brook, IL 60523"),
    ("Orland Park", "14489 John Humphrey Drive, Suite 202, Orland Park, IL 60462"),
]
INTRO = ("Hopemark Health provides evidence-based psychiatric care for children, adolescents, and adults. "
         "Our multidisciplinary team supports accurate diagnosis, individualized treatment, and coordination "
         "with referring providers.")
TRD_1 = ("When depression has not improved enough after at least two antidepressants taken at an adequate dose "
         "for an adequate length of time, it may be treatment-resistant depression (TRD).")
TRD_2 = "Symptoms such as persistent sadness, low energy, and loss of interest can continue to affect everyday life."
COMMON = ("A U.S. study estimated that approximately one-third of adults receiving medication for major depression "
          "had treatment-resistant depression.")
HELP = ("Our team reviews each patient’s symptoms and treatment history to build a personalized plan that may "
        "include novel therapies, medication management, and psychotherapy.")
TMS_WHAT = ("A noninvasive treatment that uses magnetic pulses to stimulate brain networks involved in mood and OCD. "
            "FDA-cleared for depression and as an additional treatment for OCD.")
TMS_BEN = ("May reduce persistent depression symptoms. An OCD-specific treatment protocol may reduce obsessive "
           "thoughts and compulsive behaviors.")
SPR_WHAT = ("An FDA-approved prescription nasal spray for adults with treatment-resistant depression. It acts on "
            "NMDA receptors in the brain’s glutamate system.")
SPR_BEN = ("May reduce depression symptoms, with improvement observed as early as approximately 24 hours in "
           "clinical trials. It can be used with or without an oral antidepressant for TRD.")
KET_WHAT = ("Low-dose ketamine delivered through an IV. It acts on NMDA receptors in the brain’s glutamate "
            "system and is used off-label for depression.")
KET_BEN = ("May relieve depression symptoms within hours for some patients when standard treatments have not "
           "provided enough relief. Additional treatments may be needed to maintain benefits.")
FOOTNOTE = ("*In a 2021 U.S. study, an estimated 30.9% of adults with medication-treated major depression had "
            "treatment-resistant depression. Source: Zhdanava et al., Journal of Clinical Psychiatry. "
            "2021;82(2):20m13699.")


def e(s):
    return html.escape(s, quote=False)


def lis(items):
    return "<ul class=\"bl\">" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def contacts(cls=""):
    return (f'<div class="cts {cls}">'
            f'<div class="ct"><span class="ctl">PHONE</span><span class="ctv">{PHONE}</span></div>'
            f'<div class="ct"><span class="ctl">FAX</span><span class="ctv">{FAX}</span></div>'
            f'<div class="ct"><span class="ctl">WEBSITE</span><span class="ctv">{WEB}</span></div></div>')


def contacts_stack():
    return (f'<div class="cts stack">'
            f'<div class="ct"><span class="ctl">PHONE</span><span class="ctv">{PHONE}</span></div>'
            f'<div class="ct"><span class="ctl">FAX</span><span class="ctv">{FAX}</span></div>'
            f'<div class="ct"><span class="ctl">WEBSITE</span><span class="ctv">{WEB}</span></div></div>')


def qr(size=""):
    return (f'<div class="qr {size}"><div class="qrb"><img src="{IMG["qr"]}" alt="QR code for HopeMark.com"></div>'
            f'<div class="qrt">HopeMark.com</div></div>')


def loc_cards():
    return "".join(f'<div class="lc"><div class="ln">{e(n)}</div><div class="la">{e(a)}</div></div>'
                   for n, a in LOCATIONS)


def loc_list():
    return "".join(f'<div class="ll"><div class="ln">{e(n)}</div><div class="la">{e(a)}</div></div>'
                   for n, a in LOCATIONS)


def ket_img(ket, cls="kph"):
    """ket: '1' | '2' | 'toggle'"""
    a1 = '<img class="k1 %s" src="%s" alt="Woman resting comfortably in a chair with an eye mask">' % (cls, IMG["ket1"])
    a2 = '<img class="k2 %s" src="%s" alt="Woman resting comfortably in a recliner with an eye mask">' % (cls, IMG["ket2"])
    if ket == "1":
        return a1
    if ket == "2":
        return a2
    return a1 + a2


def modules(ket):
    tms = f"""
<div class="mod m-tms">
  <div class="mh"><h4>Deep TMS</h4><div class="ms">Deep Transcranial Magnetic Stimulation</div></div>
  <div class="m2c">
    <p><b>What it is and how it works:</b> {e(TMS_WHAT)}</p>
    <p><b>Potential benefits:</b> {e(TMS_BEN)}</p>
  </div>
  <div class="vcard tmsc">
    <div class="tmsph"><img src="{IMG['tms']}" alt="BrainsWay Deep TMS device"></div>
    <div class="brw">
      <img src="{IMG['brains']}" alt="Brain scan pair">
      <div class="brl"><span>Before TMS</span><span>Potential response after TMS</span></div>
      <div class="brc">Educational visualization. Results vary.</div>
    </div>
  </div>
</div>"""
    spr = f"""
<div class="mod m-spr">
  <div class="mh"><h4>Spravato®</h4><div class="ms">Esketamine Nasal Spray</div></div>
  <div class="mrow">
    <div class="mtx">
      <p><b>What it is and how it works:</b> {e(SPR_WHAT)}</p>
      <p><b>Potential benefits:</b> {e(SPR_BEN)}</p>
    </div>
    <div class="vcard sprc"><img src="{IMG['spravato']}" alt="Spravato nasal spray applicator and logo"></div>
  </div>
</div>"""
    kt = f"""
<div class="mod m-ket">
  <div class="mh"><h4>IV Ketamine</h4></div>
  <div class="mrow">
    <div class="mtx">
      <p><b>What it is and how it works:</b> {e(KET_WHAT)}</p>
      <p><b>Potential benefits:</b> {e(KET_BEN)}</p>
    </div>
    <div class="vcard ketc">{ket_img(ket)}</div>
  </div>
</div>"""
    return tms, spr, kt


def trd_blocks():
    what = (f'<div class="sec"><h5>What Is Treatment-Resistant Depression?</h5>'
            f'<p>{e(TRD_1)}</p><p>{e(TRD_2)}</p></div>')
    common = (f'<div class="sec"><h5>How Common Is It?</h5><div class="about">About</div>'
              f'<div class="stat">1 in 3*</div><p>{e(COMMON)}</p></div>')
    return what, common


# ---------------------------------------------------------------- pages
def front_a():
    return f"""
<section class="pg fa" data-page="front-A">
  <div class="hero">
    <div class="hero-l">
      <img class="logo" src="{IMG['logo_dark']}" alt="Hopemark Health">
      <h1>Comprehensive Psychiatric Care</h1>
      <div class="sub">Your Trusted Referral Partner</div>
      <p class="intro">{e(INTRO)}</p>
      <div class="pill">In-person or telehealth visits available.</div>
    </div>
    <div class="hero-r"><div class="arch"><img src="{IMG['consult']}" alt="Psychiatrist and patient in consultation"></div></div>
  </div>
  <div class="grid3">
    <div class="col"><h3>Clinical Services</h3>{lis(SERVICES)}</div>
    <div class="col"><h3>Conditions We Treat</h3>{lis(CONDITIONS)}</div>
    <div class="col"><h3>Our Clinical Team</h3>{lis(TEAM)}</div>
  </div>
  <div class="locs"><h3>Hopemark Clinic Locations</h3><div class="lgrid">{loc_cards()}</div></div>
  <div class="bar">
    <div class="bar-t"><div class="bt1">Contact Information</div><div class="bt2">Referrals and appointments</div></div>
    {contacts()}
    {qr()}
  </div>
</section>"""


def back_a(ket):
    tms, spr, kt = modules(ket)
    what, common = trd_blocks()
    return f"""
<section class="pg ba" data-page="back-A">
  <aside class="sp">
    <img class="logo" src="{IMG['logo_white']}" alt="Hopemark Health">
    <h1>Treatment-Resistant Depression</h1>
    <div class="sub">More options. Renewed hope.</div>
    <hr>
    {what}
    {common}
    <div class="sp-bot">
      <div class="disc">Discuss treatment options with our team.</div>
      <div class="sp-cq">{contacts_stack()}{qr("sm")}</div>
    </div>
  </aside>
  <div class="mn">
    <div class="callout"><h5>How Hopemark Health Can Help</h5><p>{e(HELP)}</p></div>
    {tms}{spr}{kt}
    <div class="fn">{e(FOOTNOTE)}</div>
  </div>
</section>"""


def front_b():
    return f"""
<section class="pg fb" data-page="front-B">
  <div class="fb-top">
    <aside class="sp">
      <img class="logo" src="{IMG['logo_dark']}" alt="Hopemark Health">
      <div class="sec"><h3>Hopemark Clinic Locations</h3><div class="llist">{loc_list()}</div></div>
      <div class="sec"><h3>Our Clinical Team</h3>{lis(TEAM)}</div>
    </aside>
    <div class="mn">
      <h1>Comprehensive Psychiatric Care</h1>
      <div class="sub">Your Trusted Referral Partner</div>
      <p class="intro">{e(INTRO)}</p>
      <div class="pill">In-person or telehealth visits available.</div>
      <div class="ph"><img src="{IMG['consult']}" alt="Psychiatrist and patient in consultation"></div>
      <div class="two">
        <div class="col"><h3>Clinical Services</h3>{lis(SERVICES)}</div>
        <div class="col"><h3>Conditions We Treat</h3>{lis(CONDITIONS)}</div>
      </div>
    </div>
  </div>
  <div class="bar">
    <div class="bar-t"><div class="bt1">Contact Information</div><div class="bt2">Referrals and appointments</div></div>
    {contacts()}
    {qr()}
  </div>
</section>"""


def back_b(ket):
    tms, spr, kt = modules(ket)
    what, common = trd_blocks()
    return f"""
<section class="pg bb" data-page="back-B">
  <div class="bb-top">
    <aside class="sp">
      <img class="logo" src="{IMG['logo_dark']}" alt="Hopemark Health">
      <h1>Treatment-Resistant Depression</h1>
      <div class="sub">More options. Renewed hope.</div>
      <hr>
      {what}
      {common}
    </aside>
    <div class="mn">
      <div class="callout"><h5>How Hopemark Health Can Help</h5><p>{e(HELP)}</p></div>
      {tms}{spr}{kt}
    </div>
  </div>
  <div class="fn">{e(FOOTNOTE)}</div>
  <div class="bar">
    <div class="bar-t"><div class="bt1">Discuss treatment options with our team.</div></div>
    {contacts()}
    {qr("sm")}
  </div>
</section>"""


# ---------------------------------------------------------------- CSS
PAGE_CSS = r"""
@import url('assets/fonts/fonts.css');
.pg{--blk:#111111;--lav:#DFC5EE;--lav2:#C8A8E9;--soft:#F4ECF9;--call:#F3EAF9;--mut:#4B4753;
 position:relative;width:760px;aspect-ratio:8.5/11;background:#fff;color:#111;
 font-family:Inter,'Helvetica Neue',Arial,sans-serif;font-size:10px;line-height:1.42;overflow:hidden;
 display:flex;flex-direction:column;-webkit-print-color-adjust:exact;print-color-adjust:exact;text-align:left;
 font-feature-settings:'kern' 1}
.pg *{box-sizing:border-box;margin:0;padding:0}
.pg img{display:block}
.pg h1,.pg h3,.pg h4,.pg h5,.pg .sub,.pg .stat,.pg .pill,.pg .bt1{font-family:'Plus Jakarta Sans',Inter,'Helvetica Neue',Arial,sans-serif}
.pg .bl{list-style:none}
.pg .bl li{position:relative;padding-left:13px;margin-bottom:6px;font-size:11.3px;line-height:1.4}
.pg .bl li::before{content:'';position:absolute;left:0;top:.42em;width:5.5px;height:5.5px;background:var(--lav2);transform:skewX(-18deg)}
.pg h3{font-size:14px;font-weight:800;letter-spacing:-.01em;margin-bottom:11px;padding-top:11px;position:relative}
.pg h3::before{content:'';position:absolute;left:0;top:0;width:26px;height:3.5px;background:var(--lav2)}
/* contact bits */
.pg .cts{display:flex;gap:24px}
.pg .ct{display:flex;flex-direction:column;gap:2px}
.pg .ctl{font-size:7.3px;letter-spacing:.2em;font-weight:600;color:var(--lav)}
.pg .ctv{font-family:'Plus Jakarta Sans',Inter,sans-serif;font-size:13px;font-weight:700;color:#fff;letter-spacing:-.005em;white-space:nowrap}
.pg .cts.stack{flex-direction:column;gap:6px}
.pg .cts.stack .ct{flex-direction:row;align-items:baseline;gap:9px}
.pg .cts.stack .ctl{width:44px;flex:0 0 44px}
.pg .cts.stack .ctv{font-size:11.5px}
.pg .qr{display:flex;flex-direction:column;align-items:center;gap:4px;flex:0 0 auto}
.pg .qrb{background:#fff;padding:4px;width:68px;height:68px}
.pg .qrb img{width:100%;height:100%}
.pg .qr.sm .qrb{width:62px;height:62px}
.pg .qrt{font-size:8.6px;font-weight:600;color:#fff;letter-spacing:.02em}
.pg .bar{background:var(--blk);color:#fff;display:flex;align-items:center;justify-content:space-between;gap:20px;padding:0 34px}
.pg .bt1{font-size:13px;font-weight:800;letter-spacing:-.01em;color:#fff}
.pg .bt2{font-size:10px;color:#cfcfd6;margin-top:2px}
.pg .logo{height:36px;width:auto;align-self:flex-start}
.pg .sub{font-weight:600}
.pg .pill{background:var(--blk);color:#fff;border-radius:99px;padding:7px 16px;font-size:10.8px;font-weight:600;align-self:flex-start;letter-spacing:.01em;font-family:Inter,sans-serif!important}
.pg .intro{font-size:10.6px;line-height:1.5}
/* modules (shared back) */
.pg .callout{background:var(--call);padding:13px 16px 14px;border-left:4px solid var(--lav2)}
.pg .callout h5{font-size:14.5px;font-weight:800;letter-spacing:-.01em;margin-bottom:4px}
.pg .callout p{font-size:10.9px;line-height:1.48}
.pg .mod{position:relative;padding-top:10px;border-top:1px solid #d8d3df}
.pg .mod::before{content:'';position:absolute;left:0;top:-2px;width:34px;height:3px;background:var(--blk)}
.pg .mh{display:flex;align-items:baseline;gap:10px;margin-bottom:6px;flex-wrap:wrap}
.pg .mh h4{font-size:22px;font-weight:800;letter-spacing:-.025em;line-height:1.05}
.pg .ms{font-size:10.8px;font-weight:600;color:var(--mut)}
.pg .mod p{font-size:10.7px;line-height:1.46;margin-bottom:6px}
.pg .mod p b{font-weight:700}
.pg .m2c{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.pg .mrow{display:grid;grid-template-columns:1fr 196px;gap:18px;align-items:start}
.pg .vcard{background:var(--soft);border-radius:6px;padding:8px}
.pg .vcard img{width:100%}
.pg .sprc{background:#fff;border:1px solid #e4d9ee;padding:4px}
.pg .ketc{padding:0;background:#fff;overflow:hidden}
.pg .ketc .kph{width:100%;height:150px;object-fit:cover;object-position:50% 40%;border-radius:6px}
.pg .tmsc{display:flex;gap:14px;align-items:center;margin-top:6px}
.pg .tmsph{flex:0 0 96px;background:#fff;border-radius:4px;overflow:hidden}
.pg .tmsph img{width:100%}
.pg .brw{flex:1}
.pg .brw img{width:100%;border-radius:3px}
.pg .brl{display:flex;justify-content:space-between;font-size:9.2px;font-weight:700;margin-top:4px;color:#111;gap:8px}
.pg .brc{font-size:8.4px;color:var(--mut);margin-top:3px}
.pg .fn{font-size:8.2px;line-height:1.4;color:var(--mut)}
/* sidebar (shared) */
.pg .sp .sec h5{font-size:12.6px;font-weight:800;letter-spacing:.01em;margin-bottom:5px}
.pg .sp .sec p{font-size:11.1px;line-height:1.52;margin-bottom:8px}
.pg .sp h1{font-size:28px;line-height:1.05;font-weight:800;letter-spacing:-.03em}
.pg .sp .sub{font-size:14px}
.pg .sp .about{font-size:12px;font-weight:600}
.pg .sp .stat{font-size:72px;font-weight:800;letter-spacing:-.045em;line-height:1;margin:1px 0 6px}
.pg .sp hr{border:0;height:1px}

/* ============ EDITION A ============ */
.fa .hero{flex:0 0 37%;display:grid;grid-template-columns:52% 48%}
.fa .hero-l{background:#DFC5EE;padding:28px 28px 24px 34px;display:flex;flex-direction:column}
.fa .hero h1{font-size:31px;line-height:1.05;font-weight:800;letter-spacing:-.035em;margin-top:20px}
.fa .hero .sub{font-size:13.5px;margin-top:8px}
.fa .hero .intro{margin-top:12px}
.fa .hero .pill{margin-top:auto}
.fa .hero-r{background:#fff;padding:56px 22px 0 14px;display:flex;align-items:flex-end}
.fa .arch{width:100%;height:100%;border-radius:999px 999px 0 0;overflow:hidden;background:var(--lav)}
.fa .arch img{width:100%;height:100%;object-fit:cover;object-position:60% 40%}
.fa .grid3{flex:1;display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:24px;padding:30px 34px 0}
.fa .locs{padding:0 34px 22px}
.fa .lgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.fa .lc{background:var(--soft);border-radius:5px;padding:12px 13px 13px;border-left:3px solid var(--lav2)}
.pg .ln{font-size:11.6px;font-weight:700;font-family:'Plus Jakarta Sans',Inter,sans-serif}
.pg .la{font-size:10.3px;color:var(--mut);line-height:1.4;margin-top:3px}
.fa .bar{flex:0 0 11%}
.fa .bar-t{flex:0 0 138px}

.ba{flex-direction:row}
.ba .sp{flex:0 0 34%;background:var(--blk);color:#fff;padding:26px 22px 22px;display:flex;flex-direction:column;gap:0}
.ba .sp .logo{height:38px;margin-bottom:20px}
.ba .sp .sub{color:var(--lav);margin-top:8px}
.ba .sp hr{background:rgba(255,255,255,.35);margin:14px 0 14px}
.ba .sp .sec{margin-bottom:26px}
.ba .sp .sec h5{color:#fff}
.ba .sp .sec p{color:#e8e6ee}
.ba .sp .stat{color:var(--lav)}
.ba .sp .about{color:#fff}
.ba .sp-bot{margin-top:auto;border-top:1px solid rgba(255,255,255,.35);padding-top:12px}
.ba .disc{font-family:'Plus Jakarta Sans',Inter,sans-serif;font-size:14px;font-weight:800;line-height:1.25;margin-bottom:10px}
.ba .sp-cq{display:flex;justify-content:space-between;align-items:flex-end;gap:8px}
.ba .sp-cq .ctv{font-size:11px}
.ba .sp-cq .cts.stack .ctl{width:38px;flex-basis:38px}
.ba .mn{flex:1;padding:24px 26px 18px;display:flex;flex-direction:column;justify-content:space-between;gap:12px;min-width:0}
.ba .mn .m-tms{flex:0 0 auto}

/* ============ EDITION B ============ */
.fb .fb-top,.bb .bb-top{flex:1;display:flex;min-height:0}
.fb .sp,.bb .sp{flex:0 0 34%;background:#DFC5EE;padding:26px 22px 20px;display:flex;flex-direction:column}
.fb .sp .logo{height:40px;margin-bottom:26px}
.fb .sp .sec{margin-bottom:26px}
.fb .sp h3::before{background:#111}
.fb .sp .bl li::before{background:#111}
.fb .sp .sec:last-child,.bb .sp .sec:last-child{margin-top:auto;margin-bottom:6px}
.fb .llist{display:flex;flex-direction:column;gap:13px}
.fb .ll{border-top:1px solid rgba(17,17,17,.28);padding-top:8px}
.fb .ll .la{color:#2c2634}
.fb .mn{flex:1;padding:30px 28px 18px;display:flex;flex-direction:column;min-width:0}
.fb h1{font-size:33px;line-height:1.04;font-weight:800;letter-spacing:-.035em}
.fb .mn .sub{font-size:14px;margin-top:9px}
.fb .mn .intro{margin-top:12px}
.fb .mn .pill{margin-top:14px}
.fb .ph{margin:18px 0 18px;border-radius:200px 200px 6px 6px;overflow:hidden;flex:1;min-height:300px;background:var(--lav)}
.fb .ph img{width:100%;height:100%;object-fit:cover;object-position:60% 35%}
.fb .two{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.fb .bar,.bb .bar{flex:0 0 10.4%}
.fb .bar-t{flex:0 0 132px}

.bb .sp .logo{height:38px;margin-bottom:20px}
.bb .sp h1{color:#111}
.bb .sp .sub{margin-top:8px;color:#111}
.bb .sp hr{background:#111;opacity:.45;margin:14px 0}
.bb .sp .sec{margin-bottom:26px}
.bb .sp .sec p{color:#1c1823}
.bb .sp .stat{color:#111}
.bb .mn{flex:1;padding:20px 26px 8px;display:flex;flex-direction:column;justify-content:space-between;gap:10px;min-width:0}
.bb .fn{padding:6px 24px 8px}
.bb .bar{flex:0 0 9%}
.bb .bar-t{flex:0 0 180px}
.bb .bar .bt1{font-size:12.5px;line-height:1.25}
.bb .cts{gap:22px}
.bb .ctv{font-size:12.5px}
.k2{display:block}
[data-ket="1"] .k2{display:none!important}
[data-ket="2"] .k1{display:none!important}
"""
