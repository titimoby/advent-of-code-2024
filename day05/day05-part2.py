from collections import defaultdict


def parse_input(file_path):
    with open(file_path) as f:
        rules, updates = f.read().strip().split("\n\n")
    return rules.splitlines(), updates.splitlines()


def build_page_ordering_rules(rules):
    page_ordering_rules = defaultdict(list)
    for rule in rules:
        before, after = map(int, rule.split("|"))
        page_ordering_rules[before].append(after)
    return page_ordering_rules


def is_valid_update(update_list, page_ordering_rules):
    return all(
        after in page_ordering_rules[page]
        for i, page in enumerate(update_list)
        for after in update_list[i + 1 :]
    )


def sort_update_list(update_list, page_ordering_rules):
    sorted_list = []
    to_sort = set(update_list)
    while to_sort:
        for n in to_sort:
            if all(n2 in page_ordering_rules[n] for n2 in to_sort if n2 != n):
                sorted_list.append(n)
                to_sort.remove(n)
                break
    return sorted_list


def main():
    rules, updates = parse_input("input-files/day05-part1.input")
    page_ordering_rules = build_page_ordering_rules(rules)

    middle_page_sum = 0

    for update_str in updates:
        update_list = list(map(int, update_str.split(",")))

        if not is_valid_update(update_list, page_ordering_rules):
            sorted_list = sort_update_list(update_list, page_ordering_rules)
            middle_page_sum += sorted_list[len(sorted_list) // 2]

    print(middle_page_sum)


if __name__ == "__main__":
    main()
# 4922
