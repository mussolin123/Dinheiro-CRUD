// Função para cadastrar e adicionar despesas
document.getElementById('formDespesa').addEventListener('submit', async (e) => {
    e.preventDefault();

    const descricao = document.getElementById('descricao').value;
    const tipo = document.getElementById('tipo').value;
    const valor = parseFloat(document.getElementById('valor').value);
    const status_pago = document.getElementById('status').value === 'true';

    const despesa = {
        descricao,
        tipo,
        valor,
        status_pago
    };

    try {
        await fetch('http://127.0.0.1:8000/api/despesas/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(despesa)
        });

        alert('Despesa cadastrada com sucesso!');
        formDespesa.reset();
        listarDespesas();

    } catch (err) {
        console.error('Erro ao cadastrar despesa', err);
    }
});

// Adicione a função cadastrarDespesa como ajuste adicional
async function cadastrarDespesa() {
    try {
        const descricao = document.getElementById('descricao').value;
        const data = document.getElementById('data').value;
        const valor = parseFloat(document.getElementById('valor').value);
        const tipo = document.getElementById('tipo').value;
        const status = document.getElementById('status').value;

        const despesa = {
            descricao,
            data,
            valor,
            tipo,
            status
        };

        await fetch('http://127.0.0.1:8000/api/despesas/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(despesa)
        });

        alert('Despesa cadastrada com sucesso!');
        formDespesa.reset();
        listarDespesas();

    } catch (error) {
        console.error('Erro ao cadastrar despesa:', error);
    }
}

// Função para listar despesas
async function listarDespesas() {
    const tbody = document.getElementById('listaDespesas');

    try {
        const response = await fetch('http://127.0.0.1:8000/api/despesas/');
        const despesas = await response.json();

        tbody.innerHTML = '';

        despesas.forEach(item => {
            const row = `<tr>
                <td>${item.descricao}</td>
                <td>${item.tipo}</td>
                <td>${item.data}</td>
                <td>R$ ${item.valor.toFixed(2)}</td>
                <td>${item.status_pago ? '<span class="badge bg-success">Pago</span>' : '<span class="badge bg-warning text-dark">Pendente</span>'}</td>
            </tr>`;

            tbody.innerHTML += row;
        });
    } catch (err) {
        console.error('Erro ao buscar despesas', err);
    }
}

// Listar despesas ao carregar a página
document.addEventListener('DOMContentLoaded', listarDespesas);
