# import sys
import sys
sys.path.append("..\crawler")
import db_load_data as db
import json 

def main():
    doc_education_level = open("education_level.json",'r')
    doc_housing_price = open("aurin/housing_price.json",'r')
    doc_education_metadata = open("aurin/education_metadata.json",'r')
    doc_education_origin_data = open("aurin/education_origin_data.json",'r')
    doc_house_origin_data = open("aurin/house_origin_data.json",'r')
    doc_house_price_metadata = open("aurin/house_price_metadata.json",'r')

    db.initialize_couchdb()
    db.store_to_aurin_cache_db(json.load(doc_education_level))
    db.store_to_cache_db(json.load(doc_housing_price))
    db.store_to_cache_db(json.load(doc_education_metadata))
    db.store_to_cache_db(json.load(doc_education_origin_data))
    db.store_to_cache_db(json.load(doc_house_origin_data))
    db.store_to_cache_db(json.load(doc_house_price_metadata))
    
main()


    
    
    
    
    

