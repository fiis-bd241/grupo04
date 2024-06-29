CREATE TABLE Almacen(
	id_almacen CHAR(2) PRIMARY KEY,
	tipo_almacen VARCHAR(50) NOT NULL,
	descripcion_almacen VARCHAR(150) NOT NULL
);

CREATE TABLE Secciones(
	seccion CHAR(1) PRIMARY KEY,
	peso_soporta DECIMAL(5,1) NOT NULL,
	id_almacen CHAR(2),	
	CHECK (peso_soporta>0),
	CONSTRAINT sector FOREIGN KEY (id_almacen) REFERENCES almacen(id_almacen)
);

CREATE TABLE Repisas(
	seccion CHAR(1),
	id_repisas CHAR(2),
	altura DECIMAL(5,1) NOT NULL,
	CHECK (altura BETWEEN 15.0 AND 300.0),
	PRIMARY KEY (seccion,id_repisas),
	FOREIGN KEY (seccion) REFERENCES secciones(seccion)
);

CREATE TABLE Estands(
	seccion CHAR(1),
	id_stand CHAR(2),
	largo DECIMAL(5,1) NOT NULL,
	ancho DECIMAL(5,1) NOT NULL,
	CHECK(largo BETWEEN 30.0 AND 300.0),
	CHECK(ancho BETWEEN 30.0 AND 100.0),
	PRIMARY KEY (seccion,id_stand),
	FOREIGN KEY (seccion) REFERENCES secciones(seccion)
);
	
CREATE TABLE Ubicacion(
	seccion CHAR(1),
	id_stand CHAR(2),	
	id_repisas CHAR(2),
	PRIMARY KEY(seccion,id_stand,id_repisas),
	FOREIGN KEY(seccion,id_repisas) REFERENCES Repisas(seccion,id_repisas),
	FOREIGN KEY(seccion,id_stand) REFERENCES Estands(seccion,id_stand)
);

CREATE TABLE Tipo_Producto(
	id_tipo_producto SERIAL PRIMARY KEY,
	nombre_tipo_producto VARCHAR(50) NOT NULL
);

CREATE TABLE Categoria_Producto(
	nombre_categoria VARCHAR(20) PRIMARY KEY,
	funcion_principal VARCHAR(150) NOT NULL,
	id_tipo_producto INT,
	CONSTRAINT sub FOREIGN KEY (id_tipo_producto) REFERENCES Tipo_Producto(id_tipo_producto)
);

CREATE TABLE Funciones_Categoria (
	id_funcion SERIAL PRIMARY KEY,
	nombre_funcion VARCHAR(100) NOT NULL,
	caracteristica_general VARCHAR(200)
);

CREATE UNIQUE INDEX idx_nombre_funcion ON Funciones_Categoria(nombre_funcion);

CREATE TABLE CategoriaxFunciones (
	nombre_categoria VARCHAR(20),
	id_funcion INT,
	caracteristica_especifica VARCHAR(200),
	PRIMARY KEY(nombre_categoria,id_funcion),
	FOREIGN KEY(nombre_categoria) REFERENCES Categoria_Producto(nombre_categoria),
	FOREIGN KEY(id_funcion) REFERENCES Funciones_Categoria(id_funcion)
);

CREATE TABLE Categoria_Producto_Zona(
	nombre_categoria VARCHAR(20),
	zona VARCHAR(10),
	PRIMARY KEY(nombre_categoria,zona),
	FOREIGN KEY (nombre_categoria) REFERENCES Categoria_Producto(nombre_categoria) ON DELETE CASCADE
);

CREATE TABLE Categoria_Producto_Sub_Tipo_Existe(
	nombre_categoria VARCHAR(20),
	sub_tipo_existe VARCHAR(30),
	PRIMARY KEY(nombre_categoria,sub_tipo_existe),
	FOREIGN KEY (nombre_categoria) REFERENCES Categoria_Producto(nombre_categoria)
);

CREATE TABLE Marca(
	id_marca VARCHAR(30) PRIMARY KEY,
	rubro VARCHAR(100) NOT NULL
);

CREATE TABLE Presentacion(
	id_presentacion SERIAL PRIMARY KEY,
	tipo_presentacion VARCHAR(30)
);

CREATE UNIQUE INDEX idx_tipo_presentacion ON Presentacion(tipo_presentacion);

