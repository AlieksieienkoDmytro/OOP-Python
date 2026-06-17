INSERT INTO privatkunde
(name, address, email, phone, password, birthdate)
VALUES
    ('Max Verstappen', 'Red Bull Ring Straße 1', 'max@verstappen.com', '+436641111111', 'Password123', '1997-09-30'),
    ('Lando Norris', 'McLaren Avenue 7', 'lando@norris.com', '+436642222222', 'Password123', '1999-11-13'),
    ('Charles Leclerc', 'Monaco Harbor 12', 'charles@leclerc.com', '+436643333333', 'Password123', '1997-10-16');


INSERT INTO firmenkunde
(name, address, email, phone, password, company_id)
VALUES
    ('Red Bull Racing GmbH', 'Milton Keynes, UK', 'info@redbullracing.com', '+441901111111', 'Business123', 'RBR-001'),
    ('Mercedes AMG Petronas', 'Brackley, UK', 'info@mercedesf1.com', '+441902222222', 'Business123', 'MER-001'),
    ('Ferrari S.p.A.', 'Maranello, Italy', 'info@ferrari.com', '+390533333333', 'Business123', 'FER-001');


INSERT INTO buch
(name, price, weight, author, pages)
VALUES
    ('Python Crash Course', 35.99, 0.80, 'Eric Matthes', 544),
    ('Clean Code', 42.50, 0.95, 'Robert C. Martin', 464),
    ('Design Patterns', 55.00, 1.10, 'Erich Gamma', 395),
    ('The Pragmatic Programmer', 39.90, 0.75, 'Andrew Hunt', 352),
    ('Fluent Python', 59.99, 1.25, 'Luciano Ramalho', 1014);


INSERT INTO elektronik
(name, price, weight, brand, warranty_years)
VALUES
    ('MacBook Pro 14', 2499.99, 2.10, 'Apple', 2),
    ('ThinkPad X1 Carbon', 1899.99, 1.35, 'Lenovo', 3),
    ('Galaxy S25 Ultra', 1399.99, 0.23, 'Samsung', 2),
    ('iPhone 17 Pro', 1499.99, 0.22, 'Apple', 2),
    ('RTX 5080', 1299.99, 1.80, 'NVIDIA', 3);


INSERT INTO kleidung
(name, price, weight, size, color)
VALUES
    ('BMW Motorsport Hoodie', 79.99, 0.70, 'L', 'Black'),
    ('Ferrari Team T-Shirt', 39.99, 0.25, 'M', 'Red'),
    ('Red Bull Racing Cap', 29.99, 0.15, 'One Size', 'Navy'),
    ('Mercedes Jacket', 119.99, 0.95, 'XL', 'Black'),
    ('Puma Sneakers', 89.99, 0.85, '43', 'White');