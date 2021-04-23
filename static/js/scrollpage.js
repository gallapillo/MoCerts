console.log('it works')

 scrollpage();
function scrollpage() {
    let down;
    let x;
    let y;
    document.onmousemove = mousemove;
    document.onmousedown = function(e) {
      e = e || window.event;
      down = 1;
      x = e.clientX;
      y = e.clientY;
    }

    document.onmouseup = function(e){
        e = e || window.event;
        down = 0;
    }

    function mousemove(e) {
     if(down == 1){
      if (x && y) {
        window.scrollBy(x - e.clientX, y - e.clientY);
      }
      x = e.clientX;
      y = e.clientY;
     }}
}