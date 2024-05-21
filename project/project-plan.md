# Project Plan

## Title
Library visit in Chicago

## Main Question

The main goal of this data engineering project is to integrate and analyze **visitor and weather data for Chicago to establish the city's suitability for library visitors**. By examining trends in visitor counts from the Chicago library dataset from 2018 and the city's weather patterns, the project aims to determine if Chicago's infrastructure and climate support a conducive and enjoyable environment for library visitors.

## Description

This data science initiative will examine library visits in Chicago using 2018 data. The goal is to assess Chicago's effectiveness as a major destination for library visitors. By analyzing visitor trends and correlating them with weather and climate conditions, the project aims to uncover insights into the city's visitor-friendliness. A thorough investigation of Chicago's library infrastructure and environmental factors will reveal if the city supports a strong and comfortable environment for library patrons.

**Library Enthusiasts:** For individuals with a passion for exploring libraries, the project's findings will be invaluable. The insights derived from the analysis of Chicago's library visitors and weather conditions will enable visitors to better plan to visit the library, potentially boosting the city's appeal as a destination for all people.

**Urban Planners in Chicago:** The insights garnered from this project can serve as a strategic tool for urban planners, helping to enhance the quality and safety of the city's library infrastructure. By pinpointing specific areas where facilities are lacking, city planners can strategically direct investments to upgrade and expand infrastructure, thereby creating a more accessible and enjoyable environment for library visitors in Chicago.

## Datasources


### Datasource1: Library Visitor Data in Chicago
* Metadata URL: [https://catalog.data.gov/dataset/libraries-2018-visitors-by-location](https://catalog.data.gov/dataset/libraries-2018-visitors-by-location)
* Sample Data URL: [https://data.cityofchicago.org/api/views/i7zz-iiza/rows.csv](https://data.cityofchicago.org/api/views/i7zz-iiza/rows.csv)
* Data Type: CSV

This data source contains Chicago's library visitor data generated in 2018.

### Datasource2: Weather and Climate Data of London
* Metadata URL: [https://www.visualcrossing.com/weather/weather-data-services](https://www.visualcrossing.com/weather/weather-data-services)
* Sample Data URL: [https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=62G5GK5U8LGWQHURAMBAZE6CF&taskId=f4c31e40d2e716f3ef71821413d86d28&zip=false](https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=62G5GK5U8LGWQHURAMBAZE6CF&taskId=f4c31e40d2e716f3ef71821413d86d28&zip=false)
* Data Type: CSV

This data source will provide weather and climate data in Chicago, including datetime, tempmax, feellinke, humidity, max_temp, mean_temp, snow, couldcover, visibility, snow_depth, sunrise, sunset, etc.

## Work Packages


1. Extract Data from Multiple Sources [#1][i1]
2. Implement Data Transformation Step in ETL Pipeline [#2][i2]
3. Implement Data Loading Step in ETL Data Pipeline [#3][i3]
4. Automated Tests for the Project [#4][i4]
5. Continuous Integration Pipeline for the Project [#5][i5]
6. Final Report and Presentation Submission [#6][i6]

[i1]: https://github.com/SK-Subroto/fau-made-template-ss24/issues/1
[i2]: https://github.com/SK-Subroto/fau-made-template-ss24/issues/2
[i3]: https://github.com/SK-Subroto/fau-made-template-ss24/issues/3
[i4]: https://github.com/SK-Subroto/fau-made-template-ss24/issues/4
[i5]: https://github.com/SK-Subroto/fau-made-template-ss24/issues/5
[i6]: https://github.com/SK-Subroto/fau-made-template-ss24/issues/6
