from marketplace import Marketplace
import docs

if __name__ == '__main__':

    command = ''
    marketplace = Marketplace.create_marketplace()
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
                            marketplace.create_new_buyer(username)
                            marketplace.select_id(marketplace.get_buyer_id(username))
                            cmd = None

                        case 'sb':

                            username = input("Name: ")
                            if marketplace.buyer_exists(marketplace.get_buyer_id(username)):
                                marketplace.select_id(marketplace.get_buyer_id(username))
                                cmd = None
                            else:
                                print(f"\n██╗ {username} is not a valid user user name.\n╚═╝\n")

                        case 'id':

                            if marketplace.buyer_exists(marketplace.get_current_id()):
                                print(f"{marketplace.get_buyer(marketplace.get_current_id())}")
                            else:
                                print(f"\n██╗ Select a buyer.\n╚═╝\n")

                        case 'h':

                            print(docs.SELECT)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None

            case 'b':

                if marketplace.get_current_id() > 0:

                    print(docs.BUYER)
                    cmd = ''

                    while cmd is not None:

                        cmd = input("Please select an option: ")

                        match cmd:

                            case 'lc':

                                if marketplace.has_cards_for_sale():
                                    print(
                                        f"\n██╗ Current available cards:\n╚═╝\n" +
                                        f"{marketplace.get_listed_cards()}\n╚═╝\n"
                                    )
                                else:
                                    print(f"\n██╗ No cards listed at the moment.\n╚═╝\n")

                            case 'lst':

                                card_name = input("Card name: ")
                                if marketplace.has_card(card_name):
                                    marketplace.get_card_stats(card_name)
                                else:
                                    print(f"\n██╗ {card_name.title()}'s card is not listed\n╚═╝\n")

                            case 'oc':

                                if marketplace.buyer_has_cards(marketplace.get_current_id()):
                                    print(
                                        f"\n██╗ Owned cards:\n{marketplace.get_buyer_cards(marketplace.get_current_id())}\n╚═╝\n"
                                    )
                                else:
                                    print("\n██╗ You don't have any cards.\n╚═╝\n")

                            case 'ost':

                                card_name = input("Card name: ")
                                if marketplace.buyer_owns_this_card(marketplace.get_current_id(), card_name):
                                    marketplace.get_buyer_card_stats(marketplace.get_current_id(), card_name)
                                else:
                                    print(f"\n██╗ You don't own {card_name.title()} card.\n╚═╝\n")

                            case 'bc':

                                card_name = input("Card name: ")
                                if marketplace.has_card(card_name):
                                    if marketplace.card_is_for_sale(card_name):
                                        if marketplace.can_purchase(card_name, marketplace.get_current_id()):
                                            marketplace.purchase(card_name, marketplace.get_current_id(), )
                                        else:
                                            print("\n██╗ You can't purchase this at the moment.\n╚═╝\n")
                                    else:
                                        print(f"\n██╗ {card_name.title()}'s is not for sale.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ {card_name.title()}'s card is not listed.\n╚═╝\n")

                            case 'cc':

                                print(
                                    '\n██╗ Current Balance: ' +
                                    str(marketplace.get_buyer_balance(marketplace.get_current_id())) +
                                    " Coins\n╚═╝\n"
                                )

                            case 'ac':

                                amount = int(input("Amount: "))
                                marketplace.add_buyer_coins(marketplace.get_current_id(), amount)
                                print(
                                    '\n██╗ Current Balance: ' +
                                    str(marketplace.get_buyer_balance(marketplace.get_current_id())) +
                                    " Coins\n╚═╝\n"
                                )

                            case 'cs':

                                print(
                                    '\n██╗ Current Balance: ' +
                                    str(marketplace.get_buyer_spent_coins(marketplace.get_current_id())) +
                                    " Coins\n╚═╝\n"
                                )

                            case 'id':

                                if marketplace.buyer_exists(marketplace.get_current_id()):
                                    print(f"{marketplace.get_buyer(marketplace.get_current_id())}")
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

                            if marketplace.has_cards_for_sale():
                                print(
                                    f"\n██╗ Current available cards:\n╚═╝\n" +
                                    f"{marketplace.get_listed_cards()}\n╚═╝\n"
                                )
                            else:
                                print(f"\n██╗ No card available at the moment.\n╚═╝\n")

                        case 'bcd':

                            user_id = int(input("User ID: "))
                            if marketplace.buyer_exists(user_id):
                                print(marketplace.get_buyer_cards(user_id))
                            else:
                                print(f"\n██╗ {user_id} is not a valid user user ID.\n╚═╝\n")

                        case 'lcd':

                            print("\n██╗ Please insert your card parameters.\n╚═╝\n")

                            name = input('\nName: ')
                            overall = int(input('Overall: '))
                            position = input('Position: ').upper()
                            team = input('Team: ')
                            price = int(input('Price: '))
                            marketplace.list_card(name, overall, position, team, price)
                            if marketplace.has_card(name):
                                print(docs.LISTED)
                            else:
                                print('\n██╗ Please check your parameters.\n╚═╝\n')
                                pass

                        case 'ucd':

                            card_name = input("Card name: ")
                            if marketplace.has_card(card_name):
                                marketplace.remove_card()
                                print(docs.UNLISTED)
                            else:
                                print(f"\n██╗ {card_name.title()}'s card it's not available at the moment.\n╚═╝\n")

                        case 'lp':

                            print(docs.PRICE)

                        case 'lps':

                            print(docs.POS)

                        case 'bl':

                            if marketplace.has_buyers():
                                print(
                                    "\n██╗ Registered buyers:\n╚═╝\n" +
                                    f"{marketplace.get_buyer_list()}"
                                )

                        case 'cb':

                            temp_id = int(input("User ID: "))
                            if marketplace.has_buyer_registered(temp_id):
                                print(f"\n██╗ {marketplace.get_buyer(temp_id)}\n╚═╝\n")

                        case 'cmp':

                            print(f"\n██╗ Current profit: {marketplace.get_market_profit()}.\n╚═╝\n")

                        case 'h':

                            print(docs.ADMIN)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None

            case 'id':

                if marketplace.buyer_exists(marketplace.get_current_id()):
                    print(f"{marketplace.get_buyer(marketplace.get_current_id())}")
                else:
                    print(f"\n██╗ Select a buyer.\n╚═╝\n")

            case 'e':

                command = None
