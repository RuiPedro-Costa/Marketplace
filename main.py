from marketplace import Marketplace
import docs

if __name__ == '__main__':

    command = ''
    market = Marketplace.create_marketplace()
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
                            market.create_new_buyer(username)
                            market.select_id(market.get_buyer_id(username))
                            cmd = None

                        case 'sb':

                            username = input("Name: ")
                            if market.buyer_exists(market.get_buyer_id(username)):
                                market.select_id(market.get_buyer_id(username))
                                cmd = None
                            else:
                                print(f"\n██╗ {username} is not a valid user user name.\n╚═╝\n")

                        case 'id':

                            if market.get_current_id() > 0:
                                print(f"\n██╗ Current User ID: {market.get_current_id()}.\n╚═╝\n")
                            else:
                                print(f"\n██╗ Not a valid ID.\n╚═╝\n")

                        case 'h':

                            print(docs.SELECT)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None

            case 'b':

                if market.get_current_id() > 0:

                    print(docs.BUYER)
                    cmd = ''

                    while cmd is not None:

                        cmd = input("Please select an option: ")

                        match cmd:

                            case 'lc':

                                if market.has_cards_for_sale():
                                    print(
                                        f"\n██╗ Current available cards:\n{market.get_listed_cards()}\n╚═╝\n"
                                    )
                                else:
                                    print(f"\n██╗ No card available at the moment.\n╚═╝\n")

                            case 'lst':

                                card_name = input("Card name: ")
                                if market.has_card(card_name):
                                    market.get_card_stats(card_name)
                                else:
                                    print(f"\n██╗ There is no {card_name.title()} card available.\n╚═╝\n")

                            case 'oc':

                                if market.buyer_has_cards():
                                    print(
                                        f"\n██╗ Owned cards:\n{market.get_buyer_cards(market.get_current_id())}"
                                    )
                                else:
                                    print("\n██╗ You don't have any cards.\n╚═╝\n")

                            case 'ost':

                                card_name = input("Card name: ")
                                if market.buyer_owns_this_card(market.get_current_id(), card_name):
                                    market.get_buyer_card_stats(market.get_current_id(), card_name)
                                else:
                                    print(f"\n██╗ You don't own {card_name.title()} card.\n╚═╝\n")

                            case 'bc':

                                card_name = input("Card name: ")
                                if market.has_card(card_name):
                                    if market.card_is_for_sale(card_name):
                                        if market.can_purchase(card_name, market.get_current_id()):
                                            market.purchase(card_name, market.get_current_id(), )
                                        else:
                                            print("\n██╗ You can't make this purchase at the moment.\n╚═╝\n")
                                    else:
                                        print(f"\n██╗ {card_name.title()} it is not for sale at the moment.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ {card_name.title()}'s card it is not listed at the moment.\n╚═╝\n")

                            case 'cc':

                                print(
                                    '\n██╗ Current Balance: ' + str(market.get_buyer_balance(market.get_current_id())) + " Coins\n╚═╝\n"
                                )

                            case 'ac':

                                amount = int(input("Amount: "))
                                market.add_buyer_coins(market.get_current_id(), amount)
                                print(
                                    '\n██╗ Current Balance: ' + str(market.get_buyer_balance(market.get_current_id())) + " Coins\n╚═╝\n"
                                )

                            case 'cs':

                                print(
                                    '\n██╗ Current Balance: ' + str(market.get_buyer_spent_coins(market.get_current_id())) + " Coins\n╚═╝\n"
                                )

                            case 'id':

                                if market.get_current_id() > 0:
                                    print(f"\n██╗ Current User ID: {market.get_current_id()}.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ Not a valid ID.\n╚═╝\n")

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

                            if market.has_cards_for_sale():
                                print(
                                    f"\n██╗ Current available cards:\n{market.get_listed_cards()}\n╚═╝\n"
                                )
                            else:
                                print(f"\n██╗ No card available at the moment.\n╚═╝\n")

                        case 'bcd':

                            user_id = int(input("User ID: "))
                            if market.buyer_exists(user_id):
                                print(market.get_buyer_cards(user_id))
                            else:
                                print(f"\n██╗ {user_id} is not a valid user user ID.\n╚═╝\n")

                        case 'lcd':

                            print("\n██╗ Please insert your card parameters.\n╚═╝\n")

                            name = input('\nName: ')
                            overall = int(input('Overall: '))
                            position = input('Position: ').upper()
                            team = input('Team: ')
                            price = int(input('Price: '))
                            market.list_card(name, overall, position, team, price)
                            if market.has_card(name):
                                print(docs.LISTED)
                            else:
                                print('\n██╗ Please check your parameters.\n╚═╝\n')
                                pass

                        case 'ucd':

                            card_name = input("Card name: ")
                            if market.has_card(card_name):
                                market.remove_card()
                                print(docs.UNLISTED)
                            else:
                                print(f"\n██╗ {card_name.title()}'s card it's not available at the moment.\n╚═╝\n")

                        case 'lp':

                            print(docs.PRICE)

                        case 'lps':

                            print(docs.POS)

                        case 'bl':

                            if market.has_buyers():
                                print(market.get_buyer_list())

                        case 'cb':

                            temp_id = int(input("User ID: "))
                            if market.has_buyer_registered(temp_id):
                                print(f"\n██╗ {market.get_buyer(temp_id)}\n╚═╝\n")

                        case 'cmp':

                            print(f"\n██╗ Current profit: {market.get_market_profit()}.\n╚═╝\n")

                        case 'h':

                            print(docs.ADMIN)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None

            case 'id':

                if market.get_current_id() > 0:
                    print(f"\n██╗ Current User ID: {market.get_current_id()}.\n╚═╝\n")
                else:
                    print(f"\n██╗ Not a valid ID.\n╚═╝\n")

            case 'e':

                command = None
