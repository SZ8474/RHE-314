# 1.28


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Upstart</title>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <meta name="keywords" content="poem, generator" />
  <meta name="date" content="2013-10-09" />
  <style type="text/css">a:link {text-decoration:none;}</style>
</head>
<body style="font-family: Helvetica, 'Nimbus Sans L', 'Liberation Sans', Arial, sans-serif; background:white; color:black; padding:14px 28px 0 28px">
<div style="text-align:center; font-size:15px; padding: 14px 0 28px 0;"><b style="font-size:20px">Upstart,</b> the morphological productivity of tomorrow, today. By <a href="http://nickm.com">Nick Montfort.</a></div>
<div style="width:628px; font-size:36px; margin-left:auto; margin-right:auto">
<div id="dotcom1" style="text-align:center; height:250px; width:800px; line-height:250px; background:red; color:white; float:left"></div>
<div id="dotcom3" style="text-align:center; height:250px; width:300px; line-height:250px; background:green; color:white; float:right"></div>
<div style="height:28px; clear:both"></div>
<div id="dotcom4" style="text-align:center; height:250px; width:300px; line-height:250px; background:blue; color:white; float:left; margin-bottom:28px"></div>
<div id="dotcom2" style="text-align:center; height:250px; width:300px; line-height:250px; background:orange; color:white; float:right; margin-bottom: 28px"></div>
</div>
<script type="text/javascript">
var panel = 1, names = [
    ['Drop', 'box'],
    ['Face', 'book'],
    ['You', 'tube'],
    ['Rock', 'star'],
    ['Net', 'flix'],
    ['Insta', 'gram'],
    ['Kick', 'starter'],
    ['Four', 'square'],
    ['Mash', 'able'],
    ['Micro', 'soft'],
    ['Red', 'hat'],
    ['Bit', 'coin'],
    ['Point', 'cast'],
    ['Path', 'finder'],
    ['Hot', 'bot'],
    ['Web', 'van'],
    ['Black', 'berry'],
    ['Nap', 'ster'],
    ['Seg', 'way'],
    ['Dot', 'com']
    ], fonts = [
    'Arial, Helvetica, sans-serif',
    'Arial Black, Gadget, sans-serif',
    'Impact, Charcoal, sans-serif',
    'Lucida Console, Monaco, monospace',
    'Lucida Sans Unicode, Lucida Grande, sans-serif',
    'Tahoma, Geneva, sans-serif',
    'Trebuchet, Trebuchet MS, sans-serif',
    'Verdana, Geneva, sans-serif'
    ]
function rand_index(len) {
    return Math.floor(Math.random() * len);
}
function update() {
    "use strict";
    var first, second, font, dotcomdiv = document.getElementById('dotcom' + panel);
    first = rand_index(names.length);
    second = rand_index(names.length - 1);
    if (second === first)
        { second = names.length - 1; }
    dotcomdiv.innerHTML = names[first][0] + names[second][1];
    panel = panel + 1;
    if (panel === 5)
        { panel = 1; }
    font = fonts[rand_index(fonts.length)];
    dotcomdiv.style.fontFamily = font;
}
update();
update();
update();
update();
setInterval(update, 20);
</script>
</body>
</html>
