import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Ouvrir l'URL de la page web
driver.get("https://weathershopper.pythonanywhere.com/")
time.sleep(2)

# Identifier l'éléments contenant le texte "i" et cliquer la dessus
element = driver.find_element_by_class_name("octicon octicon-info")
element.click()

# Récupérer le texte de l'élément
texte_complet = element.text

# Séparer le texte en mots et choisir le 2eme mots  (Les valeurs si ne changent pas pas la peine de faire le Split)
texte_complet = "Shop for moisturizers if the weather is below 19 degrees. Shop for suncreens if the weather is above 34 degrees."
x1 = texte_complet.split()
T1 = x1[8]


# Identifier les éléments contenant les valeurs à comparer
element1 = driver.find_element_by_xpath("//span[@id='temperature']")

# Extraire la valeur de élément (température qu'on veut comparer)
value1 = element1.text

# Comparer les valeurs
if value1 < 19:
    element = driver.find_element_by_class_name("btn-primary")
    element.click()

elif value1 > 34:
      element = driver.find_element_by_class_name("btn-primary")
    element.click()

#else:
#   print("No need to shop for specific products")


driver.close()
driver.quit()
print("Done")



