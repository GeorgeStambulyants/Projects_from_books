var app = new Vue({
    el: '#notebook',

    data() {
        return {
            content: 'This is note'
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
        }
    },

    computed: {
        notePreview() {
            return marked(this.content);
        },
    },
    watch: {
        content: 'saveNote',
    },
})
