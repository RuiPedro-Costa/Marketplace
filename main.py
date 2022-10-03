from marketplace import Marketplace
import docs

if __name__ == '__main__':

    command = ''
    mp = Marketplace.create_marketplace()
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
                            mp.create_new_buyer(username)
                            mp.select_id(mp.get_buyer_id(username))
                            print(docs.MENU)
                            cmd = None

                        case 'sb':

                            username = input("Name: ")
                            if mp.buyer_exists(mp.get_buyer_id(username)):
                                mp.select_id(mp.get_buyer_id(username))
                                print(docs.MENU)
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

                            print(docs.MENU)
                            cmd = None

                        case 'e':

                            answer = input("\n██╗ Are you sure (y/n)?")
                            if answer == 'y':
                                print(docs.LOGO2)
                                print(
                                    "\n██╗ Thank you for playing!" +
                                    "\n██║ Leaving ErrePe's Marketplace...\n╚═╝\n"
                                )
                                command = None
                            else:
                                print(docs.SELECT)

                        case _:
                            print('\n██╗ Command unrecognized.\n╚═╝\n██╗ Please try again.\n╚═╝\n')
                            pass

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
                                        f"{mp.get_listed_cards()}╚═╝\n"
                                    )
                                else:
                                    print(f"\n██╗ No cards listed at the moment.\n╚═╝\n")

                            case 'lst':

                                card_name = input("Card name: ")
                                if mp.has_card(card_name):
                                    print(mp.get_card_stats(card_name))
                                else:
                                    print(f"\n██╗ {card_name.title()}'s card is not listed\n╚═╝\n")

                            case 'oc':

                                if mp.buyer_has_cards(mp.get_current_id()):
                                    print(
                                        f"\n██╗ Owned cards:\n╚═╝\n" +
                                        f"\n{mp.get_buyer_cards(mp.get_current_id())}\n╚═╝\n"
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
                                            mp.purchase(card_name, mp.get_current_id())
                                            print(docs.BOUGHT)
                                        else:
                                            print("\n██╗ You can't purchase this at the moment.\n╚═╝\n")
                                    else:
                                        print(f"\n██╗ {card_name.title()}'s is not for sale.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ {card_name.title()}'s card is not listed.\n╚═╝\n")

                            case 'ps':

                                if mp.buyer_exists(mp.get_current_id()):
                                    print(mp.get_buyer(mp.get_current_id()))
                                else:
                                    print("\n██╗ Please select a buyer first.\n╚═╝\n")

                            case 'ac':

                                amount = int(input("Amount: "))
                                mp.add_buyer_coins(mp.get_current_id(), amount)
                                print(
                                    '\n██╗ Current Balance: ' +
                                    str(mp.get_buyer_balance(mp.get_current_id())) +
                                    " Coins\n╚═╝\n"
                                )

                            case 'cu':

                                if mp.buyer_exists(mp.get_current_id()):
                                    print(f"\n██╗ Buyer Name: {mp.get_buyer_name(mp.get_current_id())}.\n╚═╝\n")
                                else:
                                    print("\n██╗ Please select a buyer first.\n╚═╝\n")

                            case 'h':

                                print(docs.BUYER)

                            case 'm':

                                print(docs.MENU)
                                cmd = None

                            case 'e':

                                answer = input("Are you sure (y/n)?")
                                if answer == 'y':
                                    print(docs.LOGO2)
                                    print(
                                        "\n██╗ Thank you for playing!" +
                                        "\n██║ Leaving ErrePe's Marketplace...\n╚═╝\n"
                                    )
                                    command = None
                                else:
                                    print(docs.BUYER)
                                    pass

                            case _:
                                print('\n██╗ Command unrecognized.\n╚═╝\n██╗ Please try again.\n╚═╝\n')
                                pass

                else:
                    print("\n██╗ Please select a buyer first.\n╚═╝\n")

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
                                    f"{mp.get_listed_cards()}╚═╝\n"
                                )
                            else:
                                print(f"\n██╗ No card available at the moment.\n╚═╝\n")

                        case 'lst':

                            card_name = input("Card name: ")
                            if mp.has_card(card_name):
                                print(mp.get_card_stats(card_name))
                            else:
                                print(f"\n██╗ {card_name.title()}'s card is not listed\n╚═╝\n")

                        case 'bcd':

                            answer = input("Search by 'id' or 'name'? ")
                            if answer == "id":
                                userid = int(input("User ID: "))
                                if mp.buyer_exists(userid):
                                    if mp.buyer_has_cards(mp.get_buyer_id(userid)):
                                        print(mp.get_buyer_cards(mp.get_buyer_id(userid)))
                                    else:
                                        print(f"\n██╗ {mp.get_buyer(userid)} does not have any cards.\n╚═╝\n")
                                else:
                                    print(f"{userid} is not a registered ID.")
                            elif answer == "name":
                                name = input("Buyer name: ")
                                if mp.buyer_exists(mp.get_buyer_id(name)):
                                    if mp.buyer_has_cards(mp.get_buyer_id(name)):
                                        print(mp.get_buyer_cards(mp.get_buyer_id(name)))
                                    else:
                                        print(f"\n██╗ {name} does not have any cards.\n╚═╝\n")
                                else:
                                    print(f"\n██╗ {name} is not a registered name.\n╚═╝\n")
                            else:
                                print("\n██╗ Not a valid command.\n╚═╝\n")

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
                                mp.remove_card_from_sale()
                                print(docs.UNLISTED)
                            else:
                                print(f"\n██╗ {card_name.title()}'s card it's not available at the moment.\n╚═╝\n")

                        case 'rc':

                            if mp.has_cards_in_record():
                                print(
                                    "\n██╗ Cards on record:\n╚═╝\n" +
                                    mp.get_record_cards() +
                                    "╚═╝\n"
                                )
                            else:
                                print("\n██╗ We have no cards on record\n╚═╝\n")

                        case 'grc':

                            answer = input("Search byr 'id' or 'name'? ")
                            if answer == 'id':
                                purchase_id = int(input("Purchase ID: "))
                                if mp.has_cards_in_record():
                                    if mp.has_this_card_in_record(purchase_id):
                                        print(mp.get_card_from_record(purchase_id))
                                    else:
                                        print("\n██╗ This card is not on record.\n╚═╝\n")
                                else:
                                    print("\n██╗ We have no cards on record.\n╚═╝\n")
                            elif answer == 'name':
                                card_name = input("Card name: ")
                                if mp.has_cards_in_record():
                                    if mp.has_this_card_in_record(mp.get_record_purchase_id(card_name)):
                                        print(mp.get_card_from_record(mp.get_record_purchase_id(card_name)))
                                    else:
                                        print(f"{card_name.title()}'s card is not on record.\n╚═╝\n")
                                else:
                                    print("\n██╗ We have no cards on record\n╚═╝\n")
                            else:
                                print("\n██╗ Not a valid command.\n╚═╝\n")

                        case 'rrc':

                            if mp.has_cards_in_record():
                                card_name = int(input("Purchase ID: "))
                                mp.remove_card_from_record(card_name)
                                print("\n██╗ Card removed from record.\n╚═╝\n")
                            else:
                                print("\n██╗ We have no cards on record\n╚═╝\n")

                        case 'bl':

                            if mp.has_buyers():
                                print(
                                    "\n██╗ Registered buyers:\n╚═╝\n" +
                                    f"{mp.get_buyer_list()}"
                                )

                        case 'cb':

                            answer = input("Search by 'id' or 'name'? ")
                            if answer == "id":
                                userid = int(input("User ID: "))
                                if mp.buyer_exists(userid):
                                    print(mp.get_buyer(userid))
                                else:
                                    print(f"{userid} is not a registered ID.")
                            elif answer == "name":
                                name = input("Buyer name: ")
                                if mp.buyer_exists(mp.get_buyer_id(name)):
                                    print(mp.get_buyer(mp.get_buyer_id(name)))
                                else:
                                    print(f"\n██╗ {name} is not a registered name.\n╚═╝\n")
                            else:
                                print(f"\n██╗ Not a valid command.\n╚═╝\n")

                        case 'mst':

                            print(mp)

                        case 'h':

                            print(docs.ADMIN)

                        case 'm':
                            print(docs.MENU)
                            cmd = None

                        case 'e':

                            answer = input("\n██╗ Are you sure (y/n)?")
                            if answer == 'y':
                                print(docs.LOGO2)
                                print(
                                    "\n██╗ Thank you for playing!" +
                                    "\n██║ Leaving ErrePe's Marketplace...\n╚═╝\n"
                                )
                                command = None
                            else:
                                print(docs.ADMIN)

                        case _:
                            print('\n██╗ Command unrecognized.\n╚═╝\n██╗Please try again.\n╚═╝\n')
                            pass

            case 'cu':

                if mp.buyer_exists(mp.get_current_id()):
                    print(f"\n██╗ Buyer Name: {mp.get_buyer_name(mp.get_current_id())}.\n╚═╝\n")
                else:
                    print("\n██╗ Please select a buyer first.\n╚═╝\n")

            case 'e':

                answer = input("Are you sure (y/n)?")
                if answer == 'y':
                    print(docs.LOGO2)
                    print(
                        "\n██╗ Thank you for playing!" +
                        "\n██║ Leaving ErrePe's Marketplace...\n╚═╝\n"
                    )
                    command = None
                else:
                    print(docs.MENU)
                    pass

            case _:
                print('\n██╗ Command unrecognized.\n╚═╝\n██╗Please try again.\n╚═╝\n')
                pass
