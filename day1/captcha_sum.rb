class CaptchaSum
  def calc_single_step(data)
    calc_sum(data.to_s.split(''), 1, 0)
  end

  def calc_circular_step(data)
    data_as_array = data.to_s.split('')
    calc_sum(data_as_array, data_as_array.count / 2, 0)
  end

  private

  def calc_sum(list, steps, index)
    if index == list.count - 1
      list[index] == list[steps - 1] ? list[index].to_i : 0
    elsif list[index] == list[(steps - ((list.count - 1) - index)) - 1]
      list[index].to_i + calc_sum(list, steps, index + 1)
    else
      calc_sum(list, steps, index + 1)
    end
  end
end
