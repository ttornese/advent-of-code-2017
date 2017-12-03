class Checksum
  def calc_checksum(spreadsheet)
    sort_spreadsheet(spreadsheet).map { |row| row[row.count - 1] - row[0] }.inject(0,:+)
  end


  def calc_even_divide_sum(spreadsheet)
    sort_spreadsheet(spreadsheet).map do |row|
      traverse_row(row.reverse)
    end.inject(0,:+)
  end

  private

  def sort_spreadsheet(spreadsheet)
    spreadsheet.map { |row| row.sort }
  end

  def check_divsors(row, rest_of_row, index)
    rest_of_row.map.with_index do |divisor, divisor_index|
      if row[index] % rest_of_row[divisor_index] == 0
        row[index] / rest_of_row[divisor_index]
      else
        0
      end
    end.inject(0,:+)
  end

  def traverse_row(row)
    row.map.with_index do |number, index|
      check_divsors(row, row.drop(index + 1), index)
    end.inject(0,:+)
  end
end