CREATE TABLE Colores(
	id_color SERIAL PRIMARY KEY,
	nombre_color VARCHAR(30) NOT NULL,
	cod_hexa CHAR(7)
);

CREATE UNIQUE INDEX idx_cod_hexa ON Colores(cod_hexa);
CREATE UNIQUE INDEX idx_nombre_color ON Colores(nombre_color);

CREATE TABLE Proveedor(
	ruc_proveedor CHAR(11) PRIMARY KEY,
  	razon_social VARCHAR(100) NOT NULL,
	contacto VARCHAR(50) NOT NULL,
	telefono_contacto VARCHAR(12) NOT NULL,
	correo_proveedor VARCHAR(60),
	ciudad_proveedor VARCHAR(100) NOT NULL,
	direccion_proveedor VARCHAR(255),
  	sitio_web VARCHAR(100),
	id_tipo_producto INT,
  	fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	observaciones VARCHAR(200),
	CONSTRAINT oferta FOREIGN KEY (id_tipo_producto) REFERENCES Tipo_Producto(id_tipo_producto)
);

CREATE UNIQUE INDEX idx_telefono_contacto ON Proveedor(telefono_contacto);

CREATE TABLE Producto(
	id_producto VARCHAR(8) PRIMARY KEY,
	id_presentacion INT,
	id_color INT,
	nombre_producto VARCHAR(100) NOT NULL,
	id_marca VARCHAR(30),
	especificaciones VARCHAR(150) NOT NULL,
	observaciones VARCHAR(150),
	precio_unitario DECIMAL(6,2) NOT NULL,
	peso_unitario DECIMAL(6,3) NOT NULL,
	ancho_present DECIMAL(4,1) NOT NULL,
	largo_present DECIMAL(4,1) NOT NULL,
	alto_present DECIMAL(4,1) NOT NULL,
	fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	cantidad_minima INT NOT NULL,
	valoracion INT NOT NULL,
	nombre_categoria VARCHAR(20),
	FOREIGN KEY (id_presentacion) REFERENCES Presentacion(id_presentacion),
	FOREIGN KEY (id_color) REFERENCES Colores(id_color),
	FOREIGN KEY (id_marca) REFERENCES Marca(id_marca),
	FOREIGN KEY (nombre_categoria) REFERENCES Categoria_Producto(nombre_categoria)
);

CREATE OR REPLACE FUNCTION actualizar_fecha_actualizacion()
RETURNS TRIGGER AS $$
BEGIN
    NEW.fecha_actualizacion = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER actualizar_fecha_actualizacion_trigger
BEFORE UPDATE ON Producto
FOR EACH ROW
EXECUTE FUNCTION actualizar_fecha_actualizacion();

CREATE TABLE ProductoxProveedor(
	ruc_proveedor CHAR(11),
	id_producto VARCHAR(8),
	precio_unit_prod_prov DECIMAL(6,2) NOT NULL,
	precio_mayor_prod_prov DECIMAL(6,2),
	cantidad_min_mayor INT,
	PRIMARY KEY (ruc_proveedor,id_producto),
	FOREIGN KEY (ruc_proveedor) REFERENCES Proveedor(ruc_proveedor),
	FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

CREATE TABLE Imagenes(
	id_imagen SERIAL PRIMARY KEY,
	path_imagen VARCHAR(255) NOT NULL,
	largo_imagen INT NOT NULL,
	alto_imagen INT NOT NULL,
	profundidad_bits INT NOT NULL,
	id_producto VARCHAR(8),
	CONSTRAINT tamañokb FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)	
);

CREATE TABLE Inventario(
	id_inventario SERIAL PRIMARY KEY,
	id_producto VARCHAR(8),	
	entradas INT NOT NULL,
	salidas INT NOT NULL,	
	seccion CHAR(1),
	id_stand CHAR(2),
	id_repisas CHAR(2),
	ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,	
	FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
	CONSTRAINT lugar FOREIGN KEY (seccion,id_stand,id_repisas) REFERENCES Ubicacion(seccion,id_stand,id_repisas)
);

CREATE OR REPLACE FUNCTION actualizar_ultima_actualizacion()
RETURNS TRIGGER AS $$
BEGIN
    NEW.ultima_actualizacion = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER actualizar_ultima_actualizacion_trigger
