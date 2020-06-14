var app = new Vue({
    el: '#notebook',

    data() {
        return {
            content: 'This is note',
            notes: [],
        }
    },

    created() {
        this.content = localStorage.getItem('content') || 'You can write in **markdown**';
    },

    methods: {
        saveNote() {
            console.log('saving note:', this.content);
            localStorage.setItem('content', this.content);
            this.reportOperation('saving');
        },

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
    },

    computed: {
        notePreview() {
            return marked(this.content);
        },

        addButtonTitle() {
            return this.notes.length + ' note(s) already'
        },
    },
    watch: {
        content: 'saveNote',
    },
})
