def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        city_name = city.lower()
        if (city_name in cache):
            answer += 1
            cache.remove(city_name)
            cache.append(city_name)
        else :
            answer += 5
            if (cacheSize == 0):
                continue
            # 캐시 사이즈 이상이면 삭제
            if len(cache) >= cacheSize:
                cache.pop(0)
            # 신규 추가
            cache.append(city_name)

    return answer

print(solution(	2, ["Jeju", "Pangyo", "NewYork", "newyork"]))