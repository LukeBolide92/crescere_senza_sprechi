function calcPregnancy(dateStr) {
  const dpa = new Date(dateStr);
  const today = new Date();
  const daysLeft = Math.ceil((dpa - today) / (1000*60*60*24));
  const week = Math.max(1, Math.floor((280 - daysLeft)/7)+1);
  return week + 'ª sett • ' + (week>=28 ? '3° Trim' : week>=14 ? '2° Trim' : '1° Trim');
}
function calcBaby(dateStr) {
  const b = new Date(dateStr);
  const t = new Date();
  const m = (t.getFullYear()-b.getFullYear())*12 + t.getMonth()-b.getMonth();
  return 'Circa ' + Math.max(0,Math.min(12,m)) + ' mesi';
}
console.log('timeline JS attivo');