BEFORE UPDATE ON Inventario
FOR EACH ROW
EXECUTE FUNCTION actualizar_ultima_actualizacion();

CREATE TABLE Rol(
	id_rol CHAR(3) PRIMARY KEY,
	nombre_rol VARCHAR(50) NOT NULL,
	nivel_rol INT NOT NULL
);

CREATE TABLE Persona(
	id_persona VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	primer_apellido VARCHAR(50) NOT NULL,
	segundo_apellido VARCHAR(50) NOT NULL,
	fecha_nacimiento DATE NOT NULL,
	sexo_persona CHAR(1) NOT NULL,
	correo_persona VARCHAR(200) UNIQUE,
	telefono_persona CHAR(9) NOT NULL,
	id_rol CHAR(3),
	FOREIGN KEY (id_rol) REFERENCES Rol(id_rol)
);

CREATE UNIQUE INDEX idx_correo_persona ON Persona(correo_persona);
CREATE UNIQUE INDEX idx_telefono_persona ON Persona(telefono_persona);

CREATE TABLE Area(
	cod_area CHAR(2) PRIMARY KEY,
	nombre_area VARCHAR(20) NOT NULL,
	funcion_area VARCHAR(200) NOT NULL
);

CREATE TABLE Gestor(
	id_persona VARCHAR(10) PRIMARY KEY,
	nombre_usuario VARCHAR(20) UNIQUE NOT NULL,
	contraseña_trabajador VARCHAR(25) NOT NULL,
	fecha_ingreso DATE NOT NULL,
	cod_area CHAR(2),
	id_gestor VARCHAR(10),
	CHECK (LENGTH(contraseña_trabajador)>=8),
	FOREIGN KEY (id_persona) REFERENCES Persona(id_persona),
	FOREIGN KEY (cod_area) REFERENCES Area(cod_area),
	FOREIGN KEY (id_gestor) REFERENCES Gestor(id_persona)
);

CREATE TABLE Estado_Cliente(
	id_estado_cliente CHAR(1) PRIMARY KEY,
	nombre_estado_cliente VARCHAR(30) NOT NULL
);

CREATE TABLE Cliente(
	id_persona VARCHAR(10) PRIMARY KEY,
	nombre_usuario VARCHAR(20) UNIQUE NOT NULL,
	contraseña_cliente VARCHAR(25) NOT NULL,
	fecha_registro DATE NOT NULL,
	login_ultimo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	id_estado_cliente CHAR(1),
	CHECK (LENGTH(contraseña_cliente)>=8),
	FOREIGN KEY (id_persona) REFERENCES Persona(id_persona),
	FOREIGN KEY (id_estado_cliente) REFERENCES Estado_Cliente(id_estado_cliente)
);

CREATE MATERIALIZED VIEW nombre_usuario_unificado AS
SELECT nombre_usuario FROM Gestor
UNION
SELECT nombre_usuario FROM Cliente
UNION
SELECT nombre_usuario FROM Repartidor;

CREATE UNIQUE INDEX idx_nombre_usuario_unificado ON nombre_usuario_unificado(nombre_usuario);

CREATE OR REPLACE FUNCTION actualizar_login_ultimo()
RETURNS TRIGGER AS $$
BEGIN
    NEW.login_ultimo = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER actualizar_login_ultimo_trigger
BEFORE UPDATE ON Cliente
FOR EACH ROW
EXECUTE FUNCTION actualizar_login_ultimo();

CREATE TABLE Zona(
	id_zona SERIAL PRIMARY KEY,
	nombre_zona VARCHAR(50)
);

CREATE TABLE Zona_distritos_principales(
	id_zona INT,
	distritos_principales VARCHAR(50) NOT NULL,
	orden INT NOT NULL,
	tiempo_promedio INT NOT NULL,
	PRIMARY KEY (id_zona,distritos_principales),
	FOREIGN KEY (id_zona) REFERENCES Zona(id_zona)
);

