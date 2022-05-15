# import aurin.store_to_db 
# import nlp.store_data 
import nltk

from aurin import store_to_db
from nlp import store_data
#store_to_db.aurin_main()
nltk.download('vader_lexicon')
store_data.nlp_main()
