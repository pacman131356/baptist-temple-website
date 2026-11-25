#!/usr/bin/env python3
"""Builds the Baptist Temple concept preview: one shared header/footer, one folder per page.
Run: python3 build.py   (writes index.html files; no other dependencies)"""
import os, html, re

CDN = "https://images.squarespace-cdn.com/content/v1/69c2f93f5ac9211335b03425/"
def img(path, w=1500): return f"{CDN}{path}?format={w}w"

IMG = {
    "logo": CDN + "d2fd2b12-c2a1-4f72-b96d-07d4c56fd907/Baptist+Temple.png?format=750w",
    "mark": img("af8a34e6-af14-48a3-8293-bb2dea45f3d1/BT.png", 300),
    "worship": img("e378b8b1-31d3-4c08-afa0-35310423bd89/IMG_6968.jpg", 1500),
    "worship_wide": img("e378b8b1-31d3-4c08-afa0-35310423bd89/IMG_6968.jpg", 2500),
    "preach": img("cd1e4a0b-e41f-4de5-9050-74a3e52968cd/IMG_7106.jpg", 2500),
    "lectern": img("6e0050a5-a156-40ac-9248-0c06280ac3d4/IMG_6993.jpg"),
    "aerial": img("bd5d86e3-f96b-4fd8-9ca3-9ea1f11c6f39/491735833_980411590846482_4012375894134007581_n+%281%29.jpg", 2500),
    "front": img("2aa5b4b6-ad73-4204-af04-d59a00751541/DJI_0424.00_01_05_51.Still002.jpg", 2500),
    "class": img("06d5e5ef-516a-4042-9139-da05cfe2dbb7/IMG_6753.jpg"),
    "kids": img("94f6acde-113e-4453-ae8d-3a871a573c6c/IMG_6888.jpg"),
    "students": img("d96848c5-23ad-4f12-8b57-4769f52632f8/IMG_5848.jpg"),
    "adults": img("2e4fc092-c417-41e5-ba21-1470e12860fb/IMG_6673.jpg"),
    "coffee": img("8f2c42c4-ee3f-480e-bc2a-cd5545440b89/IMG_6537.jpg"),
    "boy": img("e3d21c45-2af9-4c28-93d2-de2113e31e56/IMG_6657.jpg"),
    "ss": img("8a7ea41b-2a96-48a9-882c-54d776501e9c/IMG_6686.jpg"),
    "kids_wing": img("ab1c47e3-beff-4fee-9a3f-39dbe6578914/IMG_6861.jpg", 2500),
    "stu_hero": img("c07a9fee-08c5-4567-b940-0565759b2cad/IMG_6802.jpg", 2500),
    "p_ss": img("25643c34-7deb-4916-bfea-d50b1383e64f/priscilla-du-preez--mCXEsLd2sU-unsplash.jpg"),
    "p_kc": img("f3d977f8-3d03-4ac1-a53b-d6e30e2194fe/jesus-loves-austin-TqHDqXkWSCk-unsplash.jpg"),
    "p_vbs": img("ce2c9cdf-5f4c-4ea9-8eed-35e77990adef/erika-giraud-4EFeD-VTgu4-unsplash.jpg", 2500),
    "p_tk": img("6f177715-7f72-401d-9c62-b469069b9b12/IMG_6869.jpg"),
    "p_sum": img("e0cf7c91-954b-4948-9468-33e707481973/artem-kniaz-DqgMHzeio7g-unsplash.jpg"),
}

# Where the faces are in each photo (object-position), so crops never cut them off.
FOCUS = {
    "IMG_6968": "47% 40%", "IMG_7106": "53% 42%", "IMG_6993": "40% 24%", "IMG_6753": "55% 28%",
    "IMG_5848": "55% 14%", "IMG_6673": "62% 32%", "IMG_6537": "90% 26%", "IMG_6657": "37% 70%",
    "IMG_6802": "50% 32%", "priscilla-du-preez": "80% 22%", "jesus-loves-austin": "70% 18%",
    "erika-giraud": "58% 12%", "artem-kniaz": "50% 58%", "IMG_6869": "62% 50%", "IMG_6888": "70% 35%",
}
def apply_focus(doc):
    def fix(m):
        tag = m.group(0)
        key = next((k for k in FOCUS if k in tag), None)
        if not key: return tag
        pos = FOCUS[key]
        if "object-position:" in tag: return re.sub(r"object-position:[^;\"]*", "object-position:" + pos, tag)
        if 'style="' in tag: return tag.replace('style="', f'style="object-position:{pos};', 1)
        return tag[:-1].rstrip("/").rstrip() + f' style="object-position:{pos}">'
    return re.sub(r"<img\b[^>]*>", fix, doc)
GIVE = "https://giving.myamplify.io//app/giving/temple"
FB = "https://www.facebook.com/connersvillebt/"
YT = "https://www.youtube.com/@ConnersvilleBaptistTemple/featured"
YT_LIVE = "https://www.youtube.com/@ConnersvilleBaptistTemple/streams"
APP_IOS = "https://apps.apple.com/app/id1644388825"
APP_AND = "https://play.google.com/store/apps/details?id=com.ministrybrands.easytithepro"
ADDR = "1380 IN-44, Connersville, IN 47331"
MAPS = "https://www.google.com/maps/search/?api=1&query=Baptist+Temple+1380+IN-44+Connersville+IN+47331"
MAP_EMBED = "https://www.google.com/maps?q=Baptist+Temple,+1380+IN-44,+Connersville,+IN+47331&output=embed"
PHONE, PHONE_TEL, EMAIL = "765-825-5196", "+17658255196", "staff@baptist-temple.com"

ICON = {
 "fb": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9h3l.5-4h-3.5V8.9c0-.6.4-.9 1-.9z"/></svg>',
 "yt": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.8 15.1V8.9L15.5 12l-5.7 3.1z"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "play": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "chev": '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
}

NAV = [
    ("About", [("Our Story &amp; Beliefs", "/about/"), ("Our Team", "/staff/")]),
    ("Ministries", [("Kids", "/kids/"), ("Students", "/students/"), ("Sunday School", "/sunday-school/"), ("Adults &amp; Outreach", "/ministries/")]),
    ("Watch", "/watch/"),
    ("Plan a Visit", "/plan-a-visit/"),
    ("Contact", "/contact/"),
]

