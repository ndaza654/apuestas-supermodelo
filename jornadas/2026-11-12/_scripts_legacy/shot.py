import sys, asyncio
from playwright.async_api import async_playwright
async def main(f, out):
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 420, 'height': 900})
        html = open(f, encoding='utf8').read()
        await pg.set_content('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' + html + '</body></html>')
        await pg.wait_for_timeout(600)
        await pg.screenshot(path=out, clip={'x': 0, 'y': 0, 'width': 420, 'height': 2600}, full_page=True)
        w = await pg.evaluate('document.documentElement.scrollWidth'); print('scrollWidth', w)
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2]))
