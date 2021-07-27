# Pharmaceutical Sales prediction across multiple stores

## Business Need
You work at Rossmann Pharmaceuticals as a Machine Learning Engineer. The finance team wants to forecast sales in all their stores across several cities six weeks ahead of time. Managers in individual stores rely on their years of experience as well as their personal judgement to forecast sales. 

The data team identified factors such as promotions, competition, school and state holidays, seasonality, and locality as necessary for predicting the sales across the various stores.

Your job is to build and serve an end-to-end product that delivers this prediction to analysts in the finance team. 

## Data and Features
### Data fields
Most of the fields are self-explanatory. The following are descriptions for those
that aren't.
* __Id__ - an Id that represents a (Store, Date) duple within the test set
* __Store__ - a unique Id for each store
* __Sales__ - the turnover for any given day (this is what you are predicting)
* __Customers__ - the number of customers on a given day
* __Open__ - an indicator for whether the store was open: 0 = closed, 1 = open
* __StateHoliday__ - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on
public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
* __SchoolHoliday__ - indicates if the (Store, Date) was affected by the closure of public schools
* __StoreType__ - differentiates between 4 different store models: a, b, c, d
* __Assortment__ - describes an assortment level: a = basic, b = extra, c = extended.
* __CompetitionDistance__ - distance in meters to the nearest competitor store
* __CompetitionOpenSince[Month/Year]__ - gives the approximate year and month of the time the nearest competitor was opened
* __Promo__ - indicates whether a store is running a promo on that day
* __Promo2__ - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
* __Promo2Since[Year/Week]__ - describes the year and calendar week when the store started participating in Promo2
* __PromoInterval__ - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store

## Tasks
* __Task 1 - Exploration of customer purchasing behavior__
  * __1.2 - Logging__
* __Task 2 - Prediction of store sales__ 
  * __2.1 Preprocessing__
  * __2.2 Building models with sklearn pipelines__
  * __2.3 Choose a loss function__
  * __2.4 Post Prediction analysis__
  * __2.5 Serialize models__
  * __2.6 Building model with deep learning__ 
  * __2.7 Using MLFlow to serve the prediction__
* __Task 3 - Serving predictions on a web interface__
 
 
 ## Information about the files
 * [data](https://github.com/Luel-Hagos/Pharmaceutical-Sales-prediction-across-multiple-stores/tree/main/data) contains the data files.
 * [notebooks](https://github.com/Luel-Hagos/Pharmaceutical-Sales-prediction-across-multiple-stores/tree/main/notebooks) contains the notebook files.
