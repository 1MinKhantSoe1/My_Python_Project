import subprocess


def main():
    print("WiFi Password Recovery")
    print("----------------------")

    print("")

    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    print("    Wifi Name \t\t\t Password ")
    print("-" * 20, "\t\t-----------------")
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
            'ISO-8859-1').split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))



if __name__ == '__main__':
    main()

    print("")

    print("Created By Min Khant Soe (HakHak)")

    input("")
