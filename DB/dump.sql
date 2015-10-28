BEGIN TRANSACTION;
CREATE TABLE usuario(id INTEGER PRIMARY KEY, 
								username TEXT, 
								pass TEXT, 
								activo INTEGER DEFAULT 1
								);
COMMIT;
