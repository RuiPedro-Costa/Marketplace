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



                        case 'cb':



                        case 'h':

                            print(docs.SELECT)

                        case 'm':

                            cmd = None

                        case 'e':

                            cmd = None
                            command = None


            case 'b':

                print(docs.BUYER2)
                cmd = ''

                while cmd is not None:

                    cmd = input("Please select an option: ")

                    match cmd:

                        case 'clc':

                        case 'cst':

                        case 'bc':

                        case 'cc':

                        case 'ac':

                        case 'cs':

                        case 'h':

                            print(docs.BUYER2)

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
