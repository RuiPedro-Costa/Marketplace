from marketplace import Marketplace
import docs

if __name__ == '__main__':

    command = ''
    marketplace = Marketplace.create_marketplace()
    print(docs.LOGO1)
    print(docs.MENU)

    while command is not None:

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

                        case 'sb':

                            username = input("Name: ")
                            if marketplace.buyer_exists(username):
                                marketplace.select_id(username)
                            else:
                                print(f"\n██╗ {username} is not a valid user user name.\n╚═╝\n")

                        case 'id':

                            if marketplace.get_current_id() > 0:
                                print(f"\n██╗ Current User ID: {marketplace.get_current_id()}.\n╚═╝\n")
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

                if marketplace.get_current_id() > 0:

                    print(docs.BUYER)
                    cmd = ''

                    while cmd is not None:

                        cmd = input("Please select an option: ")

                        match cmd:

                            case 'clc':

                                if marketplace.has_cards_for_sale():
                                    marketplace.get_listed_cards()
                                else:
                                    print("\n██╗ We currently have no cards listed.\n╚═╝\n")

                            case 'cst':

                                temp_name = input("Card name: ")
                                if marketplace.has_card(temp_name):
                                    marketplace.get_card_stats(temp_name)
                                else:
                                    print(f"\n██╗ There is no {temp_name.title()} card available.\n╚═╝\n")

                            case 'bc':

                                card_name = input("Card name: ")
                                if marketplace.has_card(card_name):
                                    if marketplace.card_is_for_sale():
                                        if marketplace.can_purchase():
                                            marketplace.purchase(card_name, marketplace.get_current_id())
                                        else: print("\n██╗ You can't make this purchase at the moment.\n╚═╝\n")
                                    else:
                                        print(f"\n██╗ {card_name.title()} it is not for sale at the moment.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ {card_name.title()}'s card it is not listed at the moment.\n╚═╝\n")

                            case 'cc':

                                marketplace.get_buyer_balance(marketplace.get_current_id())
                                print(
                                    '\n██╗ Current Balance: ' + str(marketplace.get_buyer_balance()) + " Coins\n╚═╝\n"
                                )

                            case 'ac':

                                marketplace.add_buyer_coins(marketplace.get_current_id(), int(input("Amount: ")))
                                print(
                                    '\n██╗ Current Balance: ' + str(marketplace.get_buyer_balance()) + " Coins\n╚═╝\n"
                                )

                            case 'cs':

                                marketplace.get_buyer_spent_coins(marketplace.get_current_id())
                                print(
                                    '\n██╗ Current Balance: ' + str(marketplace.get_buyer_spent_coins()) + " Coins\n╚═╝\n"
                                )

                            case 'id':

                                if marketplace.get_current_id() > 0:
                                    print(f"\n██╗ Current User ID: {marketplace.get_current_id()}.\n╚═╝\n")
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

                        case 'ac':

                            if marketplace.has_cards_for_sale():
                                print(
                                    f"\n██╗ Current available cards:\n╚═╝\n{marketplace.get_buyer_list()}\n╚═╝\n"
                                )
                            else:
                                print(f"\n██╗ No card available at the moment.\n╚═╝\n")

                        case 'lcd':

                            print("\n██╗ Please insert your card parameters.\n╚═╝\n")

                            name = input('\nName: ')
                            overall = int(input('Overall: '))
                            position = input('Position: ').upper()
                            team = input('Team: ')
                            price = int(input('Price: '))
                            marketplace.list_card(name, overall, position, team, price)
                            if marketplace.has_card():
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

                        case 'ul':

                            if marketplace.has_buyers():
                                print("\n██╗ Registered buyers:")
                                marketplace.get_buyer_list()
                                print("\n╚═╝\n")

                        case 'cb':

                            temp_id = int(input("User ID: "))
                            if marketplace.has_buyer_registered():
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

                if marketplace.get_current_id() > 0:
                    print(f"\n██╗ Current User ID: {marketplace.get_current_id()}.\n╚═╝\n")
                else:
                    print(f"\n██╗ Not a valid ID.\n╚═╝\n")

            case 'e':

                command = None
