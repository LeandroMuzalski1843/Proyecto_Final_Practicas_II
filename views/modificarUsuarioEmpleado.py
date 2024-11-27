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

        self.db = Database()
        self.btnCancelar_Modificar.clicked.connect(self.close)
        self.btnAceptar_Modificar.clicked.connect(self.modificar_usuario)
        self.accion = "Modifico un Usuario"

        self.comboBoxUsuario.setDisabled(True)
        self.cargar_datos_usuario_sesion()

    def validar_contrasena(self, contrasena):
        """Verifica si la contraseña cumple con los requisitos mínimos."""
        return len(contrasena) >= 8

    def cargar_datos_usuario_sesion(self):
        """Carga los datos del usuario que está en sesión en los campos."""
        try:
            sesion = UserSession()
            user_id = sesion.get_user_id()

            if not user_id:
                QMessageBox.warning(self, 'Advertencia', 'No hay un usuario logueado en la sesión.')
                self.close()
                return

            usuario = self.db.obtener_usuario_por_id(user_id)

            if usuario:
                self.lineEdit_Nombre.setText(usuario[1])
                # self.lineEdit_Contrasenia.setText(usuario[2])
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
        user_id = sesion.get_user_id()
        nuevo_nombre = self.lineEdit_Nombre.text().strip()
        nueva_contrasena = self.lineEdit_Contrasenia.text().strip()
        rol = self.comboBoxUsuario.currentText()
        fecha_modificacion = datetime.now()

        if not nuevo_nombre:
            QMessageBox.warning(self, 'Advertencia', 'El campo de nombre de usuario es obligatorio.')
            return

        if not nueva_contrasena:
            QMessageBox.warning(self, 'Advertencia', 'El campo de contraseña es obligatorio.')
            return

        if not self.validar_contrasena(nueva_contrasena):
            QMessageBox.warning(self, 'Advertencia', 'La contraseña debe tener al menos 8 caracteres.')
            return

        # Validar si el nuevo nombre de usuario ya está en uso por otro usuario
        try:
            # Obtener los datos actuales del usuario
            usuario_actual = self.db.obtener_usuario_por_id(user_id)

            if usuario_actual and usuario_actual[1] != nuevo_nombre:  # El nombre está siendo modificado
                if self.db.usuario_existe(nuevo_nombre):
                    QMessageBox.warning(self, 'Advertencia', 'El nombre de usuario ya está en uso. Por favor, elija otro.')
                    return
        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'Error al verificar el nombre de usuario.')
            return

        # Proceder con la modificación
        try:
            contrasenia_encriptada = generar_password(nueva_contrasena)
            self.db.modificar_usuario(user_id, nuevo_nombre, contrasenia_encriptada, rol, fecha_modificacion)
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