def header(current):
    items, mob = [], []
    for i, (label, target) in enumerate(NAV):
        if isinstance(target, list):
            links = "".join(f'<a href="{h}">{t}</a>' for t, h in target)
            items.append(f'<div class="nav-group"><button type="button" aria-expanded="false" aria-controls="m{i}">{label} {ICON["chev"]}</button><div class="menu" id="m{i}" hidden>{links}</div></div>')
            mob.append(f'<details><summary>{label}</summary>{links}</details>')
        else:
            items.append(f'<a href="{target}">{label}</a>')
            mob.append(f'<a href="{target}">{label}</a>')
    mob.append(f'<a href="{GIVE}">Give</a>')
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="ribbon">Concept preview prepared by <a href="https://holdencreative.co">Holden Creative</a>. Not the official Baptist Temple website.</div>
<header class="nav" id="nav">
  <div class="nav-row">
    <a class="nav-brand" href="/" aria-label="Baptist Temple home"><img class="mark" src="/img/bt-mark.png" alt="" width="46" height="46"><span class="word wordtext">Baptist Temple<small>Connersville</small></span></a>
    <nav class="nav-menu" aria-label="Main">{"".join(items)}</nav>
    <div class="nav-end"><a class="nav-give" href="{GIVE}">Give</a><a class="btn btn-amber" href="/plan-a-visit/">Plan a Visit</a><button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button></div>
  </div>
  <nav class="mobile-menu" id="mobile-menu" aria-label="Mobile">{"".join(mob)}</nav>
</header>"""

FOOTER = f"""<footer class="site-foot">
  <div class="wrap">
    <div class="foot-cta reveal">
      <h2>There's a seat saved <em>for you</em> this Sunday.</h2>
      <div class="btns"><a class="btn btn-amber" href="/plan-a-visit/">Plan a Visit {ICON["arrow"]}</a><a class="btn btn-ghost" href="/watch/">{ICON["play"]} Watch Live</a></div>
    </div>
    <div class="foot-grid">
      <div class="foot-times">
        <img src="{IMG["logo"]}" alt="Connersville Baptist Temple" width="240" height="44" loading="lazy">
        <strong>Sundays 9:30 &amp; 10:30</strong>
        <p>Sunday School at 9:30, Worship at 10:30.<br>On campus and online.</p>
        <div class="social"><a href="{FB}" aria-label="Facebook">{ICON["fb"]}</a><a href="{YT}" aria-label="YouTube">{ICON["yt"]}</a></div>
      </div>
      <div>
        <h4>Visit</h4>
        <ul>
          <li><a href="{MAPS}">1380 IN-44<br>Connersville, IN 47331</a></li>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/plan-a-visit/">Plan a Visit</a></li>
          <li><a href="/about/">Our Story &amp; Beliefs</a></li>
          <li><a href="/staff/">Our Team</a></li>
          <li><a href="/ministries/">Ministries</a></li>
          <li><a href="/watch/">Watch</a></li>
        </ul>
      </div>
      <div>
        <h4>Connect</h4>
        <ul>
          <li><a href="/connect/">Connection Card</a></li>
          <li><a href="/prayer/">Prayer Requests</a></li>
          <li><a href="{GIVE}">Give Online</a></li>
          <li><a href="{APP_IOS}">Church App for iPhone</a></li>
          <li><a href="{APP_AND}">Church App for Android</a></li>
        </ul>
      </div>
    </div>
    <div class="big-word" aria-hidden="true">Baptist Temple</div>
    <div class="foot-bottom">
      <span>&copy; <span id="yr">2026</span> Connersville Baptist Temple</span>
      <span>Concept preview by <a href="https://holdencreative.co">Holden Creative</a></span>
    </div>
  </div>
