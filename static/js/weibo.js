var bindEventWeiboEdit = function() {
    $('.tell1story-weibo-cell').on('click', '.tell1story-weibo-update', function() {
        var weiboCell =  $(this).closest('.tell1story-weibo-cell')
        var weiboContent =  $(this).closest('.tell1story-weibo-content')
        var weiboId = weiboContent.find('.tell1story-weibo-id').text()
        var weiboUpdateContent = weiboContent.find('.form-control').val()
        var form = {
            weibo_id: weiboId,
            weibo_content: weiboUpdateContent,
        }

        var response = function(r) {
            if (r.success) {
                var w = r.data
                weiboCell.find('.tell1story-weibo-input-div').addClass('ya-hide')
                weiboContent.find('.tell1story-weibo-content-text').text(w.weibo_content)
            } else {
                alert(r.message)
            }
        }

        api.weiboUpdate(form, response)
    })

    $('.tell1story-weibo-cell').on('click', '.tell1story-weibo-edit', function() {
        var weiboCell =  $(this).closest('.tell1story-weibo-cell')
        weiboCell.find('.tell1story-weibo-input-div').toggleClass('ya-hide')
    })
}

var bindEvents = function() {
    bindEventWeiboEdit()
}

$(document).ready(function(){
    bindEvents()
})