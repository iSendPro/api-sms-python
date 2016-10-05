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

from __future__ import absolute_import

# import models into model package
from .comptage_reponse import ComptageReponse
from .comptage_reponse_etat import ComptageReponseEtat
from .comptage_reponse_etat_etat import ComptageReponseEtatEtat
from .comptage_request import ComptageRequest
from .credit_response import CreditResponse
from .credit_response_etat import CreditResponseEtat
from .erreur import Erreur
from .erreur_etat import ErreurEtat
from .erreur_etat_etat import ErreurEtatEtat
from .hlr_reponse import HLRReponse
from .hlr_reponse_etat import HLRReponseEtat
from .hlr_reponse_etat_etat import HLRReponseEtatEtat
from .hl_rrequest import HLRrequest
from .listenoire_reponse import LISTENOIREReponse
from .listenoire_reponse_etat import LISTENOIREReponseEtat
from .listenoire_reponse_etat_etat import LISTENOIREReponseEtatEtat
from .repertoir_ecreatereponse import REPERTOIREcreatereponse
from .repertoir_ecreatereponse_etat import REPERTOIREcreatereponseEtat
from .repertoir_ecreatereponse_etat_etat import REPERTOIREcreatereponseEtatEtat
from .repertoir_ecreaterequest import REPERTOIREcreaterequest
from .repertoir_emodifreponse import REPERTOIREmodifreponse
from .repertoir_emodifreponse_etat import REPERTOIREmodifreponseEtat
from .repertoir_emodifreponse_etat_etat import REPERTOIREmodifreponseEtatEtat
from .repertoir_emodifrequest import REPERTOIREmodifrequest
from .sms_reponse import SMSReponse
from .sms_reponse_etat import SMSReponseEtat
from .sms_reponse_etat_etat import SMSReponseEtatEtat
from .sms_request import SMSRequest
from .sms_unique_request import SmsUniqueRequest