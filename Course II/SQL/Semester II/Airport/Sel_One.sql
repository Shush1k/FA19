SELECT P.PID, P.FName, P.LName, T.idTicket, T.class, T.booking_date, T.seat
FROM Passenger P
JOIN Passenger_Ticket PT ON P.PID = PT.Passenger_PID
JOIN Ticket T ON PT.idTicket = T.idTicket;
