# coding: utf-8

"""
    API iSendPro

    [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP 

    OpenAPI spec version: 1.0.0
    Contact: support@isendpro.com
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


class REPERTOIREcreaterequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, keyid=None, repertoire_edit='create', repertoire_nom=None):
        """
        REPERTOIREcreaterequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'keyid': 'str',
            'repertoire_edit': 'str',
            'repertoire_nom': 'str'
        }

        self.attribute_map = {
            'keyid': 'keyid',
            'repertoire_edit': 'repertoireEdit',
            'repertoire_nom': 'repertoireNom'
        }

        self._keyid = keyid
        self._repertoire_edit = repertoire_edit
        self._repertoire_nom = repertoire_nom

    @property
    def keyid(self):
        """
        Gets the keyid of this REPERTOIREcreaterequest.
        Clé API

        :return: The keyid of this REPERTOIREcreaterequest.
        :rtype: str
        """
        return self._keyid

    @keyid.setter
    def keyid(self, keyid):
        """
        Sets the keyid of this REPERTOIREcreaterequest.
        Clé API

        :param keyid: The keyid of this REPERTOIREcreaterequest.
        :type: str
        """

        self._keyid = keyid

    @property
    def repertoire_edit(self):
        """
        Gets the repertoire_edit of this REPERTOIREcreaterequest.
        Action à réaliser doit valoir \"create\" ici.

        :return: The repertoire_edit of this REPERTOIREcreaterequest.
        :rtype: str
        """
        return self._repertoire_edit

    @repertoire_edit.setter
    def repertoire_edit(self, repertoire_edit):
        """
        Sets the repertoire_edit of this REPERTOIREcreaterequest.
        Action à réaliser doit valoir \"create\" ici.

        :param repertoire_edit: The repertoire_edit of this REPERTOIREcreaterequest.
        :type: str
        """
        allowed_values = ["create"]
        if repertoire_edit not in allowed_values:
            raise ValueError(
                "Invalid value for `repertoire_edit` ({0}), must be one of {1}"
                .format(repertoire_edit, allowed_values)
            )

        self._repertoire_edit = repertoire_edit

    @property
    def repertoire_nom(self):
        """
        Gets the repertoire_nom of this REPERTOIREcreaterequest.
        Nom du répertoire (libellé) à créer

        :return: The repertoire_nom of this REPERTOIREcreaterequest.
        :rtype: str
        """
        return self._repertoire_nom

    @repertoire_nom.setter
    def repertoire_nom(self, repertoire_nom):
        """
        Sets the repertoire_nom of this REPERTOIREcreaterequest.
        Nom du répertoire (libellé) à créer

        :param repertoire_nom: The repertoire_nom of this REPERTOIREcreaterequest.
        :type: str
        """

        self._repertoire_nom = repertoire_nom

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
