/* article-sort.js */

/*jQuery(document).ready(function($) {
    if ($(".errornote").length) {
        var mylist = $('div.items');
        var listitems = mylist.children('div.inline-related').get();
        listitems.sort(function(a, b) {
            if ($(a).find('select[id$=article]').val() && $(a).find('select[id$=article]').val()) {
               var compA = $(a).find('input[id$=order]');
               var compB = $(b).find('input[id$=order]');
               return (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
            }
        })
        $.each(listitems, function(idx, itm) { mylist.append(itm); });
    }
});
*/

jQuery(function($) {
    $('div.sortable').sortable({
        /*containment: 'parent',
        zindex: 10, */
        items: 'div.inline-related',
        handle: 'div.module',
        opacity: 0.8,
        axis: 'y',
        containment: 'parent',
        placeholder: 'ui-state-highlight',
        update: function() {
            $(this).find('div.inline-related').each(function(i) {
                if ($(this).find('select[id$=article]').val()) {
                    $(this).find('input[id$=order]').val(i+1);
                }
            });
        }
    });
    $('div.inline-related div.module').css('cursor', 'move');
    $('div.inline-related div.module').attr('title', "Drag to reorder");
    $('div.inline-related').find('div.order').hide();
    $('div.legend').find('div.order').hide();
});


