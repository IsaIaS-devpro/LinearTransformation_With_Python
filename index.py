import numpy as np
import math

# Funções de Translação
def translate2D(vector, dx, dy):
    x, y = vector
    x_translated = x + dx
    y_translated = y + dy
    return [x_translated, y_translated]

def translate3D(vector, dx, dy, dz):
    x, y, z = vector
    x_translated = x + dx
    y_translated = y + dy
    z_translated = z + dz
    return [x_translated, y_translated, z_translated]

# Funções de Rotação
def rotation2D(vector, angle):
    x, y = vector
    theta = math.radians(angle)
    x_rotated = x * math.cos(theta) - y * math.sin(theta)
    y_rotated = x * math.sin(theta) + y * math.cos(theta)
    return [x_rotated, y_rotated]

def rotation3DX(vector, angle):
    x, y, z = vector
    theta = math.radians(angle)
    y_rotated = y * math.cos(theta) - z * math.sin(theta)
    z_rotated = y * math.sin(theta) + z * math.cos(theta)
    return [x, y_rotated, z_rotated]

def rotation3DY(vector, angle):
    x, y, z = vector
    theta = math.radians(angle)
    x_rotated = x * math.cos(theta) + z * math.sin(theta)
    z_rotated = -x * math.sin(theta) + z * math.cos(theta)
    return [x_rotated, y, z_rotated]

def rotation3DZ(vector, angle):
    x, y, z = vector
    theta = math.radians(angle)
    x_rotated = x * math.cos(theta) - y * math.sin(theta)
    y_rotated = x * math.sin(theta) + y * math.cos(theta)
    return [x_rotated, y_rotated, z]

# Funções de Reflexão
def reflection2DX(vector):
    x, y = vector
    return [x, -y]

def reflection2DY(vector):
    x, y = vector
    return [-x, y]

def reflection3DX(vector):
    x, y, z = vector
    return [x, -y, -z]

def reflection3DY(vector):
    x, y, z = vector
    return [-x, y, -z]

def reflection3DZ(vector):
    x, y, z = vector
    return [-x, -y, z]

# Funções de Projeção
def projection2DX(vector):
    x, y = vector
    return [x, 0]

def projection2DY(vector):
    x, y = vector
    return [0, y]

def projection3DX(vector):
    x, y, z = vector
    return [x, 0, 0]

def projection3DY(vector):
    x, y, z = vector
    return [0, y, 0]

def projection3DZ(vector):
    x, y, z = vector
    return [0, 0, z]

# Função de Cisalhamento
def shearing(vector, kx, ky):
    # Define a matriz de cisalhamento
    M = np.array([[1, kx],
                  [ky, 1]])
    # Converte o vetor em uma matriz coluna
    v = np.array(vector).reshape(-1, 1)
    # Aplica a transformação de cisalhamento
    v_sheared = np.dot(M, v)
    # Retorna o vetor resultante como uma lista
    return v_sheared.flatten().tolist()




# AQUI TEMOS OS PARÂMETROS PARA USAR NOS CÁLCULOS...
#  .......................
# .........................
vector2D = [1, 2]       # Vetor original em 2D
vector3D = [3, 2, 1]    # Vetor original em 3D

#CISALHAMENTO
kx = 4                  # Fator de cisalhamento na direção x
ky = 5                   # Fator de cisalhamento na direção y

#DESLOCAMENTO......
dx = 5        # Deslocamento em x
dy = 4               # Deslocamento em y
dz = 6            # Deslocamento em z

#ÂNGULO.............
angle = 45       # Ângulo de rotação em graus
# .........................
# .........................
# .........................




# Translação
translated_2d = translate2D(vector2D, dx, dy)
translated_3d = translate3D(vector3D, dx, dy, dz)

# Rotação
rotated_2d = rotation2D(vector2D, angle)
rotated_3dx = rotation3DX(vector3D, angle)
rotated_3dy = rotation3DY(vector3D, angle)
rotated_3dz = rotation3DZ(vector3D, angle)

# Reflexão
reflected_2dx = reflection2DX(vector2D)
reflected_2dy = reflection2DY(vector2D)
reflected_3dx = reflection3DX(vector3D)
reflected_3dy = reflection3DY(vector3D)
reflected_3dz = reflection3DZ(vector3D)

# Projeção
projected_2dx = projection2DX(vector2D)
projected_2dy = projection2DY(vector2D)
projected_3dx = projection3DX(vector3D)
projected_3dy = projection3DY(vector3D)
projected_3dz = projection3DZ(vector3D)

# Cisalhamento
sheared_2d = shearing(vector2D, kx, ky)

print("Translação 2D:", translated_2d)
print("Translação 3D:", translated_3d)
print("Rotação 2D:", rotated_2d)
print("Rotação 3D em torno de X:", rotated_3dx)
print("Rotação 3D em torno de Y:", rotated_3dy)
print("Rotação 3D em torno de Z:", rotated_3dz)
print("Reflexão 2D em relação a X:", reflected_2dx)
print("Reflexão 2D em relação a Y:", reflected_2dy)
print("Reflexão 3D em relação a X:", reflected_3dx)
print("Reflexão 3D em relação a Y:", reflected_3dy)
print("Reflexão 3D em relação a Z:", reflected_3dz)
print("Projeção 2D em X:", projected_2dx)
print("Projeção 2D em Y:", projected_2dy)
print("Projeção 3D em X:", projected_3dx)
print("Projeção 3D em Y:", projected_3dy)
print("Projeção 3D em Z:", projected_3dz)
print("Cisalhamento 2D:", sheared_2d)


