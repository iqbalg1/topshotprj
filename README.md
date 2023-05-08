# topshotprj
Automation of NBA Topshot Site

Setup Instructions:
1. Have Python 3, Firefox and Pip installed
2. Run 'pip3 install -r requirements.txt'
3. Run 'pytest' from the project root folder 

Note: if your Firefox driver fails to run, install geckodriver (https://github.com/mozilla/geckodriver/releases) and add to your PATH

Automation Strategy:
* Implemented a standard page object model with python and selenium webdriver, creating a BasePage class with common webdriver actions that is inherited by each Page Object. Given each Topshot page has a distinct function with minimal overlap, the page object model applies well
* The GraphQL api functionality was implemented as an example to show how it could be used to confirm all the data being sent back by the server is rendered correctly in the UI. For a full framework, having a dedicated set of API tests to confirm all user actions & state changes are reflected in the backend (Sign Up, Purchasing Moments, Completing Challenges) would allow testing of basic functionality faster, with UI end to end tests focusing on UI specific actions
* Selenium Webdriver had issues with rendering all the React Javascript correctly, see the screenshots in the repo (DapperMissingMoments.png, DapperEmptyMarketPlaceConsoleOpen.png, DapperMarketPlaceConsoleClosed.png). These issues happened consistently in any browser opened via the Webdriver API and would have needed further investigation..
* After spending time understanding the product and automation needs, my recommended solution would be to implement a framework in Cypress. Given it is written in Javascript, it would not face the same issues with rendering the dynamic parts of the site and would encourage developer adoption of the test framework. Cypress also supports integration tests with a mocked out back end as well as GraphQL api tests so would be able to implement test cases covering most of the test pyramid. 
* Given time constraints, I only implemented the python framework and added a few test cases from the NBA Topshot CSV plan. The Marketplace tests currently fail due to the above mentioned issues with missing moments and site elements
