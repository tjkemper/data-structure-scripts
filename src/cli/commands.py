import click
from src.data_structures.maxheap import MaxHeap
from src.data_structures.avl import AVL


@click.command()
@click.option('--sort', '-s', is_flag=True, help="Return sorted list (descending).")
@click.option('--pretty-print', '-p', is_flag=True, help="Pretty print max heap.")
@click.argument('file', type=click.File(), default='-', required=False)
def maxheap(file, pretty_print, sort):
    """Max Heap manipulation.

    \b
    The default behavior returns a max heap. Each element is separated by a newline.

    \b
    Arguments:
      FILE -- Non-negative integers separated by newlines.
    """
    try:
        input_array = [int(i) for i in file.read().split()]
    except ValueError:
        raise click.UsageError("Only integers are allowed.")

    heap = MaxHeap(input_array)

    if pretty_print and sort:
        raise click.UsageError("Cannot use --pretty-print and --sort together.")

    if pretty_print:
        heap.pretty_print()
    elif sort:
        click.echo(list_output(heap.sorted_array()))
    else:
        click.echo(list_output(heap._heap))


@click.command()
@click.option('--pretty-print', '-p', is_flag=True, help="Pretty print AVL tree.")
@click.argument('file', type=click.File(), default='-', required=False)
def avl(file, pretty_print):
    """AVL Tree manipulation.

    \b
    The default behavior returns a sorted list (ascending). Each element is separated by a newline.
    This is accomplished by doing an 'in order' traversal of the AVL tree.

    \b
    Arguments:
      FILE -- Distinct integers separated by newlines.
    """
    try:
        input_array = set([int(i) for i in file.read().split()])
    except ValueError:
        raise click.UsageError("Only distinct integers are allowed.")

    avl_tree = AVL(input_array)

    if pretty_print:
        avl_tree.pretty_print()
    else:
        click.echo(list_output(avl_tree.in_order()))


def list_output(integers):
    return "\n".join(str(i) for i in integers)
