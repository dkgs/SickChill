# coding: utf-8

"""
    TheTVDB API v2

    API v2 targets v1 functionality with a few minor additions.
    The API is accessible via https://api.thetvdb.com and provides the following REST endpoints in JSON format.

    OpenAPI spec version: 2.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class JSONErrors(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, invalid_filters=None, invalid_language=None, invalid_query_params=None):
        """
        JSONErrors - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'invalid_filters': 'list[str]',
            'invalid_language': 'str',
            'invalid_query_params': 'list[str]'
        }

        self.attribute_map = {
            'invalid_filters': 'invalidFilters',
            'invalid_language': 'invalidLanguage',
            'invalid_query_params': 'invalidQueryParams'
        }

        self._invalid_filters = invalid_filters
        self._invalid_language = invalid_language
        self._invalid_query_params = invalid_query_params

    @property
    def invalid_filters(self):
        """
        Gets the invalid_filters of this JSONErrors.
        Invalid filters passed to route

        :return: The invalid_filters of this JSONErrors.
        :rtype: list[str]
        """
        return self._invalid_filters

    @invalid_filters.setter
    def invalid_filters(self, invalid_filters):
        """
        Sets the invalid_filters of this JSONErrors.
        Invalid filters passed to route

        :param invalid_filters: The invalid_filters of this JSONErrors.
        :type: list[str]
        """

        self._invalid_filters = invalid_filters

    @property
    def invalid_language(self):
        """
        Gets the invalid_language of this JSONErrors.
        Invalid language or translation missing

        :return: The invalid_language of this JSONErrors.
        :rtype: str
        """
        return self._invalid_language

    @invalid_language.setter
    def invalid_language(self, invalid_language):
        """
        Sets the invalid_language of this JSONErrors.
        Invalid language or translation missing

        :param invalid_language: The invalid_language of this JSONErrors.
        :type: str
        """

        self._invalid_language = invalid_language

    @property
    def invalid_query_params(self):
        """
        Gets the invalid_query_params of this JSONErrors.
        Invalid query params passed to route

        :return: The invalid_query_params of this JSONErrors.
        :rtype: list[str]
        """
        return self._invalid_query_params

    @invalid_query_params.setter
    def invalid_query_params(self, invalid_query_params):
        """
        Sets the invalid_query_params of this JSONErrors.
        Invalid query params passed to route

        :param invalid_query_params: The invalid_query_params of this JSONErrors.
        :type: list[str]
        """

        self._invalid_query_params = invalid_query_params

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other