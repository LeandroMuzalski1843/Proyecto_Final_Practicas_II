import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from datetime import datetime
from database.conexion import Database  
from error.logger import log
from PyQt5.uic import loadUi  
from views.password import generar_password
from views.session import UserSession
class ModificarUsuarioE(QMainWindow):
    def __init__(self, parent=None):
        super(ModificarUsuarioE, self).__init__(parent)
        loadUi("ui\\modificarUsuario.ui", self)

        # Inicializar base de datos
        self.db = Database()

        # Conectar el botón de guardar a la función para modificar usuario
        self.btnCancelar_Modificar.clicked.connect(self.close)
        self.btnAceptar_Modificar.clicked.connect(self.modificar_usuario)
        self.accion = "Modifico un Usuario"

        # Bloquear el comboBox para que no se pueda cambiar el rol
        self.comboBoxUsuario.setDisabled(True)

        # Cargar datos del usuario en sesión
        self.cargar_datos_usuario_sesion()

    def cargar_datos_usuario_sesion(self):
        """Carga los datos del usuario que está en sesión en los campos."""
        try:
            # Obtener el usuario en sesión
            sesion = UserSession()
            user_id = sesion.get_user_id()

            if not user_id:
                QMessageBox.warning(self, 'Advertencia', 'No hay un usuario logueado en la sesión.')
                self.close()
                return

            # Consultar datos del usuario en sesión
            usuario = self.db.obtener_usuario_por_id(user_id)

            if usuario:
                self.lineEdit_Nombre.setText(usuario[1])  # Nombre de usuario
                self.lineEdit_Contrasenia.setText(usuario[2])  # Contraseña
                rol = usuario[3]
                if rol == 'Administrador':
                    self.comboBoxUsuario.setCurrentIndex(0)
                elif rol == 'Empleado':
                    self.comboBoxUsuario.setCurrentIndex(1)
            else:
                QMessageBox.warning(self, 'Advertencia', 'No se encontraron datos para el usuario en sesión.')
                self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', f"Error al cargar los datos del usuario en sesión: {str(e)}")

    def modificar_usuario(self):
        """Modifica los datos del usuario en sesión."""
        sesion = UserSession()
        user_id = sesion.get_user_id()  # ID del usuario en sesión
        nuevo_nombre = self.lineEdit_Nombre.text()
        nueva_contrasena = self.lineEdit_Contrasenia.text()
        rol = self.comboBoxUsuario.currentText()  # Rol del usuario (bloqueado, no editable)
        fecha_modificacion = datetime.now()

        if not nuevo_nombre or not nueva_contrasena:
            QMessageBox.warning(self, 'Advertencia', 'Todos los campos son obligatorios.')
            return

        try:
            # Encriptar la nueva contraseña
            contrasenia_encriptada = generar_password(nueva_contrasena)

            # Modificar usuario en la base de datos
            self.db.modificar_usuario(user_id, nuevo_nombre, contrasenia_encriptada, rol, fecha_modificacion)

            # Registrar historial
            self.db.registrar_historial_usuario(user_id, self.accion)

            QMessageBox.information(self, 'Éxito', 'Datos del usuario modificados correctamente.')
            self.close()
        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', f"Error al modificar los datos del usuario: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModificarUsuarioE()
    window.show()
    sys.exit(app.exec_())
