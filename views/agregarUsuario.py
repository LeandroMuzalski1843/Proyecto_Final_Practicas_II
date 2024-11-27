import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from database.conexion import Database
from error.logger import log
from datetime import datetime
from views.session import UserSession
from views.password import generar_password  # Importa la función de encriptación

class AgregarUsuario(QMainWindow):   
    def __init__(self, parent=None):
        super(AgregarUsuario, self).__init__(parent)
        loadUi("ui\\agregarUsuario.ui", self)

        # Conectar el botón de guardar a la función para agregar usuario
        self.btnAceptar_3.clicked.connect(self.agregar_usuario)
        self.btnCancelar_3.clicked.connect(self.close)
        self.accion="Creo un Usuario"

        # Configurar el valor por defecto del comboBox
        self.comboBoxUsuario.setCurrentText("Administrador")

    def validar_contrasena(self, contrasena):
        """Verifica si la contraseña cumple con los requisitos mínimos."""
        # Requisitos: al menos 8 caracteres
        if len(contrasena) < 8:
            return False
        return True
    
    def agregar_usuario(self):
        """Obtiene los datos del formulario y los inserta en la base de datos."""
        nombre = self.lineEdit_Nombre.text().strip()
        contrasena = self.lineEdit_Contrasenia.text().strip()
        rol = self.comboBoxUsuario.currentText()
        fecha_creacion = datetime.now()

        # Validaciones iniciales
        if not nombre:
            QMessageBox.warning(self, 'Advertencia', 'El campo de nombre de usuario es obligatorio.')
            return

        if not contrasena:
            QMessageBox.warning(self, 'Advertencia', 'El campo de contraseña es obligatorio.')
            return

        if not self.validar_contrasena(contrasena):
            QMessageBox.warning(self, 'Advertencia', 'La contraseña debe tener al menos 8 caracteres.')
            return

        # Validar si el usuario ya existe en la base de datos
        try:
            db = Database()
            if db.usuario_existe(nombre):  # Supongamos que `usuario_existe` es un método en la clase Database
                QMessageBox.warning(self, 'Advertencia', 'El nombre de usuario ya existe. Por favor, elija otro.')
                return
        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'Hubo un error al verificar la existencia del usuario.')
            return

        # Encriptar la contraseña
        contrasena_encriptada = generar_password(contrasena)

        # Insertar usuario en la base de datos
        try:
            sesion = UserSession()
            id_user = sesion.get_user_id()
            db.insertar_usuario(nombre, contrasena_encriptada, rol, fecha_creacion)  # Inserta el usuario
            QMessageBox.information(self, 'Éxito', 'Usuario agregado correctamente.')

            # Registrar la acción en el historial
            db.registrar_historial_usuario(id_user, self.accion)

            self.close()
        except Exception as error:
            log(error, "error")
            QMessageBox.critical(self, 'Error', f"Hubo un error al agregar el usuario: {error}")


def main():
    app = QApplication(sys.argv)
    ventana = AgregarUsuario()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

