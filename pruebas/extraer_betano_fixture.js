// Prueba del extractor de Betano con un evento de juguete que reproduce la tabla de jugadores del 22-nov (ver betano_extraer.js). Uso: node pruebas/extraer_betano_fixture.js
const fs = require('fs'), path = require('path');
const fx = fs.readFileSync(path.join(__dirname, 'fixtures', 'betano_tabla_jugadores.json'), 'utf8');
global.window = {}; global.document = { querySelectorAll: () => [] };
global.fetch = async () => ({ ok: true, json: async () => JSON.parse(fx) });
const src = fs.readFileSync(path.join(__dirname, '..', 'recoleccion', 'betano_extraer.js'), 'utf8');
(0, eval)(src + '\nglobalThis.extraerBetano = extraerBetano;');
extraerBetano('local-visita', '1').then(t => { console.log(t); console.log('AVISOS|' + JSON.stringify(window.__betanoAvisos)); }).catch(e => { console.error('ERROR ' + e.message); process.exit(1); });
