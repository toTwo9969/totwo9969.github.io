---
title: 相册
date: 2018-05-17 11:54:50
type: "photos"
comments: true
---
<link rel="stylesheet" href="/static/css/ins.css">
<link rel="stylesheet" href="/static/css/photoswipe.css">
<link rel="stylesheet" href="/static/css/default-skin.css">
<div class="photos-btn-wrap">
	<a class="photos-btn active" href="index.html" style="display:inline;color:red">Photos</a>
    <a class="photos-btn active" href="funny.html" style="display:inline">Funny</a>
</div>
<div class="instagram itemscope">
	<a href="https://mbinary.github.io" target="_blank" class="open-ins"><i class="fa fa-spinner"></i></a>
</div>
 
<script>
  (function() {
    var loadScript = function(path) {
      var $script = document.createElement('script')
      document.getElementsByTagName('body')[0].appendChild($script)
      $script.setAttribute('src', path)
    }
    setTimeout(function() {
        loadScript('https://mbinary.github.io/static/js/ins.js');
    }, 0)
  })()
</script>
