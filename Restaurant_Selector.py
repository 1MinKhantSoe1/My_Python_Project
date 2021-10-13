"""

    Restaurant Selector

    This program is "Yes" or "No" question for a group of friend come from out of town and make sure what kind of
    local restaurant they want to go.
    The following restaurant will be show as a output upon on user answer:

    Joes’ Gourmet Burgers – Vegetarian: No, Vegan: No, Gluten-Free: No
    Main Street Pizza – Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
    Corner Cafe – Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
    Luigi’s Fine Italian Restaurant – Vegetarian: Yes, Vegan: No, Gluten-Free: No
    The Chef’s Kitchen – Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
 
 """


def main():

    # user input start here
    vegetarian = input("Is anyone in your party a vegetarian (Yes/No): ").strip()

    vegan = input("Is anyone in your party a vegan (Yes/No): ").strip()

    gluten_free = input("Is anyone in your party gluten-free (Yes/No): ").strip()
    # user input end here

    # Start If Condition
    if vegetarian[0].upper() in "Yes" and vegan[0].upper() in "No" and gluten_free[0].upper() in "Yes":
        """If user enter "Yes" for vegetarian, "No" for vegan and "Yes" for gluten free then this condition will true"""

        print("Here are your restaurant choices: \nMain Street \nCorner Café \nThe Chef's Kitchen")

    elif vegetarian[0].upper() in "Yes" and vegan[0].upper() in "Yes" and gluten_free[0].upper() in "Yes":
        """If user enter "Yes","Yes" and "Yes" this condition will true"""

        print("Here are your restaurant choices: \nMain Street \nCorner Café \nThe Chef's Kitchen")

    elif vegetarian[0].upper() in "Yes" and vegan[0].upper() in "Yes" and gluten_free[0].upper() in "No":
        """If user enter "Yes", "Yes" and "No" this condition will true"""

        print("Here are your restaurant choices: \nCorner Café \nThe Chef's Kitchen")

    elif vegetarian[0].upper() in "No" and vegan[0].upper() in "No" and gluten_free[0].upper() in "No":
        """If user enter "No", "No" and "No" this condition will true"""

        print("Here are your restaurant choices: \nJoes’ Gourmet Burgers \nLuigi’s Fine Italian Restaurant")

    elif vegetarian[0].upper() in "Yes" and vegan[0].upper() in "No" and gluten_free[0].upper() in "No":
        """If user enter "Yes", "No" and "No" this condition will true"""

        print("Here are your restaurant choices: \nLuigi’s Fine Italian Restaurant")

    elif vegetarian[0].upper() in "No" and vegan[0].upper() in "Yes" and gluten_free[0].upper() in "No":
        """If user enter "No", "Yes" and "No" this condition will true"""

        print("Here are your restaurant choices: \nJoes’ Gourmet Burgers")

    elif vegetarian[0].upper() in "No" and vegan[0].upper() in "No" and gluten_free[0].upper() in "Yes":
        """If user enter "No", "No" and "Yes" this condition will true"""

        print("Here are your restaurant choices: \nJoes’ Gourmet Burgers")

    else:
        """All above conditions are not true this condition will work"""

        print("Sorry, somethings wrong! \nPlease Enter Yes or No only!")
    # End If Condition

    print("")

    print("Created By Min Khant Soe (HakHak)")

    input("")

if __name__ == '__main__':
    main()