CREATE TABLE Direccion_Cliente(
	id_direccion SERIAL PRIMARY KEY,
	departamento VARCHAR(50) NOT NULL,
	provincia VARCHAR(50) NOT NULL,
	distrito VARCHAR(50) NOT NULL,
	direccion VARCHAR(255) NOT NULL,
	numero_direccion INT NOT NULL,
	tipo_vivienda CHAR(1) NOT NULL,
	numero_departamento INT,
	referencia VARCHAR(255),
	id_zona INT,
	FOREIGN KEY (id_zona) REFERENCES Zona(id_zona)
);

CREATE TABLE ClientexDireccion_Cliente(
	id_persona VARCHAR(10),
	id_direccion INT,
	FOREIGN KEY (id_persona) REFERENCES Cliente(id_persona),
	FOREIGN KEY (id_direccion) REFERENCES Direccion_Cliente(id_direccion)
);

CREATE TABLE Estado_Repartidor(
	id_estado_repartidor CHAR(1) PRIMARY KEY,
	nombre_estado_repartidor VARCHAR(20) NOT NULL
);

CREATE TABLE Repartidor(
	id_persona VARCHAR(10) PRIMARY KEY,
	nombre_usuario VARCHAR(20) UNIQUE NOT NULL,
	contraseña_repartidor VARCHAR(25) NOT NULL,
	fecha_ingreso DATE NOT NULL,
	tipo_transporte VARCHAR(30) NOT NULL,
	color_transporte VARCHAR(20) NOT NULL,
	nro_placa CHAR(7) NOT NULL,
	nro_licencia CHAR(10) NOT NULL,
	id_estado_repartidor CHAR(1),
	FOREIGN KEY (id_persona) REFERENCES Persona(id_persona),
	FOREIGN KEY (id_estado_repartidor) REFERENCES Estado_Repartidor(id_estado_repartidor)
);

CREATE TABLE RepartidorxZona(
	id_persona VARCHAR(10),
	id_zona INT,
	FOREIGN KEY (id_persona) REFERENCES Repartidor(id_persona),
	FOREIGN KEY (id_zona) REFERENCES Zona(id_zona)
);

CREATE TABLE Tipo_Movimiento(
	id_tipo_mov SERIAL PRIMARY KEY,
	nombre_movimiento VARCHAR(30) NOT NULL
);

CREATE TABLE Kardex(
	id_kardex VARCHAR(10) PRIMARY KEY,
	fecha_kx TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	id_tipo_mov INT,
	id_pedido VARCHAR(10),
	id_tipo_entrega CHAR(1),
	id_cotizacion VARCHAR(15),
	FOREIGN KEY (id_tipo_mov) REFERENCES Tipo_Movimiento(id_tipo_mov),
	FOREIGN KEY (id_pedido,id_tipo_entrega) REFERENCES Pedido(id_pedido,id_tipo_entrega),
	FOREIGN KEY (id_cotizacion) REFERENCES Cotizacion(id_cotizacion)
);

