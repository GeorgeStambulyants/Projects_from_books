var app = new Vue({
    el: '#notebook',

    data() {
        return {
            notes: [],
            selectedId: null,
        }
    },

    methods: {
        reportOperation(opName) {
            console.log('The', opName, 'operation was completed!')
        },

        addNote() {
            const time = Date.now();
            const note = {
                id: String(time),
                title: 'New note ' + (this.notes.length + 1),
                content: '**Hi!** This note book is using [markdown]<url to github repo here> for formatting!',
                created: time,
                favorite: false,
            };
            this.notes.push(note);
        },

        selectNote(note) {
            this.selectedId = note.id;
        },
    },

    computed: {
        notePreview() {
            return this.selectedNote ? marked(this.selectedNote.content) : '';
        },

        addButtonTitle() {
            return this.notes.length + ' note(s) already'
        },

        selectedNote() {
            return this.notes.find(note => note.id === this.selectedId) || '';
        }
    },
})
