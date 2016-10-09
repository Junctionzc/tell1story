var bingEventBlogShow = function() {
    var content = $('#div-blog-content').text()
    var converter = new showdown.Converter()
    var html = converter.makeHtml(content)
    $('#div-blog-content').html(html)
} 

var bindEvents = function() {
    bingEventBlogShow()
}

$(document).ready(function(){
    bindEvents()
})