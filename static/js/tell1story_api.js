var log = function() {
    console.log(arguments)
}

var api = {}

api.ajax = function(url, method, form, callback) {
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
    
    $.ajax(request)
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