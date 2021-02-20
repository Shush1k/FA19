SELECT P.PID, P.FName, P.LName, T.idTicket, S.cost, Sc.flight, Sc.classType, Pl.idPlane, Pl.model, R.city_from, R.city_to
FROM Passenger P
JOIN Ticket T ON P.PID = T.PID
JOIN Sale S ON T.idSale = S.idSale
JOIN Schedule Sc ON S.idSchedule = Sc.idSchedule
JOIN Plane Pl ON Sc.idPlane = Pl.idPlane
JOIN Rout R ON Sc.idRout = R.idRout;