const { chromium } = require('playwright');
(async () => {
  const file = 'file://' + process.argv[2], shot = process.argv[3];
  const b = await chromium.launch(); const errs = [];
  for (const [w, h, tag] of [[1280, 900, 'pc'], [390, 800, 'movil']]) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    p.on('console', m => { if (m.type() === 'error') errs.push(tag + ' consola: ' + m.text()); });
    p.on('pageerror', e => errs.push(tag + ' error: ' + e.message));
    await p.goto(file);
    const cnt = () => p.$eval('#cnt', e => e.textContent);
    const o = { todos: await cnt() };
    await p.selectOption('#fs', 'crítico'); o.criticos = await cnt(); o.ids_criticos = await p.$$eval('#lista .id', x => x.map(e => e.textContent));
    await p.selectOption('#fs', ''); await p.selectOption('#fa', 'G'); o.areaG = await cnt();
    await p.selectOption('#fa', ''); await p.selectOption('#fv', 'RECONSTRUIR'); o.reconstruir = await cnt();
    await p.selectOption('#fv', ''); await p.fill('#fq', 'CLV'); o.busca_clv = await cnt();
    await p.fill('#fq', 'zzzz'); o.vacio = await p.$eval('#lista', e => e.textContent);
    await p.click('#fx'); o.tras_quitar = await cnt();
    await p.click('button[data-area="A"]'); o.boton_area_A = await cnt();
    await p.click('#fx');
    o.scroll_horizontal = await p.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
    o.resumen = await p.$$eval('ol li', x => x.length); o.semaforo = await p.$$eval('.sem .card', x => x.length);
    await p.evaluate(() => window.scrollTo(0, 0));
    if (shot) await p.screenshot({ path: shot + '_' + tag + '.png' });
    if (shot && tag === 'movil') { await p.$eval('#lista', e => e.scrollIntoView({ block: 'start' })); await p.screenshot({ path: shot + '_movil_lista.png' }); }
    console.log(tag, JSON.stringify(o));
    await p.close();
  }
  console.log('ERRORES:', errs.length ? errs : 'ninguno');
  await b.close();
})();
