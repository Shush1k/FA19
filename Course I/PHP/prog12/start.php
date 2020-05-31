<?php
if (isset($_POST['enterStart'])) // Проверка - является ли скрипт результатом ввода формы
{
    require_once('./connector.php');

    $pass = md5($_POST['password']);
    $sql = "SELECT name, password FROM simple_users WHERE id=" . $_POST['id'] . " and password='" . $pass . "'";

    $result = mysqli_query($link, $sql);
    if ($result->num_rows == 0)
        die("Неверный пароль<br><a  href='./index.php' role='button'>Назад</a>");
    else
        print("Авторизация прошла успешно!
        <form action='pr.php' method='post'>
        <div class='form-group row'>    
        <input name='add1'  type='submit' value='Перейти к работе'>
        </div>
        </form>"
        );


} else
    print('<a  href="index.php">Вернуться на главную страницу </a>');

?>
</body>
</html>