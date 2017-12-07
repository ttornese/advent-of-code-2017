class Day6
  def initialize(blocks)
    @blocks = blocks
    @configurations = {}
    @steps = 0
  end

  def calc_part_one
    while !configuration_produced?(@blocks.to_s)
      @configurations[@blocks.to_s] = true
      update_blocks
      @steps += 1
    end
    @steps
  end

  def calc_part_two
    calc_part_one
    reset_instance_variables(@blocks)
    calc_part_one
  end


  private

  def reset_instance_variables(blocks)
    @blocks = blocks
    @configurations = {}
    @steps = 0
  end

  def find_first_max_block_index
    max_index = 0
    @blocks.each_with_index do |block, index|
      if @blocks.max == block
        max_index = index
        break
      end
    end
    max_index
  end

  def update_blocks
    max_block_value = @blocks.max
    max_block_index = find_first_max_block_index
    current_index = max_block_index
    @blocks[current_index] = 0
    while max_block_value > 0
      if current_index >= @blocks.count - 1
        current_index = 0
      else
        current_index += 1
      end
      max_block_value -= 1
      @blocks[current_index] += 1
    end
  end

  def configuration_produced?(configuration)
    @configurations[configuration]
  end
end
