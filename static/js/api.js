var log = function() {
    console.log(arguments)
}

var api = {}

api.ajaxBase = function(url, method, form, callback, isFile) {
    var request = {
        url: url,
        type: method,
        data: form,
        success: function(response) {
            var r = JSON.parse(response)
            callback(r)
        },
        error: function(error){
            log('网络错误', error)
            var r = {
                'success': false,
                'message': '网络错误',
            }
            callback(r)
        }
    }

    if (isFile) {
        request.cache = false
        request.contentType = false
        request.processData = false
    }
    
    $.ajax(request)
}

api.ajax = function(url, method, form, callback) {
    api.ajaxBase(url, method, form, callback, false)
}

api.get = function(url, response) {
    api.ajax(url, 'get', {}, response)
}

api.post = function(url, form, response) {
    api.ajax(url, 'post', form, response)
}

api.weiboUpdate = function(form, response) {
    var url = '/api/weibo/update'
    api.post(url, form, response)
}

api.blogUploadPicture = function(form, response) {
    var url = '/api/blog/upload/picture'
    api.ajaxBase(url, 'post', form, response, true)
}