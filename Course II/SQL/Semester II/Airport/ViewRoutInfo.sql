SELECT Sc.idSchedule , Sc.flight 'Рейс', Sc.classType 'класс', Sc.Date 'Дата', Pl.model 'Модель самолета', R.city_from 'Откуда', R.city_to 'Куда', R.flightTime 'Время полета', R.cost 'Цена'
FROM Schedule Sc
JOIN Plane Pl ON Sc.idPlane = Pl.idPlane
JOIN Rout R ON Sc.idRout = R.idRout;