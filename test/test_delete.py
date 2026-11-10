import pytest
from api.listings_api import ListingsAPI

class TestDeleteListing:
    def test_successful_listing_deletion(self, user_token, created_listing_id):
        response = ListingsAPI.delete_listing(user_token, created_listing_id)
        assert response.status_code in [200, 204]
