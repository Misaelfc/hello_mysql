
-- Obtiene las 3 primeras filas de la tabla "users"
SELECT * FROM users LIMIT 3;
-- Obtienes las 32 primeras filas de la tabla "users" con email distinto a sara@gmail.com
SELECT * FROM users WHERE NOT email = 'sara@gmail.com' OR age = 15 LIMIT 2;


