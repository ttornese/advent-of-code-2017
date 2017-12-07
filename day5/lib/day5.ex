defmodule Day5 do
  def update_maze(maze, index, part) do
    value = Enum.at(maze, index)
    if part == :part_two && value >= 3 do
      List.replace_at(maze, index, value - 1)
    else
      List.replace_at(maze, index, value + 1)
  end

  def traverse_maze(maze, index, part) do
    cond do
      index > length(maze) - 1 ->
        0
      Enum.at(maze, index) == 0 ->
        1 + traverse_maze(List.replace_at(maze, index, 1), index, part)
      true ->
        1 + traverse_maze(
          update_maze(maze, index, part),
          index + Enum.at(maze, index),
          part
        )
    end
  end

  def parse_input(input) do
    String.split(input)
    |> Enum.map(&(String.to_integer(&1)))
  end
end

{:ok, input} = File.read("lib/data.txt")
parsed_input = Day5.parse_input(input)
IO.puts "Part One Solution: #{Day5.traverse_maze(parsed_input, 0, :part_one)}"
IO.puts "Part Two Solution: #{Day5.traverse_maze(parsed_input, 0, :part_two)}"
