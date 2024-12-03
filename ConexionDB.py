import sqlite3

class ConexionBD:
    def __init__(self, rutaBd):
        """Inicializa la conexión a la base de datos y prepara el cursor."""
        self.rutaBd = rutaBd
        self.conexion = None
        self.cursor = None
        self.conectaBD()

    def conectaBD(self):
        """Conecta a la base de datos SQLite."""
        try:
            self.conexion = sqlite3.connect(self.rutaBd)
            self.cursor = self.conexion.cursor()
            print("Conexión de base de datos realizada")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def crear_tabla(self):
        """Crea la tabla 'usuarios' si no existe."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    dni TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    fallecido INTEGER NOT NULL
                )
            """)
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def consultaSenParametros(self, consultaSQL):
        """Realiza una consulta sin parámetros."""
        try:
            self.cursor.execute(consultaSQL)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error en la consulta: {e}")
            return None

    def consultaConParametros(self, consultaSQL, parametros=()):
        """Realiza una consulta con parámetros."""
        try:
            self.cursor.execute(consultaSQL, parametros)
            self.conexion.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error en la consulta con parámetros: {e}")
            return None

    def pechaBD(self):
        """Cierra la conexión con la base de datos."""
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def insertar_datos_iniciales(self):
        """Inserta datos por defecto si la tabla está vacía."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM usuarios")
            count = self.cursor.fetchone()[0]
            if count == 0:
                usuarios_iniciales = [
                    ("123123123F", "Ana Pérez", "Mujer", 0),
                    ("67676767H", "Paco Jémez", "Hombre", 1),
                    ("12389065H", "Víctor Roque", "Hombre", 0),
                    ("23423423D", "Juanita Sainz", "Mujer", 1),
                    ("12345678G", "Daniela López", "Otro", 0),
                ]
                self.cursor.executemany(
                    "INSERT INTO usuarios (dni, nombre, genero, fallecido) VALUES (?, ?, ?, ?)",
                    usuarios_iniciales,
                )
                self.conexion.commit()
                print("Datos iniciales insertados.")
        except sqlite3.Error as e:
            print(f"Error al insertar datos iniciales: {e}")


    def insertar_usuario(self, datos):
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (dni, nombre, genero, fallecido) VALUES(?, ?, ?, ?)",
                datos,
            )
            self.conexion.commit()
            print("Usuario inserido correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar datos usuarios: {e}")
