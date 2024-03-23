class Graph:
  def __init__(self, V, E, w) -> None:
    self.V = V
    self.E = E
    self.w = w

  def __str__(self) -> str:
    return f"Graph(V={self.V}, E={self.E}, w={self.w})"