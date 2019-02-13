from django.shortcuts import render
from django.views.generic import View
import json
import os
from ecom_products.responses import (init_response, send_200, send_400)
from filters.constants import (DATERANGE, COLOUR, SIZE,
                               IS_VERIFIED_PURCHASE, RATING, SENTIMENT, STR_INVALID_INPUT,
                               STR_PRODUCTS_FETCHED)

module_dir = os.path.dirname(__file__)
file_path=os.path.join(module_dir,'sentimentAnalysis.json')


# Create your views here.


class ApplyFilterView(View):
    
    
    def __init__(self):
        self.response = init_response()  
    
    def filterJSON(self,json_input, date_range,color,size,is_verified_purchase,rating,sentiment):
        results = []                 

        reviews_json=json_input

        def filterVerified(reviews,is_verified_purchase):        
            verifiedResults = []
            for r in reviews:
                if(r['VerifiedPurchase']==is_verified_purchase):
                    verifiedResults.append(r)         
            return verifiedResults

        def filterColour(reviews, color):
            colorResults = []
            for r in reviews:
                if(r['Colour']==COLOUR):
                    colorResults.append(r)
            return colorResults

        def filterRating(reviews, rating):
            rateResults = []
            for r in reviews:
                if(r['Rating']==RATING):
                    rateResults.append(r)
            return rateResults

        def filterSentiment(reviews, sentiment):
            sentiResults = []
            for r in reviews:
                if(r['Sentiment']==SENTIMENT):
                    sentiResults.append(r)
            return sentiResults

        def checkResults(results):
            if(len(results)>0):
                reviews_json= results


        if(is_verified_purchase is not None):
                IS_VERIFIED_PURCHASE= is_verified_purchase
                results = filterVerified(reviews_json, IS_VERIFIED_PURCHASE)       
                checkResults(results)

        if(color is not None):
            COLOUR= color
            results = filterColour(reviews_json, COLOUR)       
            checkResults(results)

        if(size is not None):
            SIZE= size
            results = filterSize(reviews_json, SIZE)       
            checkResults(results)

        if(rating is not None):
            RATING= rating
            results = filterRating(reviews_json, RATING)
            checkResults(results)

        if(sentiment is not None):
                SENTIMENT= sentiment
                results = filterSentiment(reviews_json, SENTIMENT)
                checkResults(results)
                
        if([date_range,color,size,is_verified_purchase,rating,sentiment] is None):
            results = reviews_json

        if(date_range=='asc'):
            sorted(results, key=lambda k: k['DateOfReview']) 
        else:
            sorted(results, key=lambda k: k['DateOfReview'], reverse=True)

        return results

    def _applyfilters(self, req_data, json_input):
        output = None
        
        date_range = req_data.get(DATERANGE)
        color = req_data.get(COLOUR)
        size = req_data.get(SIZE)
        is_verified_purchase = req_data.get(IS_VERIFIED_PURCHASE)
        rating = float(req_data.get(RATING, 0))
        sentiment = float(req_data.get(SENTIMENT, 0))
        output= self.filterJSON(json_input,date_range,color,size,is_verified_purchase,rating,sentiment)
        
        return output
        
        
    def get(self, request):
        req_data = request.GET
        json_input = json.load(open(file_path))
        try:
            output = self._applyfilters(req_data, json_input)
            self.response['res_str'] = STR_PRODUCTS_FETCHED
            self.response['res_data'] = output
            return send_200(self.response)
        except ValueError as e:
            self.response['res_str'] = STR_INVALID_INPUT
        except Exception as e:
            self.response['res_str'] = str(e)
        return send_400(self.response)
