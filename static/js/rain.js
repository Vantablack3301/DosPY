class Drop {
    constructor () {
        this.y=(Math.random()*100)-100;
        this.x=Math.random()*100;
        this.speed=Math.random()*8+2;
        this.height=Math.random()*9+12;
    }
    show () {
        if (this.y>=100) {
            this.y=(Math.random()*100)-100;
            this.x=Math.random()*100;
            this.speed=Math.random()*8+3;            
        }

        this.y+=this.speed;
        $('body').append('<div class="drop" id="'+this.y+'" style="height:'+this.height+'px;top:'+this.y+'%;left:'+this.x+'%"></div>');
    }
}

var drops=[];//Makes the drops
for (var i=0; i<=700; i++) {
    drops.push(new Drop());
}

function draw() {//Draws the drops
    $('body').html('');
    for (var i=0; i<=100; i++) {
        drops[i].show();
    }
}

setInterval(draw, 1);