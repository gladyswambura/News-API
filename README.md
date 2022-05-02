# News-API

## Built By [Gladys Wambura](https://github.com/gladyswambura)

## Description
News-API is a web application that displays a list of various news sources like BBC and CNN. On choosing a news source on the navigation bar, it will preview the top news sources of the day. Clicking a news article will redirect the user to read the news article. It achieves this by using the [News API](https://newsapi.org/).

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See various news sources 
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of sources |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click on read atricle button** | Redirected to the entire article |

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
