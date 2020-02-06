import pytest

from draw_box import create_box


def test_no_box_is_created_if_width_and_height_are_0():
    box = create_box(width=0, height=0)
    assert box == []


def test_small_box_is_created():
    expected = [
        '┌┐',
        '└┘',
    ]
    box = create_box(width=2, height=2)
    assert box == expected


def test_square_box_is_created():
    expected = [
        '┌──┐',
        '│  │',
        '│  │',
        '└──┘',
    ]
    box = create_box(width=4, height=4)
    assert box == expected


def test_rectangular_box_is_created():
    expected = [
        '┌────┐',
        '│    │',
        '│    │',
        '└────┘',
    ]
    box = create_box(width=6, height=4)
    assert box == expected
