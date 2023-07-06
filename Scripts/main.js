// clickme.addEventListener('click',function(){
//     alert('AUUUUUUGHH');
// })
let x =1;
let width = 20;
const element = document.getElementById("demo");
setInterval(test, 1000);

function test(){
    element.innerHTML =x
    x++;
    var bar = document.getElementById('bar');
    if(bar && bar.style){
        bar.style.height = '20px';
        bar.style.width = width+'px';
    }
    width++;
}

