<?php 
$re=exec("cat /home/pi/final/OSS-Final-Project/tempLog"); 
$tem_c=explode(" ",$re); //현재 시간 과 온도값을 천으로 나누고, 소숫점 둘째자리에서 반올림 해서 출력한다. 
echo ( "Time = ".date("Y-m-d H:i:s")." , Temperature = ".$tem_c[1]." C "); 
?>

