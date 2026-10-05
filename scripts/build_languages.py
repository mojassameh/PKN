"""Generate static English and Persian pages from the Dutch template. Run after editing it."""
from pathlib import Path
import re
from html import escape
ROOT=Path(__file__).resolve().parents[1]
base=(ROOT/'public/index.html').read_text()
data={
'en': {
'name':'The Real Protestant Church in the Netherlands', 'brand':'The Real Protestant Church<br><span>in the Netherlands</span>',
'heading':'An independent voice on the Protestant Church in the Netherlands (PKN)',
'label':'Disclaimer — independent website',
'lead':'This is not the official website of the Protestant Church in the Netherlands (PKN).',
'intro':'This website is a personal, independent initiative and is not operated on behalf of the PKN.',
'body':'This website was established in the belief that freedom and freedom of expression deserve protection. Its founder considers himself a victim of the PKN and uses this website to share his experiences and make his voice heard. The views and experiences published here are those of the founder.',
'official':'The official website of the Protestant Church in the Netherlands is',
'description':'An independent, personal voice on the PKN (Protestant Church in the Netherlands), personal experiences and freedom of expression. Not the official PKN website.',
'keywords':'PKN, Protestant Church in the Netherlands, Protestantse Kerk in Nederland, experiences with PKN, criticism of PKN, freedom of expression',
'locale':'en_US', 'suffix':'Independent voice on the PKN',
'labels':{'Taal kiezen':'Choose language','Website header':'Website header','Featured content area':'Featured content area','Content areas':'Content areas','Footer content area':'Footer content area'}
},
'fa': {
'name':'کلیسای واقعی پروتستان در هلند', 'brand':'کلیسای واقعی پروتستان<br><span>در هلند</span>',
'heading':'صدایی مستقل دربارهٔ کلیسای پروتستان در هلند (PKN)',
'label':'توضیح دربارهٔ استقلال وب‌سایت',
'lead':'این وب‌سایت، وب‌سایت رسمی کلیسای پروتستان در هلند (PKN) نیست.',
'intro':'این وب‌سایت ابتکاری شخصی و مستقل است و از طرف PKN اداره نمی‌شود.',
'body':'این وب‌سایت با این باور ایجاد شده است که آزادی و آزادی بیان شایستهٔ حمایت‌اند. بنیان‌گذار آن خود را قربانی PKN می‌داند و می‌خواهد از طریق این وب‌سایت تجربه‌هایش را به اشتراک بگذارد و صدای خود را به گوش دیگران برساند. دیدگاه‌ها و تجربه‌های منتشرشده در این وب‌سایت متعلق به بنیان‌گذار آن است.',
'official':'وب‌سایت رسمی کلیسای پروتستان در هلند در این نشانی در دسترس است:',
'description':'صدایی شخصی و مستقل دربارهٔ کلیسای پروتستان در هلند (PKN)، تجربه‌های شخصی و آزادی بیان. این وب‌سایت رسمی PKN نیست.',
'keywords':'PKN, Protestantse Kerk in Nederland, کلیسای پروتستان در هلند, تجربه‌های شخصی از PKN, نقد PKN, آزادی بیان',
'locale':'fa_IR','suffix':'صدایی مستقل دربارهٔ PKN',
'labels':{'Taal kiezen':'انتخاب زبان','Website header':'سربرگ وب‌سایت','Featured content area':'بخش محتوای ویژه','Content areas':'بخش‌های محتوا','Footer content area':'پابرگ وب‌سایت'}
}}
for lang,d in data.items():
 s=base.replace('<html lang="nl">',f'<html lang="{lang}" dir="{"rtl" if lang=="fa" else "ltr"}">')
 title=d['name']+' | '+d['suffix']
 s=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',s)
 for key,val in [('description',d['description']),('keywords',d['keywords']),('og:locale',d['locale']),('og:site_name',d['name']),('og:title',title),('og:description',d['description']),('twitter:title',title),('twitter:description',d['description'])]:
  s=re.sub(r'(<meta (?:name|property)="'+re.escape(key)+r'" content=")[^"]*(">)',lambda m:m[1]+escape(val,quote=True)+m[2],s)
 s=s.replace('De echte Protestantse Kerk<br><span>in Nederland</span>',d['brand'])
 s=s.replace('href="/" aria-label="De echte Protestantse Kerk in Nederland — home"',f'href="/{lang}/" aria-label="{d["name"]}"')
 s=s.replace(' aria-current="page"','').replace(f'hreflang="{lang}"><img',f'hreflang="{lang}" aria-current="page"><img')
 for old,new in d['labels'].items(): s=s.replace(f'aria-label="{old}"',f'aria-label="{new}"')
 section=f'''<section class="disclaimer wrap" aria-labelledby="disclaimer-title">
      <p class="disclaimer-label">{d['label']}</p>
      <h1 id="disclaimer-title">{d['heading']}</h1>
      <p><strong>{d['lead']}</strong> {d['intro']}</p>
      <p>{d['body']}</p>
      <p>{d['official']} <a href="https://protestantsekerk.nl/" dir="ltr">protestantsekerk.nl</a>.</p>
    </section>'''
 s=re.sub(r'<section class="disclaimer wrap".*?</section>',lambda m:section,s,flags=re.S)
 path=ROOT/'public'/lang/'index.html'; path.parent.mkdir(exist_ok=True); path.write_text(s)
print('Generated English and Farsi pages.')