</footer>"""

def page(path, title, desc, body, current=None):
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0c1621">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{IMG["aerial"]}">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" href="/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,600..900&family=Fraunces:ital,opsz,wght@1,9..144,400..500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://images.squarespace-cdn.com">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
{header(current or path)}
<main id="main">
{body}
</main>
{FOOTER}
<script src="/site.js" defer></script>
</body>
</html>
'''
    out = "index.html" if path == "/" else path.strip("/") + "/index.html"
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w").write(apply_focus(doc))

def page_hero(eyebrow, h1, lede, bg, pos="center"):
    return f'''<section class="page-hero">
  <img class="bg" src="{bg}" alt="" style="object-position:{pos}">
  <div class="wrap">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>'''

TRIO = f"""<section class="section mist">
  <div class="wrap">
    <div class="trio stagger">
      <a class="reveal" href="/prayer/"><h3>Prayer Request</h3><p>Share what's on your heart. Our team would be honored to pray with you.</p><span>Send a request {ICON["arrow"]}</span></a>
      <a class="reveal" href="/plan-a-visit/"><h3>Plan a Visit</h3><p>Know what to expect before you pull in on Sunday morning.</p><span>Start here {ICON["arrow"]}</span></a>
      <a class="reveal" href="/connect/"><h3>Get Connected</h3><p>Joined us in person or online? Let us know and we'll be in touch.</p><span>Fill out a card {ICON["arrow"]}</span></a>
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------- HOME
MARQ = "".join(f'<span>{t}<b></b></span>' for t in ["Sunday School <em>9:30</em>", "Worship <em>10:30</em>", "Coffee &amp; donuts from <em>9:00</em>", "On campus <em>&amp;</em> online", "Everyone is <em>welcome</em>", "Connersville, Indiana"])
page("/", "Baptist Temple · Connersville, Indiana · Sundays 9:30 & 10:30",
 "Connersville Baptist Temple: a ministry for the whole family. Sunday School at 9:30 AM and Worship at 10:30 AM, on campus and online at 1380 IN-44, Connersville, IN.",
 f"""<section class="hero">
  <div class="hero-bg"><img src="{IMG["worship_wide"]}" alt="" fetchpriority="high"></div>
  <div class="wrap hero-inner">
    <span class="eyebrow" style="color:var(--sky);animation:fade 1s both">Baptist Temple · Connersville, Indiana</span>
    <h1 style="margin-top:22px"><span class="line"><span>A ministry for</span></span><span class="line"><span><span class="rotator" aria-label="the whole family"><span class="on" aria-hidden="true">the whole family.</span><span aria-hidden="true">your kids.</span><span aria-hidden="true">your teens.</span><span aria-hidden="true">every age.</span><span aria-hidden="true">you.</span></span></span></span></h1>
    <p class="hero-sub">Everyone is welcome here. Join us this Sunday on campus off State Road 44, or worship with us online wherever you are.</p>
    <div class="btns"><a class="btn btn-amber" href="/plan-a-visit/">Plan Your Visit {ICON["arrow"]}</a><a class="btn btn-ghost" href="/watch/">{ICON["play"]} Watch Live</a></div>
    <div class="hero-foot">
      <div class="hero-times"><div>Sunday School<strong>9:30 AM</strong></div><div>Worship<strong>10:30 AM</strong></div><div>Online<strong>Facebook &amp; YouTube</strong></div></div>
      <a class="scroll-cue" href="#sundays"><i></i>Scroll</a>
    </div>
  </div>
</section>
<div class="marquee" aria-hidden="true"><div class="marquee-track">{MARQ}{MARQ}</div></div>

<section class="section" id="sundays">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Your first Sunday</span><h2>Here's how a Sunday <em>morning</em> flows.</h2></div><a class="btn btn-line" href="/plan-a-visit/">What to expect {ICON["arrow"]}</a></div>
    <div class="timeline">
      <div class="stop"><div class="t">9:00<small>AM</small></div><h3>Coffee &amp; donuts</h3><p>Free in the café until 10:30. Stop by the Welcome Center and say hi.</p></div>
      <div class="stop"><div class="t">9:30<small>AM</small></div><h3>Sunday School</h3><p>Classes for every age, from the nursery to adults, all across campus.</p></div>
      <div class="stop"><div class="t">10:30<small>AM</small></div><h3>Worship</h3><p>Blended worship and Bible-centered preaching, plus Kids Church. About an hour.</p></div>
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <span class="eyebrow" style="color:var(--sky)">Everyone is welcome</span>
    <p class="statement" style="margin-top:22px"><span data-words>No matter your age, your story, or where you've been, you have a</span> <em data-words>place here.</em> <span data-words>Come as you are. Wear what's comfortable. We'd love to meet you.</span></p>
  </div>
</section>

<section class="section mist">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow">Something for everyone</span><h2>Ministry for every <em>age</em> and stage.</h2></div>
      <a class="btn btn-line" href="/ministries/">All ministries {ICON["arrow"]}</a>
    </div>
    <div class="bento">
      <a class="tile" href="/sunday-school/"><img src="{IMG["class"]}" alt="Adults taking notes during a Sunday School class" loading="lazy"><div class="tile-body"><div><small>Sundays · 9:30</small><h3>Sunday School</h3></div><span class="go">{ICON["arrow"]}</span></div></a>
      <a class="tile" href="/kids/"><img src="{IMG["p_vbs"]}" alt="Kids raising their hands during a Bible lesson" loading="lazy"><div class="tile-body"><div><small>Birth to 6th grade</small><h3>Kids</h3></div><span class="go">{ICON["arrow"]}</span></div></a>
      <a class="tile" href="/students/"><img src="{IMG["students"]}" alt="A student playing air hockey in the youth room" loading="lazy"><div class="tile-body"><div><small>7th to 12th grade</small><h3>Students</h3></div><span class="go">{ICON["arrow"]}</span></div></a>
      <a class="tile" href="/ministries/"><img src="{IMG["adults"]}" alt="Adults studying their Bibles together around a table" loading="lazy" style="object-position:center 40%"><div class="tile-body"><div><small>Groups, missions &amp; outreach</small><h3>Adults &amp; Outreach</h3></div><span class="go">{ICON["arrow"]}</span></div></a>
    </div>
  </div>
</section>

<section class="watch">
  <div class="bg" data-parallax><img src="{IMG["preach"]}" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="watch-copy reveal">
      <span class="live"><i></i>Live Sundays at 10:30</span>
      <h2>Church that goes <em>wherever</em> you go.</h2>
      <p>Can't make it in person? Worship with us live on Facebook and YouTube, or catch up on past messages anytime.</p>
      <div class="btns"><a class="btn btn-white" href="/watch/">{ICON["play"]} Watch Live</a><a class="btn btn-ghost" href="{YT}">Past Messages</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Plan your visit</span><h2>On the east side of <em>Connersville</em>.</h2></div></div>
    <div class="visit">
      <div class="visit-photo reveal"><img src="{IMG["aerial"]}" alt="Aerial view of the Baptist Temple building and parking lot on State Road 44" loading="lazy"><span class="pin">{ICON["pin"]}Guest parking by the main entrance</span></div>
      <div class="visit-card reveal">
        <h2>We saved you a <em>seat.</em></h2>
        <div class="info">
          <div>{ICON["clock"]}<span><small>Sundays</small>Sunday School 9:30 AM<br>Worship Service 10:30 AM</span></div>
          <div>{ICON["pin"]}<span><small>Address</small><a href="{MAPS}">1380 IN-44<br>Connersville, IN 47331</a></span></div>
          <div>{ICON["phone"]}<span><small>Phone</small><a href="tel:{PHONE_TEL}">{PHONE}</a></span></div>
          <div>{ICON["mail"]}<span><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></span></div>
        </div>
        <div class="btns"><a class="btn btn-amber" href="/plan-a-visit/">Plan a Visit</a><a class="btn btn-ghost" href="{MAPS}">Directions</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section mist">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Many members, one body</span><h2>Take your next <em>step.</em></h2></div></div>
    <div class="trio stagger">
      <a class="reveal" href="/prayer/"><h3>Prayer Request</h3><p>Share what's on your heart. Our team would be honored to pray with you.</p><span>Send a request {ICON["arrow"]}</span></a>
      <a class="reveal" href="/plan-a-visit/"><h3>Plan a Visit</h3><p>Know what to expect before you pull in on Sunday morning.</p><span>Start here {ICON["arrow"]}</span></a>
      <a class="reveal" href="/connect/"><h3>Get Connected</h3><p>Joined us in person or online? Let us know and we'll be in touch.</p><span>Fill out a card {ICON["arrow"]}</span></a>
    </div>
  </div>
</section>""")

