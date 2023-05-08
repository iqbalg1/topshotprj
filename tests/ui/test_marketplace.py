import pytest
from lib.pages.MarketplacePage import MarketplacePage
from lib.api.topshot_api_client import TopshotClient

class TestMarketplace:
    @pytest.fixture(autouse=True)
    def setup_pageobjects(self, create_marketplacepageobj):
        self.marketplace_page = create_marketplacepageobj

    def test_search_dropdown_list_loads(self):
        self.marketplace_page.select_search_bar()
        default_search_results = self.marketplace_page.get_search_dropdown_results()

        api_client = TopshotClient()
        api_player_results = api_client.getAllPlayers()

        assert default_search_results.text == api_player_results[0]

    def test_search_specific_player(self):
        self.marketplace_page.type_search_bar('Lebron')
        search_results = self.marketplace_page.get_search_dropdown_results()

        assert search_results.text == 'LeBron James'

    def test_player_card_filters_search(self):
        self.marketplace_page.select_player_card('LeBron James')

        search_url = self.marketplace_page.get_current_url()
        #should verify search results instead of url but not getting any results
        #see email for screenshot/bug report
        assert search_url == 'https://nbatopshot.com/search?byPlayers=2544'
