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
<title>Materials managment</title>
<link rel="icon" type="image/x-icon" href="/favicon.ico">
</head>
<body style="font-family:Verdana;color:#aaaaaa;">

<div style="background-color:#e5e5e5;padding:0.33%;text-align:center;">
  <h2>Select:</h2>
</div>

<div style="overflow:auto">
  <div class="collum btnGreen" id="main" onclick="location.href='./simpleQuizEngine/main/';">
    <h2>View avalable quizes</h2>
  </div>
  <div id="split"></div>
  <div class="collum btnRed" id="right" onclick="location.href='./simpleQuizEngine/editor/';">
    <h2>Open editor</h2>
  </div>
</div>
<div style="overflow:auto">
  <div class="collum btnGreen" id="main" onclick="location.href='./flashcards/';">
    <h2>View flashcards</h2>
  </div>
  <div id="split"></div>
  <div class="collum btnRed" id="right" onclick="location.href='./flashcards/be/';">
    <h2>Open flashcards editor</h2>
  </div>
</div>
<div style="overflow:auto">
  <div class="collum btnGreen" id="main" onclick="location.href='./folderTreeView/';">
    <h2>View files/documents</h2>
  </div>
  <div id="split"></div>
  <div class="collum btnRed" id="right" onclick="location.href='./folderTreeOrganiser/';">
    <h2>Open files organiser</h2>
  </div>
</div>
<div style="background-color:#e5e5e5;text-align:center;padding:0.25%;margin-top:7px;"><!-- footer / © copyright --></div>

</body>
</html>