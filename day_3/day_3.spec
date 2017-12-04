require './day_3'

describe Day3 do
  before do
    @day_3 = Day3.new
  end

  describe "part_1" do
    it "calculates appropriate Manhattan Distance" do
      expect(@day_3.part_one(1)).to eq(0)
      expect(@day_3.part_one(12)).to eq(3)
      expect(@day_3.part_one(23)).to eq(2)
      expect(@day_3.part_one(1024)).to eq(31)
      expect(@day_3.part_one(361527)).to eq(326)
    end
  end
end
