


# Solution #1
# O(n^2) time | O(n) space
def minRewards(score):
    rewards = [1 for _ in score]
    for i in range(1, len(score)):
        j = i - 1
        if score[i] > score[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >=0 and score[j] > score[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)



# Solution #2
# O(n) time | O(n) space
def minRewards(score):
    pass



# Solution #3
# O(n) time | O(n) space
def minRewards(score):
    rewards = [1 for _ in score]
    for i in range(1, len(score)):
        if score[i] > score[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed((range(len(score) - 1))):
        if score[i] > score[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)