class ToDoClass {
    constructor() {
        alert('Hello World!');
    }
}
let toDo;
window.addEventListener('load', () => {
    toDo = new ToDoClass();
});
