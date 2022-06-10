"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

"""

def findRestaurant(list1, list2):
    hash_map = {}         # hash map
    result = []
    min_sum = float('inf')         # trick

    for i,v in enumerate(list1):          # create hash_map using list1
        hash_map[v] = i
    for i,v in enumerate(list2):           # check list2 value in hash_map, and generate sum
        if v in hash_map:
            sum = hash_map[v] + i
            if sum<min_sum:
                result = [v]
                min_sum = sum           # reduce sum accordingly 
            elif sum == min_sum:
                result.append(v)
    return result

    






list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(findRestaurant(list1, list2))