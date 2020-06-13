var app = new Vue({
    el: '#notebook',

    data() {
        return {
            content: 'This is note'
        }
    },

    computed: {
        notePreview() {
            return marked(this.content);
        },
    },
})