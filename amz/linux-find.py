#https://leetcode.com/discuss/interview-question/369272/Amazon-or-Onsite-or-Linux-Find-Command
class Filter:  # abstract class
  def apply(self, file):
    if not isinstance(file, File):  # file validation
      raise TypeError

class SizeFilter(Filter):
  def __init__(self, size, larger=False):
    self._size = size
    self._larger = larger

  def apply(self, file):  # returns true if correct file
    super().apply(file)
      
    if file.size < self._size and not self._larger:
      return True
    elif file.size > self._size and self._larger:
      return True
    else:
      return False

class TypeFilter(Filter):
  def __init__(self, file_type):
    self._file_type = file_type

  def apply(self, file):
    super().apply(file)

    if file.file_type == self._file_type:
      return True
    return False 

class FindCommand:
  def find_all(self, curr_dir, filters):
    all_files = []
    for file in curr_dir.files:
      if isinstance(file, Directory):
        all_files += self.find_all(file, filters)
      for f in filters:
        if f.apply(file):
          all_files.append(file.name)
    return all_files