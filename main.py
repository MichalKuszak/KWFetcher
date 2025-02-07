import os
from dotenv import load_dotenv
from KWFetcher import KWFetcher, MainKW

load_dotenv()
kw_no = os.environ.get("TEMP_KW_NO")
fetcher = MainKW(kw_no)

print(fetcher.residential_premises)

