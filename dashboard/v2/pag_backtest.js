/* ===== Backtest histórico: el explorador de pruebas/backtest/ dentro del dashboard ===== */
let _btUrl=null;
const btUrl=()=>{if(!_btUrl&&DB.BT)_btUrl=URL.createObjectURL(new Blob([DB.BT],{type:'text/html'}));return _btUrl};
PAGES.backtest={render(){
 if(!DB.BT)return`<h1>Backtest histórico</h1><div class="card"><div class="empty">Esta versión del dashboard se construyó sin los datos del backtest (<code>pruebas/backtest/datos.json</code>).</div></div>`;
 return`<h1>Backtest histórico</h1>
 <p class="mut">La regla «X de 10» y el colchón medidos en 50.408 partidos de las 5 grandes ligas y Brasil (2000–2026), sin mirar el futuro. Solo mide % de acierto, no ganancia. Pestañas: hallazgos, <b>Hoy</b> (tus líneas de hoy con su tasa histórica), Explorar (filtros por mercado, línea, regularidad, colchón, cuota, liga, temporada y equipo), <b>Mi línea</b> (calculadora), ranking y partidos.</p>
 <div class="row" style="margin-bottom:8px"><button class="btn soft" data-act="btdl">Descargar el explorador (HTML)</button><span class="xs mut">Las cuotas de la base son de casas europeas, no de Betano; clubes, no selecciones.</span></div>
 <div class="card flush" style="overflow:hidden"><iframe id="btf" title="Explorador del backtest" src="${btUrl()}" style="width:100%;height:calc(100vh - 210px);min-height:640px;border:0;display:block"></iframe></div>`}};
