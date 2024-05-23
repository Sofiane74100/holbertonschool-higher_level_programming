#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Essayer de formater et d'imprimer la valeur en tant qu'entier
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Si une exception est levée, retourner False
        return False
