import itertools
def solution(land, P, Q):
    land = list(itertools.chain.from_iterable(land))
    land = sorted(land)
    land_len = len(land)
    block_sum = sum(land)
    answer = (block_sum - land[0] * land_len) * Q
    prev_block = land[0]
    for i in range(1, land_len):
        if land[i] != land[i - 1]:
            to_be_removed = block_sum - (land_len - i) * land[i] - prev_block
            to_be_added = i * land[i] - prev_block
            cost = to_be_removed * Q + to_be_added * P
            if cost >= answer:
                break
            answer = cost
        prev_block += land[i]
    return answer
    