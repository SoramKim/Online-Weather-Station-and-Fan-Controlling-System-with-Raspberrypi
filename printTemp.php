<html>
<body>

<h1>Welcome to Soram's Temperature Station </h1> 
<?php 
$re=exec("cat /home/pi/final/OSS-Final-Project/tempLog_everySecond"); 
$tem_c=explode(" ",$re); 
echo ( "Time = ".date("Y-m-d H:i:s")." , Temperature = ".$tem_c[0]." C "." , Humidity = ".$tem_c[1]); 
?>

</body>
</html>


