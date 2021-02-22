SELECT *
FROM Passenger P
JOIN Booking B ON P.PID = B.PID
JOIN Flight F ON B.idFlight = F.idFlight
JOIN Route R ON F.idRoute = R.idRoute;