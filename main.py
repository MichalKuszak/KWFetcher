import os
from dotenv import load_dotenv
from KWFetcher import KWFetcher, MainKW

load_dotenv()
kw_no = os.environ.get("TEMP_KW_NO")
fetcher = MainKW(kw_no)

print(fetcher.residential_premises)

# data_list = []
# counter = 0
# with open("dane.txt", "w", encoding="utf-8") as file:
#     for item in apt_kw_list:
#
#         # Wyswietl l.p. i nr KW
#         counter += 1
#         print(f"{counter}.")
#         print(f"{item[0]}/{item[1]}/{item[2]}")
#
#         # Zapisz l.p. i nr KW do pliku
#         file.write(f"{counter}\n")
#         file.write(f"{item[0]}/{item[1]}/{item[2]}\n")
#
#         #Pobierz adres
#         load_kw(item)
#         time.sleep(2.6)
#         street = driver.find_element(By.XPATH, "/html/body/div/table[3]/tbody/tr[5]/td[4]").text
#         flat_no = driver.find_element(By.XPATH, "/html/body/div/table[3]/tbody/tr[5]/td[5]").text
#         apt_no = driver.find_element(By.XPATH, "/html/body/div/table[3]/tbody/tr[5]/td[6]").text
#         full_address = (f"{street.title()} {flat_no} lok. {apt_no}")
#         print(full_address)
#         file.write(full_address + "\n")
#
#
#         driver.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[3]/form/input[7]").click()
#         time.sleep(3)
#         owners = driver.find_elements(By.XPATH, '//td[2][@class = "csDane"]')
#         owners_data_list = [item.text.title().strip().split(",") for item in owners[1::2]]
#
#         # Pobierz i zapisz nazwiska i PESELe wlascicieli
#         for _ in owners_data_list:
#             try:
#                 print(f"{_[0]}\nPESEL:{_[3]}")
#                 file.write(f"{_[0]}\nPESEL:{_[3]}")
#             except IndexError:
#                 print(f"{_[0]}\nPESEL:{_[1]}")
#                 file.write(f"{_[0]}\nPESEL {_[1]}")
#
#             # Pobierz i zapisz tylko nazwiska wlascicieli
#             # print(f"{_[0]}")
#             # file.write(f"{_[0]}")
#
#         print("-" * 20)
#         file.write("\n" + "-" * 20 + "\n")
#         # property_dict = {"Adres": full_address,
#         #                  "Wlasciciele": owners_data_list,
#         #                  }
#         # data_list.append(property_dict)
#     # print(data_list)
#
#