# ---------------------------------------------------------------- PLAN A VISIT
page("/plan-a-visit/", "Plan a Visit · Baptist Temple, Connersville",
 "What to expect on your first Sunday at Baptist Temple: times, parking, kids, dress, and where to go.",
 page_hero("Plan a visit", "Trying a new church can be stressful. We want to <em>help.</em>",
  "Here's everything you need to know before your first Sunday, from where to park to what your kids will do.", IMG["front"]) + f'''
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Sunday schedule</span><h2>Here's how Sunday mornings work.</h2></div></div>
    <div class="table-wrap reveal"><table class="schedule">
      <thead><tr><th>Time</th><th>What's happening</th><th>Where</th></tr></thead>
      <tbody>
        <tr><td>9:00 to 10:30 AM</td><td>Free coffee and donuts</td><td>Café, main building</td></tr>
        <tr><td>9:30 AM</td><td>Sunday School for all ages</td><td>Across campus. Greeters can point you to a class.</td></tr>
        <tr><td>10:30 AM</td><td>Worship Service (usually a little over an hour)</td><td>Worship Center, main building</td></tr>
        <tr><td>10:30 AM</td><td>Kids Church for elementary ages</td><td>Family Life Center</td></tr>
        <tr><td>All services</td><td>Nursery for ages 0 to 3</td><td>Main building, off the lobby</td></tr>
      </tbody>
    </table></div>
  </div>
</section>

<section class="section mist">
  <div class="wrap split">
    <div class="reveal photo-wrap"><img class="photo" src="{IMG["lectern"]}" alt="Pastor preaching from the lectern during a Sunday service" loading="lazy"></div>
    <div class="reveal">
      <span class="eyebrow">What to expect</span>
      <h2>Family-friendly, Bible-centered, and relaxed.</h2>
      <ul class="checks">
        <li><b>Preaching</b> is Bible-centered and practical. Bring a Bible, or grab a free one at the Welcome Center.</li>
        <li><b>Worship</b> is blended: contemporary songs and fresh arrangements of hymns, led by a band and singers.</li>
        <li><b>No offering plates.</b> Offering boxes are in the lobby and Welcome Center. Guests are never expected to give.</li>
        <li><b>Dress</b> is mostly casual or business casual. Your being here matters more than what you wear.</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cards stagger">
      <div class="card reveal"><span class="when">Parking</span><h3>Reserved for guests</h3><p>First-time guest spaces are right by the main entrance, with handicap parking nearby.</p></div>
      <div class="card reveal"><span class="when">Kids</span><h3>Safe and fun</h3><p>Nursery during all services, Sunday School at 9:30, and Children's Church at 10:30. Every worker is a screened and trained adult.</p></div>
      <div class="card reveal"><span class="when">Arriving</span><h3>Come a few minutes early</h3><p>Give yourself time to park and find your way. Greeters will help you find a Sunday School class for your family.</p></div>
      <div class="card reveal"><span class="when">Wednesdays</span><h3>Kids &amp; teens</h3><p>Temple Kids and the Teen Ministry meet Wednesday nights in the Family Life Center.</p></div>
    </div>
  </div>
</section>

<section class="section mist">
  <div class="wrap split flip">
    <div class="reveal"><iframe class="map" src="{MAP_EMBED}" title="Map to Baptist Temple" loading="lazy" referrerpolicy="no-referrer-when-downgrade" style="min-height:380px"></iframe></div>
    <div class="reveal">
      <span class="eyebrow">Finding us</span>
      <h2>East side of Connersville, off State Road 44.</h2>
      <p class="lede">1380 IN-44, Connersville, IN 47331</p>
      <ul class="checks">
        <li><b>Main building:</b> Worship Center, café, classrooms, and church offices.</li>
        <li><b>Family Life Center:</b> Temple Kids, children's Sunday School rooms, Team K.I.D., the gym, kitchen, and Teen Ministry.</li>
      </ul>
      <div class="btns" style="margin-top:26px"><a class="btn btn-blue" href="{MAPS}">Get Directions</a><a class="btn btn-line" href="tel:{PHONE_TEL}">Call {PHONE}</a></div>
    </div>
  </div>
</section>
''' + TRIO)

