## QA Test: Netflix login form ##

# TSC001 - Login with invalid email (Negative Test)

**Pre-conditions:**
* The netflix homepage is opened.

**Test Steps:**
* Click on the button "Přihlásit se".
* Type "patrik.test.cz" into the email input field.
* Click on the button "Pokračovat".

**Expected Result:**
* The email input field displays an error message: "Zadejte platnou e-mailovou adresu."

# TSC002 - Login with non-registered email (Negative Test)

**Pre-conditions:**
* The netflix homepage is opened.

**Test Steps:**
* Click on the button "Přihlásit se".
* Type "test@email.cz" into the email input field.
* Click on the button "Pokračovat".

**Expected Result:**
* An error message is displayed at the top of the page: "Něco se pokazilo. Zkontrolujte e-mailovou adresu a zkuste to znova."

# TSC003 - Login with empty fields (Negative Test)

**Pre-conditions:**
* The netflix homepage is opened.

**Test Steps:**
* Click on the button "Přihlásit se".
* Leave the email input field empty.
* Click on the button "Pokračovat".

**Expected Result:**
* The email input field shows an error message: "Zadejte platný e-mail nebo mobilní číslo."

# TSC004 - Login with invalid verification code (Negative Test)

**Pre-conditions:**
* The netflix homepage is opened.

**Test Steps:**
* Click on the button "Přihlásit se".
* Type "YOUR_REGISTERED_EMAIL" into the email input field.
* Click on the button "Pokračovat".
* Type "1", "2", "3", "4" into the verification code input fields.

**Expected Result:**
* The verification code input fields show an error message: "Kód je nesprávný. Zkuste to znova."
