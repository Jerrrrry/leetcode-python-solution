class LFUCache:

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.key_to_val = dict()
		self.key_to_freq = dict()
		self.freq_to_keys = collections.defaultdict(list)
		self.min_freq = 0
		self.item_nums = 0


	def get(self, key: int) -> int:
		if self.capacity<=0: 
			return -1
		if key not in self.key_to_val:
			return -1
		freq = self.key_to_freq[key]
		self.freq_to_keys[freq].remove(key) 
		self.key_to_freq[key]= freq+1
		self.freq_to_keys[freq+1].append(key)
		if len(self.freq_to_keys[freq])==0:
			if freq == self.min_freq: 
				self.min_freq += 1
		return self.key_to_val[key]

	def put(self, key: int, value: int) -> None:
		if self.capacity<=0:
			pass
		else:
			if key in self.key_to_val: 
				freq = self.key_to_freq[key] 
				self.freq_to_keys[freq].remove(key)            
				self.key_to_val[key] = value
				self.key_to_freq[key] = freq+1
				self.freq_to_keys[freq+1].append(key)
				if len(self.freq_to_keys[freq])==0:
					if freq ==self.min_freq:
						self.min_freq += 1

			elif key not in self.key_to_val: 
				if self.item_nums < self.capacity:
					self.key_to_val[key] = value
					freq = 1
					self.key_to_freq[key] = freq
					self.item_nums += 1
					self.freq_to_keys[freq].append(key)
					self.min_freq = 1
				elif self.item_nums >= self.capacity:    
					pop_key = self.freq_to_keys[self.min_freq].pop(0) 
					self.key_to_val.pop(pop_key)
					self.key_to_freq.pop(pop_key)
					# if len( == 0
					freq = 1
					self.key_to_val[key] = value
					self.key_to_freq[key] = freq
					self.freq_to_keys[freq].append(key)
					self.min_freq =  freq
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)