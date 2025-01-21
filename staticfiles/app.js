document.addEventListener('DOMContentLoaded', () => {
    const taskList = document.getElementById('task-list');
    const taskForm = document.getElementById('add-task-form');
    const taskTitle = document.getElementById('task-title');
    const taskDesc = document.getElementById('task-desc');

    const apiUrl = 'http://127.0.0.1:8000/api/tarefas/';

    // Função para exibir as tarefas na interface
    function renderTasks(tasks) {
        taskList.innerHTML = '';
        if (tasks.length === 0) {
            taskList.innerHTML = '<li>Nenhuma tarefa encontrada.</li>';
            return;
        }
        tasks.forEach((task) => {
            const li = document.createElement('li');
            li.innerHTML = `
                <strong>${task.titulo}</strong>
                <p>${task.descricao}</p>
                <small>Prazo: ${new Date(task.prazo_para_conclusao).toLocaleString()}</small>
            `;
            taskList.appendChild(li);
        });
    }

    // Função para carregar tarefas da API
    async function loadTasks() {
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error('Erro ao carregar tarefas');
            const tasks = await response.json();
            renderTasks(tasks);
        } catch (error) {
            console.error('Erro ao carregar tarefas:', error);
            taskList.innerHTML = '<li>Erro ao carregar tarefas. Tente novamente mais tarde.</li>';
        }
    }

    // Função para adicionar uma nova tarefa
    async function addTask(title, desc) {
        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    titulo: title,
                    descricao: desc,
                    prazo_para_conclusao: new Date().toISOString(),
                    situacao: 'P',
                }),
            });
            if (!response.ok) throw new Error('Erro ao adicionar tarefa');
            loadTasks();
        } catch (error) {
            console.error('Erro ao adicionar tarefa:', error);
            alert('Erro ao adicionar tarefa. Verifique os dados e tente novamente.');
        }
    }

    // Evento de envio do formulário
    taskForm.addEventListener('submit', (e) => {
        e.preventDefault();
        if (taskTitle.value.trim() === '' || taskDesc.value.trim() === '') {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        addTask(taskTitle.value, taskDesc.value);
        taskTitle.value = '';
        taskDesc.value = '';
    });

    // Carregar tarefas ao iniciar
    loadTasks();
});
