  def findDuplicates(self, nums):
    duplicateNumbers = []
    i = 0
    while i < len(nums):
      if nums[i] == -1:
        i += 1
        continue

      val = nums[i]
      correct_index = val - 1

      if nums[i] == i + 1:
        # Already in the correct place
        i += 1
      elif nums[correct_index] == val:
        # Found duplicate
        duplicateNumbers.append(val)
        nums[i] = -1  # mark this index as handled
        i += 1
      else:
        # Swap to put val in the correct position
        nums[i], nums[correct_index] = nums[correct_index], nums[i]

    return duplicateNumbers
