class Day3
  def part_one(input)
    find_perfect_square(input)
  end

  private

  def find_closest_smaller_perfect_square(input)
    while true
      square_root = Math.sqrt(input)
      if square_root % 1 == 0 && square_root % 2 != 0
        return input
      end
      input -= 1
    end
  end

  def find_closest_larger_perfect_square(input)
    while true
      square_root = Math.sqrt(input)
      if square_root % 1 == 0 && square_root % 2 != 0
        return input
      end
      input += 1
    end
  end

  def find_perfect_square(input)
    smaller_square = find_closest_smaller_perfect_square(input)
    larger_square = find_closest_larger_perfect_square(input)
    puts "sm #{smaller_square}"
    puts "lg #{larger_square}"
    [input - smaller_square, larger_square - input].min
  end
end
