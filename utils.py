from datetime import datetime
import secrets
import string
import random


def parse_datetime_to_european_format(dt: datetime) -> str:
    """Formats a datetime object as DD/MM/YYYY HH:mm.

    Args:
        dt: The datetime object to format.

    Returns:
        The formatted string.
    """

    return dt.strftime("%d/%m/%Y %H:%M")


def generate_random_string(size: int, char_set: str = None) -> str:
    """Generates a secure random string of the specified length.

    Args:
        size: The desired length of the string.

    Returns:
        A secure random string.
    """
    chars = char_set
    if not char_set:
        chars= string.ascii_letters + string.digits

    random_str = ''.join(secrets.choice(chars) for i in range(size))
    return random_str



def escape_js_string(value: str) -> str:
    """
    Escapa manualmente los caracteres especiales que puedan causar problemas en JavaScript.
    """
    escapes = {
        '\\': '\\\\',
        '"': '\\"',
        "'": "\\'",
        '\n': '\\n',
        '\r': '\\r',
        '\t': '\\t',
        '\b': '\\b',
        '\f': '\\f',
        '\v': '\\v',
    }
    return ''.join(escapes.get(c, c) for c in value)


def insert_str_between_the_date_and_hour(date_str: str, insert_str: str) -> str:
    """
    Insert a given string between the date and time parts of the datetime string.
    
    :param date_str: The original string in the format 'dd/mm/yyyy HH:MM'
    :param insert_str: The string to insert
    :return: Modified string with the inserted value
    """
    # Find the index where the date part ends and the time part begins
    split_index = date_str.index(' ')  # Finds the first space between date and time
    return date_str[:split_index] + insert_str + date_str[split_index:]



def insert_str_into_date_part(date_str: str, insert_str: str) -> str:
    """
    Insert a given string into the date part of the datetime string, 
    not at the first or last position of the date.
    
    :param date_str: The original string in the format 'dd/mm/yyyy HH:MM'
    :param insert_str: The string to insert
    :return: Modified string with the inserted value
    """
    # Separate date and time parts
    date_part, time_part = date_str.split(' ')
    
    # Get valid positions for insertion (excluding first and last)
    valid_positions = range(1, len(date_part) - 1)
    
    # Randomly select a valid insertion position
    insert_position = random.choice(valid_positions)
    
    # Insert the string at the chosen position
    modified_date = date_part[:insert_position] + insert_str + date_part[insert_position:]
    
    # Return the modified string
    return modified_date + ' ' + time_part


def insert_str_into_time_part(date_str: str, insert_str: str) -> str:
    """
    Insert a given string into the time part of the datetime string, 
    not at the first or last position of the time part.
    
    :param date_str: The original string in the format 'dd/mm/yyyy HH:MM'
    :param insert_str: The string to insert
    :return: Modified string with the inserted value
    """
    # Separate date and time parts
    date_part, time_part = date_str.split(' ')
    
    # Get valid positions for insertion (excluding first and last position of time part)
    valid_positions = range(1, len(time_part) - 1)
    
    # Randomly select a valid insertion position
    insert_position = random.choice(valid_positions)
    
    # Insert the string at the chosen position in the time part
    modified_time = time_part[:insert_position] + insert_str + time_part[insert_position:]
    
    # Return the full modified string with date and modified time
    return date_part + ' ' + modified_time



def extract_rgb_values(rgb_string: str):
    """
    Extracts the numeric RGB values from a string in the format 'rgb(r, g, b)'.
    
    :param rgb_string: A string containing RGB values in the format 'rgb(r, g, b)'
    :return: A tuple of three integers representing the RGB values (r, g, b)
    """
    # Remove 'rgb(' and ')' and split by comma
    rgb_values = rgb_string.replace('rgb(', '').replace(')', '').split(',')
    
    # Convert to integers and return as a tuple
    return tuple(map(int, rgb_values))



def is_color_within_margin(color: tuple, target_color: tuple, margin: int = 5) -> bool:
    """
    Check if the RGB values of the first color are within a margin of the target color's RGB values.
    
    :param color: A tuple representing the RGB values of the color to check (r, g, b)
    :param target_color: A tuple representing the target RGB values to compare against (r, g, b)
    :param margin: The allowed margin (default is 5) for each color component
    :return: True if the color is within the margin for all RGB components, False otherwise
    """
    return all(
        abs(color[i] - target_color[i]) <= margin for i in range(3)
    )
