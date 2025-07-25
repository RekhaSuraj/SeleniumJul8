from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.get('file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample16.html')
time.sleep(3)

listbox1 = driver.find_element(By.ID,'A1')
sel = Select(listbox1)

sel.select_by_visible_text('Snacks')
time.sleep(2)
sel.select_by_value('a')
time.sleep(2)
sel.select_by_value('b')
print(sel.first_selected_option.text)
# Snacks

# is_multiple() - Returns True if the listbox allows multiple selections, else False
print(sel.is_multiple)
# True

# sel.deselect_by_value('c')
# We can also deselect all selected values in a listbox, but select_all() is not possible
sel.deselect_all()
time.sleep(3)

listbox2 = driver.find_element(By.ID, 'A2')
sel2 = Select(listbox2)
print(sel2.all_selected_options)

# Print all the items which are selected in the multiple selection listbox
for s in sel2.all_selected_options:
    print(s.text)

# Tea
# Milk
# Juice

sel.deselect_all()
