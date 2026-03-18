CREATE TABLE lager
(
    ProductName             varchar(255),
    ProductID               serial PRIMARY KEY,
    ProductStockQuantity    integer,
    ProductLocation         varchar(255)
);

INSERT INTO lager (ProductName, ProductID, ProductStockQuantity, ProductLocation)
VALUES
('Sko',      22341,     52,     'Ballerup'),
('T-shirt',  88321,     10,     'Odense'),
('Jakke #1', 55321,     200,    'Aarhus'),
('Bukser',   25321,     0,      'København'),
('Undertøj', 78321,     300,    'Ballerup');
