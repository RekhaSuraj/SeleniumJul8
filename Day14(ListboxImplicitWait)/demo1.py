from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.get('file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample15.html')
time.sleep(3)

listbox = driver.find_element(By.ID, 'A1')
sel = Select(listbox)
time.sleep(2)
# sel.select_by_index(2) #Agra in index 2
# time.sleep(2)
# sel.select_by_value('b') # Bangalore in value 'b'
# time.sleep(2)
# sel.select_by_visible_text('Delhi') #Delhi visible text

# time.sleep(5)

# print(sel.options)

# Looping through all the options as a list to fetch the text - items in the listbox
for s in sel.options:
    print(s.text)

# Count number of options in the listbox
print(len(sel.options))

