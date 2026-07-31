# closed class
from any import Any
from board.cell import Cell
from component.queue.queue import ComponentQueue
from board.generator.generator import Generator
from component.set.component_set import ComponentSet
class Matrix(Any):

    COLS = "ABCDEFGH"

    # construstor
    def __init__(self, size = 8):
        self.__size = size
        self.array = [Cell] * (size**2)
        self.components_queue = ComponentQueue()

        self.EMPTY_METRIX_STATE = True
        self.EMPTY_MATRIX_CELLS_STATE = True

        # 0 - init
        # 1 - success
        # -1 - failed
        self.REMOVE_SEQUENCE_STATUS = 0

        # 0 - init
        # 1 - success
        # -1 - failed
        self.ROLLBACK_STATUS = 0

        # 0 - init
        # 1 - success
        # -1 - failed
        self.COLLAPSE_COLUMN_STATUS = 0

        # 0 - init
        # 1 - success
        # -1 - failed
        self.COLLAPSE_GRID_STATUS = 0

    # for pretty print
    def __str__(self) -> str:
        lines = ["   " + "  ".join(self.COLS[:self.__size])]

        for r in range(self.__size - 1, -1, -1):
            row = self.array[r * self.__size:(r + 1) * self.__size]
            body = " ".join(value.get_component().get_value() for value in row)
            lines.append(f"{r + 1:>2} │{body}│ {r + 1}")
        lines.append("   " + "  ".join(self.COLS[:self.__size]))

        return "\n".join(lines)

    # commands
    
    # pre-cond: 
    #   - base array not null
    #   - arrange components not null
    # post-cond: base array has been filling
    def fill_all(self, arrange_component: list[Cell]):
        if len(arrange_component) == 0:
            return
        
        not_empty = self.EMPTY_METRIX_STATE != True
        if not_empty:
            return
        
        for i in range(len(self.array)):
            self.array[i] = arrange_component[i]

        self.EMPTY_METRIX_STATE = False

    # pre-cond: array is not empty
    # post-cond: cells have chnged position
    def move(self, first_cell: Cell, second_cell: Cell):
        first_cell.component, second_cell.component = second_cell.component, first_cell.component

    # pre-cond:
    #   - array is not empty
    #   - sequence is valis
    # post-cond: from array has removed a sequence of cells
    def remove_sequence(self, sequence: list[Cell]):
        for cell in sequence:
            cell.set_to_delete()

    # pre-cond:
    #   - array is not empty
    # post-cond: from array has removed a sequence of cells and filling from queue
    def collapse_column(self, col_index: int):
        column = self.get_column(col_index)

        write_index = 0

        for read_index, cell in enumerate(column):
            delete = cell.get_delete_state()

            if delete:
                continue

            if read_index != write_index:
                column[write_index].component = cell.component
                column[write_index].reset_delete_state()

            write_index += 1

        for i in range(write_index, len(column)):
            component = self.components_queue.pop()
            column[i].component = component
            column[i].reset_delete_state()
            self.components_queue.fill_queue()

        self.COLLAPSE_COLUMN_STATUS = 1

    # pre-cond:
    #   - array is not empty
    # post-cond: from array has removed a sequence of cells and filling from queue
    def collapse_grid(self):
        for col_indx in range(self.__size):
            self.collapse_column(col_indx)

        self.COLLAPSE_GRID_STATUS = 1

    def rollback(self, first_cell: Cell, second_cell: Cell):
        self.move(first_cell, second_cell)
        self.ROLLBACK_STATUS = 1

    # requests
    
    # pre-cond: board_matrix is not empty 
    # post-cond: has found at least one valid sequence OR hasn't found either
    def find_sequences_in_line(self, line: list[Cell]) -> list[Cell]:
        matched: list[Cell] = []
        run = [line[0]]

        for cell in line[1:]:
            if self.__same_component(cell, run[-1]):
                run.append(cell)
            else:
                if len(run) >= 3:
                    matched.extend(run)
                run = [cell]

        if len(run) >= 3:
            matched.extend(run)

        return matched

    def __same_component(self, first_cell: Cell, second_cell: Cell) -> bool:
        return first_cell.get_component().get_value() == second_cell.get_component().get_value()
    
    # pre-cond: array is not empty
    # post-cond: have found sequence of cells
    def valid_sequence(self, first_cell: Cell, second_cell: Cell) -> list[Cell]:
        self.move(first_cell, second_cell)

        first_cell_y = first_cell.get_y()
        first_cell_x = first_cell.get_x()

        second_cell_y = second_cell.get_y()

        line = self.get_row(first_cell_y)
        if first_cell_y != second_cell_y:
            line = self.get_column(first_cell_x)

        matched = self.find_sequences_in_line(line)

        self.rollback(first_cell, second_cell)

        if not matched:
            return []

        return matched

    def get_remove_status(self) -> int:
        return self.REMOVE_SEQUENCE_STATUS

    def get_rollback_status(self) -> int:
        return self.ROLLBACK_STATUS

    def get_row(self, y: int) -> list[Cell]:
            return self.array[y * self.__size : (y + 1) * self.__size]
    
    def get_column(self, x: int) -> list[Cell]:
        return [self.array[y * self.__size + x] for y in range(self.__size)]