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

class DocumentsUpdateBody(object):
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
        'title': 'str',
        'text': 'str',
        'append': 'bool',
        'publish': 'bool',
        'done': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'text': 'text',
        'append': 'append',
        'publish': 'publish',
        'done': 'done'
    }

    def __init__(self, id=None, title=None, text=None, append=None, publish=None, done=None):  # noqa: E501
        """DocumentsUpdateBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._text = None
        self._append = None
        self._publish = None
        self._done = None
        self.discriminator = None
        self.id = id
        if title is not None:
            self.title = title
        if text is not None:
            self.text = text
        if append is not None:
            self.append = append
        if publish is not None:
            self.publish = publish
        if done is not None:
            self.done = done

    @property
    def id(self):
        """Gets the id of this DocumentsUpdateBody.  # noqa: E501

        Unique identifier for the document. Either the UUID or the urlId is acceptable.  # noqa: E501

        :return: The id of this DocumentsUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsUpdateBody.

        Unique identifier for the document. Either the UUID or the urlId is acceptable.  # noqa: E501

        :param id: The id of this DocumentsUpdateBody.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this DocumentsUpdateBody.  # noqa: E501

        The title of the document.  # noqa: E501

        :return: The title of this DocumentsUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DocumentsUpdateBody.

        The title of the document.  # noqa: E501

        :param title: The title of this DocumentsUpdateBody.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def text(self):
        """Gets the text of this DocumentsUpdateBody.  # noqa: E501

        The body of the document, may contain markdown formatting.  # noqa: E501

        :return: The text of this DocumentsUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this DocumentsUpdateBody.

        The body of the document, may contain markdown formatting.  # noqa: E501

        :param text: The text of this DocumentsUpdateBody.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def append(self):
        """Gets the append of this DocumentsUpdateBody.  # noqa: E501

        If true the text field will be appended to the end of the existing document, rather than the default behavior of replacing it. This is potentially useful for things like logging into a document.  # noqa: E501

        :return: The append of this DocumentsUpdateBody.  # noqa: E501
        :rtype: bool
        """
        return self._append

    @append.setter
    def append(self, append):
        """Sets the append of this DocumentsUpdateBody.

        If true the text field will be appended to the end of the existing document, rather than the default behavior of replacing it. This is potentially useful for things like logging into a document.  # noqa: E501

        :param append: The append of this DocumentsUpdateBody.  # noqa: E501
        :type: bool
        """

        self._append = append

    @property
    def publish(self):
        """Gets the publish of this DocumentsUpdateBody.  # noqa: E501

        Whether this document should be published and made visible to other team members, if a draft  # noqa: E501

        :return: The publish of this DocumentsUpdateBody.  # noqa: E501
        :rtype: bool
        """
        return self._publish

    @publish.setter
    def publish(self, publish):
        """Sets the publish of this DocumentsUpdateBody.

        Whether this document should be published and made visible to other team members, if a draft  # noqa: E501

        :param publish: The publish of this DocumentsUpdateBody.  # noqa: E501
        :type: bool
        """

        self._publish = publish

    @property
    def done(self):
        """Gets the done of this DocumentsUpdateBody.  # noqa: E501

        Whether the editing session has finished, this will trigger any notifications. This property will soon be deprecated.  # noqa: E501

        :return: The done of this DocumentsUpdateBody.  # noqa: E501
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this DocumentsUpdateBody.

        Whether the editing session has finished, this will trigger any notifications. This property will soon be deprecated.  # noqa: E501

        :param done: The done of this DocumentsUpdateBody.  # noqa: E501
        :type: bool
        """

        self._done = done

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
        if issubclass(DocumentsUpdateBody, dict):
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
        if not isinstance(other, DocumentsUpdateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
