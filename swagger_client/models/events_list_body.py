# coding: utf-8

"""
    Outline API

    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an  [openapi specification](https://github.com/outline/openapi) if that’s your  jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a method on `https://app.getoutline.com/api/method`. Both `GET` and `POST`  methods are supported but it’s recommended that you make all call using POST. Only HTTPS is supported and all response payloads are JSON.  When making `POST` requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  ``` curl https://app.getoutline.com/api/documents.info -X POST -H 'authorization: Bearer MY_API_KEY' -H 'content-type: application/json' -H 'accept: application/json' -d '{\"id\": \"outline-api-NTpezNwhUP\"}' ```  Or, with JavaScript:  ```javascript const response = await fetch(\"https://app.getoutline.com/api/documents.info\", {   method: \"POST\",   headers: {     Accept: \"application/json\",     \"Content-Type\": \"application/json\",     Authorization: 'Bearer MY_API_KEY'   } })  const body = await response.json(); const document = body.data; ```  # Authentication  To access API endpoints, you must provide a valid API key. You can create new API keys in your [account settings](https://app.getoutline.com/settings). Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you can supply the API key as a header (`Authorization: Bearer YOUR_API_KEY`) or as part of the payload using `token`  parameter. Header based authentication is highly recommended so that your keys don’t accidentally leak into logs.  Some API endpoints allow unauthenticated requests for public resources and they can be called without an API key.  # Errors  All successful API requests will be returned with a 200 or 201 status code and `ok: true` in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  ``` {   \"ok\": false,   \"error: \"Not Found\" } ```  # Pagination  Most top-level API resources have support for \"list\" API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both `limit` and `offset`.  Responses will echo these parameters in the root `pagination` key, and also include a `nextPath` key which can be used as a handy shortcut to fetch the next page of results. For example:  ``` {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \"/api/documents.list?limit=25&offset=25\"   } } ```  # Policies  Many API resources have associated \"policies\", these objects describe the current API keys authorized actions related to an individual resource. It should be noted that the policy \"id\" is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these are used in the main Outline UI to adjust which elements are visible.   # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: hello@getoutline.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.pagination import Pagination  # noqa: F401,E501

class EventsListBody(Pagination):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sort': 'str',
        'direction': 'str',
        'name': 'str',
        'actor_id': 'str',
        'document_id': 'str',
        'collection_id': 'str',
        'audit_log': 'bool'
    }
    if hasattr(Pagination, "swagger_types"):
        swagger_types.update(Pagination.swagger_types)

    attribute_map = {
        'sort': 'sort',
        'direction': 'direction',
        'name': 'name',
        'actor_id': 'actorId',
        'document_id': 'documentId',
        'collection_id': 'collectionId',
        'audit_log': 'auditLog'
    }
    if hasattr(Pagination, "attribute_map"):
        attribute_map.update(Pagination.attribute_map)

    def __init__(self, sort=None, direction=None, name=None, actor_id=None, document_id=None, collection_id=None, audit_log=None, *args, **kwargs):  # noqa: E501
        """EventsListBody - a model defined in Swagger"""  # noqa: E501
        self._sort = None
        self._direction = None
        self._name = None
        self._actor_id = None
        self._document_id = None
        self._collection_id = None
        self._audit_log = None
        self.discriminator = None
        if sort is not None:
            self.sort = sort
        if direction is not None:
            self.direction = direction
        if name is not None:
            self.name = name
        if actor_id is not None:
            self.actor_id = actor_id
        if document_id is not None:
            self.document_id = document_id
        if collection_id is not None:
            self.collection_id = collection_id
        if audit_log is not None:
            self.audit_log = audit_log
        Pagination.__init__(self, *args, **kwargs)

    @property
    def sort(self):
        """Gets the sort of this EventsListBody.  # noqa: E501


        :return: The sort of this EventsListBody.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this EventsListBody.


        :param sort: The sort of this EventsListBody.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def direction(self):
        """Gets the direction of this EventsListBody.  # noqa: E501


        :return: The direction of this EventsListBody.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this EventsListBody.


        :param direction: The direction of this EventsListBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASC", "DESC"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def name(self):
        """Gets the name of this EventsListBody.  # noqa: E501

        Filter to a specific event, e.g. \"collections.create\". Event names are in the format \"objects.verb\"  # noqa: E501

        :return: The name of this EventsListBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventsListBody.

        Filter to a specific event, e.g. \"collections.create\". Event names are in the format \"objects.verb\"  # noqa: E501

        :param name: The name of this EventsListBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def actor_id(self):
        """Gets the actor_id of this EventsListBody.  # noqa: E501

        Filter to events performed by the selected user  # noqa: E501

        :return: The actor_id of this EventsListBody.  # noqa: E501
        :rtype: str
        """
        return self._actor_id

    @actor_id.setter
    def actor_id(self, actor_id):
        """Sets the actor_id of this EventsListBody.

        Filter to events performed by the selected user  # noqa: E501

        :param actor_id: The actor_id of this EventsListBody.  # noqa: E501
        :type: str
        """

        self._actor_id = actor_id

    @property
    def document_id(self):
        """Gets the document_id of this EventsListBody.  # noqa: E501

        Filter to events performed in the selected document  # noqa: E501

        :return: The document_id of this EventsListBody.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this EventsListBody.

        Filter to events performed in the selected document  # noqa: E501

        :param document_id: The document_id of this EventsListBody.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def collection_id(self):
        """Gets the collection_id of this EventsListBody.  # noqa: E501

        Filter to events performed in the selected collection  # noqa: E501

        :return: The collection_id of this EventsListBody.  # noqa: E501
        :rtype: str
        """
        return self._collection_id

    @collection_id.setter
    def collection_id(self, collection_id):
        """Sets the collection_id of this EventsListBody.

        Filter to events performed in the selected collection  # noqa: E501

        :param collection_id: The collection_id of this EventsListBody.  # noqa: E501
        :type: str
        """

        self._collection_id = collection_id

    @property
    def audit_log(self):
        """Gets the audit_log of this EventsListBody.  # noqa: E501

        Whether to return detailed events suitable for an audit log. Without this flag less detailed event types will be returned.  # noqa: E501

        :return: The audit_log of this EventsListBody.  # noqa: E501
        :rtype: bool
        """
        return self._audit_log

    @audit_log.setter
    def audit_log(self, audit_log):
        """Sets the audit_log of this EventsListBody.

        Whether to return detailed events suitable for an audit log. Without this flag less detailed event types will be returned.  # noqa: E501

        :param audit_log: The audit_log of this EventsListBody.  # noqa: E501
        :type: bool
        """

        self._audit_log = audit_log

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EventsListBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventsListBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
