import sys
import json
sys.path.append("..\..\crawler")
print(sys.path)
import db_load_data

doc_education_level = "education_level.json"
doc_housing_price = "housing_price.json"

doc_education_metadata = "education_metadata.json"
doc_education_origin_data = "education_origin_data.json"
doc_house_origin_data = "house_origin_data.json"
doc_house_price_metadata = "house_price_metadata.json"

db_load_data.initialize_couchdb()

json.load(doc_education_level)
json.load(doc_housing_price)
json.load(doc_education_metadata)
json.load(doc_education_origin_data)
json.load(doc_house_origin_data)
json.load(doc_house_price_metadata)