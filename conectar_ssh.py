import paramiko

def ejecutar_comando_ssh():
    # Solicitar la dirección IP
    ip_destino = input("Ingrese la dirección IP de la máquina a la que desea conectarse: ")

    # Usuario fijo
    usuario = "rtx11462"

    try:
        # Comando SSH con HostKeyAlgorithms
        comando_ssh = 'ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss {0}@{1}'.format(usuario, ip_destino)

        # Ejecutar el comando
        paramiko.util.log_to_file("paramiko.log")  # Puedes comentar esta línea si no necesitas el registro
        ssh_client = paramiko.SSHClient()
        ssh_client.load_system_host_keys()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Conectar al servidor remoto
        ssh_client.connect(ip_destino, username=usuario)

        # Ejecutar el comando en el servidor remoto
        stdin, stdout, stderr = ssh_client.exec_command(comando_ssh)

        # Imprimir la salida del comando
        print(stdout.read().decode())

    except Exception as e:
        print("Error al conectarse por SSH:", str(e))

    finally:
        # Cerrar la conexión SSH
        ssh_client.close()

if __name__ == "__main__":
    ejecutar_comando_ssh()
