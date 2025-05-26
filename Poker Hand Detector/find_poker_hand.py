def get_highest_hand(possible_hands):
    mappings = {
        10: "Royal Flush",
        9: "Straight FLush",
        8: "Four of a Kind",
        7: "Full House",
        6: "Flush",
        5: "Straight",
        4: "Three of a Kind",
        3: "Two Pair",
        2: "Pair",
        1: "High Card"
    }

    if len(possible_hands):
        return mappings[max(possible_hands)]
    return mappings[1]


def is_straight(ranks):
    ranks = sorted(set(ranks))
    if ranks == [2, 3, 4, 5, 14]:  # Ace as 1
        return True
    return all(ranks[i] + 1 == ranks[i+1] for i in range(len(ranks)-1))


def find_poker_hand(hand):
    ranks, suits, possible_hands = [], [], []
    for card in hand:
        if len(card) == 3:
            ranks.append(int(card[0:2]))
            suits.append((card[2]))
        else:
            rank = card[0]
            if rank == 'A':
                rank = 14
            elif rank == 'K':
                rank = 13
            elif rank == 'Q':
                rank = 12
            elif rank == 'J':
                rank = 11
            else:
                rank = int(rank)
            ranks.append(rank)
            suits.append(card[1])
    ranks = sorted(ranks)
    # print(ranks, suits)
    # Royal Flush, Straight Flush and Flush
    if len(set(suits)) == 1:
        # Royal Flush
        if [10, 11, 12, 13, 14] == ranks:
            possible_hands.append(10)
        # Straight Flush
        elif is_straight(ranks):
            possible_hands.append(9)
        # Flush
        else:
            possible_hands.append(6)

    # Straight
    if is_straight(ranks):
        possible_hands.append(5)

    # Four of a Kind and Full House
    unique_vals = list(set(ranks))
    if len(unique_vals) == 2:
        for val in unique_vals:
            if ranks.count(val) == 4:
                possible_hands.append(8)
            elif ranks.count(val) == 3:
                possible_hands.append(7)

    # Three of a Kind and Two Pair
    if len(unique_vals) == 3:
        for val in unique_vals:
            if ranks.count(val) == 3:
                possible_hands.append(4)
            elif ranks.count(val) == 2:
                possible_hands.append(3)

    # Pair
    if len(unique_vals) == 4:
        for val in unique_vals:
            if ranks.count(val) == 2:
                possible_hands.append(2)

    result = get_highest_hand(list(set(possible_hands)))
    print(result)

    return result


if __name__ == "__main__":
    find_poker_hand(["AH", "KH", "QH", "JH", "10H"])  # Royal Flush
    find_poker_hand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    find_poker_hand(["5C", "5S", "5H", "5D", "QH"])  # Four of a Kind
    find_poker_hand(["2H", "2D", "2S", "10H", "10C"])  # Full House
    find_poker_hand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    find_poker_hand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    find_poker_hand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
    find_poker_hand(["KD", "KH", "5C", "5S", "6D"])  # Two Pair
    find_poker_hand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    find_poker_hand(["KD", "5H", "2D", "10C", "JH"])  # High Card