# ---------------------------------------------------------------- ABOUT / BELIEFS
BELIEFS = [
 ("God", "There is one God, eternally existing in three equal persons: Father, Son, and Holy Spirit. He is the Creator, unchanging, holy, loving, merciful, and just, and He will judge the world."),
 ("The Bible", "The Old and New Testaments were written by men inspired by the Holy Spirit. The Bible is God's revelation of Himself, completely true and trustworthy, and all of it points to Jesus Christ."),
 ("Man", "People were created in God's image and without sin. Through Adam's fall, sin and spiritual death passed to all humanity, so no one can come to God apart from His grace."),
 ("Jesus", "Jesus is the eternal Son of God, fully God and fully man, born of the Virgin Mary. He died on the cross in our place, rose bodily from the dead, ascended to heaven, and will return to judge and reign."),
 ("The Holy Spirit", "The Holy Spirit is fully God. He inspired Scripture, exalts Christ, and convicts the world. He brings new birth, places believers into the body of Christ, seals, sanctifies, and comforts them, and gives spiritual gifts to the church."),
 ("Salvation", "Salvation redeems the whole person and is offered freely to all who repent and trust in Jesus. It is by grace alone, through faith alone, in Christ alone."),
 ("Assurance of Believers", "Those who are truly redeemed are kept secure in Christ forever by God's power. Salvation can't be earned or lost by what we do, and that assurance leads to joyful obedience."),
 ("The Church", "The church is the body and bride of Christ, made up of all believers with Jesus as its head. Local churches are independent and led by pastors under Christ's authority, and observe two ordinances: believer's baptism and the Lord's Supper. Our mission is to share the gospel with every nation, starting with our neighbors."),
]
acc = "".join(f'<details><summary>{t}</summary><div><p>{d}</p></div></details>' for t, d in BELIEFS)
page("/about/", "Our Story & Beliefs · Baptist Temple, Connersville",
 "Baptist Temple's mission, vision, and statement of faith: deepening faith, maturing in Christ, and reaching our community.",
 page_hero("About us", "A ministry for the <em>whole family.</em>",
  "We're committed to serving and nurturing every member, so our ministry supports the spiritual journey of every age.", IMG["aerial"]) + f'''
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Our mission</span><h2>Three things we're about.</h2></div></div>
    <div class="steps stagger">
      <div class="step reveal"><h3>Deepening faith</h3><p>Growing in our knowledge of God's Word and how to live it out.</p></div>
      <div class="step reveal"><h3>Maturing in Christ</h3><p>Becoming committed, growing followers of Jesus.</p></div>
      <div class="step reveal"><h3>Community outreach</h3><p>Meeting the physical and spiritual needs of Connersville and leading people to a relationship with Jesus Christ.</p></div>
    </div>
  </div>
</section>

<section class="section mist" id="beliefs">
  <div class="wrap split" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">What we believe</span>
      <h2>Our statement of faith.</h2>
      <p class="lede">Questions about anything here? We'd love to talk with you.</p>
      <div class="btns" style="margin-top:24px"><a class="btn btn-blue" href="/contact/">Contact Us</a><a class="btn btn-line" href="/plan-a-visit/">Plan a Visit</a></div>
    </div>
    <div class="acc reveal">{acc}</div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal photo-wrap"><img class="photo" src="{IMG["coffee"]}" alt="A church member serving coffee and donuts in the café" loading="lazy"></div>
    <div class="reveal">
      <span class="eyebrow">Our team</span>
      <h2>Meet the people who serve here.</h2>
      <p class="lede">From our pastors to the folks who keep the building running, get to know the team behind Baptist Temple.</p>
      <a class="btn btn-blue" href="/staff/" style="margin-top:12px">Meet Our Team {ICON["arrow"]}</a>
    </div>
  </div>
</section>''')

# ---------------------------------------------------------------- STAFF
STAFF = [
 ("Joe Ferreira", "Senior Pastor", "0659f722-96d6-4502-bf2c-88f30c6c3573/Joe+Ferriera.jpeg",
  "Pastor Joe and his wife Darcie came to Connersville in October 2017 after more than 20 years at their church in Tampa, Florida. Joe came to faith while serving in the U.S. Air Force and soon left the military for full-time ministry. They have two sons, Jason and Justin."),
 ("Ethan Rogers", "Youth Pastor", "486053c5-0789-4976-8ff2-3329dce2e8a8/Ethan+Rogers.jpeg",
  "Ethan and his wife Joy moved to Connersville in January 2024. He grew up in Indiana and holds bachelor's and master's degrees in Pastoral Studies from Moody Bible Institute."),
 ("Joy Rogers", "Children's Director", "04ca47a3-3ef4-4b2c-bb1e-ac4c829284ee/Joy+Rogers.jpeg",
  "Joy directs Sunday Kids Ministry and plans the curriculum for kindergarten through 6th grade."),
 ("Deborah Huff", "Children's Director", "cfc815bb-a98b-4170-8c2a-ba25d51d1a53/Deborah+Huff.jpeg",
  "Deb has taught Sunday School, children's church, Awana, and Sunday Night Kids for 40 years. She coordinates the Wednesday night Children's Program."),
 ("Andy Boger", "Music Director", "03be1439-bc2c-4786-a967-5a7ba6d620f3/Andy+Boger.jpeg",
  "A lifelong Connersville resident, Andy began serving at Baptist Temple in May 2024 and has led worship for more than 25 years."),
 ("Abby Howard", "Music Director", "a4c3d955-5425-4130-87d0-1dec820b7c85/Abby+Howard.jpeg",
  "Abby grew up in Connersville and began serving at Baptist Temple in May 2024. She and her husband Tim have three children."),
 ("Jeremy Mullins", "Facilities Manager", "9f6ac629-ccc7-43f4-afa9-ab8e513bfc56/Jeremy+Mullins.jpeg",
  "Jeremy has served as facilities manager since November 2023 and grew up in the Connersville area."),
 ("Traci Garrison", "Financial Secretary", "07ba6013-4821-4f07-a845-49da24aebf7e/Traci+Garrison.jpeg",
  "Traci joined the team in October 2022 after more than 30 years in ministry, including 17 as a missionary in the Dominican Republic."),
 ("Janet Martin", "Church Secretary", "56cb8251-4a69-471c-bde8-546acd0b70af/Janet+Martin.jpeg",
  "Janet has served on staff since April 2010, supporting the church staff and its ministries."),
 ("Kara DeBoard", "Janitorial Staff", "d672ef90-f427-43ef-92aa-a2e3a851a741/Kara+DeBoard.jpeg", ""),
 ("Heather Boger", "Janitorial Staff", "9a39163f-d1ca-4455-80df-d3c6b0029425/Heather+Boger.jpeg", ""),
]
cards = []
for i, (name, role, p, bio) in enumerate(STAFF):
    cls = "person lead" if i == 0 else "person"
    w = 1000 if i == 0 else 600
    cards.append(f'<article class="{cls} reveal"><div class="ph"><img src="{img(p, w)}" alt="{name}, {role}" loading="lazy"></div><div class="person-body"><h3>{name}</h3><div class="role">{role}</div>{f"<p>{bio}</p>" if bio else ""}</div></article>')
page("/staff/", "Our Team · Baptist Temple, Connersville",
 "Meet the pastors and staff of Baptist Temple in Connersville, Indiana.",
 page_hero("Our team", "The people who <em>serve</em> at Baptist Temple.",
  "Have a question for someone on our team? Email the office and we'll get it to the right person.", IMG["worship"], "center 30%") + f'''
<section class="section">
  <div class="wrap"><div class="team stagger">{"".join(cards)}</div>
  <p class="form-note" style="margin-top:28px">Reach any of our staff at <a href="mailto:{EMAIL}">{EMAIL}</a> or {PHONE}.</p></div>
</section>''')

