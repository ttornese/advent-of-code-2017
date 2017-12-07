defmodule Day5Test do
  use ExUnit.Case
  doctest Day5

  test "correctly solves number of steps for part one's logic" do
    assert Day5.traverse_maze([0, 3, 0, 1, -3], 0, :part_one) == 5
  end

    test "correctly solves number of steps for part two's logic" do
    assert Day5.traverse_maze([0, 3, 0, 1, -3], 0, :part_two) == 10
  end
end
