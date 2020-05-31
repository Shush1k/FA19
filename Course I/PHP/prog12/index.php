<?php
require_once('./connector.php');
$result = mysqli_query($link, "SELECT * FROM simple_users ORDER BY name");

print('
  <form action="./start.php" method="post">
  <br>

  Выберите логин:
  <select name="id" id="exampleFormControlSelect1">
  ');

while ($row = $result->fetch_assoc())
    print("<option value='" . $row["id"] . "'>" . $row['name']);


print("</select>
    <br>Введите пароль:<input type='password'  name='password'>
  <br>

  <input name='enterStart' type='submit'  value='Перейти к работе с базой'>
    <br>
  </form>
  ");

?>

</body>
</html>