# ---------------------------------------------------------------- KIDS
PICO = {
 "safe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V6z"/><path d="M8.8 12.2l2.2 2.2 4.4-4.6"/></svg>',
 "fun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8.5 14.5c.9 1.3 2.1 2 3.5 2s2.6-.7 3.5-2"/><path d="M9 9.5h.01M15 9.5h.01" stroke-width="2.6"/></svg>',
 "gospel": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 19.5V5.5"/><path d="M12 7v7M9.5 9.5h5"/></svg>',
 "talk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h12v8H9l-4 3v-3H4z"/><path d="M16 9h4v8h-1v3l-4-3h-4v-2"/></svg>',
}
def pillars(items):
    return '<div class="pillars stagger">' + "".join(
        f'<div class="pillar reveal"><span class="p-ico">{PICO[ic]}</span><span class="p-label">{i:02d} · {lab}</span><h3>{h}</h3><p>{t}</p></div>'
        for i, (ic, lab, h, t) in enumerate(items, 1)) + '</div>'
def programs(items):
    return '<div class="programs stagger">' + "".join(
        f'<article class="prog{" big" if big else ""} reveal"><div class="ph"><img src="{src}" alt="{alt}" loading="lazy"><span class="chip">{when}</span></div><div class="body"><h3>{h}</h3><p>{t}</p></div></article>'
        for big, src, alt, when, h, t in items) + '</div>'

