CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  stock INTEGER DEFAULT 0
);

-- Do not modify above this line --

INSERT INTO products (name, id)
  VALUES ('Apple', 1),
    ('Banana', 2),
    ('Orange', 3);



-- Do not modify below this line --
SELECT * FROM products;
