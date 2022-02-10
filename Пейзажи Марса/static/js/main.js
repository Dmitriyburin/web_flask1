let count = 0;
setInterval(()=>{
    count = (count + 1) % 3;
    let elements = document.querySelectorAll('.carousel-item');
    for (let [i, elem] of elements.entries()) {
        elem.classList.remove('active');
        if (i == count) {
            elem.classList.add('active')
        }
    }
},5000)