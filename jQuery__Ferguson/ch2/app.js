$(function() {
    let box = $('#box');
    let para = $('p');
    let i = 0;

    para.text(i);
    function toggleBox(i) {
        box.fadeToggle(500, function() {
            i += 1;
            if (i < 10) {
                para.text(i + 1);
                toggleBox(i);
            };
        });
    };

    toggleBox(i);
});