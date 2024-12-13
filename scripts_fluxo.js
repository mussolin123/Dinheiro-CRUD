async function listarDespesas() {
    const tbody = document.getElementById('listaFinanceiro');

    try {
        const res = await fetch('http://127.0.0.1:8000/api/despesas/');
        
        if (!res.ok) {a
            throw new Error('Erro ao acessar a API');
        }

        const dados = await res.json();

        tbody.innerHTML = dados.map(item => `
            <tr>
                <td>${item.descricao}</td>
                <td>${item.tipo}</td>
                <td>R$ ${item.valor.toFixed(2)}</td>
                <td>
                    <span class="${item.status_pago ? 'badge bg-success' : 'badge bg-warning'}">
                        ${item.status_pago ? 'Pago' : 'Pendente'}
                    </span>
                </td>
                <td>${item.data}</td>
            </tr>`).join('');

    } catch (err) {
        console.error('Erro ao carregar as despesas:', err);
        tbody.innerHTML = `<tr><td colspan="5" class="text-danger">Erro ao carregar despesas</td></tr>`;
    }
}

// Carrega a lista das despesas ao abrir a tela
document.addEventListener('DOMContentLoaded', listarDespesas);

// Função para adicionar despesas à tabela e calcular totais
function adicionarDespesa(despesas) {
    const tbody = document.getElementById('listaFinanceiro');
    tbody.innerHTML = '';  // Limpa a tabela antes de adicionar elementos

    let totalPagas = 0;
    let totalPendentes = 0;

    despesas.forEach(despesa => {
        const { descricao, tipo, valor, status, data } = despesa;

        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${descricao}</td>
            <td>${tipo}</td>
            <td>R$ ${parseFloat(valor).toFixed(2)}</td>
            <td>${status ? 'Pago' : 'Pendente'}</td>
            <td>${data}</td>
        `;

        tbody.appendChild(tr);

        // Somar os valores das despesas pagas e pendentes
        if (status) {
            totalPagas += parseFloat(valor);
        } else {
            totalPendentes += parseFloat(valor);
        }
    });

    const total = totalPagas + totalPendentes;

    // Adicionar o resumo ao final da tabela
    const resumo = document.createElement('tr');
    resumo.innerHTML = `
        <td><strong>Totais</strong></td>
        <td></td>
        <td><strong>R$ ${totalPagas.toFixed(2)}</strong></td>
        <td><strong>R$ ${totalPendentes.toFixed(2)}</strong></td>
        <td><strong>R$ ${total.toFixed(2)}</strong></td>
    `;

    tbody.appendChild(resumo);
}


