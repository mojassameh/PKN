"""Story content and markup. Add future titles, image paths and summaries here."""
from html import escape
COPY = {
 'nl': {'heading':'Mijn verhalen', 'eyebrow':'Een persoonlijke blik', 'title':'De kerk die het verhaal van David vertelt, is zelf Goliath geworden', 'alt':'Symbolische illustratie van David met een slinger tegenover de reus Goliath.', 'pending':'De tekst van dit verhaal volgt binnenkort.', 'next':'Meer verhalen', 'soon':'Binnenkort', 'slot':'Verhaal', 'summary':'Hier volgt binnenkort een nieuw verhaal.', 'image':'Afbeelding volgt'},
 'en': {'heading':'My stories', 'eyebrow':'A personal perspective', 'title':'The church that tells David’s story has itself become Goliath', 'alt':'Symbolic illustration of David holding a sling as he faces the giant Goliath.', 'pending':'The text of this story is coming soon.', 'next':'More stories', 'soon':'Coming soon', 'slot':'Story', 'summary':'A new story will appear here soon.', 'image':'Image to follow'},
 'fa': {'heading':'روایت‌های من', 'eyebrow':'از نگاه من', 'title':'کلیسایی که داستان داوود را روایت می‌کند، خود به جالوت بدل شده است', 'alt':'تصویری نمادین از داوود با فلاخن در برابر جالوت غول‌پیکر.', 'pending':'متن این روایت به‌زودی منتشر خواهد شد.', 'next':'روایت‌های بیشتر', 'soon':'به‌زودی', 'slot':'روایت', 'summary':'به‌زودی روایت تازه‌ای در این بخش منتشر خواهد شد.', 'image':'تصویر به‌زودی اضافه می‌شود'}
}
def render_stories(lang):
 d=COPY[lang]
 cards=[]
 for number in range(2,5):
  n=str(number) if lang!='fa' else str(number).translate(str.maketrans('0123456789','۰۱۲۳۴۵۶۷۸۹'))
  cards.append(f'''<article class="story-card" aria-labelledby="story-{number}-title">
        <div class="story-image-placeholder" role="img" aria-label="{d['image']}"><span aria-hidden="true">{n.zfill(2) if lang!='fa' else n}</span></div>
        <div class="story-card-copy"><p class="story-eyebrow">{d['soon']}</p><h3 id="story-{number}-title">{d['slot']} {n}</h3><p>{d['summary']}</p></div>
      </article>''')
 return f'''<section class="stories wrap" aria-labelledby="stories-title">
      <div class="stories-heading"><p class="story-eyebrow">{d['eyebrow']}</p><h2 id="stories-title">{d['heading']}</h2></div>
      <article class="story-featured" aria-labelledby="story-1-title">
        <img class="story-featured-image" src="/assets/david-and-goliath.png" width="1448" height="1086" alt="{escape(d['alt'],quote=True)}" fetchpriority="high">
        <div class="story-featured-copy"><p class="story-eyebrow">{d['eyebrow']}</p><h3 id="story-1-title">{d['title']}</h3><p class="story-summary">{d['pending']}</p></div>
      </article>
      <h2 class="more-stories-title">{d['next']}</h2>
      <div class="story-grid">{''.join(cards)}</div>
    </section>'''
