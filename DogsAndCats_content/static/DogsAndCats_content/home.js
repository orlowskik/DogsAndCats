
function get_breed() {
    let kind = document.getElementById("kind").value
    if (kind !== ""){
        $.ajax({
            type: "POST",
            url: "/get_breeds",
            data: {
                'result': kind,
                csrfmiddlewaretoken: CSRF_TOKEN
            },
            dataType: "json",
            success: function (data) {
                let breeds = document.getElementById('breed')
                breeds.options.length = 0
                Object.keys(data).forEach(
                    function (key) {
                        let option = document.createElement("option")
                        option.value = key
                        option.text = data[key]
                        breeds.add(option)
                    }
                )
                breeds.disabled = false
            },
            failure: function(){
                alert("failed to get breeds")
            }
        })
    }
}
