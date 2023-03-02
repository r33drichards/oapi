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

class FileOperation(object):
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
        'id': 'str',
        'type': 'str',
        'state': 'str',
        'collection': 'AllOfFileOperationCollection',
        'user': 'User',
        'size': 'float',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'state': 'state',
        'collection': 'collection',
        'user': 'user',
        'size': 'size',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, type=None, state=None, collection=None, user=None, size=None, created_at=None):  # noqa: E501
        """FileOperation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._state = None
        self._collection = None
        self._user = None
        self._size = None
        self._created_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if collection is not None:
            self.collection = collection
        if user is not None:
            self.user = user
        if size is not None:
            self.size = size
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this FileOperation.  # noqa: E501

        Unique identifier for the object.  # noqa: E501

        :return: The id of this FileOperation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileOperation.

        Unique identifier for the object.  # noqa: E501

        :param id: The id of this FileOperation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this FileOperation.  # noqa: E501

        The type of file operation.  # noqa: E501

        :return: The type of this FileOperation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileOperation.

        The type of file operation.  # noqa: E501

        :param type: The type of this FileOperation.  # noqa: E501
        :type: str
        """
        allowed_values = ["import", "export"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def state(self):
        """Gets the state of this FileOperation.  # noqa: E501

        The state of the file operation.  # noqa: E501

        :return: The state of this FileOperation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FileOperation.

        The state of the file operation.  # noqa: E501

        :param state: The state of this FileOperation.  # noqa: E501
        :type: str
        """
        allowed_values = ["creating", "uploading", "complete", "error", "expired"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def collection(self):
        """Gets the collection of this FileOperation.  # noqa: E501


        :return: The collection of this FileOperation.  # noqa: E501
        :rtype: AllOfFileOperationCollection
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this FileOperation.


        :param collection: The collection of this FileOperation.  # noqa: E501
        :type: AllOfFileOperationCollection
        """

        self._collection = collection

    @property
    def user(self):
        """Gets the user of this FileOperation.  # noqa: E501


        :return: The user of this FileOperation.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this FileOperation.


        :param user: The user of this FileOperation.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def size(self):
        """Gets the size of this FileOperation.  # noqa: E501

        The size of the resulting file in bytes  # noqa: E501

        :return: The size of this FileOperation.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileOperation.

        The size of the resulting file in bytes  # noqa: E501

        :param size: The size of this FileOperation.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def created_at(self):
        """Gets the created_at of this FileOperation.  # noqa: E501

        The date and time that this object was created  # noqa: E501

        :return: The created_at of this FileOperation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FileOperation.

        The date and time that this object was created  # noqa: E501

        :param created_at: The created_at of this FileOperation.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if issubclass(FileOperation, dict):
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
        if not isinstance(other, FileOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
