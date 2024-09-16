import os
import uuid
import secrets

def generate_prng(prng_type: str, size: int = 0, min: int = 0, max: int = 0, encoding: str = 'utf-8'):
    if prng_type == "bytes":
        # Generar bytes aleatorios
        return os.urandom(size).hex() if encoding == 'hex' else os.urandom(size).decode(encoding)
    elif prng_type == "int":
        if min > max:
            raise ValueError(f"Minimum value ({min}) cannot be greater than maximum value ({max})")
        # Generar un entero aleatorio dentro del rango especificado
        return secrets.randbelow(max - min) + min
    elif prng_type == "uuid":
        # Generar un UUID
        return str(uuid.uuid4())
    else:
        raise ValueError(f"PRNG type '{prng_type}' not supported")

def main():
    # Ejemplo de uso:
    print(generate_prng("bytes", size=16, encoding="hex"))  # Generar bytes aleatorios en formato hexadecimal
    print(generate_prng("int", min=1, max=100))  # Generar un entero aleatorio entre 1 y 100
    print(generate_prng("uuid"))  # Generar un UUID aleatorio

if __name__ == "__main__":
    main()