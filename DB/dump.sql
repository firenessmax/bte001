BEGIN TRANSACTION;
CREATE TABLE bitacora(id INTEGER PRIMARY KEY, 
								fecha TEXT,
								tipo INTEGER, 
								evento TEXT, 
								so TEXT, 
								idUsuario INTEGER DEFAULT 0
								);
CREATE TABLE empresas(id INTEGER PRIMARY KEY,
								rut TEXT, 
								razonSocial TEXT
								);
INSERT INTO "empresas" VALUES(1,'17920814-8','loco');
INSERT INTO "empresas" VALUES(2,'17966491-7','asdasd');
INSERT INTO "empresas" VALUES(3,'18274169-8','Matias');
CREATE TABLE facturas(id INTEGER PRIMARY KEY,
	 							venta INTEGER  DEFAULT 0,
								sucursal INTEGER, 
								TipoDocumento INTEGER, 
								numDocumento INTEGER, 
								nulo INTEGER DEFAULT 0, 
								correlativo INTEGER, 
								fecha TEXT, 
								idEmisor INTEGER,
								
								idReceptor INTEGER,
								montoExento INTEGER, 
								montoAfecto INTEGER, 
								montoIVA INTEGER, 
								montoTotal INTEGER, 
								Glosa TEXT, 
								cuentaProveedores TEXT, 
								codigoEspecial TEXT, 
								fechaVencimiento TEXT, 
								contracuenta INTEGER, 
								centroResultados TEXT, 
								activoFijo INTEGER DEFAULT 0, 
								sinDerechoaCredito INTEGER DEFAULT 0, 
								conCreditoFiscal INTEGER DEFAULT 0, 
								mImpuestoEspecifico1 INTEGER, 
								mImpuestoEspecifico2 INTEGER, 
								impuestoEspecificoFijo INTEGER, 
								impuestoEspecificoVariable INTEGER, 
								M3 TEXT, 
								CodImpuesto2 TEXT, 
								montoImpuesto2 INTEGER, 
								codImpuesto3 TEXT, 
								montoImpuesto3 INTEGER, 
								contabilizado INTEGER DEFAULT 0, 
								idUsuario INTEGER DEFAULT 0,
								FOREIGN KEY(idEmisor) REFERENCES empresas(id),
								FOREIGN KEY(idReceptor) REFERENCES empresas(id)
								);
INSERT INTO "facturas" VALUES(1,0,1,1,9,0,620,'2015-10-02',1,2,0,0,0,0,'','0','','2015-11-01',0,'',0,0,0,0,0,0,0,'','',0,'',0,0,0);
INSERT INTO "facturas" VALUES(2,1,1,1,1,0,0,'2015-10-02',1,2,0,0,0,0,'','0','','',0,'',0,0,0,0,0,0,0,'','',0,'',0,0,0);
INSERT INTO "facturas" VALUES(3,1,1,1,2,0,0,'2015-10-02',1,2,0,0,0,0,'','0','','',0,'',0,0,0,0,0,0,0,'','',0,'',0,0,0);
INSERT INTO "facturas" VALUES(4,1,1,1,3,0,0,'2015-10-02',1,2,0,0,0,0,'','0','','',0,'',0,0,0,0,0,0,0,'','',0,'',0,0,0);
INSERT INTO "facturas" VALUES(5,1,1,1,4,0,0,'2015-10-02',1,2,0,0,0,0,'','0','','',0,'',0,0,0,0,0,0,0,'','',0,'',0,0,0);
INSERT INTO "facturas" VALUES(6,0,1,1,4,0,621,'2015-10-02',1,2,0,0,0,0,'','0','','',0,'',0,0,0,0,0,0,0,'','',0,'',0,0,0);
INSERT INTO "facturas" VALUES(7,0,1,1,8,0,622,'2015-10-02',1,2,0,0,0,0,'','0','','',0,'',0,0,0,0,0,0,0,'','',0,'',0,0,0);
INSERT INTO "facturas" VALUES(8,0,1,1,65151651,0,0,'2015-10-02',3,1,0,0,0,0,'','0','','',0,'',0,0,0,0,0,0,0,'','',0,'',0,0,0);
CREATE TABLE usuario(id INTEGER PRIMARY KEY, 
								username TEXT, 
								pass TEXT, 
								activo INTEGER DEFAULT 1
								);
COMMIT;
