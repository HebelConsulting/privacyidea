import logging

from privacyidea.lib.containerclass import TokenContainerClass

log = logging.getLogger(__name__)


class YubikeyContainer(TokenContainerClass):

    def __init__(self, db_container):
        super().__init__(db_container)

    @classmethod
    def get_class_type(cls):
        """
        Returns the type of the container class.
        """
        return "yubikey"

    @classmethod
    def get_supported_token_types(cls):
        """
        Returns the token types that are supported by the container class.
        """
        return ["hotp", "certificate", "webauthn"]

    @classmethod
    def get_container_policy_info(cls):
        """
        Returns the policy information of the container class.
        """
        res = {
            "token_count": {"type": "int",
                            "value": "any",
                            "desc": "The maximum number of tokens in this container"},
            "token_types": {"type": "list",
                            "value": cls.get_supported_token_types(),
                            "desc": "The token types that can be stored in this container"},
            "user_modifiable": {"type": "bool",
                                "value": ["false"],
                                "desc": "Whether the user can modify the tokens in this container"}
        }

        return res

    @classmethod
    def get_class_prefix(cls):
        """
        Returns the container class specific prefix for the serial.
        """
        return "YUBI"

    @classmethod
    def get_class_description(cls):
        """
        Returns a description of the container class.
        """
        return "Yubikey hardware device that can hold HOTP, certificate and webauthn token"
