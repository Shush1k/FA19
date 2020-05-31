<html><head>
<title> Вторая программа </title>
</head><body>
<?php
//Пример использования констант
print('Пример использования констант<br>');
define("koeff", 60);
$h = 3.5;
echo " Число минут в указанном значении в часах =" . $h * koeff . "<br>";
echo PHP_VERSION; 
?>
</body></html>