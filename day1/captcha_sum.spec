require './captcha_sum'

describe CaptchaSum do
  before do
    @captcha_sum = CaptchaSum.new
  end

  describe "calc_single_step" do
    it "calculates appropriate sums for a single steps" do
      expect(@captcha_sum.calc_single_step(1122)).to equal(3)
      expect(@captcha_sum.calc_single_step(1111)).to equal(4)
      expect(@captcha_sum.calc_single_step(1234)).to equal(0)
      expect(@captcha_sum.calc_single_step(91212129)).to equal(9)
    end
  end

  describe "calc_circular_step" do
    it "calculates appropriate sums for a circular steps" do
      expect(@captcha_sum.calc_circular_step(1212)).to equal(6)
      expect(@captcha_sum.calc_circular_step(1221)).to equal(0)
      expect(@captcha_sum.calc_circular_step(123425)).to equal(4)
      expect(@captcha_sum.calc_circular_step(123123)).to equal(12)
      expect(@captcha_sum.calc_circular_step(12131415)).to equal(4)
    end
  end
end
