from db_load_data import *
import datetime
import schedule

def map_reduce(db): 
    map_housing_sentiment = """
                function(doc) {
                if(doc.doc){
                    if (doc.house>0) 
                        if (doc.doc.place.name=="Melbourne")
                            emit(["housing_sentiment",doc.year+'-'+doc.month+'-'+doc.day,doc.doc.place.bounding_box.coordinates[0][4],doc.melbourne_area],doc.sentiment);
                }
                if(!doc.doc){
                    if (doc.house >0) 
                         if (doc.place.name=="Melbourne")
                            emit(["housing_sentiment",doc.year+'-'+doc.month+'-'+doc.day,doc.place.bounding_box.coordinates[0][4],doc.melbourne_area],doc.sentiment);
                }
                }
                """
    map_eduction_sentiment = """
                function(doc) {
                if(doc.doc){
                    if (doc.education >0) 
                        if (doc.doc.place.name=="Melbourne")
                            emit(["eduction_sentiment",doc.year+'-'+doc.month+'-'+doc.day,doc.doc.place.bounding_box.coordinates[0][4],doc.melbourne_area],doc.sentiment);
                }
                if(!doc.doc){
                    if (doc.education >0) 
                         if (doc.place.name=="Melbourne")
                            emit(["eduction_sentiment",doc.year+'-'+doc.month+'-'+doc.day,doc.place.bounding_box.coordinates[0][4],doc.melbourne_area],doc.sentiment);
                }
                }
                """
    map_eduction_polarity = """
                function(doc) {
                if(doc.doc){
                    if (doc.education>0) 
                        if (doc.doc.place.name=="Melbourne")
                            emit(["eduction_polarity",doc.year+'-'+doc.month+'-'+doc.day,doc.doc.place.bounding_box.coordinates[0][4],doc.melbourne_area],doc.polarity);
                }
                if(!doc.doc){
                    if (doc.education>0) 
                         if (doc.place.name=="Melbourne")
                            emit(["eduction_polarity",doc.year+'-'+doc.month+'-'+doc.day,doc.place.bounding_box.coordinates[0][4],doc.melbourne_area],doc.polarity);
                }
                }
                """
    map_housing_polarity = """
                function(doc) {
                if(doc.doc){
                    if (doc.house >0) 
                        if (doc.doc.place.name=="Melbourne")
                            emit(["housing_polarity",doc.year+'-'+doc.month+'-'+doc.day,doc.doc.place.bounding_box.coordinates[0][4],doc.melbourne_area],doc.polarity);
                }
                if(!doc.doc){
                    if (doc.house >0) 
                         if (doc.place.name=="Melbourne")
                            emit(["housing_polarity",doc.year+'-'+doc.month+'-'+doc.day,doc.place.bounding_box.coordinates[0][4],doc.melbourne_area],doc.polarity);
                }
                }
                """  

        
    design = { 
                "housing_sentiment_sum": {
                    "map": map_housing_sentiment,
                    "reduce": "_sum"
                },
                "housing_sentiment_count": {
                    "map": map_housing_sentiment,
                    "reduce": "_count"
                },
                "eduction_sentiment_sum":{
                    "map":map_eduction_sentiment,
                    "reduce": "_sum"
                },
                "eduction_sentiment_count":{
                    "map":map_eduction_sentiment,
                    "reduce": "_count"
                },  
                'eduction_polarity_sum':{
                    "map":map_eduction_polarity,
                    "reduce":"_sum"
                },
                'eduction_polarity_count':{
                    "map":map_eduction_polarity,
                    "reduce":"_count"
                },
                'housing_polarity_sum':{
                    "map":map_housing_polarity,
                    "reduce":"_sum"
                },
                'housing_polarity_count':{
                    "map":map_housing_polarity,
                    "reduce":"_count"
                }
            } 
    
    name = datetime.datetime.now().now().strftime('%m%d%H')
    db["_design/"+name] = dict(language='javascript', views=design)
    key_list =[]
    for key in db["_design/"+name]["views"]:
            key_list.append(key)
    result = {"_id": "_design/"+name,"data":{}}
    for key_value in key_list:
        row_name = name+'/'+key_value
        result['data'][key_value] = {} 
        for row in db.view(row_name,group=True):
            result['data'][key_value].update({row.key[3]:[]})
    for key_value in key_list:
        row_name = name+'/'+key_value
        for row in db.view(row_name,group=True):
            result['data'][key_value][row.key[3]].append({"date":row.key[1],"coord":row.key[2],'area':row.key[3],'value':row.value})
    store_to_cache_db(result)
    




def start_run():
    processed = get_spec_db('processed_tweets')
    map_reduce(processed)

if __name__ == "__main__":  
    initialize_couchdb()
    start_run()
    # schedule.every().day.at("04:00").do(start_run)
    # schedule.every().day.at("16:00").do(start_run)
    # while(True):
    #     schedule.run_pending()

