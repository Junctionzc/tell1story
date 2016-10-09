var setSelectionRange = function(input, selectionStart, selectionEnd) {
    if (input.setSelectionRange) {
        input.focus();
        input.setSelectionRange(selectionStart, selectionEnd);
    } else if (input.createTextRange) {
        var range = input.createTextRange();
        range.collapse(true);
        range.moveEnd('character', selectionEnd);
        range.moveStart('character', selectionStart);
        range.select();
    }
}

var setCaretToPos = function(input, pos) {
    setSelectionRange(input, pos, pos);
}

var content_insert_text = function(insert_text, cursor_offset_forward=0) {
    var content = $('#textarea-content')
    var caretPos = $(content)[0].selectionStart
    var content_text = content.val()
    content.val(content_text.substring(0, caretPos) + insert_text + content_text.substring(caretPos))
    setCaretToPos(content[0], caretPos + cursor_offset_forward)
}

var markdown_preview = function() {
    var content = $('#textarea-content').val()
    var converter = new showdown.Converter()
    var html = converter.makeHtml(content)
    $('#div-preview-content').html(html)
}

var insert_trigger_keyup = function() {
    $('#textarea-content').trigger('keyup')
}

var bingEventBlogEditLoad = function() {
    markdown_preview()
}

var bindEventBlogEdit = function() {
    $('#input-title').on('keyup', function() {
        var title = $(this).val()
        $('#div-preview-title').text(title)
    })
    $('#textarea-content').on('keyup', function() {
        markdown_preview();
    })
    $('#button-bold').on('click', function() {
        content_insert_text('****', 2)
        insert_trigger_keyup()
    })
    $('#button-italic').on('click', function() {
        content_insert_text('**', 1)
        insert_trigger_keyup()
    })
    $('#button-list').on('click', function() {
        content_insert_text('* 列表条目', '* 列表条目'.length)
        insert_trigger_keyup()
    })
    $('#button-font').on('click', function() {
        content_insert_text('##', 2)
        insert_trigger_keyup()
    })
    $('#button-link').on('click', function() {
        content_insert_text('[提示文字](链接地址)', 1)
        insert_trigger_keyup()
    })
} 

var bindEventBlogUploadPicture = function () {
    $('#button-upload-picture').on('click', function() {
        var form = new FormData($('#form-upload')[0])
        var response = function(r) {
            if (r.success) {
                var w = r.data
                log(w.picture_url)
                content_insert_text(`![](${ w.picture_url })`)
                $('#button-close-modal').trigger('click')
                insert_trigger_keyup()
            } else {
                alert(r.message)
            }
        }

        api.blogUploadPicture(form, response)
    })
}

var bindEvents = function() {
    bingEventBlogEditLoad()
    bindEventBlogEdit()
    bindEventBlogUploadPicture()
}

$(document).ready(function(){
    bindEvents()
})