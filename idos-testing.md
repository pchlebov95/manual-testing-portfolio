## QA Test: IDOS.cz ##

# TSC001 - Valid Connection Search (Positive Test)

**Pre-conditions:**
* The IDOS homepage is opened.

**Test Steps:**
* Type "Teplice v Čechách" into the "FROM" input field.
* Type "Praha hl.n." into the "TO" input field.
* Click on the button "Search".

**Expected Result:**
* Search result page shows list of the connections.


# TSC002 - Empty input (Negative Test)

**Pre-conditions:**
* The IDOS homepage is opened.
* The IDOS page remembers the last search data.

**Test Steps:**
* Click on the button "Search"

**Expected Result:**
* Search results page displays the list of the last connections.


# TSC003 - Search with date in the past (Negative Test)

**Pre-conditions:**
* The IDOS homepage is opened.
* The last search data is deleted (Click on the hamburger menu and select "Clear saved data").

**Test Steps:**
* Type "Teplice v Čechách" into the "FROM" input field.
* Type "Praha hl.n." into the "TO" input field.
* Type "7.10.2020" into the "DATE" input field.
* Press Enter.

**Expected Result:**
* System automatically changes the date to "14.12.2025".


# TSC004 - Swap "FROM" <-> "TO" destinations. (Positive Test)

**Pre-conditions:**
* The IDOS homepage is opened.
* The last search data is deleted (Click on the hamburger menu and select "Clear saved data").

**Test Steps:**
* Type "Teplice v Čechách" into the "FROM" input field.
* Type "Praha hl.n." into the "TO" input field.
* Click on "Swap button".

**Expected Result:**
* The values in the "FROM" and "TO" fields are swapped.


# TSC005 - Invalid input (Negative Test)

**Pre-conditions:**
* The IDOS homepage is opened.
* The last search data is deleted (Click on the hamburger menu and select "Clear saved data").

**Test steps:**
* Type "R2-D2" into the "FROM" input field.
* Type "C-3PO" into the "TO" input field.
* Press Enter.

**Expected Result:**
* The IDOS homepage displays an error message: "Takové místo neznáme".
