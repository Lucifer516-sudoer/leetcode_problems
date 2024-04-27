from typing import List
from rich import print

class Solution:
    # def get_the_size_of_the_binary_matrix(
    #     self, matrix: List[List[int]]
    # ) -> tuple[int, int]:
    #     return len(matrix), len(
    #         matrix[0]
    #     )  # since this is just a binary matrix ( square matrix i guess)

    def traverse_and_invert_image_value(
        self, matrix: List[List[int]]
    ) -> List[List[int]]:
        new_matrix: list[int] = []

        for (
            row
        ) in matrix:  # can use comprehensions to make it faster but it will be messy
            new_temp_row = []
            for value in row:
                new_temp_row.append(0 if value == 1 else 1)
            else:
                new_matrix.append(new_temp_row)
                new_temp_row = []
        else:
            return new_matrix

    def flip_the_image_horizontally(self, matrix: List[List[int]]) -> List[List[int]]:
        _ = [row.reverse() for row in matrix]
        del _

        return matrix

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        """speed 52 ms"""
        return self.traverse_and_invert_image_value(
            self.flip_the_image_horizontally(matrix=image)
        )



