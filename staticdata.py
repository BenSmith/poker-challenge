CARD_RANKS = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    '10': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

CARD_SUITS = (
    "H",
    "C",
    "S",
    "D"
)

SCORE = {
    'High': 0,
    'Pair': 1,
    'Two Pair': 2,
    'Three Of A Kind': 3,
    'Straight': 4,
    'Flush': 5,
    'Full House': 6,
    'Four Of A Kind': 7,
    'Straight Flush': 8
}

INV_SCORE = {v: k for k, v in SCORE.items()}
