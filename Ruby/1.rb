def multiple_of_3_or_5(n)
  sum = 0
  1.upto n-1 do |i|
    if (i % 3 == 0) or (i % 5 == 0)
      sum += i
    end
  end
  sum
end

puts multiple_of_3_or_5(1000)
