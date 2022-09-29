from marketplace import Marketplace
import docs

if __name__ == '__main__':

    command = ''
    mp = Marketplace.create_marketplace()
    print(docs.LOGO1)

    while command is not None:

        print(docs.MENU)
        command = input("Please select an option: ")

        match command:

            case 's':

                cmd = ''
                print(docs.SELECT)

                while cmd is not None:

                    cmd = input("Please select an option: ")

                    match cmd:

                        case 'nb':

                            username = input("Name: ")
                            mp.create_new_buyer(username)
                            mp.select_id(mp.get_buyer_id(username))
                            cmd = None

                        case 'sb':

                            username = input("Name: ")
                            if mp.buyer_exists(mp.get_buyer_id(username)):
                                mp.select_id(mp.get_buyer_id(username))
                                cmd = None
                            else:
                                print(f"\n██╗ {username} is not a valid user user name.\n╚═╝\n")

                        case 'cu':

                            if mp.buyer_exists(mp.get_current_id()):
                                print(f"\n██╗ Buyer Name: {mp.get_buyer_name(mp.get_current_id())}.\n╚═╝\n")
                            else:
                                print(f"\n██╗ Please select a buyer first.\n╚═╝\n")

                        case 'h':

                            print(docs.SELECT)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None

            case 'b':

                if mp.get_current_id() > 0:

                    print(docs.BUYER)
                    cmd = ''

                    while cmd is not None:

                        cmd = input("Please select an option: ")

                        match cmd:

                            case 'lc':

                                if mp.has_cards_for_sale():
                                    print(
                                        f"\n██╗ Current available cards:\n╚═╝\n" +
                                        f"{mp.get_listed_cards()}\n╚═╝\n"
                                    )
                                else:
                                    print(f"\n██╗ No cards listed at the moment.\n╚═╝\n")

                            case 'lst':

                                card_name = input("Card name: ")
                                if mp.has_card(card_name):
                                    mp.get_card_stats(card_name)
                                else:
                                    print(f"\n██╗ {card_name.title()}'s card is not listed\n╚═╝\n")

                            case 'oc':

                                if mp.buyer_has_cards(mp.get_current_id()):
                                    print(
                                        f"\n██╗ Owned cards:\n{mp.get_buyer_cards(mp.get_current_id())}\n╚═╝\n"
                                    )
                                else:
                                    print("\n██╗ You don't have any cards.\n╚═╝\n")

                            case 'ost':

                                card_name = input("Card name: ")
                                if mp.buyer_owns_this_card(mp.get_current_id(), card_name):
                                    print(mp.get_buyer_card_stats(mp.get_current_id(), card_name))
                                else:
                                    print(f"\n██╗ You don't own {card_name.title()} card.\n╚═╝\n")

                            case 'bc':

                                card_name = input("Card name: ")
                                if mp.has_card(card_name):
                                    if mp.card_is_for_sale(card_name):
                                        if mp.can_purchase(card_name, mp.get_current_id()):
                                            mp.purchase(card_name, mp.get_current_id(), str(mp.get_card_stats()))
                                            print(docs.BOUGHT)
                                        else:
                                            print("\n██╗ You can't purchase this at the moment.\n╚═╝\n")
                                    else:
                                        print(f"\n██╗ {card_name.title()}'s is not for sale.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ {card_name.title()}'s card is not listed.\n╚═╝\n")

                            case 'cc':

                                print(
                                    '\n██╗ Current Balance: ' +
                                    str(mp.get_buyer_balance(mp.get_current_id())) +
                                    " Coins\n╚═╝\n"
                                )

                            case 'ac':

                                amount = int(input("Amount: "))
                                mp.add_buyer_coins(mp.get_current_id(), amount)
                                print(
                                    '\n██╗ Current Balance: ' +
                                    str(mp.get_buyer_balance(mp.get_current_id())) +
                                    " Coins\n╚═╝\n"
                                )

                            case 'cs':

                                print(
                                    '\n██╗ Current Balance: ' +
                                    str(mp.get_buyer_spent_coins(mp.get_current_id())) +
                                    " Coins\n╚═╝\n"
                                )

                            case 'cu':

                                if mp.buyer_exists(mp.get_current_id()):
                                    print(f"\n██╗ Buyer Name: {mp.get_buyer_name(mp.get_current_id())}.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ Please select a buyer first.\n╚═╝\n")

                            case 'h':

                                print(docs.BUYER)

                            case 'm':

                                cmd = None

                            case 'e':

                                cmd = None
                                command = None
                else:
                    print("Please select a buyer.")

            case 'a':

                cmd = ''
                print(docs.ADMIN)

                while cmd is not None:

                    cmd = input("Please select an option: ")

                    match cmd:

                        case 'lc':

                            if mp.has_cards_for_sale():
                                print(
                                    f"\n██╗ Current available cards:\n╚═╝\n" +
                                    f"{mp.get_listed_cards()}\n╚═╝\n"
                                )
                            else:
                                print(f"\n██╗ No card available at the moment.\n╚═╝\n")

                        case 'lst':

                            card_name = input("Card name: ")
                            if mp.has_card(card_name):
                                mp.get_card_stats(card_name)
                            else:
                                print(f"\n██╗ {card_name.title()}'s card is not listed\n╚═╝\n")

                        case 'bcd':

                            # answer is not being forced into id or name

                            answer = input("Search by \"id\" or \"name\"? ")
                            if answer == "id":
                                if mp.buyer_exists(answer):
                                    if mp.buyer_has_cards(answer):
                                        print(mp.get_buyer_cards(answer))
                                    else:
                                        print(f"\n██╗ User {answer} does not have any cards.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ {answer} is not a valid user ID.\n╚═╝\n")
                            elif answer == "name" and mp.buyer_exists(mp.get_buyer_id(answer)):
                                if mp.buyer_exists(mp.get_buyer_id(answer)):
                                    if mp.buyer_has_cards(mp.get_buyer_id(answer)):
                                        print(mp.get_buyer_cards(mp.get_buyer_id(answer)))
                                    else:
                                        print(f"\n██╗ {answer} does not have any cards.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ {answer} is not a valid name.\n╚═╝\n")

                            user_id = int(input("User ID: "))
                            if mp.buyer_exists(user_id):
                                if mp.buyer_has_cards(user_id):
                                    print(mp.get_buyer_cards(user_id))
                                else:
                                    print(f"\n██╗ {user_id} does not have any cards.\n╚═╝\n")
                            else:
                                print(f"\n██╗ {user_id} is not a valid user user ID.\n╚═╝\n")

                        case 'bst':

                            card_name = input("Card name: ")
                            buyer_id = int(input("Buyer ID: "))
                            if mp.buyer_owns_this_card(buyer_id, card_name):
                                mp.get_buyer_card_stats(buyer_id, card_name)
                            else:
                                print(f"\n██╗ {mp.get_buyer_name(buyer_id)} does not own" +
                                      f"{card_name}'s card.\n╚═╝\n")

                        case 'lp':

                            print(docs.PRICE)

                        case 'lps':

                            print(docs.POS)

                        case 'lnc':

                            print("\n██╗ Please insert your card parameters.\n╚═╝\n")

                            name = input('\nName: ')
                            overall = int(input('Overall: '))
                            position = input('Position: ').upper()
                            team = input('Team: ')
                            price = int(input('Price: '))
                            mp.list_card(name, overall, position, team, price)
                            if mp.has_card(name):
                                print(docs.LISTED)
                            else:
                                print('\n██╗ Please check your parameters.\n╚═╝\n')
                                pass

                        case 'ucd':

                            card_name = input("Card name: ")
                            if mp.has_card(card_name):
                                mp.remove_card()
                                print(docs.UNLISTED)
                            else:
                                print(f"\n██╗ {card_name.title()}'s card it's not available at the moment.\n╚═╝\n")

                        case 'rc':

                            if mp.has_cards_in_record():
                                card_name = input("Card name: ")
                                if mp.card_in_record(card_name):
                                    print(mp.get_card_from_record(card_name))
                                else:
                                    print(f"\n██╗ {card_name.title()}'s card is not on record.\n╚═╝\n")
                            else:
                                print("\n██╗ There are no cards on record.\n╚═╝\n")

                        case 'bl':

                            if mp.has_buyers():
                                print(
                                    "\n██╗ Registered buyers:\n╚═╝\n" +
                                    f"{mp.get_buyer_list()}"
                                )

                        case 'cb':

                            answer = input("Search by \"id\" or \"name\"? ")
                            if answer == "id" and mp.buyer_exists(answer):
                                print(f"\n██╗ {mp.get_buyer(answer)}\n╚═╝\n")
                            if answer == "name" and mp.buyer_exists(mp.get_buyer_id(answer)):
                                print(f"\n██╗ {mp.get_buyer(mp.get_buyer_id(answer))}\n╚═╝\n")
                            else:
                                print(f"\n██╗ No buyer found with {answer} attribute.\n╚═╝\n")

                        case 'mst':

                            print(mp)

                        case 'h':

                            print(docs.ADMIN)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None

            case 'cu':

                if mp.buyer_exists(mp.get_current_id()):
                    print(f"\n██╗ Buyer Name: {mp.get_buyer_name(mp.get_current_id())}.\n╚═╝\n")
                else:
                    print(f"\n██╗ Please select a buyer first.\n╚═╝\n")

            case 'e':

                command = None
