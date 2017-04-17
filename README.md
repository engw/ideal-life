# ideal-life

## Requirements
```
Docker 1.13.X
```

## Installation
```bash
# pull container
% docker pull engw/ideal-life
# or build locally
# % docker build . --tag engw/ideal-life
```

## Usage
```bash
# debug a spider
% scrapy runspider ideallife/spiders/homes.py

# run integration with output
% scrapy crawl homes -o output.csv
```

## Deployment
```bash
# Login to scrapinghub.com
% shub login

# Create project on your browser (and copy PROJECT_ID)
% open https://app.scrapinghub.com/

# Deploy to scrapinghub.com including dependencies
% shub deploy
```
