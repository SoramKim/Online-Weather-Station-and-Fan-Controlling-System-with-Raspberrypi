<html>
<body>

<p style="font-size:64px; color:#008080; family:'돋움'";>
Welcome to my Weather Station <br> 
</p>
<p style="font-size:48px; color:#808080; family:'돋움'";>
Current temperature and humidity in my room <br> 
</p>

<?php 
$re=exec("cat /home/pi/final/OSS-Final-Project/tempLog_everySecond"); 
$tem_c=explode(" ",$re); 
echo ("<font size= 10>"."Time = ".date("Y-m-d H:i:s")."<br>"."Temperature = ".$tem_c[0]." C "."<br>"."Humidity = ".$tem_c[1]." %"); 
?> 

</body>
</html>


