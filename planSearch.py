# implements search functions that are useful for the app
# uses functions from yelpSearch.py
# TODO: create useful functions for PlanIt

# imports all necessary yelpSearch functions
import yelpSearch


# Searches for all specified parameters and returns results in a list
# Uses list compression
def customSearch(paramList):
	searchList = [yelpSearch.getResults(USER_LOCATION_LONGITUDE, USER_LOCATION_LATITUDE, paramList[i]) \
				for i in range(len(paramList))]
	return searchList


# TODO: implement test cases
if __name__ == "__main__":
	print "Test cases have not been implemented yet"
	
