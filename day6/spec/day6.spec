require './day6'

describe Day6 do
  describe "part one" do
    it "calculates redistribution cycles" do
      expect(Day6.new([0,2,7,0]).calc_part_one).to eq(5)
      expect(Day6.new([14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]).calc_part_one).to eq(11137)
    end
  end

  describe "part two" do
    it "calculates cycles in infinite loop" do
      expect(Day6.new([0,2,7,0]).calc_part_two).to eq(4)
      expect(Day6.new([14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]).calc_part_two).to eq(1037)
    end
  end
end
