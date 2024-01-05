from enum import Enum, auto


class OverlapDirections(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
    NONE = auto()


class Borders:
    def __init__(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    @classmethod
    def create_from_tile(cls, rows):
        """
            Computes borders from a square matrix
            @param rows: A list of strings representing a tile we want the borders of
        """
        top_border = rows[0]
        bottom_border = rows[-1]
        left_border = ''.join(r[0] for r in rows)
        right_border = ''.join(r[-1] for r in rows)

        return cls(top_border, right_border, bottom_border, left_border)

    def __eq__(self, other):
        return all(getattr(self, border) == getattr(other, border) for border in ['top', 'right', 'left', 'bottom'])

    def __repr__(self):
        return f'Borders({self.top}, {self.right}, {self.bottom}, {self.left})'

    def create_rotated(self):
        """
        Rotates borders by 180 degrees
        """
        return Borders(
            top=self.bottom[::-1],
            right=self.left[::-1],
            bottom=self.top[::-1],
            left=self.right[::-1]
        )

    def create_horizontal_flipped(self):
        return Borders(
            top=self.bottom,
            right=self.right[::-1],
            bottom=self.top,
            left=self.left[::-1]
        )

    def create_vertical_flipped(self):
        return Borders(
            top=self.top[::-1],
            right=self.left,
            bottom=self.bottom[::-1],
            left=self.right
        )

    def has_overlap(self, other):
        pass

    def overlap_directions(self, other):
        """
        Indicates in what directions these borders and that of `other` overlap

        e.g returns OverlapDirections.NORTH when the `other` borders can be placed to the north of this one
        @param other:
        @return:
        """
        result = []
        if self.top == other.bottom:
            result.append(OverlapDirections.NORTH)
        if self.left == other.right:
            result.append(OverlapDirections.EAST)
        if self.right == other.left:
            result.append(OverlapDirections.WEST)
        if self.bottom == other.top:
            result.append(OverlapDirections.SOUTH)
        return result