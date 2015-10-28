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
INSERT INTO "empresas" VALUES(1,'61808000-5','AGUAS ANDINAS S A');
INSERT INTO "empresas" VALUES(2,'18598138-k','SONIA GONZALEZ ');
INSERT INTO "empresas" VALUES(3,'0-0','SONIA GONZALEZ');
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
INSERT INTO "facturas" VALUES(1,0,1,1,142363,0,1,'2015-10-23',1,2,3120,14579,2770,20470,'123123','11070100','','2015-11-22',12312312,'',0,0,0,0,0,0,0,'','',0,'',0,1,0);
INSERT INTO "facturas" VALUES(8,1,12,1,500181,0,0,'2015-10-23',1,2,0,17201,3268,20470,'433434','11040100','','2015-11-22',12312312,'',1,0,0,0,0,0,0,'','',0,'',0,1,0);
INSERT INTO "facturas" VALUES(13,1,43443,1,44059,0,0,'2015-10-24',1,2,0,17201,3268,20470,'433434','11040100','','2015-11-23',12312312,'',1,0,0,0,0,0,0,'','',0,'',0,1,0);
INSERT INTO "facturas" VALUES(16,1,43443,1,419180,0,0,'2015-09-24',1,2,4342,13552,2575,20470,'433434','4444','','2015-10-24',12312312,'',1,0,0,0,0,0,0,'','',0,'',0,1,0);
INSERT INTO "facturas" VALUES(17,0,43443,39,22322842,0,0,'2013-07-26',1,3,0,5748,1092,6841,'433434','4444','','',12312312,'',1,0,0,0,0,0,0,'','',0,'',0,0,0);
CREATE TABLE usuario(id INTEGER PRIMARY KEY, 
								username TEXT, 
								pass TEXT, 
								activo INTEGER DEFAULT 1
								);
COMMIT;
