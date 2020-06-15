Vue.filter('date', time => moment(time).format('DD/MM/YY, HH:mm'))

var app = new Vue({
    el: '#notebook',

    data() {
        return {
            notes: JSON.parse(localStorage.getItem('notes')) || [],
            selectedId: localStorage.getItem('selected-id') || null,
        }
    },

    methods: {
        addNote() {
            const time = Date.now();
            const note = {
                id: String(time),
                title: 'New note ' + (this.notes.length + 1),
                content: '**Hi!** This note book is using [markdown](https://github.com/adam-p/mardown-here/wiki/Markdown-Cheatsheet) for formatting!',
                created: time,
                favorite: false,
            };
            this.notes.push(note);
        },

        selectNote(note) {
            this.selectedId = note.id;
        },

        saveNotes() {
            localStorage.setItem('notes', JSON.stringify(this.notes));
            console.log('Notes saved!', new Date());
        },

        removeNote() {
            if (this.selectedNote && confirm('Delete the note?')) {
                const index = this.notes.indexOf(this.selectedNote);
                if (index !== -1) {
                    this.notes.splice(index, 1);
                }
            }
        },

        favoriteNote() {
            this.selectedNote.favorite ^= true;
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
        },

        sortedNotes() {
            return this.notes.slice()
                .sort((a, b) => a.created - b.created)
                .sort((a, b) => (a.favorite === b.favorite) ? 0 : a.favorite ? -1 : 1);
        },

        linesCount() {
            if (this.selectedNote) {
                // Count the number of new line characters
                return this.selectedNote.content.split(/\r\n|\r|\n/).length;
            }
        },

        wordsCount() {
            if (this.selectedNote) {
                let s = this.selectedNote.content;
                // Turn new line characters into white-spaces
                s = s.replace(/\n/g, ' ');
                // Exclude start and end white-spaces
                s = s.replace(/(^\s*)|(\s*$)/gi, '');
                // Turn 2 or more dublicate white-spaces into 1
                s = s.replace(/\s\s+/gi, ' ');
                // Return the number of words
                return s.split(' ').length
            }
        },

        charactersCount() {
            if (this.selectedNote) {
                return this.selectedNote.content.split('').length
            }
        },
    },

    watch: {
        notes: {
            handler: 'saveNotes',
            deep: true,
        },

        selectedId: {
            handler(val) {
                localStorage.setItem('selected-id', val);
            },
        },
    }
})
