def set_bit(number: int, bit_pos: int) -> int:
    return number | (1 << bit_pos)


def clear_bit(number: int, bit_pos: int) -> int:
    return number & ~(1 << bit_pos)


def test_bit(number: int, bit_pos: int) -> bool:
    return bool(number & (1 << bit_pos))
