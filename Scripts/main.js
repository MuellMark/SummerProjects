// clickme.addEventListener('click',function(){
//     alert('AUUUUUUGHH');
// })
let x =1;
const element = document.getElementById("demo");
setInterval(test, 1000);

function test(){
    element.innerHTML =x
    x++;
}