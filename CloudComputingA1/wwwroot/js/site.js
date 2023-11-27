// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

async function login() {
    const form = document.getElementById("login");
    console.log(form);


    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const payload = new FormData(form);
        console.log(...payload);

        var object = {};
        payload.forEach((value, key) => object[key] = value);
        var json = JSON.stringify(object);
        console.log(JSON.parse(json).email);
        //const l = await get("https://otqv87ky2m.execute-api.us-east-1.amazonaws.com/default/images");
        const log = await post("https://81wawzuv1e.execute-api.us-east-1.amazonaws.com/default/LOGIN", json);
        if (log === true) {
            window.location.href = "/Main/MainPage";
            console.log(sessionStorage.getItem('user_name'));
            //document.getElementById("head").innerHTML = sessionStorage.getItem("user_name");
        }
        else {
            alert("Email or Password invalid");
            object = {};
        }
    });
}

async function register() {
    const form = document.getElementById("register");
    console.log(form);


    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const payload = new FormData(form);
        console.log(...payload);

        var object = {};
        payload.forEach((value, key) => object[key] = value);
        var json = JSON.stringify(object);
        console.log(json);
        const log = await post("https://81wawzuv1e.execute-api.us-east-1.amazonaws.com/default/REGISTER", json);
        if (log === true) {
            window.location.href = "/Home/Index";
        }
        else {
            alert("The email already exists");
        }
    });
}

async function post(url, json) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
        },
        body: json,
    })
    const status = await response.status;
    if (response.status === 200) {
        const res = await response.json();
        console.log(response.status);
        sessionStorage.setItem("user_name", res.user_name);
        sessionStorage.setItem("email", res.email);
        return true;
    }
    else {
        console.log(response.status);
        return false;
    }
}

////async function get(url) {
////    const response = await fetch(url, {
////        method: "GET",
////        headers: {
////            'Accept': 'application/json',
////        },
////    })
////    const status = await response.status;
////    if (response.status === 200) {
////        const res = await response.blob();
////        console.log(res);




////        console.log(response.status);
////        //sessionStorage.setItem("user_name", res.user_name);
////        //sessionStorage.setItem("email", res.email);
////        return true;
////    }
//    else {
//        console.log(response.status);
//        return false;
//    }
//}

function isTableVisible() {
    return false;
}

