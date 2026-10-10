## QA Test: Alza Cart ##

# TSC001 - Add product to cart (Positive Test)

**Pre-conditions:**
* The Alza homepage is opened.

**Test Steps:**
* Type "iPhone 15" into the input search field.
* Click on the button "Search" or Press Enter.
* Click on the button "Add to cart".

**Expected Result:**
* The number on the shopping cart icon in the top right corner changes to 1.

# TSC002 - Change product quantity in cart (Positive Test)

**Pre-conditions:**
* The shopping cart is opened.
* There is one product in the cart.

**Test steps:**
* Click on the button "+" (Plus).

**Expected Result:**
* The quantity of the product changes to 2.
* The total price is recalculated and shows the final amount.

# TSC003 - Remove product from cart (Positive Test)

**Pre-conditions:**
* The shopping cart is opened.
* There are two products in the cart.

**Test steps:**
* Click twice on the button "-" (minus).

**Expected Result:**
* The shopping cart is empty and shows the message: "Váš košík je prázdný".

# TSC004 - Apply invalid discount code (Negative Test)

**Pre-conditions:**
* The shopping cart is opened.
* There is one product in the cart.

**Test steps:**
* Click on "Využít slevový / dárkový poukaz".
* Type "NEPLATNY-KOD-2026" into the input field.
* Click on the button "Apply".

**Expected Result:**
* The shopping cart shows an error message: "Poukaz nešlo použít Zadaný slevový / dárkový poukaz není platný".