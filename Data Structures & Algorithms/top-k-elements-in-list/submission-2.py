class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        topK = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

            # 如果这个元素已经在 topK 中，先移除（频率变了，位置需要更新）
            if num in topK:
                topK.remove(num)

            # 插入到正确位置，保持 topK 按频率降序排列
            inserted = False
            for j in range(len(topK)):
                if freq[num] >= freq[topK[j]]:
                    topK.insert(j, num)
                    inserted = True
                    break
            if not inserted:
                topK.append(num)

            # 如果超过 k 个，去掉频率最小的（最后一个）
            if len(topK) > k:
                topK.pop()

        return topK
            

            





