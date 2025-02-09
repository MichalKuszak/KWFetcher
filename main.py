import os
from dotenv import load_dotenv
from KWFetcher import KWFetcher, MainKW, ResidentialKW
from pprint import pprint

load_dotenv()
kw_no = os.environ.get("TEMP_KW_NO")
# fetcher = MainKW(kw_no)
#
# print(fetcher.residential_units)

fetcher = ResidentialKW(kw_no)
pprint(fetcher.owner_data)
