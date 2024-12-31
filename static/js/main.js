const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(()=>{
    $("#messages").fadeOut("slow");
},3000);



// This line  mean: find _alert.html popup message id and set fadeout time