# Deptos

TDdescription:

# Requirements
* Python 3.6.5

# Installation
    python -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    
# scrapy
Example quotes

New spider in scrapping/spiders

    scrapy genspider quotes quotes.com

Run a spider

    # save file into data in json lines format
    scrapy crawl quotes


# Project tree

    |-- README.md
    |-- requirements.txt
    |-- research
       |-- jupyter
    |-- data -> json lines format
    |-- src
        |-- machine_learning
            |-- data_ingestion -> create dataset from scrapping parent classs
            |-- data_cleaning -> 
            |-- feature_engineering-> generate dataset
            |-- preprocessing -> reprocessing each feature
            |-- modeling -> 
            |-- Evaluate
            |-- Pipeline -> model in prd, use preprocessing and trained model
    |-- scrapping -> scrapy data
        |-- spiders -> download data from urls and save in data folder
    |-- tests
        |-- src
            |-- machine_learning
                |-- portalinmobiliario
            |-- scrapping

# import from new source
   
    sys.path.append(<folder_path>)
