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

class Document(object):
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
        'collection_id': 'str',
        'parent_document_id': 'str',
        'title': 'str',
        'full_width': 'bool',
        'emoji': 'str',
        'text': 'str',
        'url_id': 'str',
        'collaborators': 'list[User]',
        'pinned': 'bool',
        'template': 'bool',
        'template_id': 'str',
        'revision': 'float',
        'created_at': 'datetime',
        'created_by': 'User',
        'updated_at': 'datetime',
        'updated_by': 'User',
        'published_at': 'datetime',
        'archived_at': 'datetime',
        'deleted_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'collection_id': 'collectionId',
        'parent_document_id': 'parentDocumentId',
        'title': 'title',
        'full_width': 'fullWidth',
        'emoji': 'emoji',
        'text': 'text',
        'url_id': 'urlId',
        'collaborators': 'collaborators',
        'pinned': 'pinned',
        'template': 'template',
        'template_id': 'templateId',
        'revision': 'revision',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'updated_at': 'updatedAt',
        'updated_by': 'updatedBy',
        'published_at': 'publishedAt',
        'archived_at': 'archivedAt',
        'deleted_at': 'deletedAt'
    }

    def __init__(self, id=None, collection_id=None, parent_document_id=None, title=None, full_width=None, emoji=None, text=None, url_id=None, collaborators=None, pinned=None, template=None, template_id=None, revision=None, created_at=None, created_by=None, updated_at=None, updated_by=None, published_at=None, archived_at=None, deleted_at=None):  # noqa: E501
        """Document - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._collection_id = None
        self._parent_document_id = None
        self._title = None
        self._full_width = None
        self._emoji = None
        self._text = None
        self._url_id = None
        self._collaborators = None
        self._pinned = None
        self._template = None
        self._template_id = None
        self._revision = None
        self._created_at = None
        self._created_by = None
        self._updated_at = None
        self._updated_by = None
        self._published_at = None
        self._archived_at = None
        self._deleted_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if collection_id is not None:
            self.collection_id = collection_id
        if parent_document_id is not None:
            self.parent_document_id = parent_document_id
        if title is not None:
            self.title = title
        if full_width is not None:
            self.full_width = full_width
        if emoji is not None:
            self.emoji = emoji
        if text is not None:
            self.text = text
        if url_id is not None:
            self.url_id = url_id
        if collaborators is not None:
            self.collaborators = collaborators
        if pinned is not None:
            self.pinned = pinned
        if template is not None:
            self.template = template
        if template_id is not None:
            self.template_id = template_id
        if revision is not None:
            self.revision = revision
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
        if published_at is not None:
            self.published_at = published_at
        if archived_at is not None:
            self.archived_at = archived_at
        if deleted_at is not None:
            self.deleted_at = deleted_at

    @property
    def id(self):
        """Gets the id of this Document.  # noqa: E501

        Unique identifier for the object.  # noqa: E501

        :return: The id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Document.

        Unique identifier for the object.  # noqa: E501

        :param id: The id of this Document.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def collection_id(self):
        """Gets the collection_id of this Document.  # noqa: E501

        Identifier for the associated collection.  # noqa: E501

        :return: The collection_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._collection_id

    @collection_id.setter
    def collection_id(self, collection_id):
        """Sets the collection_id of this Document.

        Identifier for the associated collection.  # noqa: E501

        :param collection_id: The collection_id of this Document.  # noqa: E501
        :type: str
        """

        self._collection_id = collection_id

    @property
    def parent_document_id(self):
        """Gets the parent_document_id of this Document.  # noqa: E501

        Identifier for the document this is a child of, if any.  # noqa: E501

        :return: The parent_document_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._parent_document_id

    @parent_document_id.setter
    def parent_document_id(self, parent_document_id):
        """Sets the parent_document_id of this Document.

        Identifier for the document this is a child of, if any.  # noqa: E501

        :param parent_document_id: The parent_document_id of this Document.  # noqa: E501
        :type: str
        """

        self._parent_document_id = parent_document_id

    @property
    def title(self):
        """Gets the title of this Document.  # noqa: E501

        The title of the document.  # noqa: E501

        :return: The title of this Document.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Document.

        The title of the document.  # noqa: E501

        :param title: The title of this Document.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def full_width(self):
        """Gets the full_width of this Document.  # noqa: E501

        Whether this document should be displayed in a full-width view.  # noqa: E501

        :return: The full_width of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._full_width

    @full_width.setter
    def full_width(self, full_width):
        """Sets the full_width of this Document.

        Whether this document should be displayed in a full-width view.  # noqa: E501

        :param full_width: The full_width of this Document.  # noqa: E501
        :type: bool
        """

        self._full_width = full_width

    @property
    def emoji(self):
        """Gets the emoji of this Document.  # noqa: E501

        An emoji associated with the document.  # noqa: E501

        :return: The emoji of this Document.  # noqa: E501
        :rtype: str
        """
        return self._emoji

    @emoji.setter
    def emoji(self, emoji):
        """Sets the emoji of this Document.

        An emoji associated with the document.  # noqa: E501

        :param emoji: The emoji of this Document.  # noqa: E501
        :type: str
        """

        self._emoji = emoji

    @property
    def text(self):
        """Gets the text of this Document.  # noqa: E501

        The text content of the document, contains markdown formatting  # noqa: E501

        :return: The text of this Document.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Document.

        The text content of the document, contains markdown formatting  # noqa: E501

        :param text: The text of this Document.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def url_id(self):
        """Gets the url_id of this Document.  # noqa: E501

        A short unique ID that can be used to identify the document as an alternative to the UUID  # noqa: E501

        :return: The url_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._url_id

    @url_id.setter
    def url_id(self, url_id):
        """Sets the url_id of this Document.

        A short unique ID that can be used to identify the document as an alternative to the UUID  # noqa: E501

        :param url_id: The url_id of this Document.  # noqa: E501
        :type: str
        """

        self._url_id = url_id

    @property
    def collaborators(self):
        """Gets the collaborators of this Document.  # noqa: E501


        :return: The collaborators of this Document.  # noqa: E501
        :rtype: list[User]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """Sets the collaborators of this Document.


        :param collaborators: The collaborators of this Document.  # noqa: E501
        :type: list[User]
        """

        self._collaborators = collaborators

    @property
    def pinned(self):
        """Gets the pinned of this Document.  # noqa: E501

        Whether this document is pinned in the collection  # noqa: E501

        :return: The pinned of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this Document.

        Whether this document is pinned in the collection  # noqa: E501

        :param pinned: The pinned of this Document.  # noqa: E501
        :type: bool
        """

        self._pinned = pinned

    @property
    def template(self):
        """Gets the template of this Document.  # noqa: E501

        Whether this document is a template  # noqa: E501

        :return: The template of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Document.

        Whether this document is a template  # noqa: E501

        :param template: The template of this Document.  # noqa: E501
        :type: bool
        """

        self._template = template

    @property
    def template_id(self):
        """Gets the template_id of this Document.  # noqa: E501

        Unique identifier for the template this document was created from, if any  # noqa: E501

        :return: The template_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this Document.

        Unique identifier for the template this document was created from, if any  # noqa: E501

        :param template_id: The template_id of this Document.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def revision(self):
        """Gets the revision of this Document.  # noqa: E501

        A number that is auto incrementing with every revision of the document that is saved  # noqa: E501

        :return: The revision of this Document.  # noqa: E501
        :rtype: float
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Document.

        A number that is auto incrementing with every revision of the document that is saved  # noqa: E501

        :param revision: The revision of this Document.  # noqa: E501
        :type: float
        """

        self._revision = revision

    @property
    def created_at(self):
        """Gets the created_at of this Document.  # noqa: E501

        The date and time that this object was created  # noqa: E501

        :return: The created_at of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Document.

        The date and time that this object was created  # noqa: E501

        :param created_at: The created_at of this Document.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Document.  # noqa: E501


        :return: The created_by of this Document.  # noqa: E501
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Document.


        :param created_by: The created_by of this Document.  # noqa: E501
        :type: User
        """

        self._created_by = created_by

    @property
    def updated_at(self):
        """Gets the updated_at of this Document.  # noqa: E501

        The date and time that this object was last changed  # noqa: E501

        :return: The updated_at of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Document.

        The date and time that this object was last changed  # noqa: E501

        :param updated_at: The updated_at of this Document.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def updated_by(self):
        """Gets the updated_by of this Document.  # noqa: E501


        :return: The updated_by of this Document.  # noqa: E501
        :rtype: User
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Document.


        :param updated_by: The updated_by of this Document.  # noqa: E501
        :type: User
        """

        self._updated_by = updated_by

    @property
    def published_at(self):
        """Gets the published_at of this Document.  # noqa: E501

        The date and time that this object was published  # noqa: E501

        :return: The published_at of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this Document.

        The date and time that this object was published  # noqa: E501

        :param published_at: The published_at of this Document.  # noqa: E501
        :type: datetime
        """

        self._published_at = published_at

    @property
    def archived_at(self):
        """Gets the archived_at of this Document.  # noqa: E501

        The date and time that this object was archived  # noqa: E501

        :return: The archived_at of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this Document.

        The date and time that this object was archived  # noqa: E501

        :param archived_at: The archived_at of this Document.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Document.  # noqa: E501

        The date and time that this object was deleted  # noqa: E501

        :return: The deleted_at of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Document.

        The date and time that this object was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this Document.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

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
        if issubclass(Document, dict):
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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other