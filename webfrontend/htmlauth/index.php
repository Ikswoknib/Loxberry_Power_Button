<?php
require_once "loxberry_web.php";
  
// This will read your language files to the array $L
$template_title = "Power Button";
$helplink = "nopanels";
$helptemplate = "";
  
LBWeb::lbheader($template_title, $helplink, $helptemplate);
 
// This is the main area for your plugin
?>

Dieses Plugin ermöglicht es einen Power Button an GPIO anzuschließen

<br/>
<br/>
Zusätzlich gibt es an GPIO eine Rückmelde LED
<br/>

 
<?php 
// Finally print the footer 
LBWeb::lbfooter();
?>
