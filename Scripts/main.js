// clickme.addEventListener('click',function(){
//     alert('AUUUUUUGHH');
// })
let x =1;
let width = 110;
var bar = document.getElementById('bar');
const element = document.getElementById("demo");

setInterval(test, 1000);

function test(){
    element.innerHTML =x
    x++;
    
    if(bar && bar.style){
        bar.height = 20;
        bar.width = width;
    }
    width+=1;
}

