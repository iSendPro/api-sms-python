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


class SMSReponseEtatEtat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, tel=None, smslong=None, message=None):
        """
        SMSReponseEtatEtat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'int',
            'tel': 'str',
            'smslong': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'tel': 'tel',
            'smslong': 'smslong',
            'message': 'message'
        }

        self._code = code
        self._tel = tel
        self._smslong = smslong
        self._message = message

    @property
    def code(self):
        """
        Gets the code of this SMSReponseEtatEtat.
        Code retour. Voir \"tableau des code retour\" dans l'annexe de la documentation

        :return: The code of this SMSReponseEtatEtat.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this SMSReponseEtatEtat.
        Code retour. Voir \"tableau des code retour\" dans l'annexe de la documentation

        :param code: The code of this SMSReponseEtatEtat.
        :type: int
        """

        self._code = code

    @property
    def tel(self):
        """
        Gets the tel of this SMSReponseEtatEtat.
        Numero de téléphone concerné

        :return: The tel of this SMSReponseEtatEtat.
        :rtype: str
        """
        return self._tel

    @tel.setter
    def tel(self, tel):
        """
        Sets the tel of this SMSReponseEtatEtat.
        Numero de téléphone concerné

        :param tel: The tel of this SMSReponseEtatEtat.
        :type: str
        """

        self._tel = tel

    @property
    def smslong(self):
        """
        Gets the smslong of this SMSReponseEtatEtat.
        Nombre de SMS longs facturés

        :return: The smslong of this SMSReponseEtatEtat.
        :rtype: str
        """
        return self._smslong

    @smslong.setter
    def smslong(self, smslong):
        """
        Sets the smslong of this SMSReponseEtatEtat.
        Nombre de SMS longs facturés

        :param smslong: The smslong of this SMSReponseEtatEtat.
        :type: str
        """

        self._smslong = smslong

    @property
    def message(self):
        """
        Gets the message of this SMSReponseEtatEtat.
        Libellé associé au code de retour

        :return: The message of this SMSReponseEtatEtat.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this SMSReponseEtatEtat.
        Libellé associé au code de retour

        :param message: The message of this SMSReponseEtatEtat.
        :type: str
        """

        self._message = message

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
