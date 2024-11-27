import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from datetime import datetime
from database.conexion import Database  
from error.logger import log
from PyQt5.uic import loadUi  
from views.password import generar_password
from views.session import UserSession
class ModificarUsuario(QMainWindow):
    def __init__(self, parent=None):
        super(ModificarUsuario, self).__init__(parent)
        loadUi("ui\\modificarUsuario.ui", self)

        self.db = Database()
        self.btnCancelar_Modificar.clicked.connect(self.close)
        self.btnAceptar_Modificar.clicked.connect(self.modificar_usuario)
        self.accion = "Modifico un Usuario"

        self.comboBoxUsuario_2.currentIndexChanged.connect(self.cargar_datos_usuario)
        self.load_users()

    def validar_contrasena(self, contrasena):
        """Verifica si la contraseña cumple con los requisitos mínimos."""
        return len(contrasena) >= 8

    def load_users(self):
        """Carga la lista de usuarios en el combo box."""
        try:
            usuarios = self.db.obtener_usuarios()
            for usuario in usuarios:
                self.comboBoxUsuario_2.addItem(f"{usuario[1]} - {usuario[3]}", usuario[0])
        except Exception as e:
            QMessageBox.critical(self, 'Error', f"Error al cargar usuarios: {str(e)}")

    def cargar_datos_usuario(self):
        """Carga los datos del usuario seleccionado en los campos."""
        user_id = self.comboBoxUsuario_2.currentData()
        if user_id:
            try:
                usuario = self.db.obtener_usuario_por_id(user_id)
                if usuario:
                    self.lineEdit_Nombre.setText(usuario[1])
                    # self.lineEdit_Contrasenia.setText(usuario[2])
                    rol = usuario[3]
                    if rol == 'Administrador':
                        self.comboBoxUsuario.setCurrentIndex(0)
                    elif rol == 'Empleado':
                        self.comboBoxUsuario.setCurrentIndex(1)
            except Exception as e:
                QMessageBox.critical(self, 'Error', f"Error al cargar datos del usuario: {str(e)}")

    def modificar_usuario(self):
        """Modifica los datos del usuario seleccionado."""
        user_id = self.comboBoxUsuario_2.currentData()
        nuevo_nombre = self.lineEdit_Nombre.text().strip()
        nueva_contrasena = self.lineEdit_Contrasenia.text().strip()
        nuevo_rol = self.comboBoxUsuario.currentText()
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

        try:
            if self.db.usuario_existe(nuevo_nombre) and nuevo_nombre != self.lineEdit_Nombre.text():
                QMessageBox.warning(self, 'Advertencia', 'El nombre de usuario ya existe. Por favor, elija otro.')
                return

            contrasenia_encriptada = generar_password(nueva_contrasena)
            sesion = UserSession()
            id_user = sesion.get_user_id()

            self.db.modificar_usuario(user_id, nuevo_nombre, contrasenia_encriptada, nuevo_rol, fecha_modificacion)
            self.db.registrar_historial_usuario(id_user, self.accion)
            QMessageBox.information(self, 'Éxito', 'Usuario modificado correctamente.')
            self.close()
        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', f"Error al modificar usuario: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModificarUsuario()
    window.show()
    sys.exit(app.exec_())