CREATE TABLE KardexxProducto(
	id_kardex VARCHAR(10),
	id_producto VARCHAR(8),
	cantidad_kx INT NOT NULL,
	observacion_kx VARCHAR(255),
	PRIMARY KEY(id_kardex,id_producto),
	FOREIGN KEY (id_kardex) REFERENCES Kardex(id_kardex),
	FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

CREATE TABLE Estado_Compra(
	id_estado_compra CHAR(1) PRIMARY KEY,
	nombre_estado_compra VARCHAR(50) NOT NULL
);

CREATE TABLE ClientexProducto(
	id_persona VARCHAR(10),
	id_producto VARCHAR(8),
	cantidad INT NOT NULL,
	fecha_inicio_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	check_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	id_estado_compra CHAR(1),
	PRIMARY KEY(id_persona,id_producto),
	FOREIGN KEY (id_persona) REFERENCES Cliente(id_persona),
	FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
	FOREIGN KEY (id_estado_compra) REFERENCES Estado_Compra(id_estado_compra)
);

CREATE OR REPLACE FUNCTION actualizar_check_compra()
RETURNS TRIGGER AS $$
BEGIN
    NEW.check_compra = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER actualizar_check_compra_trigger
BEFORE UPDATE ON ClientexProducto
FOR EACH ROW
EXECUTE FUNCTION actualizar_check_compra();

CREATE TABLE Estado_Venta(
	id_estado_venta CHAR(1) PRIMARY KEY,
	nombre_estado_venta VARCHAR(50) NOT NULL
);

CREATE TABLE Tipo_Pago(
	id_tipo_pago CHAR(1) PRIMARY KEY,
	nombre_tipo_pago VARCHAR(50) NOT NULL
);

CREATE TABLE Cupon(
	id_cupon VARCHAR(10) PRIMARY KEY,
	descripcion_cupon VARCHAR(200) NOT NULL,
	fecha_inicio_cupon DATE NOT NULL,
	fecha_fin_cupon DATE NOT NULL,
	descuento_cupon DECIMAL(3,2) NOT NULL,
	estado_activo BOOLEAN
);

CREATE TABLE Venta(
	cod_venta VARCHAR(10),
	id_cupon VARCHAR(10),
	id_persona VARCHAR(10),
	fecha_pago TIMESTAMP,
	monto_final DECIMAL(6,2) NOT NULL,
	id_tipo_pago CHAR(1),
	nro_tarjeta CHAR(16),
	comentarios_venta VARCHAR(255),
	id_estado_venta CHAR(1),
	PRIMARY KEY(cod_venta,id_persona),
	FOREIGN KEY (id_cupon) REFERENCES Cupon(id_cupon),
	FOREIGN KEY (id_persona) REFERENCES Cliente(id_persona),
	FOREIGN KEY (id_tipo_pago) REFERENCES Tipo_Pago(id_tipo_pago),
	FOREIGN KEY (id_estado_venta) REFERENCES Estado_Venta(id_estado_venta)
);

CREATE TABLE Estado_Pedido(
	id_estado_pedido CHAR(1) PRIMARY KEY,
	nombre_estado_pedido VARCHAR(30) NOT NULL
);

CREATE TABLE Tipo_Entrega(
	id_tipo_entrega CHAR(1) PRIMARY KEY,
	nombre_tipo_entrega VARCHAR(30) NOT NULL
);

CREATE TABLE Pedido(
	id_pedido VARCHAR(10),
	id_tipo_entrega CHAR(1),
	fecha_entrega DATE NOT NULL,
	check_salida TIMESTAMP,
	check_entrega TIMESTAMP,
	id_estado_pedido CHAR(1),
	cod_venta VARCHAR(10),
	id_persona VARCHAR(10),
	id_repartidor VARCHAR(10),
	PRIMARY KEY(id_pedido,id_tipo_entrega),
	FOREIGN KEY (id_tipo_entrega) REFERENCES Tipo_Entrega(id_tipo_entrega),
	FOREIGN KEY (id_estado_pedido) REFERENCES Estado_Pedido(id_estado_pedido),
	FOREIGN KEY (cod_venta,id_persona) REFERENCES Venta(cod_venta,id_persona),
	FOREIGN KEY (id_repartidor) REFERENCES Repartidor(id_persona)
);

CREATE TABLE Estado_Cotizacion(
	id_estado_cot CHAR(1) PRIMARY KEY,
	nombre_estado_cot VARCHAR(30) NOT NULL
);

CREATE TABLE Cotizacion(
	id_cotizacion VARCHAR(15) PRIMARY KEY,
	fecha_recibida TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	fecha_expira DATE NOT NULL,
	ruc_proveedor CHAR(11),
	id_estado_cot CHAR(1),
	FOREIGN KEY (ruc_proveedor) REFERENCES Proveedor(ruc_proveedor),
	FOREIGN KEY (id_estado_cot) REFERENCES Estado_Cotizacion(id_estado_cot)
);

CREATE TABLE CotizacionxProducto(
	id_cotizacion VARCHAR(15),
	id_producto VARCHAR(8),
	cantidad_prod_cot INT,
	precio_unit_prod_cot DECIMAL(6,2),
	PRIMARY KEY(id_cotizacion,id_producto),
	FOREIGN KEY (id_cotizacion) REFERENCES Cotizacion(id_cotizacion),
	FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

CREATE TABLE Tipo_Factura(
	id_tipo_factura CHAR(3) PRIMARY KEY,
	tipo_factura VARCHAR(20) NOT NULL	
);

CREATE TABLE Estado_Factura(
	id_estado SERIAL PRIMARY KEY,
	estado VARCHAR(20) NOT NULL
);

CREATE TABLE Factura(
	nro_factura INT PRIMARY KEY,
	fecha_emision DATE NOT NULL,
	fecha_vencimiento DATE NOT NULL,
	monto DECIMAL(6,2) NOT NULL,
	ruc_proveedor CHAR(11),
	id_persona VARCHAR(10),
	id_tipo_factura CHAR(3),
	id_estado INT,
	FOREIGN KEY (ruc_proveedor) REFERENCES Proveedor(ruc_proveedor),
	FOREIGN KEY (id_persona) REFERENCES Cliente(id_persona),
	FOREIGN KEY (id_tipo_factura) REFERENCES Tipo_Factura(id_tipo_factura),
	FOREIGN KEY (id_estado) REFERENCES Estado_Factura(id_estado)
);

CREATE TABLE Tipo_Asiento_Contable(
	id_tipo_asiento_contable CHAR(3) PRIMARY KEY,
	nombre_asiento_contable VARCHAR(20) NOT NULL
);

CREATE TABLE Asiento_Contable(
	id_asiento_contable VARCHAR(10) PRIMARY kEY,
	cant_debe INT,
	cant_haber INT,
	nro_factura INT,
	id_tipo_asiento_contable CHAR(3),
	FOREIGN KEY (nro_factura) REFERENCES Factura(nro_factura),
	FOREIGN KEY (id_tipo_asiento_contable) REFERENCES Tipo_Asiento_Contable(id_tipo_asiento_contable)
);

CREATE TABLE Estado_Presupuesto(
	id_estado_presupuesto CHAR(1) PRIMARY KEY,
	nombre_estado_presupuesto VARCHAR(20) NOT NULL
);

CREATE TABLE Presupuesto(
	id_presupuesto VARCHAR(10) PRIMARY KEY,
	cod_area CHAR(2),
	fecha_elaboracion DATE NOT NULL,
	fecha_inicio DATE,
	fecha_finalizacion DATE,
	monto_total DECIMAL(6,2) NOT NULL,
	monto_gastado DECIMAL(6,2),
	id_persona VARCHAR(10),
	periodo CHAR(7) NOT NULL,
	id_estado_presupuesto CHAR(1),
	FOREIGN KEY (cod_area) REFERENCES Area(cod_area),
	FOREIGN KEY (id_persona) REFERENCES Gestor(id_persona),
	FOREIGN KEY (id_estado_presupuesto) REFERENCES Estado_Presupuesto(id_estado_presupuesto)
);

CREATE OR REPLACE FUNCTION actualizar_estado_compra() RETURNS VOID AS $$
BEGIN
    UPDATE ClientexProducto cp
    SET id_estado_compra = 'C',
        check_compra = CURRENT_TIMESTAMP
    FROM Venta v
    WHERE cp.id_persona = v.id_persona
      AND v.id_estado_venta = 'B'
      AND cp.id_estado_compra != 'C';
END;
$$ LANGUAGE plpgsql;

CREATE INDEX idx_marca ON Producto(id_marca);

EXPLAIN ANALYZE
SELECT P.id_producto, P.nombre_producto, P.especificaciones
FROM Producto P
JOIN Marca M ON P.id_marca = M.id_marca
WHERE M.id_marca = 'Beauty Creations';

CREATE INDEX idx_inv_prod ON Inventario(id_producto);

EXPLAIN ANALYZE
SELECT I.id_producto, P.nombre_producto, I.entradas, I.salidas,
       (I.entradas - I.salidas) AS stock,
       U.seccion, U.id_stand, U.id_repisas
FROM Inventario I
JOIN Producto P ON I.id_producto = P.id_producto
JOIN Ubicacion U ON I.seccion = U.seccion
                AND I.id_stand = U.id_stand
                AND I.id_repisas = U.id_repisas
WHERE (I.entradas - I.salidas) > 10;

CREATE OR REPLACE FUNCTION actualizar_stock_inventario()
RETURNS VOID AS $$
DECLARE
    producto_id VARCHAR(8);
    cantidad_actual INT;
    nuevo_stock INT;
BEGIN
    FOR producto_id IN SELECT id_producto FROM Inventario LOOP
        SELECT (entradas - salidas) INTO cantidad_actual
        FROM Inventario
        WHERE id_producto = producto_id;

        UPDATE Inventario
        SET stock = cantidad_actual
        WHERE id_producto = producto_id;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT actualizar_stock_inventario();