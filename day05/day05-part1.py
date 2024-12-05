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


def sumup_correct_order(updates, page_ordering_rules):
    middle_page_sum = 0
    for update_str in updates:
        update_list = list(map(int, update_str.split(",")))
        ordered = all(
            after in page_ordering_rules[page]
            for i, page in enumerate(update_list)
            for after in update_list[i + 1 :]
        )
        middle_page_sum += ordered * update_list[len(update_list) // 2]
    return middle_page_sum


def main():
    rules, updates = parse_input("input-files/day05-part1.input")
    page_ordering_rules = build_page_ordering_rules(rules)
    middle_page_sum = sumup_correct_order(updates, page_ordering_rules)
    print(middle_page_sum)


if __name__ == "__main__":
    main()
# 3608
# ça commence à ne plus être drôle cet advent 2024
