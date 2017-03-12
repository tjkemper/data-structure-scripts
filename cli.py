import max_heap
import click


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
      FILE -- Data for max heap.
    """
    input_array = file.read().split()
    heap = max_heap.MaxHeap(input_array)

    if pretty_print and sort:
        raise click.UsageError("Cannot use --pretty-print and --sort together.")

    if pretty_print:
        heap.pretty_print()
    elif sort:
        click.echo("\n".join(heap.sorted_array()))
    else:
        click.echo("\n".join(heap._heap))