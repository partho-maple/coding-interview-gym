# https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor


# O(d) time - where d id the depth | O(1) space
def get_youngest_common_ancestor(top_ancestor, descendant_one, descendant_two):
    depth_one = get_descendant_depth(descendant_one, top_ancestor)
    depth_two = get_descendant_depth(descendant_two, top_ancestor)
    if depth_one > depth_two:
        return backtrack_ancestral_tree(descendant_one, descendant_two, depth_one - depth_two)
    else:
        return backtrack_ancestral_tree(descendant_two, descendant_one, depth_two - depth_one)


def get_descendant_depth(descendant, top_ancestor):
    depth = 0
    while descendant != top_ancestor:
        descendant = descendant.ancestor
        depth += 1
    return depth


def backtrack_ancestral_tree(lower_descendant, higher_descendant, diff):
    while diff > 0:
        lower_descendant = lower_descendant.ancestor
        diff -= 1
    while lower_descendant != higher_descendant:
        lower_descendant = lower_descendant.ancestor
        higher_descendant = higher_descendant.ancestor
    return lower_descendant


