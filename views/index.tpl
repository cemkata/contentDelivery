<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel='stylesheet' href='/static/style_main.css'>
<style>
* {
  box-sizing: border-box;
}

.collum {
  float: left;
  width: 48.9%;
  padding: 15px;
  margin-top: 7px;
  text-align: center;
  height: 80vh;
  line-height: 65vh;
  cursor: pointer;
  color: white;
}

#split {
  width: 1%;
  float: left;
  height: 80vh;
  line-height: 65vh;
}

@media only screen and (max-width: 1800px) {
  /* For small screens phones: */
  div{
      padding: 1px;
    }
}

@media only screen and (max-width: 620px) {
  /* For mobile phones: */
  .menu, #main, #right {
    width: 100%;
  }
  #main, #right {
    height: 35vh;
    line-height: 25vh;
  }
  #split {
    display: none;
  }
}
</style>
<script>
	function NewTab(url) {
		window.open(url, "_blank");
	}
</script>
<title>Materials managment</title>
<link rel="icon" type="image/x-icon" href="/favicon.ico">
</head>
<body style="font-family:Verdana;color:#aaaaaa;">

<div style="background-color:#e5e5e5;padding:0.33%;text-align:center;">
  <h2>Select:</h2>
</div>
% for app in app_names:
<div style="overflow:auto">
%if newTab:
  <div class="collum btnGreen" id="main" onclick="NewTab('.{{app[0][0]}}');">
%else:
  <div class="collum btnGreen" id="main" onclick="location.href='.{{app[0][0]}}';">
%end
    <h2>{{app[0][1]}}</h2>
  </div>
  <div id="split"></div>
%if newTab:
  <div class="collum btnRed" id="right" onclick="NewTab('.{{app[1][0]}}');">
%else:
  <div class="collum btnRed" id="right" onclick="location.href='.{{app[1][0]}}';">
%end
  
    <h2>{{app[1][1]}}</h2>
  </div>
</div>
% end
<div style="background-color:#e5e5e5;text-align:center;padding:0.25%;margin-top:7px;"><!-- footer / © copyright --></div>
</body>
</html>