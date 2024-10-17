cargo_empleado = (input("Ingrese el cargo del empleado: \n 1. Directivo \n 2. DIRECTIVO \n 3. Operativo \n 4. Auxiliar"))
Directivo = 1
DIRECTIVO = 2
Operativo = 3
Auxiliar = 4

desempeño_empleado = (input("Ingrese el desempeño del empleado: \n 1. Alto \n 2. Medio \n 3. Bajo "))
Alto = 1
Medio = 2
Bajo = 3

salario_directivo = 3000000
salario_directivo2 = 2500000
salario_operativo = 1750000
salario_auxiliar = 1300000

directivo_alto = (salario_directivo + (salario_directivo * 0.2))
directivo_medio = (salario_directivo + (salario_directivo * 0.15))
directivo_bajo = salario_directivo

DIRECTIVO_alto = (salario_directivo2 + (salario_directivo2 * 0.2))
DIRECTIVO_medio = (salario_directivo2 + (salario_directivo2 * 0.15))
DIRECTIVO_bajo = salario_directivo2

operativo_alto = (salario_operativo + (salario_operativo * 0.15))
operativo_medio = (salario_operativo + (salario_operativo * 0.05))
operativo_bajo = salario_operativo

auxiliar_alto = (salario_auxiliar + (salario_auxiliar * 0.15))
auxiliar_medio = (salario_auxiliar + (salario_auxiliar * 0.05))
auxiliar_bajo = salario_auxiliar

def calcular_salario(Cargo_empleado, desempeño_empleado, salario_directivo, salario_directivo2, salario_operativo, salario_auxiliar):
    if (cargo_empleado == 1):
        if(desempeño_empleado == 1):
            print("----Resumen del pago---- \n Cargo: " + {1} + "\n Nivel desempeño: " + {1} + "\n Salario Base: " + {salario_directivo} + "\n Total a recibir: " + {directivo_alto})
    return calcular_salario()