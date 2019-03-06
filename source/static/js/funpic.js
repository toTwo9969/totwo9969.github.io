<button type="button" onclick="f()">下一张搞笑图片~</button>
<img id="pic" style="width:300px;border:none;" src="">
<span id="joke" style="font-size:16px;align:center;display:block"></span>
<script>
    var jpgN = 56,pngN = 23,gifN=11;
    function f(){
        var preUrl ="https://mbinary0.github.io/resource/funnyPic/"
        var url;
        var num;
        if(Math.random()<0.33){
            num = Math.floor((Math.random()*jpgN));
            url = preUrl +"jpg/haha"+ num + ".jpg";
        }
        else if(Math.random()<0.66){
            num = Math.floor((Math.random()*pngN));
            url = preUrl +"png/haha"+ num + ".png";
        }
        else{
            num = Math.floor((Math.random()*gifN));
            url = preUrl +"gif/haha"+ num + ".gif";
        }
        var pic = document.getElementById("pic");
        pic.setAttribute("src",url);
    }
    window.onload = f;
</script>
