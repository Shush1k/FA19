<?php

require_once('./connector.php');

if (isset($_POST['enterNew'])) // Если это результат обработки формы данного файла
{
    $nwarehouse = $_POST['nwarehouse'];
    $ngood = $_POST['ngood'];
    $namount = $_POST['namount'];

    $query = "INSERT INTO goods (warehouse_id, name, amount) VALUES (" . $nwarehouse . ",'" . $ngood . "'," . $namount . ")";
    mysqli_query($link, $query);
}

$sql = "SELECT name, warehouse_id, amount FROM goods ORDER BY name";
$data = mysqli_query($link, $sql);

print('
    <font style="font-size:16pt">
        Имеющиеся позиции товаров :</font>
    <table border=1>
    ');

while ($line = $data->fetch_assoc()) {
    print('<tr><td>' . $line["name"] . '</td>');
    $bufresult = mysqli_query($link, "SELECT name FROM warehouse WHERE id=" . $line["warehouse_id"])->fetch_assoc()["name"];
    print("<td>" . $bufresult . "</td>");
    print("<td>" . $line["amount"] . "</td></tr>");
}

print('
    </table>
    <div style="position:absolute;top:5;left:500">
    <font size="+2"> Форма ввода новых товаров</font>
    <form method="post" action="">
        <font style="font-size:16pt">
            Название нового товара :<input type="text" name="ngood" value=""><br>
            <br>
    ');

$warehouse_result = mysqli_query($link, "SELECT id, name FROM warehouse");
print('Склад  :<select  name="nwarehouse">');


while ($line3 = $warehouse_result->fetch_assoc()) {
    print("<option value='" . $line3["id"] . "'>" . $line3["name"]);
}

print("</select><br><br>
            Количество :<input type='text' name='namount' value=''><br>
            <br><br>
            <br><input name='enterNew' type='submit' value='Ввести товар'>
    </form>
    <br><a href='index.php'>Вернуться на главную страницу </a>
    </div>
    ");
