function set_searches(){
    get_breed()
    get_colors()
}

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
                let placeholder = document.createElement("option")
                breeds.options.length = 0
                placeholder.value = "All"
                placeholder.text = "All"
                placeholder.selected = true
                breeds.add(placeholder)
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


function get_colors(){
    let kind = document.getElementById("kind").value
    if (kind !== ""){
        $.ajax({
            type: "POST",
            url: "/get_colors",
            data: {
                'result': kind,
                csrfmiddlewaretoken: CSRF_TOKEN
            },
            dataType: "json",
            success: function (data) {
                let colors = document.getElementById("colors")
                colors.replaceChildren()
                Object.keys(data).forEach(
                    function (key) {
                        let check = document.createElement("INPUT")
                        let br = document.createElement('br')
                        check.type = "checkbox"
                        check.name = "colors"
                        check.value = data[key]
                        colors.appendChild(check)
                        colors.append(data[key])
                        colors.appendChild(br)
                    }
                )
            },
            failure: function(){
                alert("failed to get breeds")
            }
        })
    }
}