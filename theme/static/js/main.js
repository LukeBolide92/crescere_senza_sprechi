// Crescere Senza Sprechi - Script principale
// Navigazione mobile, percorso personalizzato, convalida form

document.addEventListener('DOMContentLoaded', () => {
    // Toggle navigazione mobile
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('#nav-menu');
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            const open = navMenu.classList.toggle('open');
            navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            // Chiusura dropdown aperti
            document.querySelectorAll('.nav-has-dropdown.open').forEach(d => d.classList.remove('open'));
        });

        // Dropdown desktop/mobile
        document.querySelectorAll('.nav-dropdown-toggle').forEach(btn => {
            btn.addEventListener('click', () => {
                const parent = btn.closest('.nav-has-dropdown');
                const isOpen = parent.classList.toggle('open');
                btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
            });
        });
    }

    // Percorso personalizzato (sezione "Il tuo percorso")
    const percorsoForm = document.getElementById('percorso-form');
    if (percorsoForm) {
        percorsoForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const tipo = percorsoForm.querySelector('input[name="tipo"]:checked')?.value || '';
            const dataStr = percorsoForm.querySelector('input[name="data"]')?.value || '';
            const priorita = percorsoForm.querySelector('select[name="priorita"]')?.value || '';
            const resultDiv = document.getElementById('percorso-result');
            
            if (!tipo || !dataStr || !priorita) {
                if (resultDiv) resultDiv.innerHTML = '<p>Completa tutti i campi.</p>';
                return;
            }

            // Calcolo fase approssimativa (calcolo semplice per demo)
            const [anno, mese, giorno] = dataStr.split('-').map(Number);
            const oggi = new Date();
            const hoje = new Date(oggi.getFullYear(), oggi.getMonth(), oggi.getDate());
            const dataInp = new Date(anno, mese - 1, giorno);
            const diffMs = hoje - dataInp;
            const diffGiorni = Math.round(diffMs / (1000 * 60 * 60 * 24));

            let fase = '';
            if (tipo === 'gravidanza') {
                if (diffGiorni < 84) {
                    fase = 'Primo trimestre';
                } else if (diffGiorni < 168) {
                    fase = 'Secondo trimestre';
                } else {
                    fase = 'Terzo trimestre / Ultime settimane';
                }
            } else if (tipo === 'nato') {
                if (diffGiorni <= 30) {
                    fase = '0-1 mese';
                } else if (diffGiorni <= 90) {
                    fase = '2-3 mesi';
                } else if (diffGiorni <= 180) {
                    fase = '4-6 mesi';
                } else if (diffGiorni <= 270) {
                    fase = '7-9 mesi';
                } else {
                    fase = '10-12 mesi';
                }
            }

            if (resultDiv) {
                resultDiv.innerHTML = `
                    <h3>Risultato</h3>
                    <p><strong>Fase</strong>: ${fase}</p>
                    <p><strong>Priorità</strong>: ${priorita}</p>
                    <p><a href="/guide/" class="btn btn-secondary">Vedi le guide pertinenti</a></p>
                `;
            }
        });
    }

    // Caricamento immagini con lazy loading
    document.querySelectorAll('img[loading="lazy"]').forEach(img => {
        img.addEventListener('load', () => img.classList.add('loaded'));
        if (img.complete && img.naturalHeight !== 0) img.classList.add('loaded');
    });
});
