"""
Программа для шифрования с использованием автошифра
Автор: Лихач А.А. 9311 4 курс
Дата создания: 18.02.2023
"""

import click

from autokey import Autokey
from cracker import Cracker


@click.group()
def cli1():
    pass


@cli1.command()
@click.option('--alphabet', '-a', type=click.Path(exists=True), default=None, help='Filename for custom alphabet for cipher. Must be ordered.')
@click.argument('input-filename', type=click.Path(exists=True))
@click.argument('key-filename', type=click.Path(exists=True))
@click.argument('output-filename', type=click.Path(exists=False), required=False, default='encoded.txt')
def encode(alphabet, input_filename, key_filename, output_filename):
    """This command reads initital text from INPUT_FILENAME
    encodes it using key from KEY_FILENAME and writes output
    to OUTPUT_FILENAME."""
    click.echo("Starting encoding...\n")
    # read input file and key file from command arguments
    with open(input_filename, 'r', encoding='UTF-8') as i_file, open(key_filename, 'r', encoding='UTF-8') as key_file:
        text = i_file.read()
        key = key_file.read()

        # encoding
        if alphabet is not None:
            alp = Autokey.load_alphabet(alphabet)
            encoded_text = Autokey(key, alp, None).encode(text)
        else:
            encoded_text = Autokey(key).encode(text)
        try:
            with open(output_filename, 'w', encoding='UTF-8') as o_file:
                o_file.write(encoded_text)
                click.echo(f"Encoded text is written to {output_filename}!\n")
        except OSError as e:
            click.echo("Writing error:", str(e))


@click.group()
def cli2():
    pass


@cli2.command()
@click.option('--alphabet', '-a', type=click.Path(exists=True), default=None, help='Filename for custom alphabet for cipher. Must be ordered.')
@click.argument('input-filename', type=click.Path(exists=True))
@click.argument('key-filename', type=click.Path(exists=True))
@click.argument('output-filename', type=click.Path(exists=False), required=False, default='decoded.txt')
def decode(alphabet, input_filename, key_filename, output_filename):
    """This command reads encoded text from INPUT_FILENAME
    decodes it using key from KEY_FILENAME and writes output
    to OUTPUT_FILENAME  ."""
    click.echo("Starting decoding...\n")
    # read input file and key file from command arguments
    with open(input_filename, 'r', encoding='UTF-8') as i_file, open(key_filename, 'r', encoding='UTF-8') as key_file:
        text = i_file.read()
        key = key_file.read()

        # decode
        if alphabet is not None:
            alp = Autokey.load_alphabet(alphabet)
            decoded_text = Autokey(key, alp, None).decode(text)
        else:
            decoded_text = Autokey(key).decode(text)
        try:
            with open(output_filename, 'w', encoding='UTF-8') as o_file:
                o_file.write(decoded_text)
                click.echo(f"Decoded text is written to {output_filename}!\n")
        except OSError as e:
            click.echo("Writing error:", str(e))


@click.group()
def cli3():
    pass


@cli3.command()
@click.option('--verbal', is_flag=True, default=False, help='If set then logs whole process.')
@click.option('--k_max', type=int, default=4, help='Coefficient for max iterations on each key length. By default 4.')
@click.option('--key_length', type=int, default=0, help='Only check specified key length.')
@click.argument('input-filename', type=click.Path(exists=True))
@click.argument('output-filename', type=click.Path(exists=False), required=False, default=None)
def crack(verbal, k_max, key_length,  input_filename, output_filename):
    """This command tries to crack text from INPUT_FILENAME
    that is encoded with AutoKey cipher. If 
    [OUTPUT_FILENAME] is specified than decoded text is written
    to this file."""
    click.echo("Starting cracking...\n")
    cracker = Cracker(k_max, verbal)
    key, text = cracker.crack(input_filename, key_length)
    if output_filename is not None:
        with open(output_filename, 'w') as file:
            file.write(text)
            click.echo(f"Decoded text is written to {output_filename}!\n")


cli = click.CommandCollection(sources=[cli1, cli2, cli3])

if __name__ == '__main__':
    cli()
