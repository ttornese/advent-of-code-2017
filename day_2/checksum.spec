require './checksum'

describe Checksum do
  before do
    @checksum = Checksum.new
  end

  describe "calc_checksum" do
    it "calculates appropriate checksum" do
      expect(@checksum.calc_checksum([
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8]
      ])).to equal(18)
    end
  end

  describe "calc_even_divide_sum" do
    it "calculates appropriate even divide sum" do
      expect(@checksum.calc_even_divide_sum([
        [5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5]
      ])).to equal(9)
    end
  end
end
