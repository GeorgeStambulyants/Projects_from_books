class ToDoClass {
    constructor() {
        this.tasks = [
            {task: 'Go to Dentist', isComplete: false},
            {task: 'Do Gardening', isComplete: true},
            {task: 'Renew Library Account', isComplete: false},
        ];
        this.loadTasks();
    }

    loadTasks() {
        let tasksHtml = this.tasks.reduce((html, task, index) => html +=
        this.generateTaskHtml(task, index), '');
        document.getElementById('taskList').innerHTML = tasksHtml
        document.getElementById('hey').innerHTML = 'HEY'
    }

    generateTaskHtml(task, index) {
        return `
                <li class="list-group-item checkbox">
                <div class="row">
                <div class="col-md-1 col-xs-1 col-lg-1 col-sm-1 checkbox">
                    <label>
                        <input
                        id="toggleTaskStatus"
                        onchange="toDo.toggleTaskStatus(${index})"
                        type="checkbox"
                        value=""
                        class=""
                        ${task.isComplete?'checked':''}
                        checked>
                    </label>
                </div>
                <div class="col-md-10 col-xs-10 col-lg-10 col-sm-10 task-text
                        ${task.isComplete?'complete':''}">
                    ${task.task}
                </div>
                <div class="col-md-1 col-xs-1 col-lg-1 col-sm-1 delete-icon-area">
                    <a class="" href="/" onClick="toDo.deleteTask(event, ${index})">
                        <i class="delete-icon glyphicon glyphicon-trash"></i>
                    </a>
                </div>
                </div>
            </li>
        `;
    }
}

let toDo = new ToDoClass();
