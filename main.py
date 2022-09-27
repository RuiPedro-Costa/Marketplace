from marketplace import Marketplace
import docs

if __name__ == '__main__':

    command = ''
    marketplace = Marketplace.create_marketplace()
    user_id = 0
    print(docs.LOGO1)
    print(docs.MENU)

    while command is not None:

        command = input("Please select an option: ")

        match command:

            case 's':

                cmd = ''

                while cmd is not None:

                    print(docs.SELECT)
                    cmd = input("Please select an option: ")

                    match cmd:

                        case 'nb':

                            marketplace.create_new_buyer(input("Name: "))

                        case 'sb':

                            temp_id = int(input("ID: "))

                            if marketplace.buyer_exists(temp_id):
                                user_id = temp_id
                            else:
                                print(f"{temp_id} is not a valid user ID.")

                        case 'h':

                            print(docs.SELECT)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None


            case 'b':

                print(docs.BUYER)
                cmd = ''

                while cmd is not None:

                    cmd = input("Please select an option: ")

                    match cmd:

                        case 'clc':

                            if marketplace.has_cards_for_sale():
                                marketplace.get_listed_cards()
                            else:
                                print("We currently have no cards listed.")

                        case 'cst':

                            temp_name = input("Card name: ")

                            if marketplace.has_card(temp_name):
                                marketplace.get_card_stats(temp_name)
                            else:
                                print(f"There is no {temp_name.title()} card available")

                        case 'bc':

                        case 'cc':

                        case 'ac':

                        case 'cs':

                        case 'h':

                            print(docs.BUYER)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None

            case 'a':

                print(docs.ADMIN)
                cmd = ''

                while cmd is not None:

                    cmd = input("Please select an option: ")

                    match cmd:

                        case 'lcd':

                        case 'ucd':

                        case 'lp':

                        case 'lps':

                        case 'cmp':

                        case 'h':

                            print(docs.ADMIN)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None

            case 'e':

                command = None
