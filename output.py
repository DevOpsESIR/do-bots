class BinTree:

    def __init__(self, left=None, right=None, key="CONS") -> None:
        self.left = left
        self.right = right
        self.key = key

    def __str__(self) -> str:
        lines, *_ = self._display_aux()
        return "\n" + "\n".join(lines) + "\n"

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line
                    ] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line
                    ] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x -
                                      1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u +
                                       y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line
                 ] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def nope():
  global stack
  pass
  # Assign
  NIL_2 = BinTree(key= "NIL")
  if "CONS_1" not in locals():
    CONS_1 = BinTree()
  CONS_1.left = NIL_2
  NIL_3 = BinTree(key= "NIL")
  if "CONS_1" not in locals():
    CONS_1 = BinTree()
  CONS_1.right = NIL_3
  CONS_1 = CONS_1
  A_0 = CONS_1
  return A_0

def main():
  global stack
  # Assign
  FUNCTIONCALL_5 = nope()
  A_4 = FUNCTIONCALL_5
  return A_4


if __name__ == "__main__":
    stack = []
    print(main())