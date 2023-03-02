# coding: utf-8

"""
    Outline API

    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an  [openapi specification](https://github.com/outline/openapi) if that’s your  jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a method on `https://app.getoutline.com/api/method`. Both `GET` and `POST`  methods are supported but it’s recommended that you make all call using POST. Only HTTPS is supported and all response payloads are JSON.  When making `POST` requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  ``` curl https://app.getoutline.com/api/documents.info -X POST -H 'authorization: Bearer MY_API_KEY' -H 'content-type: application/json' -H 'accept: application/json' -d '{\"id\": \"outline-api-NTpezNwhUP\"}' ```  Or, with JavaScript:  ```javascript const response = await fetch(\"https://app.getoutline.com/api/documents.info\", {   method: \"POST\",   headers: {     Accept: \"application/json\",     \"Content-Type\": \"application/json\",     Authorization: 'Bearer MY_API_KEY'   } })  const body = await response.json(); const document = body.data; ```  # Authentication  To access API endpoints, you must provide a valid API key. You can create new API keys in your [account settings](https://app.getoutline.com/settings). Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you can supply the API key as a header (`Authorization: Bearer YOUR_API_KEY`) or as part of the payload using `token`  parameter. Header based authentication is highly recommended so that your keys don’t accidentally leak into logs.  Some API endpoints allow unauthenticated requests for public resources and they can be called without an API key.  # Errors  All successful API requests will be returned with a 200 or 201 status code and `ok: true` in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  ``` {   \"ok\": false,   \"error: \"Not Found\" } ```  # Pagination  Most top-level API resources have support for \"list\" API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both `limit` and `offset`.  Responses will echo these parameters in the root `pagination` key, and also include a `nextPath` key which can be used as a handy shortcut to fetch the next page of results. For example:  ``` {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \"/api/documents.list?limit=25&offset=25\"   } } ```  # Policies  Many API resources have associated \"policies\", these objects describe the current API keys authorized actions related to an individual resource. It should be noted that the policy \"id\" is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these are used in the main Outline UI to adjust which elements are visible.   # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: hello@getoutline.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.documents_api import DocumentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    def setUp(self):
        self.api = DocumentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_documents_archive_post(self):
        """Test case for documents_archive_post

        Archive a document  # noqa: E501
        """
        pass

    def test_documents_create_post(self):
        """Test case for documents_create_post

        Create a document  # noqa: E501
        """
        pass

    def test_documents_delete_post(self):
        """Test case for documents_delete_post

        Delete a document  # noqa: E501
        """
        pass

    def test_documents_drafts_post(self):
        """Test case for documents_drafts_post

        List all draft documents  # noqa: E501
        """
        pass

    def test_documents_export_post(self):
        """Test case for documents_export_post

        Export a document as markdown  # noqa: E501
        """
        pass

    def test_documents_import_post(self):
        """Test case for documents_import_post

        Import a file as a document  # noqa: E501
        """
        pass

    def test_documents_info_post(self):
        """Test case for documents_info_post

        Retrieve a document  # noqa: E501
        """
        pass

    def test_documents_list_post(self):
        """Test case for documents_list_post

        List all documents  # noqa: E501
        """
        pass

    def test_documents_move_post(self):
        """Test case for documents_move_post

        Move a document  # noqa: E501
        """
        pass

    def test_documents_restore_post(self):
        """Test case for documents_restore_post

        Restore a document  # noqa: E501
        """
        pass

    def test_documents_search_post(self):
        """Test case for documents_search_post

        Search all documents  # noqa: E501
        """
        pass

    def test_documents_star_post(self):
        """Test case for documents_star_post

        Star a document  # noqa: E501
        """
        pass

    def test_documents_templatize_post(self):
        """Test case for documents_templatize_post

        Create a template from a document  # noqa: E501
        """
        pass

    def test_documents_unpublish_post(self):
        """Test case for documents_unpublish_post

        Unpublish a document  # noqa: E501
        """
        pass

    def test_documents_unstar_post(self):
        """Test case for documents_unstar_post

        Unstar a document  # noqa: E501
        """
        pass

    def test_documents_update_post(self):
        """Test case for documents_update_post

        Update a document  # noqa: E501
        """
        pass

    def test_documents_viewed_post(self):
        """Test case for documents_viewed_post

        List all recently viewed documents  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
