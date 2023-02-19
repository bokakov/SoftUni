cards_nc = input().split(", ")
num_cards_nc = int(input())


def add_nc(card_nc):
    if card_nc in cards_nc:
        print("Card is already in the deck")
    else:
        cards_nc.append(card_nc)
        print("Card successfully added")


def remove_nc(card_nc):
    if card_nc in cards_nc:
        cards_nc.remove(card_nc)
        print("Card successfully removed")
    else:
        print("Card not found")


def remove_idx_nc(card_idx_nc):
    if card_idx_nc >= len(cards_nc):
        print("Index out of range")
    else:
        cards_nc.remove(card_idx_nc)
        print("Card successfully removed")


def insert_nc(card_idx_nc, name_of_card_nc):
    if name_of_card_nc in cards_nc and 0 <= card_idx_nc < len(cards_nc):
        print("Card is already added")
    elif 0 <= card_idx_nc < len(cards_nc):
        cards_nc.insert(card_idx_nc, name_of_card_nc)
        print("Card successfully added")
    else:
        print("Index out of range")


for card in range(num_cards_nc):
    command_nc = input().split(", ")
    command_name_nc = command_nc[0]
    card_command_name_nc = command_nc[1]

    if command_name_nc == "Add":
        add_nc(card_command_name_nc)
    elif command_name_nc == "Remove":
        remove_nc(card_command_name_nc)
    elif command_name_nc == "Remove At":
        remove_idx_nc(int(card_command_name_nc))
    elif command_name_nc == "Insert":
        card_name = command_nc[2]
        insert_nc(int(card_command_name_nc), card_name)

print(", ".join(cards_nc))
