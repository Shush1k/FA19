<html><head>
<title> Четвертая программа </title>
</head><body>
<?php
//Работа с файлами в PHP, а также счетчик
print("Работа с файлами в PHP и счетчик посещений сайта<br>");
$file = "counter.txt";
//и зачем тут код который никогда не выполнится? мы же создаем файл в любом случае "or die("Файл не открывается")"
$f = fopen($file, 'a+t');
flock($f,2);
$counter = fgets($f);
$counter++;
ftruncate($f,0);
fputs($f,$counter);
flock($f,3);
fclose($f);
echo $counter;
?>
</body></html>