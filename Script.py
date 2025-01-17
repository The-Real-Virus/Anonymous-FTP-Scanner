import ftplib
import os

def show_banner():
    """
    Displays the banner for the script.
    """
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" < 
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  Anonymous FTP Scanner
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

def anon_login(hostname):
    """
    Attempts an anonymous FTP login to the given hostname.
    
    Parameters:
    hostname (str): The hostname or IP address of the FTP server.
    
    Returns:
    bool: True if the anonymous login succeeds, False otherwise.
    """
    try:
        # Attempting to connect to the FTP server
        ftp = ftplib.FTP(hostname, timeout=10)  # Setting a timeout for better reliability
        ftp.login()  # Attempt anonymous login
        print(f"\n[+] Anonymous login successful on: {hostname}")
        ftp.quit()
        return True
    except ftplib.error_perm as e:
        print(f"\n[-] Permission denied for anonymous login on: {hostname}. Error: {e}")
    except ftplib.all_errors as e:
        print(f"\n[-] Could not connect to {hostname}. Error: {e}")
    return False

def main():
    """
    Main function to interact with the user and check for anonymous FTP login.
    """
    # Display banner
    show_banner()

    # Prompt for user input to continue or exit
    choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()
    if choice == 'n':
        print("\nExiting the script. Goodbye!")
        return
    elif choice != 'y':
        print("\nInvalid choice. Exiting the script.")
        return

    # Clear the console
    os.system('clear' if os.name == 'posix' else 'cls')  # 'clear' for Linux/Mac, 'cls' for Windows

    # Loop to test multiple FTP servers
    while True:
        hostname = input("\nEnter the FTP server hostname or IP (or type 'exit' to quit): ").strip()
        if hostname.lower() == 'exit':
            print("\nExiting the program. Goodbye!")
            break

        if hostname:
            print(f"\nAttempting anonymous login to: {hostname}")
            result = anon_login(hostname)
            if result:
                print("[INFO] The server allows anonymous access. Use caution when sharing sensitive data.")
            else:
                print("[INFO] The server does not allow anonymous login or is unreachable.")
        else:
            print("\nInvalid input. Please enter a valid hostname or IP address.\n")

if __name__ == "__main__":
    main()
