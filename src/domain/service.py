from .model import Batch, OrderLine, Reference


class OutOfStock(Exception):
    pass


def allocate(line: OrderLine, batches: list[Batch]) -> Reference:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")

    return batch.reference