page("/kids/", "Kids · Baptist Temple, Connersville",
 "Temple Kids at Baptist Temple: Sunday School, Kids Church, Wednesday nights, and VBS for kids from birth through 6th grade.",
 page_hero("Temple Kids · Birth to 6th grade", "The best part of <em>their week.</em>",
  "A place where your child can laugh and play, learn and grow, make friends, and most importantly, discover God's great love for them.", IMG["p_sum"].replace("format=1500w","format=2500w")) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Why parents love it</span><h2>Fun, safe, and <em>relational.</em></h2><p class="lede">Our goal is to make Sundays and Wednesdays the best days of your child's week, so they can meet Jesus on their level.</p></div></div>
    {pillars([
      ("safe", "Safe", "Secure check-in", "Every child is checked in with a matching pick-up receipt. Volunteers are highly trained and screened with several background checks, and our safety team routinely patrols the building."),
      ("fun", "Fun", "Joy you can hear", "We find our joy in Jesus, so we put a big emphasis on fun. Songs, games, crafts, and lessons all teach kids about God and His love for them."),
      ("gospel", "Gospel-focused", "Jesus at the center", "We gather to worship the God who wants a relationship with us, and we make sure your child understands that every Sunday they're with us."),
    ])}
  </div>
</section>
<section class="section mist">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Our kids programs</span><h2>Something every <em>week of the year.</em></h2></div></div>
    {programs([
      (True, IMG["p_ss"], "A child reading a Bible with a teacher", "Sundays · 9:30 AM", "Sunday School", "Age-based classes from the nursery through 6th grade, in kid-friendly rooms in the main building and the Family Life Center."),
      (True, IMG["p_kc"], "A girl playing a game at a table during Kids Church", "Sundays · 10:30 AM", "Kids Church", "For elementary-age kids. We meet in the Temple Kids Room during the morning service for our own worship, Bible study, games, and more."),
      (False, IMG["p_tk"], "The Temple Kids sign in the kids wing", "Wednesdays · 6:30 PM", "Temple Kids", "During the school year, 6:30 to 8:00 PM: a free dinner every week, plus lessons, games, crafts, Bible memory, and more."),
      (False, IMG["p_sum"], "Kids playing with a colorful parachute outside", "Summers · 6:30 PM", "Summer Programs", "When Temple Kids is on break for the summer, we keep the fun going with other kids activities from 6:30 to 8:00 PM."),
      (False, IMG["p_vbs"], "Kids raising their hands during Vacation Bible School", "Summers · Usually July", "Vacation Bible School", "A fun-packed week of music, games, Bible study, crafts, skits, and so much more. Get ready for a wild week every summer."),
    ])}
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="reveal photo-wrap"><img class="photo" src="{IMG["boy"]}" alt="A baby playing with toys in the nursery" loading="lazy"></div>
    <div class="reveal"><span class="eyebrow">First time?</span><h2>We'll help you get checked in.</h2><p class="lede">Arrive a few minutes early and a greeter will walk you to the right room. The nursery is in the main building, off the lobby.</p><a class="btn btn-blue" href="/plan-a-visit/">Plan a Visit {ICON["arrow"]}</a></div>
  </div>
</section>""")

# ---------------------------------------------------------------- STUDENTS
page("/students/", "Students · Baptist Temple, Connersville",
 "Student ministry for 7th through 12th grade at Baptist Temple: Wednesdays 6:30 to 8:30 PM.",
 page_hero("Students · 7th to 12th grade", "Christ-centered <em>difference makers.</em>",
  "From the fun lessons to the crazy games, everything we do is about helping students follow Jesus and make a difference.", IMG["stu_hero"]) + f"""
<section class="facts-band">
  <div class="wrap">
    <div class="facts reveal">
      <div class="fact"><small>Wednesdays</small><strong>6:30<span>&ndash;</span>8:30 PM</strong></div>
      <div class="fact"><small>Grades</small><strong>7th<span>&ndash;</span>12th</strong></div>
      <div class="fact"><small>Every week</small><strong>Games · Food · Lessons</strong></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">What to expect</span><h2>A place to be <em>yourself.</em></h2></div></div>
    {pillars([
      ("safe", "Safe", "Screened leaders", "Your student's safety is one of our highest priorities. Every volunteer who works with students goes through screening and follows the church's protection policies."),
      ("fun", "Fun", "Crazy games, real joy", "We find our joy in Jesus, so fun is a big deal here. Through games and lessons, students learn about God and His love for them."),
      ("talk", "Authentic", "Real life, real faith", "Students deal with a lot in today's culture. We work to create an authentic space where they can be themselves and grow in Christ together."),
    ])}
  </div>
</section>
<section class="section mist">
  <div class="wrap split">
    <div class="reveal"><span class="eyebrow">Sunday mornings</span><h2>The Orchard</h2><p class="lede">Our Sunday School class for grades 7 to 12 meets at 9:30 AM in the Youth Room (FLC Room 202), led by Youth Pastor Ethan Rogers.</p><a class="btn btn-blue" href="/staff/">Meet Pastor Ethan {ICON["arrow"]}</a></div>
    <div class="reveal photo-wrap"><img class="photo" src="{IMG["students"]}" alt="A student playing air hockey in the youth room" loading="lazy"></div>
  </div>
</section>""")

# ---------------------------------------------------------------- SUNDAY SCHOOL
rows_adult = [("Adult Bible Class", "Adults and senior adults", "Dan Cline", "Worship Center, main building"),
              ("Learning to Live", "Adults of all ages and life stages", "Pastor Joe Ferreira", "Room 130, main building"),
              ("Ambassadors Class", "Mixed adults", "Mark George &amp; Boyd Huff", "Room 120, main building")]
rows_kids = [("Nursery", "Infants and one-year-olds", "Sam &amp; Tiffany Tuttle", "Room 106, main building"),
             ("2's &amp; 3's", "Ages 2 and 3", "Monica Boger, Aaron &amp; Tracy Geist", "Room 108, main building"),
             ("K to 2nd Grade", "Kindergarten to 2nd grade", "Frances Zimmerman, Dale &amp; Vicki Carpenter", "FLC Room 306"),
             ("3rd to 6th Grade", "Grades 3 to 6", "Joy Rogers", "FLC Room 302"),
             ("The Orchard", "Grades 7 to 12", "Ethan Rogers, Youth Pastor", "Youth Room, FLC Room 202")]
def trows(rows): return "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows)
page("/sunday-school/", "Sunday School · Baptist Temple, Connersville",
 "Sunday School at Baptist Temple: classes for kids, students, and adults every Sunday at 9:30 AM.",
 page_hero("Sundays · 9:30 AM", "A class for <em>every age.</em>",
  "Classes meet across campus before the worship service. Greeters at the main entrances and Welcome Center can point you to the right room.", IMG["class"]) + f'''
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Adults</span><h2>Adult classes</h2></div></div>
    <div class="table-wrap reveal"><table class="schedule"><thead><tr><th>Class</th><th>Who it's for</th><th>Teachers</th><th>Room</th></tr></thead><tbody>{trows(rows_adult)}</tbody></table></div>
  </div>
</section>
<section class="section mist">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Kids &amp; students</span><h2>Classes for kids and students</h2><p class="lede">Children's and youth rooms are in the Family Life Center (FLC), next to the main building. The nursery and 2's &amp; 3's are in the main building.</p></div></div>
    <div class="table-wrap reveal"><table class="schedule"><thead><tr><th>Class</th><th>Who it's for</th><th>Teachers</th><th>Room</th></tr></thead><tbody>{trows(rows_kids)}</tbody></table></div>
  </div>
</section>''' + TRIO)

# ---------------------------------------------------------------- MINISTRIES
MIN_GROW = [
 ("Worship", "Sundays, 10:30 AM", "Biblically centered, Christ-honoring music in a blended style of contemporary and traditional songs."),
 ("Joshua's Men", "Saturdays, 7 AM", "A men's discipleship group with a verse-by-verse Bible study, building godly men who lead their families and church."),
 ("Women's Ministry", "", "Connecting women to Jesus and to one another through conferences, crafting, Bible studies, and fellowship and service events. All women are welcome."),
 ("Senior Adults", "", "Events and activities for senior adults. Check the bulletin or call the church office for what's coming up."),
 ("Sonshiner's", "Sundays, 10:30 AM · Room 113", "A class for adults with special needs: Bible verses, trivia with prizes, prayer, singing, and refreshments. Anyone is welcome to join."),
]
MIN_SERVE = [
 ("Community Outreach", "", "A food pantry (bring donations to the church office), Friends of the Lord's Table serving meals two Monday nights a month, and Mats for the Homeless on Tuesdays and Thursdays at 1 PM, January through April."),
 ("International Missions", "", "Spreading the gospel locally and around the world and supporting missionary families. See the weekly Missionary Spotlight in the bulletin."),
 ("Video &amp; Live Streaming", "Every Sunday", "Our T3 team streams worship each week so people who can't be there in person can still worship and study with us."),
 ("Bus &amp; Van Ministry", "Call to schedule", "Need a ride to church? Call the office and we'll arrange a pickup."),
]
def mrows(items, start):
    out = []
    for i, (t, w, d) in enumerate(items, start):
        meta = f'<span class="m-when">{w}</span>' if w else ''
        out.append(f'<li class="m-row reveal"><span class="m-num">{i:02d}</span><div class="m-head"><h3>{t}</h3>{meta}</div><p>{d}</p></li>')
    return "".join(out)
page("/ministries/", "Ministries · Baptist Temple, Connersville",
 "Adult ministries and community outreach at Baptist Temple: men's and women's ministries, senior adults, Sonshiner's, missions, and more.",
 page_hero("Adults &amp; outreach", "Find your people. <em>Serve your neighbors.</em>",
  "There's a place for you to grow and serve at Baptist Temple. For details, call the church office or check the weekly bulletin.", IMG["adults"]) + f'''
<section class="section">
  <div class="wrap">
    <div class="m-group">
      <div class="m-side"><span class="eyebrow">For adults</span><h2>Grow <em>together.</em></h2><p>Groups and classes for every season of life.</p></div>
      <ol class="m-list">{mrows(MIN_GROW, 1)}</ol>
    </div>
    <div class="m-group">
      <div class="m-side"><span class="eyebrow">Outreach</span><h2>Reach <em>out.</em></h2><p>Ways we care for Connersville and the world.</p></div>
      <ol class="m-list">{mrows(MIN_SERVE, len(MIN_GROW)+1)}</ol>
    </div>
  </div>
</section>
<section class="section mist">
  <div class="wrap split">
    <div class="reveal photo-wrap"><img class="photo" src="{IMG["coffee"]}" alt="A church member serving coffee and donuts in the café" loading="lazy"></div>
    <div class="reveal"><span class="eyebrow">Serve</span><h2>Want to get involved?</h2><p class="lede">Fill out a connection card or reach out to our staff, and we'll help you find a place to serve.</p><div class="btns"><a class="btn btn-blue" href="/connect/">Get Connected</a><a class="btn btn-line" href="/contact/">Contact Us</a></div></div>
  </div>
</section>''')

# ---------------------------------------------------------------- WATCH
page("/watch/", "Watch Live · Baptist Temple, Connersville",
 "Watch Baptist Temple live on Facebook and YouTube every Sunday at 10:30 AM, or catch up on past messages.",
 page_hero("Watch", "Worship with us from <em>anywhere.</em>",
  "We stream every Sunday at 10:30 AM on Facebook and YouTube. Past messages are always available on our YouTube channel.", IMG["preach"], "30% center") + f'''
<section class="section">
  <div class="wrap">
    <div class="cards stagger">
      <a class="card dark reveal" href="{YT_LIVE}" style="text-decoration:none"><span class="when">Live Sundays 10:30</span><h3>Watch on YouTube</h3><p>Join the live stream, or browse past streams and messages.</p></a>
      <a class="card reveal" href="{FB}" style="text-decoration:none"><span class="when">Live Sundays 10:30</span><h3>Watch on Facebook</h3><p>Follow Connersville Baptist Temple on Facebook to catch us live.</p></a>
      <a class="card reveal" href="{YT}" style="text-decoration:none"><span class="when">Anytime</span><h3>Past Messages</h3><p>Catch up on a message you missed or share one with a friend.</p></a>
    </div>
  </div>
</section>
<section class="section mist">
  <div class="wrap split">
    <div class="reveal"><span class="eyebrow">Watching from home?</span><h2>Let us know you joined us.</h2><p class="lede">We'd love to know you're part of the Baptist Temple family online. Fill out a connection card and someone from our team will reach out.</p><div class="btns"><a class="btn btn-blue" href="/connect/">Connection Card</a><a class="btn btn-line" href="/prayer/">Prayer Request</a></div></div>
    <div class="reveal photo-wrap"><img class="photo" src="{IMG["worship"]}" alt="Worship team leading a Sunday service" loading="lazy" style="aspect-ratio:4/3;object-position:center 30%"></div>
  </div>
</section>''')

# ---------------------------------------------------------------- FORMS
def form(kind):
    if kind == "connect":
        inner = '''<div class="row"><label>First name<input name="first" autocomplete="given-name" required></label><label>Last name<input name="last" autocomplete="family-name" required></label></div>
<div class="row"><label>Email<input type="email" name="email" autocomplete="email"></label><label>Phone<input type="tel" name="phone" autocomplete="tel"></label></div>
<fieldset><legend>I joined</legend><div class="opts"><label><input type="radio" name="joined" value="In person"> In person</label><label><input type="radio" name="joined" value="Online"> Online</label></div></fieldset>
<fieldset><legend>I'd like to</legend><div class="opts"><label><input type="checkbox" name="next" value="Learn about membership"> Learn about making this my church home</label><label><input type="checkbox" name="next" value="Serve"> Find a place to serve</label><label><input type="checkbox" name="next" value="Talk with a pastor"> Talk with a pastor</label></div></fieldset>
<label>Anything else we should know?<textarea name="notes"></textarea></label>'''
    else:
        inner = '''<div class="row"><label>Name<input name="name" autocomplete="name"></label><label>Email or phone<input name="contact"></label></div>
<label>How can we pray for you?<textarea name="request" required></textarea></label>
<fieldset><legend>Who can see this request?</legend><div class="opts"><label><input type="radio" name="share" value="Pastors only" checked> Pastors only</label><label><input type="radio" name="share" value="Prayer team"> The prayer team</label></div></fieldset>'''
    return f'''<form class="form reveal" data-preview>{inner}
<div class="btns"><button class="btn btn-blue" type="submit">Send {ICON["arrow"]}</button></div>
<p class="form-msg" tabindex="-1" hidden></p>
<p class="form-note">Preview note: this form doesn't send anything yet. On the live site it goes straight to the church office.</p></form>'''

page("/connect/", "Connection Card · Baptist Temple, Connersville",
 "Let Baptist Temple know you joined us in person or online, or that you're interested in making it your church home.",
 page_hero("Connection card", "We're glad <em>you're here.</em>",
  "Let us know you joined us in person or online, or that you're interested in making Baptist Temple your home church. Someone from our staff or leadership team will be in touch.", IMG["coffee"]) + f'''
<section class="section"><div class="wrap" style="max-width:880px">{form("connect")}</div></section>''')

page("/prayer/", "Prayer Requests · Baptist Temple, Connersville",
 "Send a prayer request to the pastors and prayer team at Baptist Temple in Connersville, Indiana.",
 page_hero("Prayer requests", "You don't have to carry it <em>alone.</em>",
  "Share what's on your heart. Our pastors and prayer team would be honored to pray for you.", IMG["lectern"]) + f'''
<section class="section"><div class="wrap" style="max-width:880px">{form("prayer")}</div></section>''')

page("/contact/", "Contact · Baptist Temple, Connersville",
 "Contact Baptist Temple: 1380 IN-44, Connersville, IN 47331 · 765-825-5196 · staff@baptist-temple.com",
 page_hero("Contact us", "We'd love to <em>hear from you.</em>",
  "Call, email, or stop by. Our office team is happy to help with anything you need.", IMG["front"]) + f'''
<section class="section">
  <div class="wrap">
    <div class="visit">
      <iframe class="map reveal" src="{MAP_EMBED}" title="Map to Baptist Temple" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      <div class="visit-card reveal">
        <span class="eyebrow" style="color:#7cc4ea">Church office</span>
        <h2>Baptist Temple</h2>
        <div class="info">
          <div>{ICON["pin"]}<span><small>Address</small><a href="{MAPS}">1380 IN-44<br>Connersville, IN 47331</a></span></div>
          <div>{ICON["phone"]}<span><small>Phone</small><a href="tel:{PHONE_TEL}">{PHONE}</a></span></div>
          <div>{ICON["mail"]}<span><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></span></div>
          <div>{ICON["clock"]}<span><small>Sundays</small>Sunday School 9:30 AM<br>Worship Service 10:30 AM</span></div>
        </div>
        <div class="social" style="margin-top:4px"><a href="{FB}" aria-label="Facebook">{ICON["fb"]}</a><a href="{YT}" aria-label="YouTube">{ICON["yt"]}</a></div>
      </div>
    </div>
  </div>
</section>''' + TRIO)

print("built")
