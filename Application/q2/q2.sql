SELECT Salesperson.Name
FROM Salesperson
INNER JOIN Orders
ON Salesperson.ID = Orders.salesperson_id
;