import os
import click
import numpy as np
import pandas as pd


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_INPUT = os.path.join(FILE_DIR, '') #TODO set input data path
DEFAULT_DTYPE = {'Id': np.uint16
                 } #TODO set dtypes


@click.command()
@click.option('-i',
              '--input',
              default=DEFAULT_INPUT,
              type=click.Path(exists=True),
              help='specify an input file',
              metavar='input')
def main(**kwargs):

    inspect_data(kwargs['input'])


def inspect_data(input):

    with open(input, 'r') as fin:
        try:
            pd.read_csv(input,
                        header=0,
                        sep=",",
                        encoding='utf-8',
                        dtype=DEFAULT_DTYPE)
        except Exception:
            print('dtype is invalid.')
    return 1


if __name__=='__main__':
    main()