import re

# Open external links in page content in a new tab.
# ponytail: regex on rendered HTML; fine for generated markdown links, switch to an HTML parser if raw <a> tags get fancy.
EXTERNAL = re.compile(r'<a href="(https?://[^"]+)"(?![^>]*\btarget=)')


def on_page_content(html, **kwargs):
    return EXTERNAL.sub(r'<a href="\1" target="_blank" rel="noopener"', html)
